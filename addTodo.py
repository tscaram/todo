path = "/home/user/Desktop/Todo/todo.txt"

def main():
	print("What would you like to add to do? ")
	item = raw_input()
	theFile = open(path, 'a')
	theFile.write(item + '\n')


main()
