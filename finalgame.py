
import random
import serial


port = "/dev/ttyACM0"  ### Circuit Playground Express
ser = serial.Serial(port, 115200, timeout=4)

def cpxcommand(command):
    sercommand = (command + '\r\n').encode()
    ser.write(sercommand)

def print_welcome(name):
    print("Hello" ,name ,"lets start our guessing game")

def print_options():
    print("Select your options below")
    print("'W' Guess names of wild animals")
    print("'C' Guess name of countries")
    print("'q' quit the program")

def start_wild(name):
    print(name + ", you may start guesing  names of wild animals\n")

def start_countries(name):
    print(name + ", you may start guesing  names of countries\n")

def guess_animals():
    wild_animals = ["ELEPHANT", "TIGER", "DEER", "MONKEY", "BEAR", "KANGAROO", "RHINOCEROS", "HIPPOPOTAMUS", "ZEBRA","HEDGEHOG", "REINDEER", "BADGER", "GORILLA", "CROCRODILE", "SNAKE" , "ALLIGATOR", "WOODPECKER" ,"SHARK" ," WOLF" ,"LEOPARD" ,"ANTELOPE" ,"JELLYFISH" ,"WALRUS"]
    sec_word = random.choice(wild_animals)
    guesses = random.sample(sec_word, 3)
    no_of_life = 7
    
    while no_of_life != 0:
        failed = 0
        
        for letter in sec_word:
            if letter in guesses:
                
                print (letter,)
            else:
                print ("_"),
                failed += 1
        if failed == 0:
            print ("\n You won.")
            no_of_life == 0
            break

        guess = input("\n\n Guess the next character:")
        guesses += guess
        if guess not in sec_word:
            no_of_life = no_of_life - 1
            print ("\n You were wrong, you still have " + str(no_of_life) + " lives")
            if no_of_life == 0:
                cpxcommand("lost")
                print("You lose")
        else:
            print("you guessed right")
                

                

def guess_countries():
    countries = ["AFGHANISTAN", "ANGOLA", "ARGENTINA", "AUSTRALIA", "BENIN", "BELGIUM", "BRAZIL", "CANADA", "CHINA","CONGO", "DENMARK", "ETHIOPIA", "EGYPT", "GHANA", "GERMANY" , "HONDURAS", "HUNGARY" ,"ICELAND" ," JAMAICA" ,"LEBANON" ,"LUXEMBOURG" ,"MADAGASCAR" ,"NIGERIA","KOREA" ,"OMAN" ,"PARAGUAY" ,"ROMANIA" ,"GRENADINES" ,"SINGAPORE" ,"TANZANIA"]
    sec_word = random.choice(countries)
    guesses = random.sample(sec_word, 3)

    no_of_life = 7
    
    while no_of_life != 0:
        failed = 0
        
        for letter in sec_word:
            if letter in guesses:
                
                print (letter,)
            else:
                print ("_"),
                failed += 1
        if failed == 0:
            print ("\n You won.")
            no_of_life == 0
            break

        guess = input("\n\n Guess the next character:")
        guesses += guess
        if guess not in sec_word:
            no_of_life = no_of_life - 1
            print ("\n You were wrong, you still have " + str(no_of_life) + " lives")
            if no_of_life == 0:
                cpxcommand("lost")
                print("You lose")
        else:
            print("you guessed right")
             #print ("\n You were wrong, you still have " + str(no_of_life) + " lives")

#print ("Welcome " + name + ".")

#print (name + ", you may start guesing \n")

name = input("What is your name  dear friend: ")
name = name.capitalize()
print_welcome(name)

choice = "p"
while choice != "q":
    if choice == "W":
        start_wild(name)
        guess_animals()
    elif choice == "C":
        start_countries(name)
        guess_countries()
    elif choice != "q":
        print_options()
    choice = input("options: ")
        
