class Stack:
    def __init__(self): 
        self.items = []

    def IsEmpty(self):
        return len(self.items) == 0

    def Push(self, item):
        self.items.append(item)

    def Pop(self):
        if not self.IsEmpty():
            return self.items.pop()
        else:
            return None
        
    def Peek(self):
        if not self.IsEmpty():
            return self.items[-1]
        else:
            return None

    def Size(self):
        return len(self.items)
