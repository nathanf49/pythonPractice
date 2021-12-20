import time, sys

indent = 0 # Spaces to indent
indentIncreasing = True

try:
    while True: # main loop keeps running until user stops program
        if indentIncreasing:
            print()
            print()
            print()
            print()
            print()
            print()
            print(' ' * indent + '********')
            print(' ' * indent + ' ********')
            print(' ' * indent + '  ********')
            print(' ' * indent + '   ********')
            print(' ' * indent + '  ********')
            print(' ' * indent + ' ********')
            print(' ' * indent + '********')
            time.sleep(0.05)  # pause for a tenth of a second
            indent += 1
            if indent > 200:
                indentIncreasing = False
        else:
            print()
            print()
            print()
            print()
            print()
            print()
            print(' ' * indent + '   ********')
            print(' ' * indent + '  ******** ')
            print(' ' * indent + ' ********  ')
            print(' ' * indent + '********   ')
            print(' ' * indent + ' ********  ')
            print(' ' * indent + '  ******** ')
            print(' ' * indent + '   ********')
            time.sleep(0.05)  # pause for a tenth of a second
            indent -= 1
            if indent == 0:
                indentIncreasing = True
    
except KeyboardInterrupt:
    sys.exit()
        

except KeyboardInterrupt:
    sys.exit()