class Hour_Block:
    def __init__(self, time, title="", info=""):
        self.time = time
        self.title = title
        self.info = info

    def __repr__(self):
        return f"{self.time} {self.title} {self.info}"
