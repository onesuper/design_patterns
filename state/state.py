#!/usr/bin/python
# Filename: state.py

class ForenoonState:
	def WriteProgram(self, w):
		if w.Hour < 12:
			print 'time:' + str(w.Hour) + ' Forenoon, hardwork!'
		else:
			w.SetState(NoonState())
			w.WriteProgram()

class NoonState:
	def WriteProgram(self, w):
		if w.Hour < 13:
			print 'time:' + str(w.Hour) + ' Noon, tired!'
		else:
			w.SetState(AfternoonState())
			w.WriteProgram()

class AfternoonState:
	def WriteProgram(self, w):
		if w.Hour < 17:
			print 'time:' + str(w.Hour) + ' Afternoon, Ok~'
		else:
			w.SetState(EveningState())
			w.WriteProgram()

class EveningState:
	def WriteProgram(self, w):
		if w.Hour < 21:
			print 'time:' + str(w.Hour) + ' Evening, exhausted..'
		else: 
			w.SetState(SleepingState())
			w.WriteProgram()

class SleepingState:
	def WriteProgram(self, w):
		print 'time:' + str(w.Hour) + ' Sleeping zZZ...'
