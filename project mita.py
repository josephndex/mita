name = input("Enter user name: ")
#i am joseph
print(name)
password = input("Enter password: ")

while True:
    rep = input("Repeat password: ")
    if rep == password:
        print("Correct, welcome " + name)
        break  # Exit the loop if the passwords match
    else:
        print("Passwords do not match. Please try again.")
print("hi"+name)
day=input("how was your day "+name + "(good,bad)")
if day=="good":
    joke1=input("thats good to hear can i tell you a joke to make it even better "+"(yes,no)")
    if joke1=="yes":
        print("hujui jokes")
    elif joke1=="no":
        print("mschew")
elif day!="good":
    joke1=input("can i tell you tell you a joke to lighten your mood"+"(yes , no)")
    if joke1=="yes":
        print("hakuna hadi please na una tumia free plan mschew broke person")
        input("sema please")
        print("bado unangoja joke :) ANGUKA NAYO")
    elif joke1=="no":
        print("mschew broke person unathan nakusuka na unatumia free plan")
print("this is a free plan kindly select from the options listed the service u want brokiee:)")
print("calculator")
print("age calc")
print("wheight calc")
print("kukatiwa")
anss=input("?")
if anss=="calculator":
  while True:#while true is only usee to start a loop
    first = float(input("first number?=> "))
    sec = float(input("second number?=> "))
    opr = input("enter operation? +, -, *, /,=> ")
    
    if opr == "+":
        total = first + sec
    elif opr == "-":
        total = first - sec
    elif opr == "*":
        total = first * sec
    elif opr == "/":
        total = first / sec
    else:
        print("invalid operation.")
        continue  # Skip the rest of the loop and start over
    
    print(total)
    
    # Ask if the user wants to perform another calculation
    another = input("Do you want to perform another calculation? (yes/no) ")
    if another.lower() != "yes":
        break  # Exit the loop if the user doesn't want to continue
elif anss==("age calc"):
    while True:
     year=float(input("anter the year you were born? "))
     if 1901 < year < 1930:
          print("The Greatest Generation u sure u aint dead though ;0")
     elif 1931 < year < 1949:
        print("The Silent Generation: were were you watu wakiiba mashamba  sai ucould have being using the premium plan :(")
     elif 1950 < year < 1964:
        print("Baby Boomers how were the wazugus.btw  were were you watu wakiiba shamba sai ucould have being using the premium plan")
     elif 1965 < year < 1980:
        print("Generation X how was jomo kenyata? hadi wewe  were were you watu wakiiba shamba sai ucould have being using the premium plan ")
     elif 1981 < year < 1996:
        print("Millennials mwanake :)")
     elif 1997 < year < 2012:
        print("Generation Z respect")
     elif 2013 < year < 2025:
        print(" ulikuwa wapi watu wakizaliwa ")
     else:
        print("invalid try again")
        continue
     age=2024-year
     print(age) 
     another = input("Do you want to perform another calculation? (yes/no) ")
     if another.lower() != "yes":
        break  # Exit the loop if the user doesn't want to continue
if anss=="wheight calc":
   while True:
    weight=float(input("what is your wheight? "))
    element=input("is it in kg or lbs? ").lower()
    if element== "kg":
      sum=weight*2.2046 
      print("your weight is "+str(sum)+"lbs")#convert sum wich is an int to a string
      if 20<=sum<=80:
        print("eiiiiii when is the burial")
      elif 81<=sum<=159:
        print(" healthy guy am proud")
      elif 160<=sum<=600:
       print("good for you salad is cheaper though")
    elif element== "lbs":
      sum=weight/2.2046
      print("your weight is "+str(sum)+"lbs")
      if 10<=sum<=40:
        print("eiiiiii when is the burial")
      elif 41<=sum<=80:
        print("umekonda")
      elif 81<=sum<=300:
         print("good for you salad is cheaper though")
    else:
       print("try again")
    another = input("Do you want to perform another calculation? (yes/no) ")
    if another.lower() != "yes":
        break  # Exit the loop if the user doesn't want to continue
if anss=="kukatiwa":
   while True:
      name=input("what is your name? ")
      print("nice to meet you "+ name)
      ans=input(name +" are you single by any chance? ")
      if ans.lower() == "yes":
       print("lucky me")
      elif ans.lower() == "no":
       print("we both know am the better one "+ name)
      another = input("Do you want to try again? (yes/no) ")
      if another.lower() != "yes":
        break  # Exit the loop if the user doesn't want to continue
elif anss=="none":
   print(f"have a wonderfull day {name}")



    