def sortdaLista():
    thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
    thislist.sort()
    print(thislist)
sortdaLista()

def sortNumerico():
    thislist = [100, 50, 65, 82, 23]
    thislist.sort()
    print(thislist)
sortNumerico()

def sortDescendente():
    thislist = [100, 50, 65, 82, 23]
    thislist.sort(reverse = True)
    print(thislist)
sortDescendente()


def copiaList():
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)
copiaList()

"""
Method 	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""
