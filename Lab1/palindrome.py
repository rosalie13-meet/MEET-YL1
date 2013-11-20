def palindrome(x):
    if x[::-1]==x:
        return True
    else:
        return False
if __name__=="__main__":
    x=raw_input('give me a word ')
    print palindrome(x)
