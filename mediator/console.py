#!/usr/bin/python
# encoding:utf-8
# Filename: console.py

import united
import country

un = united.UnitedNation()

nation1 = country.USA(un)
nation2 = country.Iraq(un)

un.member1 = nation1
un.member2 = nation2

nation1.Declare('不准研制核武器，否则发动战争！')
nation2.Declare('我们没有核武器，也不怕侵略')
