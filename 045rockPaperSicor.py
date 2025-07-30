import random

print('Welcome'.center(50))
print("Let's play Rock , Paper and Sicors ".center(50))

 
while True :
    
    choice = input('\nEnter Your choice :\n 1 for Rock \n 2 for Paper \n 3 for Sicors \n Press q to Quit : ')
    if choice.lower() == 'q':
        print("Thanks for Playing :)")
        break
    if not choice.isdigit() or int(choice) not in [1,2,3]:
        print("\nInvalid Input please choose from numbers 1 , 2 , 3 or q to Quit")
        continue
    
    choice = int(choice)
    
    compChoice = random.randint(1,3)
    match(choice) :
        case 1 :
            if choice == 1 and compChoice == 1 :
                print("\nYou choose Rock and Computer also choose Rock , so it's a draw :/")
            elif choice == 1 and compChoice == 2 :
                print("\nYou choose Rock and Computer choose Papers , so you loose , better luck next time :(")
            elif choice == 1 and compChoice == 3 :
                print("\nYou choose Rock and Computer choose Sicors , Congratulations , you won :)")
        case 2 :
            if choice == 2 and compChoice == 1 :
                print("\nYou choose Papers and Computer choose Rock ,Congratulations , you won :) ")
            elif choice == 2 and compChoice == 2 :
                print("\nYou choose Papers and Computer also choose Papers ,so it's a draw :/ ")
            elif choice == 2 and compChoice == 3 :
                print("\nYou choose Papers and Computer choose Sicors , so you loose , better luck next time :(")
        case 3:
            if choice == 3 and compChoice == 1 :
                print("\nYou choose Sicors and Computer choose Rock , so you loose , better luck next time :(")
            elif choice == 3 and compChoice == 2 :
                print("\nYou choose Sicors and Computer choose Papers , Congratulations , you won :)")
            elif choice == 3 and compChoice == 3 :
                print("\nYou choose Sicors and Computer also choose Sicors , so it's a draw :/")
            
        
