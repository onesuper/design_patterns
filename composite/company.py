#!/usr/bin/python
# encoding: utf-8
# Filename: company.py

class Company:
	def __init__(self, name):
		self.name = name

class ConcreteCompany(Company):
	def __init__(self, name):
		Company.__init__(self, name)
		self.children = []
	def Add(self, company):   #任何company都可以添加成子节点
		self.children.append(company)
	def Remove(self, company):
		self.children.remove(company)
	def Display(self, depth):
		print '-' * depth + str(self.name)
		for c in self.children:
			c.Display(depth + 2)
	def LineOfDuty(self):
		for c in self.children:
			c.LineOfDuty()

class HRDepartment(Company):
	def __init__(self, name):
		Company.__init__(self, name)
	def Display(self, depth):
		print '-' * depth + str(self.name)
	def LineOfDuty(self):
		print str(self.name) + '\t员工招聘培训管理'

class FinanceDepartment(Company):
	def __init__(self, name):
		Company.__init__(self, name)
	def Display(self, depth):
		print '-' * depth + str(self.name)
	def LineOfDuty(self):
		print str(self.name) + '\t公司财务收支管理'

root = ConcreteCompany('北京总公司')
root.Add(HRDepartment('总公司人力资源部'))
root.Add(FinanceDepartment('总公司财务部'))

comp = ConcreteCompany('上海华东分公司')
comp.Add(HRDepartment('华东分公司人力资源部'))
comp.Add(FinanceDepartment('华东分公司财务部'))
root.Add(comp)

comp1 = ConcreteCompany('南京办事处')
comp1.Add(HRDepartment('南京办事处人力资源部'))
comp1.Add(FinanceDepartment('南京办事处财务部'))
comp.Add(comp1)

comp2 = ConcreteCompany('杭州办事处')
comp2.Add(HRDepartment('杭州办事处人力资源部'))
comp2.Add(FinanceDepartment('杭州办事处财务部'))
comp.Add(comp2)

root.Display(1)
root.LineOfDuty()
