"""
    This python program shows the demenstration of global variables being used in the local scope.
"""

## Global Variable:
a = 50

def func():
    global a
    a = 40
    print(a)

func()
print(a)
