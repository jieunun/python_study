class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLinitCalculator(Calculator):
    def add(self, val):
        if self.value+val >= 100:
            self.value = 100
        else:
            self.value += val

cal = MaxLinitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)