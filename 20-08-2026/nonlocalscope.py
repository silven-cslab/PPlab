"""
    This python program demonstrates the implementation of the nonlocal scope.
"""

number = 30
def func():
    ## Local to func:
    number = 10
    def func2():
        ## Accessing variable local to upper level function:
        nonlocal number
        number = 20
        print(number)
    print(number)
    func2()
    print(number)

func()
print(number)
