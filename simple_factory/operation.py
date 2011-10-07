#!/usr/bin/python
# Filename: operation.py

class Operation:
	def __init__(self):
		self.numberA = 0
		self.numberB = 0
	#implements GetResult in sublclass

class OperationAdd(Operation):
	def __init__(self):
		Operation.__init__(self)
	def GetResult(self):
		result = self.numberA + self.numberB
		return result

class OperationSub(Operation):
	def __init__(self):
		Operation.__init__(self)		
	def GetResult(self):
		result = self.numberA - self.numberB
		return result

class OperationMul(Operation):
	def __init__(self):
		Operation.__init__(self)
	def GetResult(self):
		result = self.numberA * self.numberB
		return result

class OperationDiv(Operation):
	def __init__(self):
		Operation.__init__(self)
	def GetResult(self):
		try:
			result = self.numberA / self.numberB
			return result
		except:
			print 'divide by zero'

class OperationFactory:
	'''make out subclasses according to the
	string given'''
	@staticmethod
	def createOperate(strOper):
		if strOper == '+':    
			oper = OperationAdd()   #create an instance of OperationAdd here
			return oper
		elif strOper == '-':
			oper = OperationSub()
			return oper
		elif strOper == '*':
			oper = OperationMul()
			return oper
		elif strOper == '/':
			oper = OperationDiv()
			return oper
		else:
			print 'the operation does not exist'
		
