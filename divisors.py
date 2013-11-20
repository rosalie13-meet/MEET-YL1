def divisors(n):
   
    for i in range(1,n):
        if n%i==0:
            print i
    
if __name__=="__main__":
    n=int(raw_input('give me a number '))
    divisors(n)
