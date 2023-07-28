import requests,json,os,sys


# 在青龙面板环境变量添加GR_COOKIE，并登录https://glados.rocks，按f12--网络获取cookie
try:
    if "GR_COOKIE" in os.environ:
        if len(os.environ["GR_COOKIE"]) > 10:
            cookie = os.environ["GR_COOKIE"]
            print(f"\n当前从环境变量获取CK\n")
except Exception as e:
    print(f"获取cookie失败：{e}")


def load_send():
    global send
    cur_path = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(cur_path)
    if os.path.exists(cur_path + "/sendNotify.py"):
        try:
            from sendNotify import send
        except:
            send=False
            print("加载通知服务失败~")
    else:
        send=False
        print("加载通知服务失败~")


def checkin():    
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload={
        'token': 'glados.one'
    }
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent})
    mess = checkin.json()['message']
    time = state.json()['data']['leftDays']
    time = time.split('.')[0]
    return mess,time


if __name__ == '__main__':
    title = "GlaDOS签到通知"
    ret,remain = checkin()
    newline = "\n"
    content = f"签到结果：{ret}{newline}剩余天数：{remain}"
    load_send()
    send(title,content)
