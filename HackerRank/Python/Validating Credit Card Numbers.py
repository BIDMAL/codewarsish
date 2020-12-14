inp = ['4123456789123456',
       '5123-4567-8912-3456',
       '61234-567-8912-3456',
       '4123356789123456',
       '5133-3367-8912-3456',
       '5123 - 3567 - 8912 - 3456']
"""
► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' ,'_', etc.
► It must NOT have 4 or more consecutive repeated digits. """
import re
for line in inp:
    digs = ''
    for sym in line:
        if sym in '0123456789':
            digs += sym 
    print('Valid' if ( re.match(r'^[456]\d{3}\-?\d{4}\-?\d{4}\-?\d{4}$', line) and (not re.search(r'(.)\1{3,}', digs)) ) else 'Invalid')