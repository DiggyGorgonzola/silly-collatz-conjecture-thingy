import math, random, time

class Collatz():
    def __init__(self, value):
        self.value = value if isinstance(value, int) else int(value) if isinstance(value, float) else 0
        self.cache = []
        self.mod_cache = []
    def c(self):
        return self.value >> 1 if self.value % 2 == 0 else 3*self.value + 1
    def c_fast_reverse(self):
        return [self.value << 1, ((self.value - 1)/3) << 1 if self.value % 3 == 1 else None]
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
a = Collatz(417)
a.run()
print(a.mod_cache)
