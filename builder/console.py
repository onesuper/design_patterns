#!/usr/bin/python
# Filename: console.py

import director
import product

director1 = director.Director()

b1 = product.ConcreteBuilder1()
director1.Construct(b1)  #let direcctor call the BuildMethod of b1<F12>
p1 = b1.GetResult()  #GetResult() returns a product
p1.Show()

b2 = product.ConcreteBuilder2()
director1.Construct(b2)
p2 = b2.GetResult()
p2.Show()
