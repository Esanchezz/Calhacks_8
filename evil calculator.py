'''
def addition(num1,num2):
    num1 = int(input("enter a number:"))
    num2 = int(input("enter a another number:"))
    result = num1 + num2
    return result

print('the sum equals',result,'or is it...?')
'''
import random


print("Hello, I am just your handy helpful calculator :)")
print('.')
print('.')
print('.')
num1 = int(input("enter a number:"))
num2 = int(input("enter another number:"))
result = num1 + num2

print('the sum equals',result,'or is it...?')

yes_no = input('Would you like to try multiplication? Type: "yes" or "no"')
if yes_no == 'yes':
    print('Okay let us continue')
elif yes_no == 'no':
     print("You do not have a choice")
else:
    print("Okay odd, moving on...")

num1 = int(input("enter a number:"))
num2 = int(input("enter another number: "))
result = random.randint(1,9999)


print('the product equals', result, '>:)')

    


    


