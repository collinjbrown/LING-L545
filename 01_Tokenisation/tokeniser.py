import sys

input = sys.stdin.read()
splitters = '.!?,:();"'
output = ''

prev = ''
for c in input:
    if c == '\n':
        continue

    if c == ' ':
        if prev == ' ':
            continue
        output += '\n'
        prev = c
        continue
    
    if c in splitters:
        if prev != ' ': output += '\n'
        output += c + '\n'
        prev = ' '
        continue

    output += c
    prev = c

print(output)
    