#!/usr/bin/python
# encoding:utf-8
# Filename: console.py

import manager
import request

managerWong = manager.CommonManager("王经理")
managerZhang = manager.Majordomo("张经理")
managerLee = manager.GeneralManager("李经理")

managerWong.SetSuperior(managerZhang)
managerZhang.SetSuperior(managerLee)

request1 = request.Request()
request1.RequestType = "请假"
request1.RequestContent = "小菜请假"
request1.Number = 1
managerWong.RequestApplications(request1)

request2 = request.Request()
request2.RequestType = "请假"
request2.RequestContent = "小菜请假"
request2.Number = 4
managerWong.RequestApplications(request2)

request3 = request.Request()
request3.RequestType = "加薪"
request3.RequestContent = "小菜请求加薪"
request3.Number = 500
managerWong.RequestApplications(request3)

request4 = request.Request()
request4.RequestType = "加薪"
request4.RequestContent = "小菜请求加薪"
request4.Number = 1000
managerWong.RequestApplications(request4)

request = request.Request()
request.RequestType = "加薪"
request.RequestType = "别人都加薪了"
request.Number = 1000


