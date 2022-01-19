#movie_titles=['The Litte Mermaid' for 3 days, 'Brother Bear' for 5 days, 'Hercules' for 1day]
# 3USD /day

from operator import truediv
from socket import TCP_NODELAY


print('Select a title to show debt')
print('Options are: the_little_mermaid, brother_bear, hercules or all_titles')
the_little_mermaid = 3*3
brother_bear = 5*3
hercules = 1*3
all_titles= the_little_mermaid + brother_bear + hercules

#Suppose you're working as a contractor for 3 companies: 
#Google, Amazon and Facebook, they pay you a different rate per hour. 
#Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
#How much will you receive in payment for this week? 
#You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

print('OR')
print("type one: 'google, amazon, fb or all' for pay balance")
google = 400*6
amazon = 380*4
fb = 350*10
all = google + amazon + fb

#A student can be enrolled to a class only 
#if the class is not full 
#and the class schedule does not conflict with her current schedule

class_full = False
schedule_conflict = False
enrolled = not class_full and not schedule_conflict

#A product offer can be applied only 
# if people buys more than 2 items, 
# and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.
today = 1-19-2022
expiration = 3-25-2022
items = 3
prem_member = False
#offer for offer if items > 2 and expiration < today OR prem_member == true

#Continue working in your data_types_and_variables.py file. 
#Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'

#Create a variable that holds a boolean value for each of the following conditions:
#the password must be at least 5 characters
password_length = len(password) >= 5
#the username must be no more than 20 characters
username_length = len(username) < 20
#the password must not be the same as the username
pass_not_username = password != username
#bonus neither the username or password can start or end with whitespace
username_space = username[0] != ' ' and username[-1] != ' '
password_space = password[0] != ' ' and password[-1] != ' '

user_pass_ok = password_length and username_length and pass_not_username and username_space and password_space

