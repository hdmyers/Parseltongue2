import sys

value = 0 
for argument in sys.argv:
    print("Argument " + str(value) + " is " + argument)
    value += 1

sys.argv.sort(key=len)
sys.argv.reverse()
for argument in sys.argv:
    print(argument)
