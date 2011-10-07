#!/usr/bin/python
# Filename: console.py

import player as player
import translator as t

b = player.Forward('Battier')
b.Defense()

m = player.Guard('McGrady')
m.Attack()

y = t.Translator('Yao Ming')
y.Attack()
y.Defense()
