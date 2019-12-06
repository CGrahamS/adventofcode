intcode_program = [1,9,10,3,2,3,11,0,99,30,40,50]

def is_opcode(number) :
	if number in [1,2,99] :
		return True
	else :
		return False

print(is_opcode(3))

# def intcode_computer(intcode_program) :
# if the current int is an opcode
	# if the int is a 1 set addition operation
	# elif the int a 2 set multiplication operation
	# elif opcode 99 stop execution
# else execute set opcode operation
	#if 1 
		# retrieve int at the position of value of current int
		# continue execution
		# retrieve int at the position of value of current int
		# add the first int to the second int and set to sum var
		# reset first and second vars
		# continue execution 
		# write the sum at the position the of the value of the current int
	#elif 2 
		# retrieve int at the position of value of current int
		# continue execution
		# retrieve int at the position of value of current int
		# multiply the first int to the second int and set to product var
		# reset first and second vars
		# continue execution 
		# write the product at the position the of the value of the current int
	#else 
		#stop execution?

