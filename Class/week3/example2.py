class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count = self.count + 1


class NewCounter(Counter):
    def __init__(self, value):
        Counter.__init__(self)
        self.value = value

    def increment(self):
        self.count += self.value


object = NewCounter(3)
object.increment()
print(object.count)
