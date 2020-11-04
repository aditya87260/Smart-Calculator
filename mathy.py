responses=["Welcome to smart calculator","My name is harry","Thanks","Sorry! this is beyond my ability","My friends are Aditya and Sunaina" ,"Ananya and Antariksh are the best friend of Sunaina","No one:("]
def extract_numbers_from_text(text):
  l=[]
  for t in text.split(' '):
      try:
         l.append(float(t))
      except ValueError:
         pass
  return (l)

def lcm(a,b):
  lcm=(a*b)/HCF(a,b)
  return lcm


def HCF(a,b):
    while(b):
      a,b=b,a%b
    return a   
   
def add(a,b):
 return a+b

def sub(a,b):
 return a-b

def multiply(a,b):
 return a*b

def division(a,b):
 return a/b

def perimeter_rectangle(a,b):
   return 2*(a+b)

def fact(n):
 if n==0:
   return 1
 else:
   return n*fact(n-1)

def square(n):
 return n*n

def end():
  print(responses[2])
  input("press enter key to exit")
  exit()

def myname():
    print(responses[1])

def sorry():
    print(responses[3])
    
def friend():
    print(responses[4])
    
def friend_1():
    print(responses[5])

def friend_2():
    print(responses[6])



operations={"PlUS":add, "ADD":add, "ADDITION":add, "SUM":add, "MINUS":sub, "SUBSTRACTION":sub ,"SUBSTRACT":sub, "DIFFERENCE":sub ,"MULTIPLICATION":multiply ,"MULTIPLY":multiply ,"PRODUCT":multiply,
              "DIVIDE":division,"DIVISION":division, "LCM":lcm ,"HCF":HCF,"PERIMETER":perimeter_rectangle}

commands={"NAME":myname ,"END":end,"FRIEND":friend,"SUNAINA":friend_1,"ADITYA":friend_2}

facto={"FACT":fact,"FACTORIAL":fact,"SQUARE":square}

            
