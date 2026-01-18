class Counter:
    def __init__(self, name, min_value, max_value):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.value = min_value
    
    def increment(self):
        if self.value < self.max_value:
            self.value += 1
        else:
            return
    
    def decrement(self):
        if self.value > self.min_value:
            self.value -= 1
        else:
            return
    
    def reset(self):
        self.value = self.min_value
    
    def __str__(self):
        return (
            f"Counter: {self.name} | Value: {self.value} (min={self.min_value}, max={self.max_value})"
        )
