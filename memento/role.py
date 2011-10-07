#!/usr/bin/python
# Filename: role.py

import memo

class GameRole:
	def __init__(self):
		self.hp = 100
		self.sp = 100
	def Display(self):
		print 'HP:' + str(self.hp)
		print 'SP:' + str(self.sp)
	def FightWithBoss(self):
		self.hp = 0
		self.sp = 0
	def Save(self):
		return memo.Copy(self.hp, self.sp)
	def Load(self, copy):
		self.hp = copy.hp
		self.sp = copy.sp


