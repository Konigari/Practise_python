number = input('input a number:')
if (number%2) == 0:
	print "hey that's an even number",number
	if (number%4) == 0:
		print "wow that's huge",number
else: 
	print "you are odd :/",number

new_number = raw_input('let\'s try something new, give me two , separated by a comma: ')
new_number = new_number.split(',') 
num = [int(x.strip()) for x in new_number]

num, check = raw_input('give two numbers, one as dividend and one as divisor: ').split(',')

if (int(num)%int(check) == 0):
	print "That's cool"
else:
	print "meh, it's fine too"