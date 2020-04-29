'''Horse Betting Game by SARWAR ALI(github.com/sarwar1227) using Python and MYSQL
           Technologies Required To Run this Code :
 1.Pyhton(32/64 bit) version 2/3+ with mysql module and connector installed
 2.MySql DBMS with Driver for Python(Python Connector)
NOTE : Extra Files(audio) Needed to make this app(game) more interactive are added in the repository too.'''
import random                                          #Module for randomly selecting choice by the computer
import os                                              #Module for performing OS related operation
import time                                            #Module for time related functions
import sys                                             #Module for System related operation
from datetime import datetime as DT                    #Module for Date and time related functions
from playsound import playsound                        #Module for Playing Sounds
import mysql.connector as MS                           #Module for Database Connectivity

#GAME LOGIN PASSWORD
password='1234'

#Connecting to Database
DB=MS.connect(host='localhost',user='root',password='''Your Root Password Here''',database='''Create a database named horse_game(create table player_data) and mention here''')
cur=DB.cursor()

os.system("cls")
flag=True             #GLOBAL variable 
now=DT.now()

first_name=input("\n\n\n\n\t\t\t\t\tEnter Your First Name : ")        #User input for first name
last_name=input("\n\t\t\t\t\tEnter Your Last Name : ")                #User input for last name
playsound("start.mp3")
name=first_name+" "+last_name
horses=[58,711,525,877,199,888,10]           #List of horses
Current_Date=now.strftime("%d"),'/',now.strftime("%m"),'/',now.strftime("%Y")        #Converting date object into string format
Current_Time=now.strftime("%H"),':',now.strftime("%M"),':',now.strftime("%S")        #Converting time object into string format
Month=now.strftime("%b")
Day=now.strftime("%a")
def password_check():                                   #Function for password login checking
    os.system("cls")
    global password
    print("\n\n\n\n\t\t\t\t\tHint : 1234")
    pwd=input("\n\t\t\t\tEnter Password To Enter into Game: ")
    if pwd==password:
        print("\n\t\t\t\tCorrect Password \n\n\t\t\t\tPress any Key To Continue....")
        input()
        return
    else:
        print("\n\t\t\t\t\tWrong Password\n\n\t\t\t\tPress any Key To Retry.....")
        input()
        password_check()
def display_screen():                                    #Function for displaying User Interective Screen
    os.system("cls")
    print("\n\n")
    print("\n\t\t\tCurrent Date : ",now.strftime("%d"),'/',now.strftime("%m"),'/',now.strftime("%Y"))
    print("\t\t\tCurrent Time : ",now.strftime("%H"),':',now.strftime("%M"),':',now.strftime("%S"))
    print("\t  \t\tMonth : ",now.strftime("%b"),"\tDay : ",now.strftime("%a"))
    print("\n \t\tWelcome",name,"to Our Horse Betting Game !!\n")
    print('''\t\t\tHorses Available for betting\n\t\t\t58  711  525  877  199  888  10\n''')
def main_menu():                                          #Function of main menu/Main Function
    display_screen()
    if flag==False:
        res=1
    else:
        res=check_choice()
    if res==1:
        try:
            user_choice=int(input("\n \t\tEnter Your Betting Horse Number : "))
            betting_amount=int(input("\n \t\tEnter Betting Amount : "))
        except ValueError:                                 #Exception Handling for User Input
            print("\t\t\tInput Other than integer not Allowed !!")
            input()
            main_menu()
        if (user_choice in horses):
            print(" \t\tHorses are Running...Lets Wait and Watch Who Wins The Game..........!!")
            playsound("horse.mp3")
            computer_choice=random.choice(horses)
            print("\t\t\tYour Horse Number :",user_choice)
            print("\t\t\tWinner Horse Number :",computer_choice)
            if user_choice==computer_choice:
                print("\t\t\tYour Horse Won The Race !!")
                amount=2*betting_amount
                print("\t\t\tPrice Amount :",amount)
                playsound("win.mp3")

                               #INSERTING DATA INTO DATABASE IF USER WINS THE GAME
                cur.execute("insert into player_data(Name,Status,Amount_Won,Date,Time) values (%s,'WON',%s,Current_Date,Current_Time)",(name,amount))
                DB.commit()
            else:
                print("\t\tYour Horse Lost The Race....Bad Luck !!....Try Again Next Time")
                amount=betting_amount-betting_amount
                time.sleep(0.1)
                playsound("lose.mp3")

                                #INSERTING DATA INTO DATABASE IF USER LOSE THE GAME
                cur.execute("insert into player_data(Name,Status,Amount_Won,Date,Time) values (%s,'LOSS',%s,Current_Date,Current_Time)",(name,amount))
                DB.commit()
            play_again()
        else:
            print(" \t\tHorse Number",user_choice,"Not Exist !!")
            temp3=input()
            main_menu()
    elif res==2:
        DB.close()
        exit_game()
    elif res==3:
        show_history()
        main_menu()
    else:
        print("\t\t\tInvalid Choice !!")
        play_again()
def check_choice():                                            #Function for checking User Choice for playing game/quitting game/Checking History from database
    temp1=input("\t\t\tPress Any Key to Continue.......")
    print("\t\t1.Play Game")
    print("\t\t2.Quit Game")
    print("\t\t3.Check History")
    try:
        x=int(input("\t\tChoose Your Option : "))
    except ValueError:                                          #Exception Handling for User Input
        print("\t\t\tInput Other than integer not Allowed !!")
        pqr=input()
        main_menu()
    return x
def show_history():                                             #Function for extracting all the data from database and displaying them
    print("\n\t\t\tPLAYING HISTORY RECORDS")
    s="select * from player_data"
    cur.execute(s)
    result=cur.fetchall()
    for rec in result:
        print(rec)
    print("\n")
    xyz=input("\t\tPress Any Key.....")
def play_again():                                                #Function for checking if user want to play again or not
    temp2=input("\t\t\tPress Any Key to Continue.......")
    os.system("cls")
    display_screen()
    print(" \t\tWant To Play Again :\n\t\t1.Yes\n\t\t2.No")
    try:
        ch=int(input("\t\tEnter Your Choice : "))
    except ValueError:                                           #Exception Handling for User Input
        print("\t\t\tInput Other than integer not Allowed !!")
        play_again()
    if ch==1:
        global flag
        flag=False
        main_menu()
    elif ch==2:
        exit_game()
    else:
        print("\t\t\tInvalid Choice !!")
        play_again()
def exit_game():                                                  #Function for exit the game
    print(" \t\tExiting...the Game...Thanks For Playing the game")
    playsound("end.mp3")
    time.sleep(0.2)
    sys.exit(" \t\tThanks !! For Playing The Game...")
password_check()       #Call of password_check() function
main_menu()            #Call of main_menu() function

