# functions that are not recursive 

def func3():
    print('Three')

def func2():
    func3()
    print('Two')

def function1():
    func2()
    print('One')


function1()
