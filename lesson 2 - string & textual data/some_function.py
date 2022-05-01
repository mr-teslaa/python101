message = "It's allah whom we worship"
print(f'Length of the string: {len(message)}')

# conver string into upppercase or lowecase
print(f'Lowercase string: {message.lower()}')
print(f'Uppercase string: {message.upper()}')

# message[0:4] means we need to display every character 
# starting form 0 and upto 4 but not include 4. So basically till 3
print(message[0:4])

# counting certein letter or words
print(f"Total 'w' is in the mesage is: {message.count('w')}")

# if you want to findout the index of an words
# if it can't find the work, it will show -1
# i.e. 'Allah' shows index 6. that means 'Allah words starts in index 6' 
print(f"Counting index of 'Allah' word: {message.find('allah')}")
print(f"Counting index of 'python' word: {message.find('python')}")

# you can also use replace function to replace any strings
# replace('previouse work', 'future word')

# for any help run this: print(help(str))
# replace 'str' with any kind of data type