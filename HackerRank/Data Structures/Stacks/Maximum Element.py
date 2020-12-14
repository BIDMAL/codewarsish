import timeit
inp = ['10',
       '1 97',
       '2',
       '1 20',
       '2',
       '1 26',
       '1 20',
       '2',
       '3',
       '1 91',
       '3']
# setup_statement = """
# with open('Data Structures/Stacks/Maximum Element Input17.txt') as f:
#     inp = f.readlines()
# n = int(inp[0])
# stack = []
# mel = '0'
# """
# 
# t1 = timeit.Timer("""
# for i in range(n):
#     q = list(map(int, inp[1+i].split()))
#     if q[0] == 1:
#         stack.append(q[1])
#     elif q[0] == 2:
#         stack.pop(-1)
#     elif q[0] == 3:
#         print(max(stack))
# """,
# setup_statement)
# 
# t2 = timeit.Timer("""
# for i in range(n):
#     q = list(map(int, inp[1+i].split()))
#     if q[0] == 1:
#         stack.append(q[1])
#         if q[1] > int(mel):
#             mel = str(q[1])
#     elif q[0] == 2:
#         z = stack.pop(-1)
#         if z == int(mel):
#             mel = str(max(stack))
#     elif q[0] == 3:
#         print(mel)
# """,
# setup_statement)

#print("TIMER1: ", t1.timeit(1))
#print("TIMER2: ", t2.timeit(1))

n = int(inp[0])
stack = []
mel = '0'
for i in range(n):
    q = list(map(int, inp[1+i].split()))
    if q[0] == 1:
        stack.append(q[1])
        if q[1] > int(mel):
            mel = str(q[1])
    elif q[0] == 2:
        z = stack.pop(-1)
        if z == int(mel):
            if len(stack) > 0:
                mel = str(max(stack))
            else:
                mel = '0'
    elif q[0] == 3:
        print(mel)