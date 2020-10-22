class Counter():
    num_instances = 0 # Class variable a common value between all counter types
    def __init__(self,value=0):
        Counter.num_instances +=1
        self.value = value # Self.value is an instance variable.

    def __str__(self):
        return "Counter value: {}".format(self.value)

    def increment(self, value=1): # If a value is put in, slef increments by that value
        self.value += value

    def decrement(self,value=1):
        self.value -= value
    
# The interface for this class is the set of methods that it defines.

counters = Counter(2) # Calls the constructor and gives it a value of 2
counters.increment(5) # Adds 5
counters.decrement(3) # Subtracts 1

print(counters)

counter2 = Counter()
for i in range(0,5):
    counter2.increment()
print(counter2)
print("The number of open instances of class Counter is",Counter.num_instances)

#####

class Stock():
    def __init__(self,company,val):
        self.company = company
        self.val = val
        
    def __str__(self):
        return "{}: {}".format(self.company, self.val)

class Portfolio():
    def __init__(self):
        self.stocklist = []
        
    def add(self,stock):
        if self.stocklist == []:
            self.stocklist = [stock]
        else:
            self.stocklist.append(stock)
    def __str__(self):
        self.outstring = ""
        for stonks in self.stocklist:
            self.outstring += "{}: {}\n".format(stonks.company, stonks.val)
        return self.outstring[:-1]


stock1 = Stock("MSFT", 100)
stock2 = Stock("GOOG", 400)
stock3 = Stock("AAPL", 200)
stock4 = Stock("CSCO", 650)
folio = Portfolio()
folio.add(stock1)
folio.add(stock2)
folio.add(stock3)
folio.add(stock4)
assert str(folio) == "MSFT: 100\nGOOG: 400\nAAPL: 200\nCSCO: 650"
assert str(Portfolio()) == ''
