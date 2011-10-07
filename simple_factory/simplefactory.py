#!/usr/bin/python
# Filename: simplefactory.py

import operation
import string

numberA = raw_input('please input numberA\n')
numberB = raw_input('please input numberB\n')
strOper = raw_input('please input an operation\n')

oper = operation.OperationFactory.createOperate(strOper)
oper.numberA = string.atoi(numberA)
oper.numberB = string.atoi(numberB)
result = oper.GetResult()
print 'the result is',result
