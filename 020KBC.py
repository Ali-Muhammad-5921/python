questions = ["1. What house is Hermione Granger in?",
             "2. Who is the Headmaster of Hogwarts during most of Harry's time there?",
             "3. What is the name of Ron Weasley's pet rat?",
             "4. Who teaches Potions in Harry's first year?",
             "5. What form does Harry's Patronus take?",
             "6. What magical object shows the deepest desires of a person's heart?",
             "7. What is Dumbledore's full name?",
             "8. What is the name of the goblin who helps Harry break into Gringotts?",
             "9. What does the spell 'Sectumsempra' do?",
             "10. Which Deathly Hallow does Harry possess first?",] 

q1options = ["1.Ravenclaw","2.Gryffindor","3.Hufflepuff","4.Slytherin"]
q2options = ["1.Severus Snape","2.Albus Dumbledore","3.Horace Slughorn","4.Minerva McGonagall"]
q3options = ["1.Scabbers","2.Crookshanks","3.Trevor","4.Fang"]
q4options = ["1.Severus Snape","2.Gilderoy Lockhart","3.Remus Lupin","4.Quirinus Quirrell"]
q5options = ["1.Phoenix","2.Rabbit","3.Stag","4.Wolf"]
q6options = ["1.The Time-Turner","2.The Mirror of Erised","3.The Philosopher's Stone","4.The Pensieve"]
q7options = ["1.Albus Percival Brian Dippet Dumbledore","2.Albus Percival Wulfric Brian Dumbledore","3.Albus Brian Wulfric Percival Dumbledore","4.Albus Wulfric Percival Brian Grindelwald"]
q8options = ["1.Ragnok","2.Griphook","3.Bogrod","4.Gnarlak"]
q9options = ["1.Makes the target silent","2.Paralyzes the target","3.Causes deep slashing wounds","4.Binds the target with ropes"]
q10options = ["1.The Invisibility Cloak","2. The Elder Wand","3.The Resurrection Stone","4.The Marauder's Map"]


asnwers = [0] * 10
correctAnswers = [2,2,1,1,3,2,2,2,3,1]
score = 0
i = 1 

while i <= 10 :
    if i <= 3:
        print("Question Type : Easy")
    if i > 3 and i <= 7 :
        print("Question Type : Medium")
    if i > 7 :
        print("Question Type : Hard")
    print(questions[i-1].center(50))
    match(i):
        case 1:
            print(q1options[0]+"\t \t \t"+q1options[1]+'\n'+q1options[2]+'\t\t\t '+q1options[3])
            asnwers[0] = int(input('Enter Your Answer (1-4): '))
        case 2:
            print(q2options[0]+"\t \t \t"+q2options[1]+'\n'+q2options[2]+'\t\t\t '+q2options[3])
            asnwers[1] = int(input('Enter Your Answer (1-4): '))
        case 3:
            print(q3options[0]+"\t \t \t"+q3options[1]+'\n'+q3options[2]+'\t\t\t '+q3options[3])
            asnwers[2] = int(input('Enter Your Answer (1-4): '))
        case 4:
            print(q4options[0]+"\t \t \t"+q4options[1]+'\n'+q4options[2]+'\t\t\t '+q4options[3])
            asnwers[3] = int(input('Enter Your Answer (1-4): '))
        case 5:
            print(q5options[0]+"\t \t \t"+q5options[1]+'\n'+q5options[2]+'\t\t\t '+q5options[3])
            asnwers[4] = int(input('Enter Your Answer (1-4): '))
        case 6:
            print(q6options[0]+"\t \t \t"+q6options[1]+'\n'+q6options[2]+'\t\t\t '+q6options[3])
            asnwers[0] = int(input('Enter Your Answer (1-4): '))
        case 7:
            print(q7options[0]+"\t \t \t"+q7options[1]+'\n'+q7options[2]+'\t\t\t '+q7options[3])
            asnwers[0] = int(input('Enter Your Answer (1-4): '))
        case 8:
            print(q8options[0]+"\t \t \t"+q8options[1]+'\n'+q8options[2]+'\t\t\t '+q8options[3])
            asnwers[0] = int(input('Enter Your Answer (1-4): '))
        case 9:
            print(q9options[0]+"\t \t \t"+q9options[1]+'\n'+q9options[2]+'\t\t\t '+q9options[3])
            asnwers[8] = int(input('Enter Your Answer (1-4): '))
        case 10:
            print(q10options[0]+"\t \t \t"+q10options[1]+'\n'+q10options[2]+'\t\t\t '+q10options[3])
            asnwers[9] = int(input('Enter Your Answer (1-4): '))

    i += 1

for i in correctAnswers:
    if asnwers[i] == correctAnswers[i]:
        score += 1
    
if score < 4 :
    print("You're a Muggle .".center(50))
elif score > 4 and score <= 7 :
    print("You're a Half-Blood .")
else :
    print("You're a Potter Head.")