'''
    Author: Ilya Kiselev
    Final Edit Date: 14/04/2021
'''

from morse import *

# To change an input message you can simply alter the function calls below

# Sheet 1 Task 1 does not have any code that we could write so is left empty


# Examples for Sheet 1 Task 2
print("Examples for Sheet 1 Task 2")

# Encode and Decode functions we were set to create
print(encode("us"))
print(decode("..- ..."))

# A print tree function I made that can create a visual represnetation of a tree in the terminal
# I left them commented out because they were not set but you can uncomment them if you want to take a look
# print_tree(MtTTree.head,0)
# print_tree(TtMTree.head,0)
# The > were initially blank spaces but that made it a little hard to distinguish between some parent and child nodes


# Sheet 1 Task 3 code and subsequent assert tests can be found in morseunit.py


# Examples for Sheet 1 Task 4
print("\nExamples for Sheet 1 Task 4")

# To insert most of the characters onto the morse to text tree I created a new function
# To show it working I also used a tester decode function which allows us to enter a tree to be used to
# decode rather than using the auto generated and working tree in morse.py
temptree = Morse_to_Text_Tree()
print(decode_tester(temptree,"..--.."))
temptree.insert_character("..--..", "?")
print(decode_tester(temptree,"..--.."))
# The insert_character function is ran multiple times at the bottom of morse.py which places
# all the additional characters on the working tree


# Examples for Sheet 2 Task 1
print("\nExamples for Sheet 2 Task 1")

# We only implemented one function for this task which is the decode_bt function
print(decode_bt('- . ... -'))


# Examples for Sheet 2 Task 2
print("\nExamples for Sheet 2 Task 2")

# Two more functions that manipulate morse code, this time with target and sender ids
print(encode_ham("beta", "alpha", "large message"))
print(decode_ham(".- .-.. .--. .... .- -.. . -... . - .- -...- .-.. .- .-. --. . / -- . ... ... .- --. . -...- -.--."))

# decode_ham_formatted is another function I decided to add even though it wasnt specified that we need it but seems like
# it would help visualise my code examples
# It also decodes the morse message expecting ham format but instead of returning the payload in three parts it simply
# converts it into print friendly format and returns it like that. (It is in the same format as the 10101 port decoder uses)
# Again I didnt want to fill up the terminal with things that you might not want to see so it is left commented out unless 
# you would like to view it then simply remove the # before the print()
# print(decode_ham_formatted(".- .-.. .--. .... .- -.. . -... . - .- -...- .-.. .- .-. --. . / -- . ... ... .- --. . -...- -.--."))


# Examples for Sheet 2 Task 3
print("\nExamples for Sheet 2 Task 3")

# For task 3 we were told to make two functions one of which sends back the message that we entered and
# the other sends back the timestamp that the message was received on the server.
# For the send_echo I return the entire payload instead of just the message to allow morseunit to have a more accurate
# test but for the example here I added a [2] on the end of the print which prints just the message
print(asyncio.run(send_echo("frazer","hey"))[2])
print(asyncio.run(send_time("frazer")))

# I believe this file shows all the functionality of worksheet 2, if you are still unsatisfied feel free to
# run any of the functions in morse.py or morseunit.py