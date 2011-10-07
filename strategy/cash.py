#!/user/bin/python
# Filename: cash.py

import string

class CashSuper:
	def acceptCash(self, cash):
		pass

class CashNormal(CashSuper):
	def acceptCash(self, cash):
		return cash

class CashRebate(CashSuper):
	rebate = 1.0
	def __init__(self, strReb):
		self.rebate = string.atof(strReb)
	def acceptCash(self, money):
		return money * self.rebate

class CashReturn(CashSuper):
	condition = 0
	returnMoney = 0 
	def __init__(self, strCon, strRet):
		self.condition = string.atoi(strCon)
		self.strRet = string.atoi(strRet)
	def acceptCash(self, money):
		if(money >= self.condition):
			return (money - (money / self.condition)*self.returnMoney)
