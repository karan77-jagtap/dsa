class Hashtable:
    def __init__(self, key, index):
        self.key=key
        self.index= index
class Table:
    def __init__(self, n):
        self.n=n
        self.arr= [None]*self.n
        
    def hashfunction(self, d):
        return d%self.n    

    def insert(self, key):
        if(None in self.arr):
            if(self.arr[self.hashfunction(key)] is None):
                self.arr[self.hashfunction(key)] = Hashtable(key, -1)
                return
            else:
                prev=self.hashfunction(key)
                i= self.hashfunction(key)
                while(1):
                    if(self.arr[i] is None):
                        self.arr[i]= Hashtable(key, -1)
                        self.arr[prev].index= i
                        return
                    elif((self.hashfunction(self.arr[i].key) == self.hashfunction(key)) and  (self.arr[i] is not None) and (self.arr[i].index==-1)):
                        prev= i
                        
                    if(i+1==self.hashfunction(key)):
                        break    
                    if(i+1==self.n):
                        i=0
                    else:
                        i+=1
        
    def display(self):
        for i in range(0, self.n):
            if(self.arr[i] is None):
                print(i, ": -   -")
            else:
                print(i, ": ", self.arr[i].key, " ", self.arr[i].index)
                
    def delete(self, key):
        s= self.search(key)
        self.arr[s]= None
        print("Deleted key ", key, " from index ", s)
                
def main():
    n= int(input("Enter size of table: "))
    obj= Table(n)
    while(1):
        print("\t----------------")
        print("\t 1: Insert")
        print("\t 2: Display")
        print("\t 3: Search")
        print("\t 4: Delete")
        print("\t-1: Delete")
        print("\t----------------")
        
        ch= int(input("Enter choice: "))
        if(ch==1):
            key= int(input("Enter data: "))
            obj.insert(key)
        elif(ch==2):
            obj.display()
        elif(ch==3):
            k= int(input("Enter key to be searched: "))
            res= obj.search(k)
            if(res is None):
                print("Key not found!")
            else:
                print(k, " found at index ", res)
        elif(ch==4):
            k= int(input("Enter key to be deleted: "))
            res= obj.search(k)
            if(res is None):
                print("Key not found!")
            else:
                obj.delete(k)
                print(k, " deleted from index ", res)
        elif(ch==-1):
            print("-------------END------------")
            break
main()