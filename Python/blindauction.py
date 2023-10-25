from asciiart import logo_hammer
import os
print(logo_hammer)
print("\nWelcome to the secret auction program.")
choice =True
dict={}

def find_max_bid():
    max=0
    nm=""
    for i in dict:
        if int(dict[i])>max:
            max=int(dict[i])
            nm=i
    max_bid=max
    max_name=nm
    print(f"The Winner is {max_name} with a bid of ${max_bid}.")
    
while choice:
    name=input("What is your name?: ")
    bid=input("What is your bid?: $")
    dict[name]=bid
    ch=input("\nAre there any other bidders? Type 'yes' or 'no'.")
    if ch=='no':
        choice=False
    os.system('cls')
find_max_bid()
