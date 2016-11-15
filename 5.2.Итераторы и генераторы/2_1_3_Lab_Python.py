class Reverse():
    def __init__(self, end):
        self.iter = end
    def __iter__(self):
        return self
      
    def next(self):   
        if(self.iter == 0):
            raise StopIteration 
        print(self.iter)
        self.iter += -1 
        return self.iter 
   
    def prev(self):
        self.iter -= 1
        if self.iter < 0:
            raise StopIteration
        return self.iter

simple_iter = Reverse(12)
#simple_iter.next()
#simple_iter.next()
#simple_iter.next()
#simple_iter.next()
#simple_iter.next()
#simple_iter.next()
#simple_iter.next()
#simple_iter.next()
#simple_iter.next()
#simple_iter.next()
#simple_iter.next()
#simple_iter.next()




class Reverse_iterator:
     def __init__(self, collection):
         self.data = collection
         self.index = len(self.data)
     def __iter__(self):
        i = self.index
        while i != 0:
            i-=1
            yield self.data[i]
            
     
for each in Reverse_iterator([1,2,3,4,5,6,7,8,9,10,12,3,4,5]):
     print (each)