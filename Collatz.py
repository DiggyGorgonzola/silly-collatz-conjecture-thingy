import math, random, time

class Collatz():
    def __init__(self, value):
        self.value = value if isinstance(value, int) else int(value) if isinstance(value, float) else 0
        self.cache = []
        self.mod_cache = []
    def c(self):
        return self.value >> 1 if self.value % 2 == 0 else 3*self.value + 1
    def c_reverse(self):
        return [self.value << 1, int(((self.value - 1)/3))] if self.value % 3 == 1 and self.value % 6 != 1 and self.value > 4 else [self.value << 1]
    def c_fast(self):
        return self.value >> 1 if self.value % 2 == 0 else (3*self.value+1) >> 1
    def run(self, function=lambda x: x>1, c_fast=True, mod_cache=10):
        while function(self.value):
            self.cache.append(self.value)
            self.mod_cache.append(self.value % mod_cache)
            if c_fast:
                self.value = self.c_fast()
            else:
                self.value = self.c()
        return self.cache
    def __repr__(self):
        return str(self.value)

if __name__ == "__main__":
    a = Collatz(1)
    l = []
    for i in range(100):
        x = a.c_reverse()
        if min(a.c_reverse()) % 3 > 0:
            if min(a.c_reverse()) < a.value:
                l.append(a.value)
            a = Collatz(min(a.c_reverse()))
        else:
            a = Collatz(max(a.c_reverse()))
    print(l)
