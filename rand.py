import random
import sys
import string

# get random password pf length 6 with letters, digits
characters = string.ascii_lowercase + string.digits 
password = ''.join(random.choice(characters) for i in range(6))
file_path = 'rand.txt'
sys.stdout = open(file_path ,'a')
print(password)
