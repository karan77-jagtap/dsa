class PhoneBook:
    def __init__(self, name, tellNo):
        self.name=name
        self.tellNo= tellNo    
class HashTable:
    def __init__(self, n):
        self.n=n
        self.arr= [None]*n 
    def h1(self, key):
        return (key %self.n)
    def hashfuntion(self, key, i):
        h2= 7 - (key% 7)
        return (self.h1(key)+ (i*h2))%self.n
    def insert(self, name, telNo):
        if(self.arr[self.h1(telNo)] is None):
            self.arr[self.h1(telNo)]= PhoneBook(name, telNo)
            print("Strored!")
            return
        i=1
        while(i<self.n):
            if(self.arr[self.hashfuntion(telNo, i)] is None):
                self.arr[self.hashfuntion(telNo, i)]= PhoneBook(name, telNo)

                print("Stored after collision!")
                break
                return
            i+=1 
    def display(self):
        for i in range(0, self.n):
            if(self.arr[i] is None):
                print(i, ":  -   -")
            else:
                print(i, ": ", self.arr[i].name, " ", self.arr[i].tellNo)
    def search(self, telNo):
        if(self.arr[self.h1(telNo)] != None):
            if(self.arr[self.h1(telNo)].tellNo== telNo):
                return self.h1(telNo)
            
        i=1
        while(i<self.n):
            if(self.arr[self.hashfuntion(telNo, i)] is not None):
                if(self.arr[self.hashfuntion(telNo, i)].tellNo == telNo):
                    return self.hashfuntion(telNo, i)
            i+=1
        return None

    def delete(self, key):
        index= self.search(key)
        if(index==None):
            print("No such entry found!")
            return
        else:
            self.arr[index]= None
            print("Entry at ", index, " is deleted!")
            return
obj= HashTable(10)
while(1):
    print("-----------------\n\t1: Input \n\t2: Display\n\t3: Search\n\t4: Delete\n   -1: Exit")
    ch= int(input("Enter choice: "))
    if(ch==1):
        tel= int(input("Enter Mobile No: "))
        name=input("Enter Name: ")
        obj.insert(name, tel)
    elif(ch==2):
        obj.display()
    elif(ch==3):
        key=int(input("Emter Mobile No. to Search: "))
        print(obj.search(key))
    elif(ch==4):
        key= int(input("Enter Mobile No to be deletd: "))
        obj.delete(key)
    elif(ch==-1):
        print("====End-====")
        break
1