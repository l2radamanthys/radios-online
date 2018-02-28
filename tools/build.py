
import sys

def main():
	stream = sys.argv[1]
	name = sys.argv[2] 
	file_ = open(name + '.pls', 'w')
	file_.write('[playlist]\nNumberOfEntries=1\n')
	file_.write('Title1=sin nombre, undefined, undefined, Argentina\n')
	file_.write('File1='+stream+'\n')
	file_.close()
	
if __name__ == '__main__':
	main()
	
