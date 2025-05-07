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
    def insert(self, key, idx):
        index= self.hashfunction(key)
        if(None in self.arr):
            if(self.arr[self.hashfunction(key)] is None):
                self.arr[self.hashfunction(key)] = Hashtable(key, idx)
                return self.hashfunction(key)
            elif(self.hashfunction(self.arr[index].key) != index):
                displacedkey= self.arr[index].key
                displacedindex= self.arr[index].index
                self.arr[index] = Hashtable(key, -1)
                newindex= self.insert(displacedkey, displacedindex)
                # arr[newindex].index= displacedindex
                i= index # i.e hashfucntionvalue or modulo
                while(1):
                    if(self.arr[i] is not None):
                        if(self.arr[i].index== index):
                            self.arr[i].index= newindex
                            break
                    if(i+1== self.n):
                        i=0
                    else:
                        i+=1
                    if(i==index):
                        break
                return index #return
            prev=self.hashfunction(key)
            i= self.hashfunction(key)
            while(1): 
                if(self.arr[i] is None): #check if new node is inserted or the replaced one throught idx
                    self.arr[i]= Hashtable(key, idx)
                    if(idx==-1):
                        self.arr[prev].index= i
                    return i
                #if key exist then store the index of the last collision in prev so that in future a cahin can be added
                elif((self.arr[i] is not None) and (self.hashfunction(self.arr[i].key) == self.hashfunction(key)) and  (self.arr[i] is not None) and (self.arr[i].index==-1)):
                    prev= i
                if(i+1==self.hashfunction(key)):
                    break    
                if(i+1==self.n):
                    i=0
                else:
                    i+=1        
        else:
            return None
    def search(self, key):
        if(self.arr[self.hashfunction(key)] is not None):
            if(self.arr[self.hashfunction(key)].key == key):
                return self.hashfunction(key)
            #if the key is not it's right position travese and find..
        i= self.hashfunction(key)
        while(1):
            if((self.arr[i] is not None) and (self.arr[i].key == key)):
                return i
            if(i+1 == self.hashfunction(key)):
                break
            if(i+1==self.n):
                i=0
            else:
                i+=1
        return Non
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
            obj.insert(key, -1)
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