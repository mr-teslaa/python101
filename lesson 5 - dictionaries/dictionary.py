student = {
    'name': 'jhone',
    'age': 22,
    'courses': [
        'Math', 'Data Science', 'Data Structure and Algorithm', 'Artificial Intelligence'
    ]
}

print(student['courses'])

# if we use `print(student['phone'])` which key is not exist it shows an error
# we can use get() method instead, that will return us a None value
print(student.get('phone')) 

# we can also set the default value of any key that doesn't exist like this
# this will return us any message instead of returning None value
print(student.get('email', 'This is not exist')) 


# we can also assign value in dictinoary or update any existing value
student['phone'] = '374837434'
student['name'] = 'Doe'
print(student.get('phone', 'phone number not exist')) 
print(student)

# instead we can also use update() method to update multiple value at a time
student.update({
    'name': 'khalid',
    'age': 23
})

print("======== after update() method =========")
print(student)


# we can delete any key using del method
del student['age']
print("======== after del method =========")
print(student)



# we can also get all of your key or values through this method
print("======== printing only keys =========")
print(student.keys())
print("======== printing only values =========")
print(student.values())

# some other useful method
print('------------ length ------------')
print(len(student))
print(student.items())


# printing all key with for loop
for key,value in student.items():
    print('-- key and value --')
    print(key, value)