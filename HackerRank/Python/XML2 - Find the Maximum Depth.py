import xml.etree.ElementTree as etree

l = ["<feed xml:lang='en'>",
     "<title>HackerRank</title>",
     "<subtitle lang='en'>Programming challenges</subtitle>",
     "<link rel='alternate' type='text/html' href='http://hackerrank.com/'/>",
     "<updated>2013-12-25T12:00:00</updated>",
     "<entry>",
     "<author gender='male'>Harsh</author>",
     "<question type='hard'>XML 1</question>",
     "<description type='text'>This is related to XML parsing</description>",
     "</entry>",
     "</feed>"]

tree = etree.ElementTree(etree.fromstringlist(l))
root = tree.getroot()

maxdepth = 0
#def depth(elem, level):
#    global maxdepth
#    level += 1
#    for subelem in elem:
#        r = depth(subelem, level)
#        if r > maxdepth:
#            maxdepth = r
#    return(level)
def depth(elem, level):
    global maxdepth
    if (level == maxdepth):
        maxdepth += 1
        
    for child in elem:
        depth(child, level + 1)

        
depth(tree.getroot(), -1)        


print(maxdepth)