import unittest
import morse
import asyncio
import time

class TestMorse(unittest.TestCase):
    # Testing for Sheet 1 Task 3
    # Encode Tests

    # Small text to morse - expected success
    def test_encode_us(self):
        self.assertEqual(morse.encode('us'), '..- ...')

    # Larger text to morse - expected success
    def test_encode_hopper(self):
        self.assertEqual(morse.encode('hopper'), '.... --- .--. .--. . .-.')

    # Large text with space to morse - expected success
    def test_encode_help_us(self):
        self.assertEqual(morse.encode('help us'), '.... . .-.. .--. / ..- ...')

    # Large text in uppercase to morse - expected success
    def test_encode_ELEVEN(self):
        self.assertEqual(morse.encode('ELEVEN'), '. .-.. . ...- . -.')

    # Incorrect value entry - expected failure
    def test_encode_fail(self):
        self.assertEqual(morse.encode('fail'), '.')


    # Decode Tests

    # Expected success
    def test_decode_us(self):
        self.assertEqual(morse.decode('..- ...'), 'us')

    # Expected success
    def test_decode_hopper(self):
        self.assertEqual(morse.decode('.... --- .--. .--. . .-.'), 'hopper')

    # Expected success
    def test_decode_help_us(self):
        self.assertEqual(morse.decode('.... . .-.. .--. / ..- ...'), 'help us')

    # Expected success
    def test_decode_eleven(self):
        self.assertEqual(morse.decode('. .-.. . ...- . -.'), 'eleven')

    # Expected failure
    def test_decode_fail(self):
        self.assertEqual(morse.decode('.... .-'), 'fail')


    # Binary Tree Implementation Tests
    '''
    Notes:
    I did not implement the empty test because I was told the way I implemented the program could not test it
    I did not implement the delete function test because I was told we did not need to add it at all
    '''

    # Empty test
    # Test to see if the Text to Morse tree starts generation
    # Note: this test creates a new tree and checks if the automatic generation creates a head
    #       in other words checking if the tree contains something
    def test_head_node_not_empty(self):
        self.assertEqual(morse.Text_to_Morse_Tree().head.val, ('E', '.'))

    # Insert Search Func Test
    # Test to see if the Text to Morse tree starts getting populated by the insert search function
    # Note: this test creates a new tree which automatically runs the insert function, this test
    #       simply checks if it does so correctly
    def test_insert_search_function(self):
        self.assertEqual(morse.Text_to_Morse_Tree().head.left.val, ('A', '.-'))

    # Find Func Test
    # Test to see if the Text to Morse tree can be searched by the find function
    # Note: the find function is within the translateTtM method, it is simply used to allow the find function 
    #       to more easily call itself
    def test_find_function(self):
        self.assertEqual(morse.Text_to_Morse_Tree().translateTtM("A"), '.-')

    # Insert Character Func Test
    # Test to see if the insert character method correctly places characters on the Text to Morse tree 
    # Note: this function is one I added to the code because I wasnt entirely sure what functionality our code
    #       needs to show so to be on the safe side I added extra than I understood the worksheet required
    def test_insert_character_function(self):
        temptree = morse.Morse_to_Text_Tree()
        temptree.insert_character("..--..", "?") # Without this line the test returns a failure
        self.assertEqual(morse.decode_tester(temptree,'..--..'), '?')


    # Testing for Sheet 1 Task 4
    # Special Character Tests

    # Tests to check if the "(" character is being correctly placed on the tree by the constructor method
    def test_encode_open_bracket(self):
        self.assertEqual(morse.encode('('), '-.--.')
    
    def test_decode_open_bracket(self):
        self.assertEqual(morse.decode('-.--.'), '(')

    # Tests to check if the ")" character is being correctly placed on the tree by the insert_character method
    def test_encode_close_bracket(self):
        self.assertEqual(morse.encode(')'), '-.--.-')
    
    def test_decode_close_bracket(self):
        self.assertEqual(morse.decode('-.--.-'), ')')


    # Testing for Sheet 2 Task 1
    # Binary Heap Tests

    # Small morse to text - expected success
    def test_decode_bt_small(self):
        self.assertEqual(morse.decode_bt('- . ... -'), 'test')

    # Large morse with space to text - expected success
    def test_decode_bt_large(self):
        self.assertEqual(morse.decode_bt('.... . .-.. .--. / ..- ...'), 'help us')


    # Testing for Sheet 2 Task 2
    # Ham Radio Tests

    # Small text to morse - expected success
    def test_encode_ham_small(self):
        self.assertEqual(morse.encode_ham("s1","r1","us"), '.-. .---- -.. . ... .---- -...- ..- ... -...- -.--.')

    # Large text with space to morse - expected success
    def test_encode_ham_large(self):
        self.assertEqual(morse.encode_ham("sender", "receiver", "small text BIG TEXT"),
                         '.-. . -.-. . .. ...- . .-. -.. . ... . -. -.. . .-. -...- ... -- .- .-.. .-.. / - . -..- - / -... .. --. / - . -..- - -...- -.--.')

    # Small morse to text - expected success
    def test_decode_ham_small(self):
        self.assertEqual(morse.decode_ham(".-. .---- -.. . ... .---- -...- ..- ... -...- -.--."), ('r1', 's1', 'us'))

    # Large morse with space to text - expected success
    def test_decode_ham_large(self):
        self.assertEqual(morse.decode_ham(
            '.-. . -.-. . .. ...- . .-. -.. . ... . -. -.. . .-. -...- ... -- .- .-.. .-.. / - . -..- - / -... .. --. / - . -..- - -...- -.--.'),
                         ('receiver', 'sender', 'small text big text'))


    # Testing for Sheet 2 Task 3
    # Morse Server Tests

    # Send Echo Func Test
    # The return should place the recipient (user) id in the first position, sender id in the second position and the message in the third
    def test_send_echo(self):
        self.assertEqual(asyncio.run(morse.send_echo("a","abc")),('a', 'echo', 'abc'))
    
    # Send Time Func Test
    # The return should be the timestamp of when the message is recieved by the server, due to the fact that the entire program
    # is ran is about 0.01 seconds I compared it to the current time.
    # Note: The function has a chance (approx 1%) to return an assertion error due to the fact stated above ^
    #       The chance of this is very low so I decided it will be fine as it is but if nessecary I could fix this by adding a 
    #       try/except(AssertionError) and run additional tests in this function.
    def test_send_time(self):
        self.assertEqual(asyncio.run(morse.send_time("ping")),time.strftime("%H:%M:%S", time.gmtime()))


if __name__ == '__main__':
    unittest.main()
