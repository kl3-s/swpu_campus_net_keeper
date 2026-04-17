"""
校园网自动重连脚本 (深澜 Srun 门户)
逻辑: 每 10 分钟 ping 一次，失败则自动登录
"""

import subprocess
import hashlib
import re
import logging
import requests
import socket
import time
from pathlib import Path

LOG_FILE = Path(__file__).parent / "campus_net.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

# ===== 填写你的账号信息 =====
USERNAME    = "your_student_id"
PASSWORD    = "your_password"
# ===========================

PORTAL_HOST = "172.16.245.50"
PORTAL_API  = "172.16.245.50:8800"
AC_ID       = "1"
PING_HOST   = PORTAL_HOST         # ping 门户本身，不依赖外网
INTERVAL    = 10 * 60             # 10 分钟


def ping_ok() -> bool:
    result = subprocess.run(
        ["ping", "-n", "1", "-w", "2000", PING_HOST],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def get_local_ip() -> str:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((PORTAL_HOST, 80))
        return s.getsockname()[0]
    except Exception:
        return ""


def login() -> bool:
    ip = get_local_ip()
    logging.info(f"本机 IP: {ip}")
    api = f"http://{PORTAL_API}"
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})

    # 获取 challenge token
    token = ""
    try:
        r = session.get(
            f"{api}/cgi-bin/get_challenge",
            params={"callback": "cb", "username": USERNAME, "ip": ip},
            timeout=5,
        )
        logging.info(f"challenge 响应 [{r.status_code}]: {r.text[:300]}")
        m = re.search(r'"challenge"\s*:\s*"([^"]+)"', r.text)
        if m:
            token = m.group(1)
    except Exception as e:
        logging.warning(f"get_challenge 失败: {e}")

    params = {
        "callback":     "cb",
        "action":       "login",
        "username":     USERNAME,
        "password":     f"{{MD5}}{hashlib.md5(PASSWORD.encode()).hexdigest()}" if token else PASSWORD,
        "ac_id":        AC_ID,
        "ip":           ip,
        "n":            "200",
        "type":         "1",
        "double_stack": "0",
    }

    try:
        r = session.get(f"{api}/cgi-bin/srun_portal", params=params, timeout=10)
        logging.info(f"登录响应 [{r.status_code}]: {r.text[:500]}")
        return any(k in r.text for k in ("login_ok", "suc_msg", "online", "ip_already_online"))
    except requests.RequestException as e:
        logging.error(f"登录请求异常: {e}")
        return False


def main():
    logging.info(f"启动校园网守护 | 用户: {USERNAME} | 间隔: {INTERVAL // 60} 分钟")
    while True:
        if ping_ok():
            logging.info(f"ping {PING_HOST} OK — 网络正常")
        else:
            logging.warning(f"ping {PING_HOST} FAIL — 开始登录...")
            if login():
                logging.info("登录成功")
            else:
                logging.warning("登录失败，下次再试")
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
