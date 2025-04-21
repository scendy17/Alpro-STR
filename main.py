class Queue:
    def __init__(self): 
        self.items = [];

    def IsEmpty(self):
        return len(self.items) == 0;

    def Enqueue(self, item):
        self.items.append(item);

    def Dequeue(self):
        if not self.IsEmpty():
            return self.items.pop(0);
        else:
            return None
        
    def Size(self):
        return len(self.items)