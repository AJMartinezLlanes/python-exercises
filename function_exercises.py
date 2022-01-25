# 1.Define a function named is_two. 
# It should accept one input and return True 
# if the passed input is either the number or the string 2, False otherwise.

from calendar import LocaleTextCalendar

from psutil import disk_io_counters


def is_two(num): 
    if num == 2:
        return True
    else:
        return False

# 2.Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.

def is_vowel(vow): 
    if vow.lower() in['a','e','i','o','u']:
        return True
    else:
        return False

# 3.Define a function named is_consonant. 
# It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.

def is_consonant(letter): 
    if is_vowel(letter):
        return False
    else:
        return True

# 4.Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word 
# if the word starts with a consonant.

def capitalize_word(word): 
    if type(word) != str():
        return False
    if is_consonant(word[0]):
        return word.capitalize()
    else:
        return word

# 5.Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip.

def calculate_tip(total_bill, tip_percent = 0.2):
    if tip_percent > 0 or tip_percent < 1:
         tip_amount = tip_percent * total_bill
         return tip_amount
    else:
        print("try a decimal")
 
# 6.Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.

def apply_disc(o_price, disc_percent):
    if disc_percent > 0 or disc_percent < 1:
         discount = disc_percent * o_price
         discounted_price = o_price - discount
         return discounted_price
    else:
        print("try a decimal") 

# 7.Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input,
# and return a number as output.
 
def handle_commas(n):
    if n == str(n):
        return float(n.replace(',', ''))
    else:
        print('try a string')

# 8.Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).
 
def get_letter_grade(grade):
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
    return grade

# 9.Define a function named remove_vowels that accepts a string and 
# returns a string with all the vowels removed.
 
def remove_vowels(rm_vowels):
    if type(rm_vowels) != str():
        return False
    for vow in rm_vowels:
        if vow in ('aeiou'):
            rm_vowels = rm_vowels.replace(vow, '')
    return rm_vowels

# 10.Define a function named normalize_name. 
# It should accept a string and return a valid python identifier, that is:
#   anything that is not a valid python identifier should be removed
#   leading and trailing whitespace should be removed
#   everything should be lowercase
#   spaces should be replaced with underscores
#   for example:
#       Name will become name
#       First Name will become first_name
#       % Completed will become completed

def normalize_name(ab_string):
    normal_string = ''
    ab_string = ab_string.lower()
    for l in ab_string:
        if l.isidentifier() or l == ' ':
            normal_string += l
    normal_string = normal_string.strip() 
    normal_string = normal_string.replace(' ','_')
    return normal_string


# 11.Write a function named cumulative_sum that accepts a list of numbers 
# and returns a list that is the cumulative sum of the numbers in the list.
#   cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#   cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(nums):
    for n in range (1, len(nums)):
        nums[n] += sum(nums[n -1:n])
    return nums

# Additional Exercise
# Once you've completed the above exercises, 
# follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 
# in order to thouroughly comment your code to explain your code.
# 
# Bonus
# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27