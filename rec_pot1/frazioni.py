
class Frazione:

    def __init__(self, num:int,denom:int):
        self.set_num(num)
        self.set_denom(denom)

    def set_denom(self,denom):
        self.__denom = denom
    def set_num(self,num):
        self.__num = num
    
    def get_denom(self):
        return self.__denom
    def get_num(self):
        return self.__num
    def value(self):
        return round(self.__num/self.__denom)
    
    def __str__(self):
        return f"{self.get_denom()}/{self.get_num()}"
    