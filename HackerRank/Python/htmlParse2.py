l = ['<head>',
    '<title>HTML</title>',
    '</head>',
    '<object type="application/x-flash" ',
    'data="your-file.swf" ',
    'width="0" height="0">',
    '<!-- <param name="movie" value="your-file.swf" /> -->',
    '<param name="quality" value="high"/>',
    '</object>']

l2 = []

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("-> ", attr[0], " > ", attr[1], sep="")
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("-> ", attr[0], " > ", attr[1], sep="")
parser = MyHTMLParser()

for i in range(9):
    parser.feed(l[i])