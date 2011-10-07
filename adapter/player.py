#!/usr/bin/python
# Filename: player.py

class Player:
	def __init__(self, name):
		self.name = name

class Forward(Player):
	def __init__(self, name):
		Player.__init__(self, name)
	def Attack(self):
		print 'forward:' + str(self.name) + ' attack!'
	def Defense(self):
		print 'forward:' + str(self.name) + ' defense!'


class Guard(Player):
	def __init__(self, name):
		Player.__init__(self, name)
	def Attack(self):
		print 'forward:' + str(self.name) + ' attack!'
	def Defense(self):
		print 'forward:' + str(self.name) + ' defense!'

#ForeignCenter hasn't the Attack/Defense method
#he only has the JinGong/FangShou method
#you can't direct him by calling Attack() or Defense()
class ForeignCenter(): 
	def __init__(self, name):
		self.name = name
	def JinGong(self):
		print 'ForeignCenter:' + str(self.name) + ' attack!'
	def FangShou(self):
		print 'ForeignCenter:' + str(self.name) + ' defense!'
