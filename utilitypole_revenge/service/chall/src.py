#!/usr/local/bin/python
import json

FAILURE_MSG = '**INTRUDER IDENTIFIED** You are locked out!'

print('''
      
 /$$$$$$$   /$$$$$$  /$$$$$$$        /$$       /$$        /$$$$$$ 
| $$__  $$ /$$__  $$| $$__  $$      | $$      | $$       /$$__  $$
| $$  \ $$| $$  \ $$| $$  \ $$      | $$      | $$      | $$  \__/
| $$$$$$$/| $$  | $$| $$$$$$$/      | $$      | $$      | $$      
| $$__  $$| $$  | $$| $$____/       | $$      | $$      | $$      
| $$  \ $$| $$  | $$| $$            | $$      | $$      | $$    $$
| $$  | $$|  $$$$$$/| $$            | $$$$$$$$| $$$$$$$$|  $$$$$$/
|__/  |__/ \______/ |__/            |________/|________/ \______/                         

        (` _  _   _ |-  |\/| _  _ _    .,_    /`|_  ,_,_ _ |
        _)(/_(_|`(/_|_  |  |(/__\_\(|(||||(|  \,||(|||||(/_|
                                     _|   _|                

All employees need to pass a security check designed by our CISO. 
The location of our new data center will only be revealed to those 
who can prove their utility pole knowledge and loyalty to ROP LLC. 

How much do you know about your fellow men?

What will the utility poles tell you?
-------------------------------------------------------------------                                                   
Enter the location of each image in the format "latitude,longitude" 
with all values to 4 decimal places. For example, the location 
39.7357681,-105.0131855 should be entered as 39.7358,-105.0132.
''')

answers = json.load(open('answer.json','r'))

for i in range(1,11):
    guess = input("\nImage {}.png: ".format(i)).strip().split(',')
    try:
        if guess[0] == answers[str(i)]["latitude"] and guess[1] == answers[str(i)]["longitude"]:
            print(answers[str(i)]["msg"])
        else:
            raise Exception
    except:
        print(FAILURE_MSG)
        exit()

print(open('flag.txt','r').read())
