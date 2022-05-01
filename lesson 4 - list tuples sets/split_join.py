courses = ['math', 'computer science', 'nano tech', 'cyber sec']

# you can also add string, comma or anything using join()
courses_str = ' - '.join(courses)

# you can also create new list from any output using split()
# in here, split(' - ') will say, hey who have '-' remove them and 
# create a new list with what's you have got
new_courses = courses_str.split(' - ')

print(courses_str)
print(new_courses)