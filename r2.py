#read file

def read_file(filename):
	new = []
	with open (filename,'r',encoding = 'utf-8-sig' ) as f:
		for line in f:
			new.append(line.strip())		
	return new
			

#convert
def convert(lines):
	s = []
	Allen_word = 0
	Allen_pic = 0
	Allen_stricker = 0
	Viki_word = 0
	Viki_pic = 0
	Viki_stricker = 0

	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			for m in s[2:]:
				if m == '圖片':
					Allen_pic += 1
				elif m == '貼圖':
					Allen_stricker += 1
				else:
					Allen_word=Allen_word + len(m)		
		if name == 'Viki':
			for m in s[2:]:
				if m == '圖片':
					Viki_pic += 1
				elif m == '貼圖':
					Viki_stricker += 1
				else:
					Viki_word=Viki_word + len(m)

	print('Allen共說了 '+ str(Allen_word) +'個字')
	print('Allen共傳了 '+ str(Allen_pic) +'張圖片')
	print('Allen共傳了 '+ str(Allen_stricker) +'張貼圖')
	print('Vike共說了 '+ str(Viki_word) +'個字')
	print('Vike共傳了 '+ str(Viki_pic) +'張圖片')
	print('Vike共傳了 '+ str(Viki_stricker) +'張貼圖')

#write file
def write_file(filename ,new):
	with open(filename,'w') as f:
		for line in new:
			f.write(line + '\n')

#main
def main():
	new = read_file('LINE-Viki.txt')
	new = convert(new)
	#write_file('output.txt',new)


main()
