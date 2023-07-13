import unittest
import main
import asyncio
import time
import websockets

async def run_tests():
    uri = "ws://localhost:5612"
    
    async with websockets.connect(uri) as websocket:
        
        # Setup for Task 1
        print("Recieved welcome packet:")
        packet = await main.recv_and_decode_packet(websocket)
        packettup = main.extract_packet(packet)

        # Task 1 Test
        # Here we are testing to see if the recieved packet payload is correct and as expected
        # This essentially checks the entire packet as the payload can only be recieved correctly if the packet is sent correctly
        # If it is not correct this is likely due to the server being down
        assert (packettup[4] == b'Welcome to IoT UDP Server'), "Welcome packet payload was not recieved correctly"
        print("\nTest 1 Passed - Welcome packet recieved correctly\n")

        # Task 2 Test
        # Here we are testing to see if the compute_checksum function is correctly calculating the checksum
        # To do so we are comparing the checksum with the checksum calculated by the server
        assert (main.compute_checksum(packettup[0],packettup[1],packettup[4]) == packettup[3]), "Checksum calculated incorrectly"
        print("Test 2 Passed - Checksum calculated correctly\n")

        # Setup for Task 3
        print("Recieved time packet:")
        await main.send_packet(websocket,0,542,b'1111')
        timepacket = await main.recv_and_decode_packet(websocket)
        packettup = main.extract_packet(timepacket)

        # Task 3 Test
        # Here we are testing to see if the time recieved from the server is correct
        # This essentially checks the entire packet as the payload can only be recieved correctly if the packet is sent correctly
        # Note: The test has a chance (less than 1%) to return an assertion error due to the fact that the timepacket might have been 
        #       recieved in the final miliseconds of the previous second
        #       The chance of this is very low so I decided it will be fine as it is but if nessecary I could fix this by adding a 
        #       try/except(AssertionError) and run additional tests.
        assert ((time.strftime("%H:%M:%S")) == packettup[4].decode('utf-8')), "Time packet payload was not recieved correctly"
        print("\nTest 3 Passed - Time packet recieved correctly")


# Runs the run_tests function and prevents imports from running it
# Not actually needed as this file isnt imported but it doesnt hurt to have
if __name__ == '__main__':
    asyncio.run(run_tests())
