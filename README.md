# 拉库指令
### 国外机直接用以下面命令：
```
ql repo https://github.com/akinlau/glados_checkin.git "check_in.py" "backUp|README.md" "sendNotify.py"
```

# 使用流程
### 1、青龙部署。

### 2、修改青龙config.sh配置，添加企业微信信息保存

### 3、新建拉库任务，并执行，刷新浏览器即可看到添加的任务。

### 4、添加GR_COOKIE环境变量（登录https://glados.rocks/，按F12--网络获取）

### 5、依赖管理选python新建依赖安装requests
