

# code goes here
number = int(input("Please enter a number: "))

def findPrime(number):
    isPrime = True
    for num in range(2, number):
        if (number % num) == 0:
            isPrime = False
            break
    if isPrime: 
        print("this is a prime number")
    else:
        print("this is not a prime number")
        

findPrime(number)
        
    
        
        