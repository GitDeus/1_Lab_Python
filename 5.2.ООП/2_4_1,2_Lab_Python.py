#1
class myclass1:
    def __init__(self, attr):
        self.attr = attr.upper()
                    #Так делать ненужно)

    def getUpperAtr(self):
        return self.attr.upper()


a = myclass1("Atr")
print(a.attr)
#2
class myclass2(dict):

    d = {}
    def __init__(self, dict):
        self.d = {dict: dict}
    def get(self):
        return self.d

    def getLen(self):
        return len(self.d)
    def getKey(self, key):
        return self.d.get(key)

b = myclass2("atr")
print(b.get())
print(b.getLen())
print(b.getKey('AtrB'))
