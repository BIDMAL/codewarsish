inp = ["11",
       "a = 1;",
       "b = input();",
       "",
       "if a + b > 0 && a - b < 0:",
       "    start()",
       "elif a*b > 10 || a/b < 1:",
       "    stop()",
       "print set(list(a)) | set(list(b)) ",
       "#Note do not change &&& or ||| or & or |",
       "#Only change those '&&' which have space on both sides.",
       "#Only change those '|| which have space on both sides"]

inp = ["1",
       "x&& &&& && && x || | ||\|| x"]
import re
for i in range(int(inp[0])):
    line = inp[i+1]
    line = re.sub(r' &&(?= )', ' and', line)
    line = re.sub(r' [|][|](?= )', ' or', line)
    print(line)