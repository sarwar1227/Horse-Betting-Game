'''Horse Betting Game by SARWAR ALI(github.com/sarwar1227) using Python and MYSQL
           Technologies Required To Run this Code :
 1.Pyhton(32/64 bit) version 2/3+ with mysql module and connector installed
 2.MySql DBMS with Driver for Python(Python Connector)
NOTE : Extra Files(audio) Needed to make this app(game) more interactive are added in the repository too.'''
import random                                       #Module for randomly selecting choice by the computer
import os                                           #Module for performing OS related operation
import time                                         #Module for time related functions
import sys                                          #Module for System related operation
from datetime import datetime as DT                 #Module for Date and time related functions
from playsound import playsound                     #Module for Playing Sounds
import mysql.connector as MS                        #Module for Database Connectivity

#Connecting to Database
DB=MS.connect(host='localhost',user='root',password='''Your Root Password Here''',database='''Create a database named horse_game(create table player_data) and mention here''')
cur=DB.cursor()

os.system("cls")
now=DT.now()

first_name=input("\n Enter Your First Name : ")      #User input for first name
last_name=input("\n Enter Your Last Name : ")        #User input for last name
playsound("start.mp3")                            
name=first_name+" "+last_name
horses=[58,711,525,877,199,888,10]                   #List of horses 
Current_Date=now.strftime("%d"),'/',now.strftime("%m"),'/',now.strftime("%Y")     #Converting date object into string format
Current_Time=now.strftime("%H"),':',now.strftime("%M"),':',now.strftime("%S")     #Converting time object into string format
Month=now.strftime("%b")
Day=now.strftime("%a")
def display_screen():                                #Function for displaying User Interective Screen
    os.system("cls")
    print("\n\tCurrent Date : ",now.strftime("%d"),'/',now.strftime("%m"),'/',now.strftime("%Y"))
    print("\tCurrent Time : ",now.strftime("%H"),':',now.strftime("%M"),':',now.strftime("%S"))
    print("\t  Month : ",now.strftime("%b"),"\tDay : ",now.strftime("%a"))
    print("\n Welcome",name,"to Our Horse Betting Game !!\n")
    print('''\tHorses Available for betting\n\t58  711  525  877  199  888  10\n''')
def main_menu():                                     #Function of main menu/Main Function
    display_screen()
    res=check_choice()
    if res==1:
        try:
            user_choice=int(input("\n Enter Your Betting Horse Number : "))
            betting_amount=int(input("\n Enter Betting Amount : "))
        except ValueError:                            #Exception Handling for User Input
            print("\tInput Other than integer not Allowed !!")
            play_again()
        if (user_choice in horses):
            print(" Horses are Running...Lets Wait and Watch Who Wins The Game..........!!")
            playsound("horse.mp3")
            computer_choice=random.choice(horses)
            print("\tYour Horse Number :",user_choice)
            print("\tWinner Horse Number :",computer_choice)
            if user_choice==computer_choice:
                print("\tYour Horse Won The Race !!")
                amount=2*betting_amount
                print("\tPrice Amount :",amount)
                playsound("win.mp3")

                #INSERTING DATA INTO DATABASE IF USER WINS THE GAME
                cur.execute("insert into player_data(Name,Status,Amount_Won,Date,Time) values (%s,'WON',%s,Current_Date,Current_Time)",(name,amount))
                DB.commit()
            else:
                print("Your Horse Lost The Race....Bad Luck !!....Try Again Next Time")
                amount=betting_amount-betting_amount
                time.sleep(0.1)
                playsound("lose.mp3")

                #INSERTING DATA INTO DATABASE IF USER LOSE THE GAME
                cur.execute("insert into player_data(Name,Status,Amount_Won,Date,Time) values (%s,'LOSS',%s,Current_Date,Current_Time)",(name,amount))
                DB.commit()
            play_again()
        else:
            print(" Horse Number",user_choice,"Not Exist !!")   
            temp3=input()
            main_menu()
    elif res==2:
        DB.close()
        exit_game()
    elif res==3:
        show_history()
        main_menu()
    else:
        print("\tInvalid Choice !!")
        play_again()
def check_choice():                              #Function for checking User Choice for playing game/quitting game/Checking History from database
    temp1=input("\tPress Any Key to Continue.......")
    print("1.Play Game")
    print("2.Quit Game")
    print("3.Check History")
    try:
        x=int(input("Choose Your Option : "))
    except ValueError:                            #Exception Handling for User Input
        print("\tInput Other than integer not Allowed !!")
        pqr=input()
        main_menu()
    return x
def show_history():                              #Function for extracting all the data from database and displaying them
    print("\n\tPLAYING HISTORY RECORDS")

    #EXTRACTING ALL DATA FROM DATABASE
    s="select * from player_data"
    cur.execute(s)
    result=cur.fetchall()
    for rec in result:
        print(rec)
    print("\n")
    xyz=input("Press Any Key.....")
def play_again():                                #Function for checking if user want to play again or not
    temp2=input("\tPress Any Key to Continue.......")
    os.system("cls")
    display_screen()
    print(" Want To Play Again :\n1.Yes\n2.No")
    try:
        ch=int(input("Enter Your Choice : "))
    except ValueError:                           #Exception Handling for User Input
        print("\tInput Other than integer not Allowed !!")
        play_again()
    if ch==1:
        main_menu()
    elif ch==2:
        exit_game()
    else:
        print("\tInvalid Choice !!")
        play_again()
def exit_game():                                  #Function for exit the game
    print(" Exiting...the Game...Thanks For Playing the game")
    playsound("end.mp3")
    time.sleep(0.2)
    sys.exit(" Thanks !! For Playing The Game...")
main_menu()
