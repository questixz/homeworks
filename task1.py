class Divisor: 
    def __init__(self,chisl,znam):
        self.chisl = chisl 
        self.znam = znam 
        
    def __add__(self,other):
        chisl = (self.chisl * other.znam) + (other.chisl * self.znam)
        znam = self.znam * other.znam
        return Divisor(chisl,znam)
        
    def __str__(self):
        return f"{self.chisl}/{self.znam}"    

if __name__ == "__main__":
    d1 = Divisor(3,5)
    d2 = Divisor(5,8)
    
    print(d1 + d2)