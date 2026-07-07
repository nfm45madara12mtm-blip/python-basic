#func(func2)

def into(a):
    print("performing operations")
    a()
    
@into #into add
def add():
    print("sum",5+10)