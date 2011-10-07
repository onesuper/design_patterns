#!/usr/bin/python
# Filename: console.py
import role

abc = role.GameRole()
abc.Display()

#save before meeting the boss
sav = abc.Save()
sav.role = abc.Save()

#see boss
abc.FightWithBoss()
abc.Display()

#load~
abc.Load(sav.role)
abc.Display()
