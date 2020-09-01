class Jar:
    '''represents a jar'''
   
    def __init__(self,jarCapacity):
        '''Jar(startCapacity) -> Jar
        constructs a Jar
        jarCapacity: int giving capacity of jar in liters'''
        self.capacity = jarCapacity # store capacity attribute
        self.liters = 0 # jar empty at beginning

    def __str__(self):
        '''str(Jar) -> str
        returns a string giving capacity of and liters of water in jar'''
        # contains string to return
        answer = str(self.capacity) 
        answer += '-liter jar with '
        answer += str(self.liters)
        answer += ' liters of water'
        return answer

    def fill_jar(self):
        '''Jar.fill_jar()
        completely fills jar'''
        self.liters = self.capacity # set liters of water in jar to capacity

    def empty_jar(self):
        '''Jar.empty_jar()
        completely empties jar'''
        self.liters = 0 # set liters of water in jar to 0

    def pour_into_jar(self,other):
        '''Jar.pour_into_jar(Jar)
        pours water from jar into other jar until jar is empty or other jar is full'''
        while self.liters > 0 and other.liters < other.capacity: # if jar isn't empty or other jar isn't full
            # pour 1 liter at a time
            self.liters -= 1
            other.liters += 1

def jar_puzzle():
    '''jar_puzzle() -> int
    solves jar puzzle with 3-liter and 5-liter jars'''
    jarOne = Jar(3) # create 3-liter jar
    jarTwo = Jar(5) # create 5-liter jar
    while jarTwo.liters != 4: # if puzzle not solved
        # fill jar 2
        jarOne.fill_jar()
        jarOne.pour_into_jar(jarTwo)
        # empty jar 2 once full and pour remaining liters in jar 1 into jar 2
        if jarTwo.liters == jarTwo.capacity:
            jarTwo.empty_jar()
            jarOne.pour_into_jar(jarTwo)
    return jarTwo.liters

# test cases
myJar = Jar(2)
myOtherJar = Jar(3)
print(myJar)
myJar.fill_jar()
myOtherJar.fill_jar()
print(myJar)
myJar.empty_jar()
print(myJar)
myOtherJar.pour_into_jar(myJar)
print(myOtherJar,myJar)
print(jar_puzzle())    
