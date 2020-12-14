import re

emails = ['its@gmail.com1',
          'mike13445@yahoomail9.server',
          'rase23@ha_ch.com',
          'daniyal@gmail.coma',
          'thatisit@thatisit']

def filter_mail(emails):
    return list(filter(fun, emails))

def fun(s):
    return(re.match(r'[\w-]+@[A-Za-z0-9]+\.[a-z]{1,3}$', s))

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


# It must have the username@websitename.extension format type.
# The username can only contain letters, digits, dashes and underscores.
# The website name can only have letters and digits.
# The maximum length of the extension is 3.