courses = ['math', 'computer science', 'nano tech', 'cyber sec']

# enumerate will return index and value at a time
for index, course in enumerate(courses):
    print(index, course)
print('+++++++++++++++++++++++++++')
# if you want to start the index from 1 
# for index, course in enumerate(courses, start=1):
#     print(index, course)
