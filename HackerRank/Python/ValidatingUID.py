lines = ['B1CD102354', 'B1CDEF2354', 'b1Cdef2354']

import re
for i in range(3):
    u = ''.join(sorted(lines[i]))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')

