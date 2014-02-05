class Integer(object):

	def __init__(self,number,positive):
		self.number=number
		self.p=positive

	def display(self):
		print self.p + str(self.number)


class NegativeInteger(Integer):

	def __init__(self,number):
		super(NegativeInteger, self).__init__(number, "-")

	def display(self):
		Integer.display(self)
		print "Wow such number"

if __name__=="__main__":
	test1=NegativeInteger(42)
	test2=Integer(21,"+")
	x=[test1,test2]
	for i in x:
		print i.display()
