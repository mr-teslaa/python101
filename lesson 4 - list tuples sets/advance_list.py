courses = ['math', 'computer science', 'nano tech', 'cyber sec']
course_lang = ['bangla', 'arabic', 'spanish']

# if we want to display first 2 value of the list 
print(courses[0:2])

# if we want to add new item in list
courses.append('digital marketing')
print(courses)

# but it add this item at the very bottom of the list
# what if we want to add this in a specific location
# for that we need a new module called insert()
courses.insert(0, 'wow')
print(courses)


# but inset works fine with single value insertion
# but not works for inserting another array
# here the extend() module come
courses.extend(course_lang)
print(courses)

# unfortunately we can assign fixed postion with extend()
# because it's only take 1 argument

# we can also delete any element from list
courses.remove('math')
print(courses)

# we also have pop() that does the exact same thing
# pop() will remove the very last item of the list
# and if you want you can store them into a var to access that later
poped = courses.pop()
print(f"Pooped item => {poped}")