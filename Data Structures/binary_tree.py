
class Tree:
    """
    Binary Search Tree
    """

    def __init__(self, v: int or float):
        self.v = v
        self.left: Tree = None
        self.right: Tree = None

    def add(self, v):
        if v >= self.v:
            if self.right is None:
                self.right = Tree(v)
            else:
                self.right.add(v)
        else:
            if self.left is None:
                self.left = Tree(v)
            else:
                self.left.add(v)

    def in_order(self, f):
        if self.left:
            self.left.in_order(f)
        f(self.v)
        if self.right:
            self.right.in_order(f)
    
    def pre_order(self, f):
        f(self.v)
        if self.left:
            self.left.pre_order(f)
        if self.right:
            self.right.pre_order(f)

    def post_order(self, f):
        if self.left:
            self.left.post_order(f)
        if self.right:
            self.right.post_order(f)
        f(self.v)

    def sum(self):
        s = 0
        def f(v):
            nonlocal s
            s += v
        self.in_order(f)
        return s

    def product(self):
        s = 1
        def f(v):
            nonlocal s
            s *= v
        self.in_order(f)
        return s

    def in_order_g(self):
        if self.left:
            yield from self.left.in_order_g()
        yield self.v
        if self.right:
            yield from self.right.in_order_g()

    def reduce(self, reducer):
        g = self.in_order_g()
        init = next(g)
        for v in g:
            init = reducer(init, v)
        return init

    def map(self, mapper):
        g = self.in_order_g()
        for v in g:
            yield mapper(v)
    
    def filter(self, filterer, opt=True):
        g = self.in_order_g()
        for v in g:
            if opt == filterer(v):
                yield v

    def contains(self, v2):
        g = self.in_order_g()
        for v in g:
            if v == v2:
                return True
        return False


t = Tree(10)
t.add(-1)
t.add(-3)
t.add(1)
t.add(2)

t.post_order(print)  # -2! -1! 0! 1! 2!
print('sum:', t.sum())
print('product:', t.product())

def add(sum, v):
    return sum+v
result = t.reduce(add)
print('reduce add:', result)

result = t.reduce(lambda prod, v: prod * v)
print('reduce mul:', result)

mapped = t.map(lambda x: x+1)
for ele in mapped:
    print(ele)
