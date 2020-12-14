queries = 100
l = ['odd 10',
     'even 7',
     'odd 4',
     'odd 10',
     'even 2',
     'odd 5',
     'odd 1',
     'even 9',
     'even 1',
     'odd 1',
     'even 1',
     'odd 1',
     'odd 10',
     'even 7',
     'even 4',
     'odd 5',
     'odd 2',
     'even 10',
     'even 10',
     'odd 4',
     'even 5',
     'odd 6',
     'even 6',
     'odd 10',
     'odd 7',
     'even 7',
     'odd 9',
     'odd 7',
     'odd 8',
     'even 1',
     'odd 9',
     'even 1',
     'odd 9',
     'even 10',
     'odd 2',
     'odd 6',
     'even 8',
     'odd 2',
     'even 2',
     'even 2',
     'odd 7',
     'odd 7',
     'odd 9',
     'even 6',
     'even 10',
     'odd 1',
     'even 10',
     'even 3',
     'even 6',
     'even 9',
     'even 4',
     'odd 2',
     'even 1',
     'even 1',
     'odd 6',
     'odd 2',
     'odd 6',
     'odd 9',
     'odd 1',
     'even 4',
     'odd 2',
     'odd 8',
     'odd 2',
     'odd 10',
     'even 9',
     'odd 5',
     'odd 2',
     'even 8',
     'odd 9',
     'odd 7',
     'odd 6',
     'even 7',
     'odd 9',
     'odd 3',
     'even 9',
     'even 8',
     'odd 7',
     'even 3',
     'odd 7',
     'even 9',
     'odd 6',
     'odd 6',
     'odd 7',
     'even 4',
     'even 3',
     'odd 7',
     'odd 8',
     'even 8',
     'even 6',
     'odd 3',
     'even 10',
     'odd 2',
     'even 10',
     'even 2',
     'even 7',
     'even 5',
     'even 2',
     'even 8',
     'even 4',
     'odd 7']

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=None):
    stream = stream or EvenStream()
    for _ in range(n):
        print(stream.get_next())


for i in range(queries):
    stream_name, n = l[i].split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())