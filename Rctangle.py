class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def set_size(self,size):
        self.width,self.height=size
    def get_size(self):
        return self.width,self.height
    size=property(get_size,set_size) #property为特性函数，可以隐藏具体的存取方法，让所有的属性看起来一样；比如这个例子，以后self.size
    #这个方法既可以读也可以写。应该使用特性而不是存取方法。

r=Rectangle() #给类赋予具体实例时，类名后面要有小括号。
#r.width=5
#r.height=10
#result=r.get_size()
#print(result)
#r.set_size((30,100))
#result=r.get_size()
#print(result)
r.size=20,30
result=r.size
print(result)