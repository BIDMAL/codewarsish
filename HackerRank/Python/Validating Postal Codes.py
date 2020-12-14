regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.


import re
P = '454286'

print(bool(re.match(regex_integer_in_range, P))) 
#print(len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#print (bool(re.match(regex_integer_in_range, P)) 
#       and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)