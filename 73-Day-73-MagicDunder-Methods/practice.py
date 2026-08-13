class details:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"My name is {self.name}"

    def __repr__(self):
        return f"Yes my name is {self.name}"

    def __call__(self):
        return f"Everything is good"
        
    def __len__(self):
        return len(self.name)

