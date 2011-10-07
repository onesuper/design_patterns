#!/usr/bin/python
# Filename: request.py

class Request:
	def __init__(self, requestType=0, requestContent=0, number=0):
		self.RequestType = requestType
		self.RequestContent = requestContent
		self.Number = number
