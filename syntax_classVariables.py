class Base:
    val = 0
    
class SubA(Base):
    pass

class SubB(Base):
    pass

Base.val = 10
a = SubA()
b = SubB()
print(a.val, b.val)