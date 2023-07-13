import asyncio
import websockets
import json
import time
import base64
from struct import *


async def recv_packet(websocket):
    ''' Function recieves a packet from the server and returns a b64 decoded version
    '''
    packet = await websocket.recv()
    print(f'Base64:  {packet}')
    return base64.b64decode(packet)


async def recv_and_decode_packet(websocket):
    ''' Function used to separate the b64 packet and the decoded byte packet
    '''
    packet = await recv_packet(websocket)
    print(f'Server Sent:  {packet}')
    return packet


def compute_checksum(source:int,dest:int,payload:bytearray):
    ''' Function calculates the checksum header parameter
        It does so by having the source port, destination port and message payload passed into it
        The length can be calculated and does not need to be passed in
    '''
    source = source.to_bytes(2,'little')
    dest = dest.to_bytes(2,'little')
    length = (8 + len(payload)).to_bytes(2,'little')
    # I didnt think we needed to add a 0 (checksum) to itself so left it out
    packet = source + dest + length + payload

    # If payload is an odd number in size an extra empty byte needs to be added to the end
    if len(payload)%2 !=0:
        packet += bytes(1) 
    
    checksum = 0
    for i in range(0,len(packet),2):
        temp = ((packet[i] << 8) | packet[i+1])
        checksum += temp

    # Bitwise NOT is performed
    checksum = (checksum >> 16) + (checksum & 0xFFFF)
    checksum = ~checksum & 0xFFFF
    return checksum


async def send_packet(websocket, source, dest, payload):
    ''' Function sends a packet to the server
        In this project used to prompt a different return packet
    '''
    checksum = compute_checksum(source,dest,payload)

    source = source.to_bytes(2,'little')
    dest = dest.to_bytes(2,'little')
    length = (8 + len(payload)).to_bytes(2,'little')
    checksum = checksum.to_bytes(2,'little')

    packet = source + dest + length + checksum + payload

    packet = base64.b64encode(packet)

    await websocket.send(packet)


# This was repeated code so I decided to add a function to calculate it
def extract_packet(packet):
    ''' Function takes a packet and returns a tuple of each of the separated values
    '''
    source = int.from_bytes(packet[0:2], 'little')
    dest = int.from_bytes(packet[2:4], 'little')
    length = int.from_bytes(packet[4:6], 'little')
    checksum = int.from_bytes(packet[6:8], 'little')
    payload = packet[8:]
    return source,dest,length,checksum,payload


# This was repeated code so I decided to add a function to calculate it
def packet_dispaly(source, dest, length, checksum, payload):
    ''' Function displays packet information in an organised fashion
    '''
    payload = payload.decode('utf-8')

    print("Decoded Packet:")
    print(f'Source Port:  {source}')
    print(f'Dest Port:  {dest}')
    print(f'Data Length:  {length}')
    print(f'Checksum:  {checksum}')
    print(f'Payload:  {payload}\n')


async def main():
    ''' Main function that operates all the other functions to complete the tasks
    '''
    uri = "ws://localhost:5612"
    
    async with websockets.connect(uri) as websocket:
        
        # Task 1
        print("Task 1")
        packet = await recv_and_decode_packet(websocket)
        packettup = extract_packet(packet)
        # packettup | [0] = source , [1] = dest , [2] = length , [3] = checksum , [4] = [payload]
        
        packet_dispaly(packettup[0], packettup[1], packettup[2], packettup[3], packettup[4])

        # Task 2
        print("Task 2")
        checksump = compute_checksum(packettup[0],packettup[1],packettup[4])
        print(f"Calculated Checksum:  {checksump}\n")

        # Task 3
        print("Task 3")

        while True:
            await send_packet(websocket,0,542,b'1111')
            timepacket = await recv_and_decode_packet(websocket)
            packettup = extract_packet(timepacket)
            packet_dispaly(packettup[0], packettup[1], packettup[2], packettup[3], packettup[4])
            time.sleep(1)


# Runs the main function and prevents imports from running it
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())