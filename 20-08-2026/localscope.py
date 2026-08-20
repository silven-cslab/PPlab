"""
    This python program shows the local scope of the variables in python.
"""

## Global Variable:
a = 20

def func():
    ## Local Variable
    a = 30
    print(a)


func()
print(a)
