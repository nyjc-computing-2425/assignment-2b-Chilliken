num = input('Enter a number (decimal only): ')
# type your code here
number = num
number = number.lstrip("0123456789")
number = number.replace(".","")
dp = len(number)


# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
