arr = list(
    map(int, "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060".split()))

print("Mode of List C is % s" % (max(set(arr), key=arr.count)))