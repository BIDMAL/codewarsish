from operator import itemgetter

l = ['Jake Jake 42 M',
          'Jake Kevin 57 M',
          'Jake Michael 91 M',
          'Kevin Jake 2 M',
          'Kevin Kevin 44 M',
          'Kevin Michael 100 M',
          'Michael Jake 4 M',
          'Michael Kevin 36 M',
          'Michael Michael 15 M',
          'Micheal Micheal 6 M']
people = [pl.split() for pl in l]

#def person_lister(f):
#    def inner(people):
#        people.sort(key=lambda x: int(x[2]))
#        for i in range(len(people)):
#            people[i] = f(people[i])
#        return(people)
#    return inner

def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: x[2]))          
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


print(*name_format(people), sep='\n')