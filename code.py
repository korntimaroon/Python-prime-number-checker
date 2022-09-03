def getCheck(p):  
  if p > 1:  
    for i in range(2, int(p/2) + 1):  
      if (p % i) == 0:  
        print(p, "is not a prime number")
        break  
      else:  
        print(p, "is a prime number")   
  else:  
    print(p, "is not a prime number")  

while True:
  p = int(input("Enter prime number:"))  
  getCheck(p)  
