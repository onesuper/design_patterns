#!/usr/bin/python
# Filename: console.py

import context
import string

former_price = string.atoi(raw_input('enter the price:'))

stype = raw_input('enter the mode:\n1.normal\n2.return money\n3.rebate\n')

cash = context.CashContext(stype)

payment = cash.GetResult(former_price)

print 'money you should pay:', payment
