from random import randint
def coinflipping():
   
    x=raw_input('Please enter n')
    if x=='n':
        y=randint(1,2)
        if y==1:
            print 'heads'
        else:
            print 'tails'
    else:
        print 'I told you to press n -_-'
      
  
def probability():
    global x
    x=raw_input('What is the probability?')
    coinflipping()
def flipcoin():
    y=randint(1,2)
    if y==1:
        return 'heads'
    else:
        return 'tails'
def numflipping():
   
    x=int(raw_input('How many times should I flip it?'))
    my_list=[]
    for i in range(1, 1+x):
   
        my_list.append(flipcoin())
    return my_list
