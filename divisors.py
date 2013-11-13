

def palindrome():
	a=raw_input("Give me a word")

	if a==a[::-1]:
		return True
	else:
		return False
print palindrome()
