# def helloFunc():
#     return 'Hello function'

# print(helloFunc())
# # we can also manipulate the string that we got from function
# print(helloFunc().upper())


def hello(name, greeting):
    return f'Hi there {name}, {greeting}'

print(hello('Tesla', 'Good Morning'))


# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# subject = ['Science', 'Bangla']
# info = {'name': 'Tesla', 'age': '22'}

# # student_info('Science', 'Bangla', name='Tesla', age='22')
# student_info(*subject, **info)