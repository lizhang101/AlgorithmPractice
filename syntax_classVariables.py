from abc import ABC

class Base(ABC):
    val = 0
    que = []
    
    @classmethod
    def set_val(cls, v):
        cls.val = v
        cls.que.append(v)
    
class SubA(Base):
    pass

class SubB(Base):
    pass

i = 0
if False:
    Base.val = 10
    a = SubA()
    b = SubB()
    print(i, ":", a.val, b.val)
    i += 1
    #change in base, both instance changed
    Base.val = 20
    print(i, ":", a.val, b.val)
    i += 1

    #change on one class, only SubA changed
    SubA.val = 30
    print(i, ":", a.val, b.val)
    i += 1

    #Base.set_val can't change SubA's value, neither does setting it directly
    Base.set_val(10)
    print(i, ":", a.val, b.val)
    i += 1

Base.val = 10
a = SubA()
b = SubB()
print(i, ":", a.val, a.que, b.val, b.que)
i += 1

SubA.que.append(30)
print(i, ":", a.val, a.que, b.val, b.que)
i += 1
