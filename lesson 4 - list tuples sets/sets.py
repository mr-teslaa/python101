# sets
list_1 = {'History', 'Math', 'Physics', 'CompSci'}
list_2 = {'History', 'Math', 'Art', 'Design'}
print(list_1)

# in the output we see that, output don't have correct order
# like 'history' is the first item but in output it's the last item

# sets throw away the duplicate
# if we add the same value twice in the list it will automatically 
# delete one value from sets

 
# you can also search any value in SETS, TUPLES or SETS
print('Math' in list_1)


# like SETS have UNION and INTERSECTION in mathemactics
# it also have that in SETS
print(f"Interseciton: {list_1.intersection(list_2)}")
print(f"Difference: {list_1.difference(list_2)}")
print(f"Union: {list_1.union(list_2)}")