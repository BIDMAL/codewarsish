from collections import OrderedDict
ordd = OrderedDict([('BANANA FRIES', 12), ('POTATO CHIPS', 60), ('APPLE JUICE', 20), ('CANDY', 20)])
print(ordd)
for item in ordd:
    print(item.key, item.value)