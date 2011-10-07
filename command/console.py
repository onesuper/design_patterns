#!/usr/bin/python
# encoding:utf-8
# Filename: console.py

import barbecuer as b
import command as c
import waiter as w

boy = b.Barbecuer()
bakeMuttonCommand1 = c.BakeMuttonCommand(boy)
bakeMuttonCommand2 = c.BakeMuttonCommand(boy)
bakeChickenWingCommand1 = c.BakeChickenWingCommand(boy)

#ordering
girl= w.Waiter()
girl.SetOrder(bakeMuttonCommand1)
girl.SetOrder(bakeMuttonCommand2)
girl.SetOrder(bakeChickenWingCommand1)
girl.Notify()


