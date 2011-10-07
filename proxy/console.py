#!/usr/bin/python
# Filename: console.py

import proxy

jiaojiao = proxy.SchoolGirl()
jiaojiao.name = 'jiaojiao'

third_one = proxy.Proxy(jiaojiao)

third_one.GiveFlowers()
# it looks like the third_one implements
# the GiveFlowers(). But if you look inside
# the proxy module, you will find out that he
# didn't pay any money!


