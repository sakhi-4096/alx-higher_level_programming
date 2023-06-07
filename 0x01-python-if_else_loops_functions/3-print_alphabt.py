#!/usr/bin/python3
for ch in range(ord('a'), ord('z')+1):
    if chr(ch) == 'q' or chr(ch) == 'e':
        continue
    else:
        print("{}".format(chr(ch)), end='')
