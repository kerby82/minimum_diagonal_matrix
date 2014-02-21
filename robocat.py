import sys, ast, getopt, types, argparse

def usage():
	print "Launch the command as the following: {} --l matrix".format(sys.argv[0])
	print "Where matrix is a list representing the matrix itself each row can be represented as a string comma separated" 
	print "while to indicate a new row use a \"-\", e.g. 1,2,3-4,5,6-7,8,9 is equivalent to:"
	print "1, 2, 3"
	print "4, 5, 6"
	print "7, 8, 9"

def matrix_test(square):
    for row in square:
        if len(row) != len(square):
             return False
    return True


def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
               yield perm[:i] + elements[0:1] + perm[i:]

if len(sys.argv) < 3:
	usage()
	sys.exit(2)
	
parser = argparse.ArgumentParser()
parser.add_argument('--l', type=str)
args = parser.parse_args()
matrix = args.l.split('-') # ['1','2','3','4']
for row in range(len(matrix)):
	matrix[row]=matrix[row].split(',')
if  not matrix_test(matrix):
	print "Is not a square so I can't calculate the minimum diagonal!"
	sys.exit(3)
n=len(matrix)
input=matrix
rows=[x for x in range(n)]
list=all_perms(rows)
min=None
order=None
try:
	for element in list:
		if min == None:
			i=0
			min=0
			for column in element:
				min=min+int(input[column][i])
				i=i+1
			order=element
		else:
			temp_min=0
			i=0
			for column in element:
				temp_min=temp_min+int(input[column][i])
				i=i+1
			if temp_min < min:
				min=temp_min
				order=element
except:
	print "An error is occured:", sys.exc_info()
	sys.exit(1)
print
print "======================="
print "The original matrix is:"
print "======================="
i=0
for row in input:
	print "{} => {}".format(i,row)
	i=i+1
print
print "==============================="
print "The Minimum diagonal Matrix is:"
print "==============================="
for row in order:
	print "{} => {}".format(row,input[row])
print
print "The sum is: {}".format(min)
