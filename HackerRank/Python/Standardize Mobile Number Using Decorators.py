def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            l[i] = '+91 ' + ' '.join([l[i][-10:-5], l[i][-5:]])
        f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

l = ['07895462130',
     '919875641230',
     '9195969878',]

sort_phone(l) 


"""
The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number. Alternatively, there may not be any prefix at all. 

+91 xxxxx xxxxx
"""