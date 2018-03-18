def main():
	a = 5
	b = 3	
	print "swapping with Add/Sub"
	print "--before swapping--"
	print_this(a, b)
	(a,b) = swap_with_add_sub(a, b)
	print "--after swapping--"
	print_this(a, b)

	print "swapping with XOR"
        print "--before swapping--"
        print_this(a, b)
        (a,b) = swap_with_xor(a, b)
        print "--after swapping--"
        print_this(a, b)

def swap_with_xor(a, b):
	a = a ^ b
	b = a ^ b
	a = a ^ b
	return (a, b)

def swap_with_add_sub(a, b):
	a = a + b
	b = a - b
	a = a - b
	return (a,b)

def print_this(a, b):
	print "a = ",a
	print "b = ",b	

if __name__ == "__main__":
	main()
