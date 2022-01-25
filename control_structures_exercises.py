# 1. Conditional Basics
#   a. prompt the user for a day of the week, print out whether the day is Monday or not

monday_is_true = input('Is Today Monday? Y/N')
if monday_is_true == 'Y':
    print('Today is Monday!')
else:
    print('Today is not Monday')

#   b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_is = input('What day is Today?\nFormat DDD')
if day_is in['SAT', 'SUN']:
    print("IT'S THE WEEKEND!!")
else:
    print('It is a Weekday...')

#   c. create variables and make up values for
#       the number of hours worked in one week
#       the hourly rate
#       how much the week's paycheck will be
#       write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
weekly_hours = 50
hourly_rate = 30
overtime_rate = hourly_rate * 1.5
week_norm = hourly_rate * 40
if weekly_hours > 40:
    ot = (weekly_hours - 40)* overtime_rate
    print(ot + week_norm)
elif weekly_hours <= 40:
    print(weekly_hours * hourly_rate)


# 2. Loop Basics
#a. While
    # Create an integer variable i with a value of 5.
    # Create a while loop that runs so long as i is less than or equal to 15
    # Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
    i += 1
    
    # Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2
    
    # Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5
    
    # Create a while loop that starts at 2, and displays the number squared on each line while 
    # the number is less than 1,000,000.

i = 2
while i <= 1000000:
    print(i)
    i **= 2

    # Write a loop that uses print to create the output shown below.
# 100
# 95
# 90
# 85
# 80
# 75
# 70
# 65
# 60
# 55
# 50
# 45
# 40
# 35
# 30
# 25
# 20
# 15
# 10
# 5

i = 100
while i >= 5:
    print(i)
    i -= 5

#b. For Loops
    # i. Write some code that prompts the user for a number, 
    # then shows a multiplication table up through 10 for that number.

factor = int(input('Give me a number to multiply for: '))
for number in range(1, 11):
    product = number * factor
    print(factor,'x', number,'=', product)
    
    # ii. Create a for loop that uses print to create the output shown below.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

for number in range(1, 10):
    print(number * str(number))

#c. break and continue

    #i. Prompt the user for an odd number between 1 and 50. 
    # Use a loop and a break statement to continue rompting the user if they enter invalid input. 
    # (Hint: use the isdigit method on strings to determine this). 
    # Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
    # except for the number the user entered.
# Number to skip is: 27

# Here is an odd number: 1
# Here is an odd number: 3
# Here is an odd number: 5
# Here is an odd number: 7
# Here is an odd number: 9
# Here is an odd number: 11
# Here is an odd number: 13
# Here is an odd number: 15
# Here is an odd number: 17
# Here is an odd number: 19
# Here is an odd number: 21
# Here is an odd number: 23
# Here is an odd number: 25
# Yikes! Skipping number: 27
# Here is an odd number: 29
# Here is an odd number: 31
# Here is an odd number: 33
# Here is an odd number: 35
# Here is an odd number: 37
# Here is an odd number: 39
# Here is an odd number: 41
# Here is an odd number: 43
# Here is an odd number: 45
# Here is an odd number: 47
# Here is an odd number: 49

while True:
    num = input('Give me an ODD number 1-50: ')
    if num.isdigit:
        if int(num) %2 == 1 and int(num)<= 50:
            break
print(f'number to skip is:', num)
for n in range(50):
    if n == int(num):
        print(f'Yikes! Skipping number:{n}')
    elif n % 2==0:
        continue
    print(f'Here is an odd number:{n}')

#d. The input function can be used to prompt for input and use that input in your python code. 
#   Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
#   (Hints: first make sure that the value the user entered is a valid number, 
#   also note that the input function returns a string, so you'll need to convert this to a numeric type.)

while True:
    num = input("Please enter a POSITIVE number:  ")
    if num.isdigit() == True and int(num) > 0:
        break
for n in range (0,int(num) + 1):
    print(n)
    
#e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

while true:
    num = input("Please enter a POSITIVE number:  ")
    if num.isdigit() == True and int(num) > 0:
        break
for num in range(int(num), 0, - 1):
    print(num)
    
# 3. Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
#   Write a program that prints the numbers from 1 to 100.
#   For multiples of three print "Fizz" instead of the number
#   For the multiples of five print "Buzz".
#   For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(1,100):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0:
        print('Fizz')
    else:
        print(n)

# 4. Display a table of powers.
#   Prompt the user to enter an integer.
#   Display a table of squares and cubes from 1 to the value entered.
#   Ask if the user wants to continue.
#   Assume that the user will enter valid data.
#   Only continue if the user agrees to.
# Bonus: Research python's format string specifiers to align the table

while True:
    num = input('Please enter a number: ')
    if num.isdigit():
        break
cont_yorn = input('Do you wish to continue(Y/N): ')
if cont_yorn.lower() == 'y':
    num = int(num)
    print (f'Number | Squared | Cubed')
    print (f'------ | ------- | -----')
    for n in range(1, num + 1):
        n_squared = n ** 2
        n_cubed = n ** 3
        print(f'{n:^6} | {n_squared:^7}  | {n_cubed:^5}')

  
# 5. Convert given number grades into letter grades.
#   Prompt the user for a numerical grade from 0 to 100.
#   Display the corresponding letter grade.
#   Prompt the user to continue.
#   Assume that the user will enter valid integers for the grades.
#   The application should only continue if the user agrees to.
while True:
    num = input('Please enter a numerical grade 0 - 100: ')
    if num.isdigit():
        num = int(num)
        if num < 0 or num > 100:
            print('try again')
            continue
        break
grade = int(num)
if grade in range(60):
    grade = 'F'
elif grade in range(60,67):
    grade = 'D'
elif grade in range(67,80):
    grade = 'C'
elif grade in range(80,88):
    grade = 'B'
else:
    grade = 'A'
print(grade)

# Bonus: Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

# 6. Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.

#   Prompt the user to enter a genre, then loop through your books list and 
#   print out the titles of all the books in that genre.

bookshelf = [
    {'title': 'Annihilation',
    'author': 'Jeff Vandermeer',
    'genre': 'Science Fiction'},
    {'title': 'Octopus Pie',
    'author': 'Maredeth Gran',
    'genre': 'Comic'},
    {'title': 'Cabin At the End of the World',
    'author': 'Paul Tremblay',
    'genre': 'Horror'},
    {'title': 'Severance',
    'author': 'Ling Ma',
    'genre': 'Science Fiction'},
]
book = ''
for key in book:
    print(key, book[key])
for book in bookshelf:
    print('we are living in a single dictionary here')
    [print(key, ': ', book[key]) for key in book]
    print('------')