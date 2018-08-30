"""

另一种创建类的方式

Version: 0.1
Author: 骆昊
Date: 2018-03-08

"""

import collections
def bar(self, name):
	self._name = name


def foo(self, course_name):
	print('%s正在学习%s.' % (self._name, course_name))


def main():
	Employee = collections.namedtuple('Employee', ['name', 'id'])
	employee = Employee("xiaowu","id")
	print(employee)
	Student = type('Student', (object,), dict(__init__=bar, study=foo))
	stu1 = Student('骆昊')
	stu1.study('Python程序设计')


if __name__ == '__main__':
	main()	
