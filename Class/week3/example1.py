class Counter:
    # def increment(self, value):
    #     value = value + 1
    #     return value

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count = self.count + 1


object = Counter()
object.increment()
print(object.count)
