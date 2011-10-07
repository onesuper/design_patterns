#!/usr/bin/python
# Filename: console.py

import web
import user 

f = web.WebsiteFactory()

web1 = f.GetWebsiteCategory("product")
web1.Use(user.User('A'))

web2 = f.GetWebsiteCategory("product")
web2.Use(user.User('B'))

web3 = f.GetWebsiteCategory("product")
web3.Use(user.User('C'))

web4 = f.GetWebsiteCategory("blog")
web4.Use(user.User('D'))

web5 = f.GetWebsiteCategory("blog")
web5.Use(user.User('E'))

web6 = f.GetWebsiteCategory("blog")
web6.Use(user.User('F'))

print f.GetWebsiteCount()
