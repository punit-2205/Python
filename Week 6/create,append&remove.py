empty_List=[]
print("Empty List is:", empty_List)

my_List=[10,507,"python"]
print("created list is:",my_List)

my_List.append(20)
my_List.append("program")
my_List.append([3,7])
print("After adding elements the new list is:",my_List)

d1=my_List.pop()
d2=my_List.pop(2)

my_List.remove(10)
print("After deleting elements the new list is:",my_List)

my_List.clear()
print("After removing all the elements the new list is:",my_List)