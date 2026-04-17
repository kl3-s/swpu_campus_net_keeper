# 🌐 SWPU Campus Network Keeper

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **自动保活西南石油大学校园网** | 一键启动，再也不用手动重连！

## 😫 为什么需要这个？

你是否经历过：
- 宿舍WiFi突然断网，需要重新登录校园网？
- 半夜WiFi掉线，得爬起来处理？
- 在做重要的事（下载、挂机、远程开发）时WiFi突然断掉？

**Keeper 帮你解决这一切** 🎯  
它在后台**自动监控**校园网连接，一旦掉线就**立即重新认证**，你完全无需操心。

---

## ✨ 主要功能

- ✅ **自动监控** - 每3秒检测一次连接状态
- ✅ **秒速重连** - 掉线自动登录，无缝保活
- ✅ **后台运行** - 无窗口、无打扰、无性能压力
- ✅ **完整日志** - 记录所有连接事件，帮助排查问题
- ✅ **开机启动** - 支持 Windows 开机自启（可选）

---

## 🚀 快速开始（3分钟）

### 1. 安装依赖
```bash
pip install requests
```

### 2. 下载项目
```bash
git clone https://github.com/kl3-s/swpu_campus_net_keeper.git
cd swpu_campus_net_keeper
```

### 3. 配置并运行

编辑 `campus_net_keepalive.py`，修改这两行：
```python
USERNAME = "你的学号"
PASSWORD = "你的密码"
```

然后运行：
```bash
python campus_net_keepalive.py
```

完成！现在校园网会自动保活了 ✨

---

## 💻 不同场景的用法

### 📱 在宿舍WiFi旁运行
```bash
python campus_net_keepalive.py
```
窗口会显示运行状态，有问题可以立即看到。

### 🔇 后台静默运行（Windows）
```bash
pythonw campus_net_keepalive.py
```
不会弹出黑色窗口，安静地在后台工作。

### 🔄 开机自动启动（Windows）

以**管理员身份**打开 PowerShell，运行：
```powershell
$taskName = "SWPU_Campus_Net_Keeper"
$scriptPath = "C:\path\to\campus_net_keepalive.py"
$action = New-ScheduledTaskAction -Execute "pythonw.exe" -Argument $scriptPath
$trigger = New-ScheduledTaskTrigger -AtLogOn
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -RunLevel Highest
```

然后每次开机就会自动运行了！

---

## 🔍 常见问题

### Q: 我的密码安全吗？
**A:** 密码保存在本地文件中，永远不会上传到 GitHub。建议：
- ✅ 不要把包含密码的文件提交到 Git
- ✅ 定期修改校园网密码
- ✅ 如果分享电脑，及时清除代码中的密码

### Q: 如何知道它在工作？
**A:** 查看日志文件 `campus_net.log`，你会看到类似的输出：
```
[2024-04-17 10:23:45] ✅ 连接正常
[2024-04-17 10:24:48] ⚠️  连接中断，尝试重新认证...
[2024-04-17 10:24:52] ✅ 重新连接成功
```

### Q: 占用资源吗？
**A:** 几乎不占用：
- 💾 内存：~30MB
- ⚡ CPU：<1%
- 🌐 流量：极少（仅 ping 请求）

### Q: 支持 Mac/Linux 吗？
**A:** 支持！代码是跨平台的，只需将开机启动部分改为对应系统的方式。

---

## 📝 日志查看

程序会在运行目录生成 `campus_net.log` 文件，记录所有事件。日志自动在达到 1MB 时轮转，不会占用太多磁盘空间。

---

## 🐛 故障排除

| 问题 | 解决方案 |
|------|---------|
| ❌ `ModuleNotFoundError: requests` | 运行 `pip install requests` |
| ❌ 连接失败 | 检查学号和密码是否正确、校园网是否在线 |
| ❌ 日志中有错误 | 查看 `campus_net.log` 了解详情 |
| ❌ 程序崩溃 | 检查是否有网络波动，日志会记录错误信息 |

---

## 🤝 贡献

欢迎贡献代码！如果你有改进想法：

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. Push 到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

### 可以改进的地方
- [ ] 图形界面（GUI）
- [ ] 支持多个校园网账户
- [ ] 更详细的连接诊断信息
- [ ] 支持其他学校的 Srun 系统

---

## 📄 许可证

本项目采用 [MIT License](LICENSE) - 详见 LICENSE 文件。

---

## 💬 有问题或建议？

- 📮 提交 [Issue](https://github.com/kl3-s/swpu_campus_net_keeper/issues)
- 💡 讨论想法和改进建议
- ⭐ 喜欢的话给个星吧！

---

**Made with ❤️ for SWPU students**
