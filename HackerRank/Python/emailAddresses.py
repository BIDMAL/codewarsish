import email.utils
import re
l = ['DEXTER <dexter@hotmail.com>', 'VIRUS <virus!@variable.:p>']
for i in range(2):
    em = email.utils.parseaddr(l[i])
    if re.match(r'[a-z][\w\.-]+@[a-z]+\.[a-z]{1,3}$', em[1], flags=re.I):
        print(email.utils.formataddr(em))