#   Ticket12306

1.拿到黑马公开的抢票代码 
2.在此基础上做一些修改，更加完善

步骤

Step1: 安装 Splinter  selenium
Splinter是一个使用Python开发的开源Web应用测试工具

Step2: 安装对应版本geckodriver，  （FireFox对应geckodriver，Chrome对应ChromeDriver）
https://github.com/mozilla/geckodriver/releases

step3:重启  要环境变量生效

step4:网站登录，验证码要自己输入

step5:个人修改的部分
username = u"***"
passwd = u"***"
# cookies值得自己去找, 下面两个分别是上海, 太原南
#上海   u"%u4E0A%u6D77%2CSHH"
# 太原南  u"%u592A%u539F%2CTYV"
starts =u"%u4E0A%u6D77%2CSHH"
ends = u"%u592A%u539F%2CTYV"
# 时间格式2018-01-19
dtime = u"2018-01-19"
###乘客名
users = [u"黄*", u"王*"]
##席位
xb = u"硬卧"
pz = u"成人票"

self.driver_name='firefox'
self.executable_path='D:\Program Files\Mozilla Firefox\geckodriver'

