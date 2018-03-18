def main():
	a = 0
	b = 1
	print a
	print b

	#print the first 10 numbers in the fibocci number series
	n = 10
	
	#as we have already printed a and b, we need to generate 8 more
	# so the while condition below is n = 10 to 2
	while n > 2:
		c = a + b
		print c
		a = b
		b = c
		n = n-1
	
if __name__ == "__main__":
	main()
