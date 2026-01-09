class car:
    num1=8
    n=int(input("Enter number: "))
    cnt=0
    for i in range(n):
        cnt+=1
        
    if cnt%2==0:print("Even")
    else:print("Odd")
    
    def __init__(self, x):
        self.num = x
        
    def dispaly(self):
        print(self.num)


obj = car(5)
obj.dispaly()
print(obj.num1)
print(f"count={obj.cnt}")
