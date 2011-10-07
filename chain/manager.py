#!/usr/bin/python
# encoding:utf-8
# Filename: manage.py

class Manager:
	def __init__(self, name):
		self.name = name
	def SetSuperior(self, superior):
		self.superior = superior

class CommonManager(Manager):
	def __init__(self, name):
		Manager.__init__(self, name)
	def RequestApplications(self, request):
		if request.RequestType == '请假' and request.Number <= 2:
			print str(self.name)+':'+request.RequestContent+' 数量'+str(request.Number)+'被批准'
		else:  #请假次数大于2次，或者是“加薪”请求，需要由上层处理
			if self.superior != None:
				self.superior.RequestApplications(request)  #传递请求

class Majordomo(Manager):
	def __init__(self, name):
		Manager.__init__(self, name)
	def RequestApplications(self, request):
		if request.RequestType == '请假' and request.Number <= 5:
			print str(self.name)+':'+request.RequestContent+' 数量'+str(request.Number)+'被批准'
		else: #请假次数大于5次，或者是“加薪”请求，需要由上层处理
			if self.superior != None:
				self.superior.RequestApplications(request)  #传递请求

class GeneralManager(Manager):
	def __init__(self, name):
		Manager.__init__(self, name)
	def RequestApplications(self, request):
		if request.RequestType == '请假':
			print str(self.name)+':'+request.RequestContent+' 数量'+str(request.Number)+'被批准'
		elif request.RequestType == '加薪' and request.Number <= 500:
			print str(self.name)+':'+request.RequestContent+' 数量'+str(request.Number)+'被批准'
		elif request.RequestType == '加薪' and request.Number > 500:
			print str(self.name)+':'+request.RequestContent+' 数量'+str(request.Number)+'再说吧'
			
