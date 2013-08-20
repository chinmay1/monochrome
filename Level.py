class Level:
    def __init__(self,list):
        self.list = list

    def level (self,target):
        return min(range(len(self.list)), key=lambda i: abs(self.list[i]-target))   
    

