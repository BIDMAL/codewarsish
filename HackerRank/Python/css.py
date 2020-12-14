import re
s = ['.stitched {',
    'padding: 20px;',
    'margin: 10px;',
    'background: #ff0030;',
    'color: #fff;',
    'font-size: 21px;',
    'font-weight: bold;',
    'line-height: 1.3em;',
    'border: 2px dashed #fff;',
    'border-radius: 10px;',
    'box-shadow: 0 0 0 4px #ff0030, 2px 1px 6px 4px rgba(10, 10, 0, 0.5);',
    'text-shadow: -1px -1px #aa3030;',
    'font-weight: normal;',
    '}']
for i in range(len(s)):
    l = s[i]
    if re.match(r'[#}{]', l) or (l == ''):
        continue
    col = re.findall(r'(#[0-9a-f]{3,6})[;,)]', l, flags=re.I)
    if len(col) > 0:
        print(*col, sep='\n')