class Filter:
    def init(self):
        self.blocked=[]
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]

class spamFilter(Filter):  #spamFilter类是Filter类的子类，Filter是超类；spamFilter集成了Filter的filter方法，但又修改了init方法；
                          # 这就是类的继承的好处
    def init(self):
        self.blocked=['SPAM']

test=spamFilter()
test.init()
result=test.filter(['SPAM','ZHAOSIQI','SPAM','SPAM','SHENYAPING','ZHAOJIAQI','SPAM','SPAM','ZHAOYI'])
print(result)