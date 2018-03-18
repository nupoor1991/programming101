def main():
	#print the factorial of 5
	n = 5
	
	product = 1
	
	while n > 0:
		product = product * n
		n = n-1

	print "factorial is: " + str(product)

if __name__ == "__main__":
	main()
