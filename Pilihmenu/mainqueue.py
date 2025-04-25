class Queue:
    def __init__(self, max_size=5):
        self.items = []
        self.max_size = max_size

    def IsEmpty(self):
        return len(self.items) == 0

    def Enqueue(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)
        else:
            print("Antrian penuh")

    def Dequeue(self):
        if not self.IsEmpty():
            return self.items.pop(0)
        else:
            return None
        
    def Size(self):
        return len(self.items)

    def MaxSize(self):
        return self.max_size
