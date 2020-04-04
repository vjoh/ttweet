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


# Create CLI parser to make sure <ServerIP> <ServerPort> and "message"
# are provided for ttweetcli
parser = argparse.ArgumentParser(prog='ttweetcli',
                                description='List of options and command '
                                + 'line arguments needed to run ttweetcli.py')
parser.add_argument('-u', help='upload a message to <ServerIP>', action='store_const', const='/UP')
parser.add_argument('-d', help='download a message from <ServerIP>', action='store_const', const='/DOWN')
parser.add_argument('<ServerIP>', help='IP number required to connect to ttweetser')
parser.add_argument('<ServerPort>', help='port number required to connect to ttweetser')
parser.add_argument('"message"', help='a message you would like to upload to ttweetser', nargs='?', default='')
try:
    args = parser.parse_args()
    # print(args)
# if problem's occur making the args, throw an error and exit
except Exception as e:
    print('error has occured related to the command-\n '
    + 'line arguments that ttweetcli.py was given: \n"%s"' % e)
    for arg in vars(args):
        print('-> ', arg, getattr(args, arg))
    sys.exit()

    # An uploaded message is stored at the server
    # will overwrite an existing message if the server
    # already has a message.
    # A download request returns the last uploaded message
    # or returns 'Empty Message' if no message has been uploaded yet.

def runClient():
    # print(len(sys.argv))
    if sys.argv[1] == '-u':
        if len(sys.argv) < 5:
            print('error found in command-line arguments')
            print('please check that your arguments as follows:')
            for arg in vars(args):
                print('-> ', arg, getattr(args, arg))
            sys.exit()

    # Create a TCP/IP clientSocket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port that ttweetser is listening on,
    # if it is available
    serverPort = int(sys.argv[3])
    print('ttweetcli connecting on port %s...' % serverPort)
    try:
        s.connect(('', serverPort))
        print('ttweetcli connected to ttweetser on port %s' % serverPort)
    except Exception as e:
        print('port error:\n-> ttweetcli cannot currently request a connection on port %s' % serverPort)
        print('->', e)
        sys.exit()

    if sys.argv[1] == "-u":
        if len(sys.argv[4]) > 150:
            message = 'Empty Message'
            print('-> /UP - FAIL')
            print('-> message upload failed:')
            print('-> 150 char limit exceeded for message size')
            sys.exit()
        elif len(sys.argv[4]) == 0:
            message = 'Empty Message'
        else:
            message = sys.argv[4]

        # set protocol request for upload
        protocol = '/UP'
        # print(sys.argv)
        print('PROTOCOL:', protocol)
        try:
            # send /UP request
            s.send(protocol.encode())
            # get response
            response = s.recv(1024).decode()
            if response == '/OK':
                print('ttweetser response:', response)
                # send message
                s.send(message.encode())
                print('uploading message to ttweetser...')
                print('-> /UP - OK')
                print('-> message upload successful: "%s"' % message)

        except Exception as e:
            print('-> /UP - FAIL')
            print('-> message upload failed:')
            print('-> check command line parameters given for accuracy')
            print('-> error:', e)
            sys.exit()

    elif sys.argv[1] == "-d":
        # set protocol request for download
        protocol = '/DOWN'
        # print(sys.argv)
        print('PROTOCOL: ', protocol)
        try:
            # send /DOWN request
            s.send(protocol.encode())
            # get response
            #response2 = s.recv(1024).decode()
            #if response2 == '/OK':
            #print('ttweetser response:', response2)
            # get old/last message
            message = s.recv(1024).decode()
            if len(message) == 0:
                message = 'Empty Message'
            print('downloading message from ttweetser...')
            print('-> /DOWN - OK')
            print('-> message download successful: "%s"' % message)

        except Exception as e:
            print('/DOWN - FAIL')
            print('-> message download failed: \n')
            print('-> check character length of message')
            print('-> ', e)
            sys.exit()

if __name__ == '__main__':
    runClient()
