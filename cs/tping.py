def gen(n):
    while True:
        yield n
        n += 1


G = gen(0)
# print(next(G))
# print(next(G))
# print(next(G))

# print([next(G) for i in range(101)])
# print([next(G) for i in range(101)])
# print([next(G) for i in range(101)])

from typing import List, final


class Ttest:
    def __init__(self, t: list = ["test", "ttest"]):
        if isinstance(t, list):
            self.t = t
            self.b = 0
        else:
            raise ValueError("Передан неверный тип данных (t)")

    @final
    @property
    def _ttest(self) -> List[str]:
        return self.t

    def __str__(self):
        return f"({self.t}, {self.b})"


class Dtest(Ttest):
    def __init__(self, t, v:list=[5, 4, 1]):
        super().__init__(t)
        if isinstance(v, list):
            self.v = v
        else:
            raise ValueError("Передан неверный тип данных (v)")


if __name__ == "__main__":
    v = Ttest(["test", "ttest"])
    print(v._ttest)
    print(v)
    print(v.__dict__)
    b = Dtest(["test", "dtest"])
    print(b._ttest)
    print(b.__dict__)
    for i in (n := ['a', 'b']):
        print(f'{n if i == "b" else 0}')
        break
