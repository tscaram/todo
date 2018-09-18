# todo
A todo program written in python

This is a program written in python 3 that is meant to be run from the command line.

The program addToDo.py adds things to the todo list, while the program todo.py removes items from it.

In both of these files, the path variable and the finished path variable should be set to the location where the user wants
their todo list and the list of items they've finished, respectively.

To use this program:
1. Run the addToDo.py program and type in the item you want to add to your todo list. ex. "Do the dishes" (leave out the
quotation marks)

2. Run the todo.py program. This will show the todo list you've created. In order to remove something from the list, type in
the item you want to remove. For the last example, you would type in "Do the dishes" without the quotation marks.

The way the program works is that it writes your input from the addToDo.py program to a todo text file. the todo.py program
will remove items from that text file and then send them to a text file labeled "finished.txt", or whatever the finishedPath
variable is set to. This means that a todo list can be created, and then as items are removed from the list they are sent to
a file that keeps track of the items that have been finished.

Type the word "quit" to exit the todo.py program, or use Ctrl-c
