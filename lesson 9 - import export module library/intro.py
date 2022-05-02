import sys
# if our module is in different loaction we can add them by this
# sys.path.append('path/to/the/module')

import myModule
from myModule import test # test a variable stroing a string
# we can also use custom name like
# import myModule as mod

# we can also import specific function among tons of function form a module
# from myModule import find_index

print(sys.path)

courses = ['History', 'Math', 'Physics', 'Computer Science']

index = myModule.find_index(courses, 'Math')
print(test)