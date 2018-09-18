
path = "/home/user/Desktop/Todo/todo.txt"
finishedPath = "/home/user/Desktop/Todo/finished.txt"

def main():
	print("Here is the list of things to do today: ")

	theFile = open(path, 'r')
	items = theFile.read().splitlines()

	for i in range(0, len(items)):
		print(str(i) + ". " + items[i])

	while len(items) != 0:
		theInput = raw_input()
		
		if theInput == "quit":
			theFile.close()
			quit()

		for i in range(0, len(items)):
			if items[i] == str(theInput):
				finishedFile = open(finishedPath, 'a')
				finishedFile.write(items[i] + '\n')
				finishedFile.close()
				items.remove(items[i])
				break
		
		newFile = open(path, 'w')
		
		for i in range(0, len(items)):
			newFile.write(items[i] + '\n')

		newFile.close()
		
		if len(items) != 0:
			print("\nWhat else?")
		
		for i in range(0, len(items)):
			print(str(i) + ". " + items[i])

main()
