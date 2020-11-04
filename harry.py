import sys
sys.path.append('/mymodules/')
import mymodules
from mymodules.mathy import*
print(responses[0])
print(responses[1])
while True:
    print()
    text=input("Hello ! What I can do for you\n")
    for word in text.split(' '):
        if word.upper() in operations.keys():
             try:
                 l=extract_numbers_from_text(text)
                 r=operations[word.upper()](l[0],l[1])
                 print(r)
                
             except:
                 print("Something is wrong please retry")
             finally:
                 break
                
        elif word.upper() in facto.keys():
           try:
             s=extract_numbers_from_text(text)
             p=facto[word.upper()](s[0])
             print(p)
           except:
                 print("Something is wrong please retry")
           finally:
                 break
                
        elif word.upper() in facto.keys():
           try:
             q=extract_numbers_from_text(text)
             n=facto[word.upper()](s[0],s[1],s[2])
             print()
           except:
                 print("Something is wrong please retry")
           finally:
                 break
        elif word.upper() in commands.keys():
             commands[word.upper()]()
             break
        
             
    else:
      sorry()
