#!/usr/bin/python
# Filename: work.py

import state

class Work:
	def __init__(self):
		self.current = state.ForenoonState()
	def SetState(self, s):
		self.current = s
	def WriteProgram(self):
		self.current.WriteProgram(self)
