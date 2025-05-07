class Telephone:
    def __init__(self, name, telNo):
        self.name= name
        self.telNo= telNo
class HashTable:
    def __init__(self, size):
        self.n= size
        self.arr= [None]*self.n
    

    def hashFunction(self, telNo):
        return (telNo % 10)

    def insert(self, name, telNo):
        if(self.arr[self.hashFunction(telNo)] is None):
            self.arr[self.hashFunction(telNo)]=Telephone(name, telNo)
            print("Stored!")
        else:
            position= self.hashFunction(telNo)
            while(1):
                if(self.arr[position] is None):
                    self.arr[position]= Telephone(name, telNo)
                    print("Stored after collision!")
                    break
                if(position+1 == self.hashFunction(telNo)):
                    break
                if(position+1 == self.n):
                    position=0
                else:
                    position+=1
    def display(self):
        for i in range(0, self.n):
            if(self.arr[i] is None):
                print(i, ":   -    -")
            else:
                print(i, ": ", self.arr[i].name, " ", self.arr[i].telNo)

    def search(self, telNo):
        if(self.arr[self.hashFunction(telNo)] != None):
            if(self.arr[self.hashFunction(telNo)].telNo == telNo):
                
                return self.hashFunction(telNo)
            
        position= self.hashFunction(telNo)
        i=0
        while(i<self.n):
            if(self.arr[position]!= None):
                if(self.arr[position].telNo == telNo):
                    
                    return position
                    break
                
            if(position+1 == self.n-1):
                position=0
            position= (position+1)%self.n
            i+=1
        return None
        
    def delete(self, telNo):
        index= self.search(telNo)
        if(self.arr[index].telNo == telNo):
            self.arr[index] = None
        else:
            print("No such entry found")
    def get(self, telNo):
        position=self.search(telNo)
        if(position!=None):
            print(position, ": ", self.arr[position].name, self.arr[position].telNo)
            return
        print("No such entry Found!")
def main():
    obj= HashTable(10)
    while(1):
        print("-----------------\n\t 1: Input \n\t 2: Display\n\t 3: Search\n\t 4: Delete\n\t-1: Exit\n-------------")
        ch=int(input("\nEnter choice: "))
        if(ch==1):
            telNo=int(input("Enter mobile no: "))
            name= input("Enter name: ")
            obj.insert(name, telNo)
        elif(ch==2):
            obj.display()
        elif(ch==3):
            findTel= int(input("Enter telNo to be searched: "))
            obj.get(findTel)
        elif(ch==4):
            findTel= int(input("Enter telNo to be deleted: "))
            obj.delete(findTel)
        elif(ch==-1):
            print("====END====")
            break
main()