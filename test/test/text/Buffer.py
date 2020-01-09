class Buffer:
    def __init__(self):
        self.data = []
        self.l = 0

    def add(self, *a):
        self.data += a
        self.l += len(a)
        n = self.l // 5
        self.l = self.l % 5
        for i in range(n):
            s = 0
            for j in range(5):
                s += self.data.pop(0)
            print(s)

    def get_current_part(self):
        return self.data

a = Buffer()
a.add(1,2,3,4)
a.add(5,6)
print(a.l, a.get_current_part())