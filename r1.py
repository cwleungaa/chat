#read file

def read_file(filename):
	new = []
	with open (filename,'r',encoding = 'utf-8-sig' ) as f:
		for line in f:
			new.append(line.strip())		
	return new
			

#convert
def convert(new):
	new2 = []
	name = None
	for line in new:
		if line == 'Allen':
			name = 'Allen'
			continue
		elif line == 'Tom':
			name = 'Tom'
			continue
		if name:
			new2.append(name +": " +line)
	print(new2)
	return new2
		
#write file
def write_file(filename ,new):
	with open(filename,'w') as f:
		for line in new:
			f.write(line + '\n')

#main
def main():
	new = read_file('input.txt')
	new = convert(new)
	write_file('output.txt',new)


main()
