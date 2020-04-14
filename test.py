""" 
This code prints a back-and-forth zig-zag pattern.
Author: Gemma
Date: 04/13/2020
"""

import sys, time

try:
    indent = 0
    indent_increase = True

    while True:
        print(' ' * indent, end='')
        print('*' * 10)
        time.sleep(0.1)

        if indent_increase:
            indent += 1
            if indent == 10:
                indent_increase = False
        else:
            indent -= 1
            if indent == 0:
                indent_increase = True
	
except KeyboardInterrupt:
    sys.exit()
