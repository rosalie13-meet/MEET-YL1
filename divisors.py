def divisors(n):
	
	x=1
	while x<=n:
	
		print x
	
  
		if n%x==0:
			print "is divisible"
		else:
			print "not divisible"
	
		x+=1
if __name__ == "__main__":
	divisors(8)
