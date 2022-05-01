courses = ['math', 'computer science', 'nano tech', 'cyber sec']
numb = [12,43,67,34,334,2,5]

# for shorting we have a buildin function
courses.sort()
numb.sort()
# it short the list in alphabetic way
print(courses)
print(numb)

# for desc order we can do that in 2 way
# 1. call the sort() and then reverse() that, or
# 2. we can pass argument through sort() function
courses.sort(reverse=True)
numb.sort(reverse=True)
print(courses)
print(numb)