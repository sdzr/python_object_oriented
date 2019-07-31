import shelve

shelf =shelve.open('test.dat')

class Foo():
    def __init__(self,value):
        print('test case',value)
        self.value=value

#F = Foo(100)

#shelf['F']=F
#print(shelf)
#shelf.sync()

#print(shelf['F'])
a = shelf['F']
print(a.value)
