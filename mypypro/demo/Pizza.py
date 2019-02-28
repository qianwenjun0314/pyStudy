class Pizza:
    def __init__(self, topps):
        self.topps = topps
        self._pineapple_allaw = False


pizza = Pizza(['cheea', 'tomato'])
print(pizza)
print(pizza.topps)
print(pizza.__class__)
