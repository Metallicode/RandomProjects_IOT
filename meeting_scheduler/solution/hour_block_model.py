class Hour_Block:
    def __init__(self, time, title):
        self.time = time
        self.title = title

    def __repr__(self):
        return f"{self.time} {self.title}"
