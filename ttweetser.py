import socket
import sys
import argparse

# Programming Assignment 1
# Author: Victoria L. Joh
# CS 3251-A Georgia Tech
# Due Date: February 12, 2020
# credits:  https://docs.python.org/3/library/socket.html
#           https://realpython.com/python-sockets/
#           https://realpython.com/command-line-interfaces-python-argparse/#displaying-a-custom-program-usage-help


def runArgParse():
    # Create a CLI Parser to make sure a port number was provided to run server on
    parser = argparse.ArgumentParser(prog='ttweetser',
                                        description='List of command line '
                                        + 'arguments needed to run ttweetser.py')
    parser.add_argument('<ServerPort>', help='A port number is required to run '
                                        + 'the ttweetser.py', type=int)
    # parse command line input for program
    try:
        args = parser.parse_args()

    except Exception as e:
        print('An error has occured related to the command '
        + 'line arguments that ttweetser.py was given: "%s"' % e)
        sys.exit()

def runServer():
    #Create message variable to store message
    message = 'Empty Message'
    # Create a TCP/IP serverSocket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Take <serverPort> input from command line
    serverPort = int(sys.argv[1])

    try:
        # Bind the socket that was created to the port requested
        s.bind(('', serverPort))
        # Listen for ttweetcli trying to connect
        s.listen(1)
        # If there are problems listening
    except Exception as e:
        print('port error:\n-> ttweetser is unable to listen or bind on port "%s"' % serverPort)
        print('->', e)
        sys.exit()

    while True:
        # Try to accept connection from a ttweetcli
        try:
            print('\nlistening for connection to ttweetcli...')
            conn, addr = s.accept()
            # Report to Command Line who is connected to ttweetser
            print('ttweetser connected to', addr)

            # While a connection exists, recieve data over connection
            while True:
                # Message size could be as large as 2048 bytes
                # decode data to plain english
                data = conn.recv(1024).decode()
                # read protocol
                if data == "/UP":
                    print('received request to upload...')
                    # get data from client
                    ok_upload = '/OK'
                    # print('send OK to upload...')
                    # # send ok
                    conn.send(ok_upload.encode())
                    # get message
                    message = conn.recv(1024).decode()
                    if len(message) == 0:
                        message = 'Empty Message'
                    print('received upload: "%s"' % message)

                elif data == "/DOWN":
                     print('received request to download...')
                     # send data to client
                     #ok_upload2 = '/OK'
                     # print('send OK to upload...')
                     # # send ok
                     #conn.send(ok_upload2.encode())
                     print('downloading last message to ttweetcli...', addr)
                     print('"%s"' % message)
                     conn.send(message.encode())

                else:
                    break

        except Exception as e:
            print('connection error:\n-> ttweetcli unable to accept connection or data from', addr)
            print('->', e)
            sys.exit()
        finally:
            # Close the connection between ttweetser and ttweetcli
            print('ttweetser closed connected to', addr)
            conn.close()


if __name__ == '__main__':
    runArgParse()
    runServer()
