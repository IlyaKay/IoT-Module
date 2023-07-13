import asyncio
import websockets
import json

# Class made for Sheet 1 Task 2 but used in most of the Tasks
class Morse_to_Text_Tree():
    ''' Class that initializes and populates a binary tree for translating morse code strings into letters.
        This class uses a more efficient way of building the morse tree than the one shown in the linked
        document and practical but it achieves the same result so I decided to use it here.
        Update note: after working through worksheet 2 I found that we actually use a similar method in the
        binary heap implementation so I just found this method to be a more efficient way of building the tree
        as well as the heap
    '''

    def __init__(self):
        self.head = Node("#")

        # All characters that are to be placed on the tree, in the order of left to right.
        letters = "ETIANMSURWDKGOHVF L PJBXCYZQ  54 3   2& +    16=    ( 7   8 90"
        current = self.head
        # Array stores the next head branch in the queue which has the next two letters attached to its left and right.
        templetters = []

        for char in letters:
            if current.left == None:
                current.left = Node(char)
            else:
                if current.right == None:
                    current.right = Node(char)
                else:
                    templetters.append(current.left)
                    templetters.append(current.right)
                    current = templetters.pop(0)
                    current.left = Node(char)

    # Function made for Sheet 1 Task 2 but used in most of the Tasks
    def translateMtT(self, morse):
        ''' Method that takes a string input of morse code and returns the letter equivalent by following the morse tree.
        '''
        current = self.head

        for char in morse:
            if char == ".":
                current = current.left
            elif char == "-":
                current = current.right

        return current.val

    # Function made for Sheet 1 Task 4 even though it was not specified I chose to
    # create it to make it possible to easily add additional characters
    def insert_character(self, morse, insert):
        ''' Method used to add any extra characters required by the worksheet
            !!! I recognise that there is a potential problem if the function attempts to insert
            into an existing node, then the currently existing branches off of the
            replaced node would be lost. This can be fixed with the following code concept:
                if current.left != None:
                    tempcurrent = current.left
                    templeft = tempcurrent.left
                    tempright = tempcurrent.right
            I did not implement it as it is not needed for this project.
        '''
        current = self.head
        count = 0
        for char in morse:
            count += 1
            if count == len(morse):
                if char == ".":
                    current.left = Node(insert)
                elif char == "-":
                    current.right = Node(insert)
            elif char == ".":
                if current.left == None:
                    current.left = Node(" ")
                current = current.left
            elif char == "-":
                if current.right == None:
                    current.right = Node(" ")
                current = current.right


# Class made for Sheet 1 Task 2 but used in most of the Tasks
class Text_to_Morse_Tree():
    ''' Class that initializes and populates a binary tree for translating letters into morse code strings.
        This is how benedict asked us to complete the encoder to show our understanding of trees
        even though there exist much more efficient alternatives.
        We essentially implemented a dictionary here.
    '''

    def __init__(self):
        self.head = Node(('E', '.'))

        # All the characters and their morse equivalents, this can essentially already be a dictionary
        # but for the worksheet we need to put the value pairs into a tree.
        pairs = [('T', '-'), ('I', '..'), ('A', '.-'),
                 ('M', '--'), ('N', '-.'), ('S', '...'),
                 ('U', '..-'), ('R', '.-.'), ('W', '.--'),
                 ('D', '-..'), ('K', '-.-'), ('G', '--.'),
                 ('O', '---'), ('H', '....'), ('V', '...-'),
                 ('F', '..-.'), ('L', '.-..'), ('P', '.--.'),
                 ('J', '.---'), ('B', '-...'), ('X', '-..-'),
                 ('C', '-.-.'), ('Y', '-.--'), ('Z', '--..'),
                 ('Q', '--.-'),
                 ('1', '.----'), ('2', '..---'), ('3', '...--'),
                 ('4', '....-'), ('5', '.....'), ('6', '-....'),
                 ('7', '--...'), ('8', '---..'), ('9', '----.'),
                 ('0', '-----'), (', ', '--..--'), ('.', '.-.-.-'),
                 ('?', '..--..'), ('=', '-...-'), ("'", '.----.'),
                 ('!', '-.-.--'), ('(', '-.--.'), (')', '-.--.-'),
                 ('&', '.-...'), (':', '---...'), (';', '-.-.-.'),
                 ('+', '.-.-.'), ('-', '-....-'), ('_', '..--.-'),
                 ('"', '.-..-.'), ('$', '...-..-'), ('¡', '--...-'),
                 ("=", "-...-")
                 ]

        # Function made for Sheet 1 Task 2 but used in most of the Tasks
        def insert_search(current, letter, morse):
            ''' This method grows the tree by comparing the letter values.
                The tree could be made more efficient by entering the letters in such an order
                that ever next letter is lower then higher after one another but we were told that
                the program efficiency is not too relevant in this case as the tree is small.
                I still chose to order it in some sort of way so I entered the letters in the morse
                order which is not perfectly ordered for this kind of tree structure but is much better
                than entering the values from A to Z which would otherwise essentially creates two
                large branches.
            '''
            if current == None:
                return Node((letter, morse))
            elif letter == current.val[0]:
                return current
            else:
                if letter < current.val[0]:
                    current.left = insert_search(current.left, letter, morse)
                    return current
                elif letter > current.val[0]:
                    current.right = insert_search(current.right, letter, morse)
                    return current

        for item in pairs:
            head = self.head
            insert_search(head, item[0], item[1])

    # Function made for Sheet 1 Task 2 but used in most of the Tasks
    def translateTtM(self, letter):
        """ Method that takes a string letter and returns the morse code equivalent by following the letter-morse tree.
        """

        # This function could be written to replace translateTtM but I wanted
        # to keep the function we were shows separate to the format of my
        # own code
        def find_search(current, letter):
            if letter < current.val[0]:
                return find_search(current.left, letter)
            elif letter > current.val[0]:
                return find_search(current.right, letter)
            else:
                return current.val[1]

        head = self.head
        return find_search(head, letter)


# Class made for Sheet 1 Task 2 but used in almost all of the Tasks
class Node(object):
    """ Class that is used to construct every tree node.
    """

    def __init__(self, char):
        self.val = char
        self.left = None
        self.right = None


# Function made for testing the tree structures visually
def print_tree(node, nest):
    '''
    Testing function, used to print a tree from a specified node.
    Example: print_tree(TtMTree.head,0)
    '''
    if node != None:
        for i in range(nest):
            print(">", end="")
        # if nest == 6:
        print(node.val)
        print_tree(node.left, nest + 1)
        print_tree(node.right, nest + 1)


# Function made for Sheet 1 Task 2 but used in most of the Tasks
def decode(msg):
    '''
    Function that takes a morse input and returns the text equivalent using a tree
    Example: decode("..- ...")
    '''
    try:
        output = ""
        letter = ""
        for element in msg:
            if element == "." or element == "-":
                letter += element
            elif element == " ":
                if letter != "":
                    output += MtTTree.translateMtT(letter)
                    letter = ""
            elif element == "/":
                output += " "
        output += MtTTree.translateMtT(letter)
        output = output.lower()
    except(AttributeError):
        output = "One of the entered morse messages does not exist on the tree"
    return output


# Function made for testing trees with parts missing or extra parts added
def decode_tester(tree,msg):
    '''
    Function that takes a tree object and morse input and returns the text equivalent using a tree
    Used by morseunit tests but can also be used in general to test incomplete trees
    '''
    try:
        output = ""
        letter = ""
        for element in msg:
            if element == "." or element == "-":
                letter += element
            elif element == " ":
                if letter != "":
                    output += tree.translateMtT(letter)
                    letter = ""
            elif element == "/":
                output += " "
        output += tree.translateMtT(letter)
        output = output.lower()
    except(AttributeError):
        output = "One of the entered morse messages does not exist on the tree"
    return output


# Function made for Sheet 1 Task 2 but used in most of the Tasks
def encode(msg):
    '''
    Function that takes a text input and returns the morse equivalent using a tree
    Example: encode("us")
    '''
    msg = msg.upper()
    output = ""
    count = 0
    for letter in msg:
        count += 1
        if letter != " ":
            output += TtMTree.translateTtM(letter)
        else:
            output += "/"
        if count != len(msg):
            output += " "

    return output


# Function made for Sheet 2 Task 1
def decode_bt(msg):
    """Function that takes a morse input and returns the text equivalent using a binary heap
    """

    # In hindsight if I knew we would have to create a full list of characters up to the 7th level ($) I would have
    # used this in the Morse_to_Text_Tree class to fill it out but kept the existing code just to show an alternative
    # way of building the tree using an insert function, as well as the fact that I would feel bad if I deleted all
    # that work
    heap = ["", "E", "T", "I", "A", "N", "M", "S", "U", "R", "W", "D", "K", "G", "O", "H", "V", "F", "", "L", "", "P",
            "J", "B", "X", "C", "Y", "Z", "Q", "", "", "5", "4", "", "3", "", "¿", "?", "2", "&", "", "+", "", "", "",
            "", "1", "6", "=", "/", "", "", "", "(", "", "7", "", "", "", "8", "", "9", "0", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "_", "", "", "", "", '"', "", "", ".", "", "", "", "", "", "", "", "", "'", "", "",
            "-", "", "", "", "", "", "", "", "", ";", "!", "", ")", "", "", "", "¡", "", ",", "", "", "", "", ":", "",
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "$"]

    output = ""
    msg = msg.split(" ")

    # I have similar functionality to this part of the code already existing in my decode()
    # function but I chose to use a different method here because I this function does
    # not call external functions
    for word in msg:
        i = 1
        for letter in word:
            if letter == ".":
                i = 2*i
            elif letter == "-":
                i = (2*i)+1
            elif letter == "/":
                output+=" "
                i = 1
        output+=heap[i-1]
    output = output.lower()
    return output


# Function made for Sheet 2 Task 2
def encode_ham(sender, receiver, msg):
    '''
    Function that takes a text input and returns the morse equivalent
    As well as the details about the sender and recipient in morse format
    Example: encode("s1","r1","us")
    '''
    sender = sender.upper()
    receiver = receiver.upper()
    msg = msg.upper()
    output = ""

    count = 0
    for letter in receiver:
        count += 1
        if letter != " ":
            output += TtMTree.translateTtM(letter)
        else:
            output += "/"
        if count != len(receiver):
            output += " "

    output += " -.. . "

    count = 0
    for letter in sender:
        count += 1
        if letter != " ":
            output += TtMTree.translateTtM(letter)
        else:
            output += "/"
        if count != len(sender):
            output += " "

    output += " -...- "

    count = 0
    for letter in msg:
        count += 1
        if letter != " ":
            output += TtMTree.translateTtM(letter)
        else:
            output += "/"
        if count != len(msg):
            output += " "

    output += " -...- -.--."

    return output


# Function made for Sheet 2 Task 2
def decode_ham(msg):
    '''
    Function that takes a morse input and returns the text equivalent
    As well as the details about the sender and recipient in text format
    Example: decode(".-. .---- -.. . ... .---- -...- ..- ... -...- -.--.")
    '''
    sender = ""
    receiver = ""
    letter = ""
    temp = ""
    # I added this lock to create a lower chance that the program mistakes
    # a regular input as the special formatting of de, = and =(
    lock = 0
    for element in msg:
        if element == "." or element == "-":
            letter += element
        elif element == " ":
            if letter != "":
                temp += MtTTree.translateMtT(letter)
                letter = ""
        elif element == "/":
            temp += " "
        if "DE" in temp and lock == 0:
            temp = temp[:-2]
            temp = temp.lower()
            sender = temp
            temp = ""
            lock += 1
        elif "=" in temp and lock == 1:
            temp = temp[:-1]
            temp = temp.lower()
            receiver = temp
            temp = ""
            lock += 1

    temp += MtTTree.translateMtT(letter)
    temp = temp[:-2]
    temp = temp.lower()

    return sender, receiver, temp


# Function made for Sheet 2 Task 2
def decode_ham_formatted(msg):
    ''' Extra function that has the same functionality as decode_ham
        but returns a formatted message
    '''
    msg = decode_ham(msg)
    output = "Message from: " + msg[1] + "\n" + "Message to: " + \
             msg[0] + "\n" + "Message content:\n" + msg[2]
    return output


# Function made for Sheet 2 Task 3
async def send_echo(sender,msg):
    '''
    Function that takes a sender id and a message and sends them to the echo server.
    The payload is encoded into morse code and sent to the echo server, the server
    acknowledges the request and echos the morse payload confirming that it recieved it. 
    The function then decodes the returned payload and returns the initial message from the function itself.
    '''
    uri = "ws://localhost:10102"
    async with websockets.connect(uri) as websocket:
        # After joining server will send client unique id.
        message = json.loads(await websocket.recv())

        # Get the client_id from the join message
        if message['type'] == 'join_evt':
            client_id = message['client_id']
        else:
            # If first message is not the join message exit
            print("Did not receive a correct join message")
            return 0

        morsepayload = encode_ham(sender,'echo', msg)
        
        # Send a ping to the server
        await send_message(websocket, morsepayload, client_id)

        # Wait for the response from the server
        response = await recv_message(websocket)

        decodedpayload = decode_ham(response)

        # The following was used for testing the message:

        # print("Payload sent to the server:")
        # print(morsepayload)

        # print("Decoded payload returned from the server:")
        # print(decodedpayload)

        return decodedpayload


# Function made for Sheet 2 Task 3
async def send_time(sender):
    '''
    Function that takes a sender id and sends a "hello world" message to the time server.
    The payload is encoded into morse code and sent to the time server, the server acknowledges the 
    request and returns an the morse payload with a morse timestamp in the place of the "hello world" message.
    The function then decodes the returned payload and returns the timestamp from the function itself.
    '''
    uri = "ws://localhost:10102"
    async with websockets.connect(uri) as websocket:
        # After joining server will send client unique id.
        message = json.loads(await websocket.recv())

        # Get the client_id from the join message
        if message['type'] == 'join_evt':
            client_id = message['client_id']
        else:
            # If first message is not the join message exit
            print("Did not receive a correct join message")
            return 0

        morsepayload = encode_ham(sender,'time', 'hello world')
        
        # Send a ping to the server
        await send_message(websocket, morsepayload, client_id)

        # Wait for the response from the server
        response = await recv_message(websocket)

        decodedpayload = decode_ham(response)

        # The following was used for testing the message:

        # print("Payload sent to the server:")
        # print(morsepayload)

        # print("Payload returned from the server:")
        # print(response)

        # print("Decoded payload returned from the server:")
        # print(decodedpayload)

        # Function returns just the timestamp from the decoded payload
        return decodedpayload[2]


# Function made for Sheet 2 Task 3
async def send_message(websocket, message, client_id):
    outward_message = {
        'client_id': client_id,
        'type': 'morse_evt',
        'payload': message
    }
    await websocket.send(json.dumps(outward_message))


# Function made for Sheet 2 Task 3
async def recv_message(websocket):
    message = json.loads(await websocket.recv())
    return message['payload']





# These are the auto generated tree structures that are used to allow the user
# to more easily run the functions
MtTTree = Morse_to_Text_Tree()
TtMTree = Text_to_Morse_Tree()
# These are additional characters of size 6 morse letter (or higher)
# that were needed by worksheet 2
# Due to the number of characters being low and the size of the 6th level of morse
# being high I decided it would be more efficient to insert them individually.
MtTTree.insert_character(".-.-.-", ".")
MtTTree.insert_character("--..--", ",")
MtTTree.insert_character("..--..", "?")
MtTTree.insert_character(".----.", "’")
MtTTree.insert_character("-.-.--", "!")
MtTTree.insert_character("-.--.-", ")")
MtTTree.insert_character("---...", ":")
MtTTree.insert_character("-.-.-.", ";")
MtTTree.insert_character("-....-", "-")
MtTTree.insert_character("..--.-", "_")
MtTTree.insert_character(".-..-.", '"')
MtTTree.insert_character("...-..-", '$') # And one character thats on the 7th level which would mean
MtTTree.insert_character("--...-", '¡')  # a crazy number of blank spaces if I used my previous inplementation
# Note: Turns out we actually had to do that for the binary heap so jokes on me I guess
#       I still chose to keep this here as it is a function that can be used in testing

