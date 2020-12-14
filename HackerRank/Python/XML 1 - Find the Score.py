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

tr = etree.ElementTree(etree.fromstringlist(l))
root = tr.getroot()

#def get_attr_number(node):    
#    n = len(node.attrib.items())
#    for subelem in node:
#        n += len(subelem.attrib.items())
#        if len(subelem.getchildren()) > 0:
#             n += get_attr_number(subelem)
#    return(n)
def get_attr_number(node):    
    return len(node.attrib) + sum(get_attr_number(child) for child in node)
print(get_attr_number(root))

