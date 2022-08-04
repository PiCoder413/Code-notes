import random as r
import json



EzAddProbs = ['0+0',"2+1","3+1","4+1","5+1","6+1","7+1","8+1","9+1","2+2","3+2","4+2","5+2","6+2","7+2","8+2","9+2","2+3","3+3",'4+3','5+3','6+3','7+3','8+3','9+3','2+4','3+4','4+4','5+4','6+4','7+4','8+4','9+4','2+5','3+5','4+5','5+5','6+5','7+5','8+5','9+5','2+6','3+6','4+6','5+6','6+6','7+6','8+6','9+6','2+7','3+7','4+7','5+7','6+7','7+7','8+7','9+7','2+8','3+8','4+8','5+8','6+8','7+8','8+8','9+8','2+9','3+9','4+9','5+9','6+9','7+9','8+9','9+9']
EzSubProbs = ['10-1','10-2','10-3','10-4','10-5','10-6','10-7','10-8','10-9','9-1','9-2','9-3','9-4','9-5','9-6','9-7','9-8','9-9','8-1','8-2','8-3','8-4','8-5','8-6','8-7','8-8','7-1','7-2','7-3','7-4','7-5','7-6','7-7','6-1','6-2','6-3','6-4','6-5','6-6','5-1','5-2','5-3','5-4','5-5','4-1','4-2','4-3','4-4','3-1','3-2','3-3','2-1','2-2','1-1']
EzMulProbs = ['0*0',"2*1","3*1","4*1","5*1","6*1","7*1","8*1","9*1","2*2","3*2","4*2","5*2","6*2","7*2","8*2","9*2","2*3","3*3",'4*3','5*3','6*3','7*3','8*3','9*3','2*4','3*4','4*4','5*4','6*4','7*4','8*4','9*4','2*5','3*5','4*5','5*5','6*5','7*5','8*5','9*5','2*6','3*6','4*6','5*6','6*6','7*6','8*6','9*6','2*7','3*7','4*7','5*7','6*7','7*7','8*7','9*7','2*8','3*8','4*8','5*8','6*8','7*8','8*8','9*8','2*9','3*9','4*9','5*9','6*9','7*9','8*9','9*9']
exp = 0
Math_Bucks = 0

rank = ["ROOKIE","BRONZE I","BRONZE II","BRONZE III","SILVER I","SILVER II","SILVER III","GOLD I","GOLD II","GOLD III","CRYSTAL I","CRYSTAL II","CRYSTAL III","MASTER I","MASTER II","MASTER III","CHAMPION I","CHAMPION II","CHAMPION III","TITAN I",'TITAN II',"TITAN III","LEGEND"]

pets = ["Dragon($1250, Mythical)","Unicorn($1250, Mythical)","Hydra($1250, Mythical)","Phoniex($1250, Mythical)","Griffin($750, Legendary)","Elemental Golem($750, Legendary)","Alpha Wolf($750, Legendary)","Peagasus($750, Legendary)","Rainbow Horse($500, Epic)","Cenetaur($500, Epic)","KungFu Panda($500, Epic)","Lizard($250, Rare)","Kitten($100, Common)","Puppie($100, Common)"]
valid_pet = ["dragon","unicorn","hydra","phoniex","griffin","elemental golem","alpha wolf","peagasus","rainbow horse","cenetaur","kungfu panda","lizard","kitten","puppie"]
prices = [1250,750,500,250,100]
def JsonLoad():
    with open("MathGameKidsStats.json","r") as f:
        try:
            data = json.load(f)
            return data
        except:
            return {}

data = JsonLoad()


def shop():
   while True:
        for pet in pets:
            print(pet)
    
        purchase = input("What would you like to purchase. You must input the name of the animal. ").lower()
        if valid_pet.count(purchase) < 1:
            print( '\n' + "Invalid pet." + "\n")
            continue
        else:
            if data["pets"].count(purchase) > 0:
                print('\n' + "You already have this pet" + "\n")
                continue
            else:
                confirm = input("Are you sure you want to purchase this pet? y/n ")
                if confirm.lower() == "y" or confirm.lower() == "yes":
                    if purchase == valid_pet[0]:
                        if data["Mathbucks"] < 1250:
                            print("\n" + "You can not afford this!!!" + "\n")
                            continue
                        else:
                            data["Mathbucks"] = data["Mathbucks"] - 1250
                            data["pets"] = data["pets"] + [purchase]
                            with open("MathGameKidsStats.json","w") as f:
                                json.dump(data, f)
                            print("\n" + "Purchase succsess!" + "\n")
                            print("You now have: " + str(data["pets"]) + "\n")
                   
                    elif purchase == valid_pet[1]:
                        if data["Mathbucks"] < 1250:
                            print("You can not afford this!!!" + "\n")
                            continue
                        else:
                            data["Mathbucks"] = data["Mathbucks"] - 1250
                            data["pets"] = data["pets"] + [purchase]
                            with open("MathGameKidsStats.json","w") as f:
                                json.dump(data, f)
                            print("\n" + "Purchase succsess!" + "\n")
                            print("You now have: " + str(data["pets"]) + "\n")
                    
                    elif purchase == valid_pet[2]:
                        if data["Mathbucks"] < 1250:
                            print("You can not afford this!!!" + "\n")
                            continue
                        else:
                            data["Mathbucks"] = data["Mathbucks"] - 1250
                            data["pets"] = data["pets"] + [purchase]
                            with open("MathGameKidsStats.json","w") as f:
                                json.dump(data, f)
                            print("\n" + "Purchase succsess!" + "\n")
                            print("You now have: " + str(data["pets"]) + "\n")
                    
                    elif purchase == valid_pet[3]:
                        if data["Mathbucks"] < 1250:
                            print("You can not afford this!!!" + "\n")
                            continue
                        else:
                            data["Mathbucks"] = data["Mathbucks"] - 1250
                            data["pets"] = data["pets"] + [purchase]
                            with open("MathGameKidsStats.json","w") as f:
                                json.dump(data, f)
                            print("\n" + "Purchase succsess!" + "\n")
                            print("You now have: " + str(data["pets"]) + "\n")
                    
                    elif purchase == valid_pet[4]:
                        if data["Mathbucks"] < 750:
                            print("You can not afford this!!!" + "\n")
                            continue
                        else:
                            data["Mathbucks"] = data["Mathbucks"] - 750
                            data["pets"] = data["pets"] + [purchase]
                            with open("MathGameKidsStats.json","w") as f:
                                json.dump(data, f)
                            print("\n" + "Purchase succsess!" + "\n")
                            print("You now have: " + str(data["pets"]) + "\n")
                    
                    elif purchase == valid_pet[5]:
                        if data["Mathbucks"] < 750:
                            print("You can not afford this!!!" + "\n")
                            continue
                        else:
                            data["Mathbucks"] = data["Mathbucks"] - 750
                            data["pets"] = data["pets"] + [purchase]
                            with open("MathGameKidsStats.json","w") as f:
                                json.dump(data, f)
                            print("\n" + "Purchase succsess!" + "\n")
                            print("You now have: " + str(data["pets"]) + "\n")
                    
                    elif purchase == valid_pet[6]:
                        if data["Mathbucks"] < 750:
                            print("You can not afford this!!!" + "\n")
                            continue
                        else:
                            data["Mathbucks"] = data["Mathbucks"] - 750
                            data["pets"] = data["pets"] + [purchase]
                            with open("MathGameKidsStats.json","w") as f:
                                json.dump(data, f)
                            print("\n" + "Purchase succsess!" + "\n")
                            print("You now have: " + str(data["pets"]) + "\n")
                    
                    elif purchase == valid_pet[7]:
                        if data["Mathbucks"] < 750:
                            print("You can not afford this!!!" + "\n")
                            continue
                        else:
                            data["Mathbucks"] = data["Mathbucks"] - 750
                            data["pets"] = data["pets"] + [purchase]
                            with open("MathGameKidsStats.json","w") as f:
                                json.dump(data, f)
                            print("\n" + "Purchase succsess!" + "\n")
                            print("You now have: " + str(data["pets"]) + "\n")
                    
                    elif purchase == valid_pet[8]:
                        if data["Mathbucks"] < 750:
                            print("You can not afford this!!!" + "\n")
                            continue
                        else:
                            data["Mathbucks"] = data["Mathbucks"] - 750
                            data["pets"] = data["pets"] + [purchase]
                            with open("MathGameKidsStats.json","w") as f:
                                json.dump(data, f)
                            print("\n" + "Purchase succsess!" + "\n")
                            print("You now have: " + str(data["pets"]) + "\n")
                    
                    elif purchase == valid_pet[9]:
                        if data["Mathbucks"] < 500:
                            print("You can not afford this!!!" + "\n")
                            continue
                        else:
                            data["Mathbucks"] = data["Mathbucks"] - 500
                            data["pets"] = data["pets"] + [purchase]
                            with open("MathGameKidsStats.json","w") as f:
                                json.dump(data, f)
                            print("\n" + "Purchase succsess!" + "\n")
                            print("You now have: " + str(data["pets"]) + "\n")
                    
                    elif purchase == valid_pet[10]:
                        if data["Mathbucks"] < 500:
                            print("You can not afford this!!!" + "\n")
                            continue
                        else:
                            data["Mathbucks"] = data["Mathbucks"] - 500
                            data["pets"] = data["pets"] + [purchase]
                            with open("MathGameKidsStats.json","w") as f:
                                json.dump(data, f)
                            print("\n" + "Purchase succsess!" + "\n")
                            print("You now have: " + str(data["pets"]) + "\n")
                    
                    elif purchase == valid_pet[11]:
                        if data["Mathbucks"] < 500:
                            print("You can not afford this!!!" + "\n")
                            continue
                        else:
                            data["Mathbucks"] = data["Mathbucks"] - 500
                            data["pets"] = data["pets"] + [purchase]
                            with open("MathGameKidsStats.json","w") as f:
                                json.dump(data, f)
                            print("\n" + "Purchase succsess!" + "\n")
                            print("You now have: " + str(data["pets"]) + "\n")
                    
                    elif purchase == valid_pet[12]:
                        if data["Mathbucks"] < 250:
                            print("You can not afford this!!!" + "\n")
                            continue
                        else:
                            data["Mathbucks"] = data["Mathbucks"] - 250
                            data["pets"] = data["pets"] + [purchase]
                            with open("MathGameKidsStats.json","w") as f:
                                json.dump(data, f)
                            print("\n" + "Purchase succsess!" + "\n")
                            print("You now have: " + str(data["pets"]) + "\n")
                    
                    elif purchase == valid_pet[13]:
                        if data["Mathbucks"] < 100:
                            print("You can not afford this!!!" + "\n")
                            continue
                        else:
                            data["Mathbucks"] = data["Mathbucks"] - 100
                            data["pets"] = data["pets"] + [purchase]
                            with open("MathGameKidsStats.json","w") as f:
                                json.dump(data, f)
                            print("\n" + "Purchase succsess!" + "\n")
                            print("You now have: " + str(data["pets"]) + "\n")
                    
                    elif purchase == valid_pet[14]:
                        if data["Mathbucks"] < 100:
                            print("You can not afford this!!!" + "\n")
                            continue
                        else:
                            data["Mathbucks"] = data["Mathbucks"] - 100
                            data["pets"] = data["pets"] + [purchase]
                            with open("MathGameKidsStats.json","w") as f:
                                json.dump(data, f)
                            print("\n" + "Purchase succsess!" + "\n")
                            print("You now have: " + str(data["pets"]) + "\n")
                else:
                    continue

        





#The more you practice in one session. The more Exp and Mathbucks you earn!!!
def practice(level):
    global exp
    global Math_Bucks
    
    

    while True:
        if level == "easy":
            while True:
                operation = input("Addition(a),Subtraction(s),Multiplication(m),Divison(d)").lower()
                if operation == "a":
                    equationAE = EzAddProbs[r.randint(0,len(EzAddProbs))-1]
                    print(equationAE)
                    answer = input("What is the answer? ")
                    if answer == str(eval(equationAE)):
                        print("Correct!")
                        exp = exp + 2
                        data["exp"] = exp + data["exp"]
                        data["Mathbucks"] = data["Mathbucks"] + 1
                        with open("MathGameKidsStats.json","w") as f:
                            json.dump(data, f )

                        print("Exp: {e}| Mathbucks: {m}".format(e= data["exp"],m=data["Mathbucks"]))
                        continue

                    else:
                        print("Incorrect")
                        print("Correct answer: {answer}".format(answer = str(eval(equationAE))))
                        continue
                elif operation == "s":
                    equationSE = EzSubProbs[r.randint(0,len(EzSubProbs))-1]
                    print(equationSE)
                    answer = input("What is the answer? ")
                    if answer == str(eval(equationSE)):
                        print("Correct!")
                        exp = exp + 2
                        data["exp"] = exp + data["exp"]
                        data["Mathbucks"] = data["Mathbucks"] + 1
                        with open("MathGameKidsStats.json","w") as f:
                            json.dump(data, f )

                        print("Exp: {e}| Mathbucks: {m}".format(e=data["exp"],m=data["Mathbucks"]))
                        continue
                

                    else:
                        print("Incorrect")
                        print("Correct answer: {answer}".format(answer = str(eval(equationSE))))
                        continue
                elif operation == "m":
                    equationME = EzMulProbs[r.randint(0,len(EzMulProbs))-1]
                    print(equationME)
                    answer = input("What is the answer? ")
                    if answer == str(eval(equationME)):
                        print("Correct!")
                        exp = exp + 5
                        data["exp"] = exp + data["exp"]
                        data["Mathbucks"] = data["Mathbucks"] + 2
                        with open("MathGameKidsStats.json","w") as f:
                            json.dump(data, f )

                        print("Exp: {e}| Mathbucks: {m}".format(e=data["exp"],m=data["Mathbucks"]))
                        continue

                    else:
                        print("Incorrect")
                        print("Correct answer: {answer}".format(answer = str(eval(equationME))))
                        continue

                        







    











while True:
    continue_or_not = input("Do you want to continue or not(yes or no)? ")
    if continue_or_not.lower() == "no":
        print("Come back later!")
        break
    
    mode = input("PRACTICE, SHOP, or view STATS ")
    if mode.lower() == "practice":
        level = input("EASY, MEDIUM, HARD ")
        practice(level)
        
    if mode.lower() == "shop":
        shop()
    
    if mode.lower() == "stats":
        print(data)
        continue

    


     
