#Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

for number in range(1,11):
    cube=number**3
    print(cube)


#Get first prime numbers up to 100

#Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

age = int((input('What is your age? ')))
if age < 18:
    print('kids')
elif age == 18:
    print('adults')
elif age <=65:
    print('adults')
else:
    print('seniors')