# SWPU Campus Network Keepalive

自动检测校园网连接状态，断线时自动重新登录。

> **适用范围：西南石油大学（SWPU）校园网**，门户地址 `172.16.245.50`，深澜 Srun 认证系统。

## 使用方法

1. 安装依赖

```bash
pip install requests
```

2. 填写账号信息

打开 `campus_net_keepalive.py`，修改顶部的两行：

```python
USERNAME = "your_student_id"   # 学号
PASSWORD = "your_password"     # 密码
```

3. 运行

```bash
# 前台运行（有输出）
python campus_net_keepalive.py

# 后台静默运行
pythonw campus_net_keepalive.py
```

4. 设置开机自启（管理员 PowerShell）

```powershell
schtasks /create /tn "CampusNet" /tr "pythonw C:\path\to\campus_net_keepalive.py" /sc onlogon /f
```

## 工作原理

每 10 分钟 ping 一次门户地址，若失败则调用 Srun 登录接口自动重新认证。日志写入同目录 `campus_net.log`。

## 注意

- 请勿将填入账号密码的文件提交到公开仓库
