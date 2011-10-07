#!/usr/bin/python
# Filename: context.py

import cash

class CashContext:
	cs = cash.CashSuper()
	def __init__(self, stype):
		if stype == 'normal':
			self.cs = cash.CashNormal()
		elif stype == 'return money':
			self.cs = cash.CashReturn('300','100')
		elif stype == 'rebate':
			self.cs = cash.CashRebate('0.8')
	
	def GetResult(self, money):
		return self.cs.acceptCash(money)
