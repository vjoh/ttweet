README

Victoria L. Joh
vjoh3@gatech.edu
CS 3251-A: Networking I
February 12, 2020
Program Assignment 1

Files Submitted:
	- tweetser.py
	- ttweetcli.py
	- README
	- Sample.txt

Instructions for Running Client and Server
Make sure you are in the working directory where the ttweetcli and ttweetser files are stored before attempting to run either files.

Note: you must run the ttweetser.py file to start up the ttweet server, before attempting to upload or download messages with ttweet client.

Recommendation: Use <ServerPort> numbers that are between 13000 and 14000.

In order to determine what commands are optional or necessary:
Run the following command in terminal:
python3 ttweetser.py -h
python3 ttweetcli.py -h

	1) To run ttweetser.py, enter the following in the terminal:
	python3 ttweetser.py <ServerIP> <ServerPort>

	2a) To upload a message to ttweetser.py, enter the following in a terminal:
	python3 ttweetcli.py -u <ServerIP> <ServerPort> "message"

	2b) To download a message from ttweetser.py, enter the following in a terminal:
	python3 ttweetcli.py -d <ServerIP> <ServerPort>


Test Scenario Output

0- (Server Not Running)
Output: 
	ttweetcli connecting on port 13001...
	port error:
	-> ttweetcli cannot currently request a connection on port 13001
	-> [Errno 111] Connection refused

1- Run Client in upload mode -- (Output: Error Message: Server Not Found -- exit gracefully)
Output: 
	ttweetcli connecting on port 13001...
	port error:
	-> ttweetcli cannot currently request a connection on port 13001
	-> [Errno 111] Connection refused
2- Run Client in download mode – (Output: Error Message: Server Not Found – exit gracefully)
Output: 
	ttweetcli connecting on port 13001...
	port error:
	-> ttweetcli cannot currently request a connection on port 13001
	-> [Errno 111] Connection refused


3- Run Server 

If the server is running, 
bound to a port and listening for client, 
the the following will be displayed in terminal:
 > listening for connection to ttweetcli...


Command that was run: python3 ttweetcli.py -u 127.0.0.1 13001 "TEST"
Server Upload Output:	
	ttweetser connected to ('127.0.0.1', 40272)
	received request to upload...
	received upload: "TEST"
	ttweetser closed connected to ('127.0.0.1', 40272)

Client Upload Output:
	ttweetcli connecting on port 13001...
	ttweetcli connected to ttweetser on port 13001
	PROTOCOL: /UP
	ttweetser response: /OK
	uploading message to ttweetser...
	-> /UP - OK
	-> message upload successful: "TEST"

______________________________________________________

Command that was run: ttweetcli.py -d 127.0.0.1 13001
Server Download Output:
	listening for connection to ttweetcli...
	ttweetser connected to ('127.0.0.1', 40276)
	received request to download...
	downloading last message to ttweetcli... ('127.0.0.1', 40276)
	"TEST"
	ttweetser closed connected to ('127.0.0.1', 40276)

Client Download Output:
	ttweetcli connecting on port 13001...
	ttweetcli connected to ttweetser on port 13001
	PROTOCOL:  /DOWN
	downloading message from ttweetser...
	-> /DOWN - OK
	-> message download successful: "TEST"

______________________________________________________


4- Run Client in download mode (Output: EMPTY Message)

Command that was run: python3 ttweetcli.py -d 127.0.0.1 13001
	Output:
	ttweetcli connecting on port 13001...
	ttweetcli connected to ttweetser on port 13001
	PROTOCOL:  /DOWN
	downloading message from ttweetser...
	-> /DOWN - OK
	-> message download successful: "Empty Message"

5- Run Client in upload mode – upload message0 > 150 characters (Output: Error, message length > 150)

Command that was run: python3 ttweetcli.py -u 127.0.0.1 13001 "TESTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"
	Output:
	ttweetcli connecting on port 13001...
	ttweetcli connected to ttweetser on port 13001
	-> /UP - FAIL
	-> message upload failed:
	-> 150 char limit exceeded for message size

6- Run Client in download mode (Output: EMPTY Message)

Command that was run: python3 ttweetcli.py -d 127.0.0.1 13001
	Output:
	ttweetcli connecting on port 13001...
	ttweetcli connected to ttweetser on port 13001
	PROTOCOL:  /DOWN
	downloading message from ttweetser...
	-> /DOWN - OK
	-> message download successful: "Empty Message"

7- Run Client in upload mode – upload message1 <= 150 characters (Output: Upload Successfully)

Command that was run: python3 ttweetcli.py -u 127.0.0.1 13001 "TEST2" 
	Output:
	ttweetcli connecting on port 13001...
	ttweetcli connected to ttweetser on port 13001
	PROTOCOL: /UP
	ttweetser response: /OK
	uploading message to ttweetser...
	-> /UP - OK
	-> message upload successful: "TEST2"

8- Run Client in download mode (Output: message1)

Command that was run: python3 ttweetcli.py -d 127.0.0.1 13001
	Output:
	ttweetcli connecting on port 13001...
	ttweetcli connected to ttweetser on port 13001
	PROTOCOL:  /DOWN
	downloading message from ttweetser...
	-> /DOWN - OK
	-> message download successful: "TEST2"

9- Run Client in upload mode – upload message 2 (different from message1)<= 150 characters (Output: Upload Successfully)

Command that was run: python3 ttweetcli.py -u 127.0.0.1 13001 "TEST different" 
	Output:
	ttweetcli connecting on port 13001...
	ttweetcli connected to ttweetser on port 13001
	PROTOCOL: /UP
	ttweetser response: /OK
	uploading message to ttweetser...
	-> /UP - OK
	-> message upload successful: "TEST different"

10- Run Client in download mode (Output: message2)

Command that was run: python3 ttweetcli.py -d 127.0.0.1 13001
	Output:
	ttweetcli connecting on port 13001...
	ttweetcli connected to ttweetser on port 13001
	PROTOCOL:  /DOWN
	downloading message from ttweetser...
	-> /DOWN - OK
	-> message download successful: "TEST different"

11- Run Client in upload mode – upload message3 > 150 characters (Output: Error, message length > 150)

Command that was run: python3 ttweetcli.py -u 127.0.0.1 13001 "TESTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTLength " 
	Output:
	ttweetcli connecting on port 13001...
	ttweetcli connected to ttweetser on port 13001
	-> /UP - FAIL
	-> message upload failed:
	-> 150 char limit exceeded for message size





Upload & Download Protocol

Once the ttweet server is running, if a user of the ttweet client wants to upload or download a message, then the user will be required to provide a flag (-u or -d).

When the -u flag is provided the client will send a prompt to the server, "/U", letting it know it would like to upload a message.

The server will respond with an "/OK", letting the client know it is ready to receive a message.

If the "/OK" comes back from the server, the client will proceed to upload a message.

When the -d flag is provided the client will send a prompt to the server, "/DOWN", letting it know it would like to download the last message stored.

The server will respond with the last message if there is one, if not it will respond with the "Empty Message" response.

Bugs and Limitations
	Limitations - Many, but none known outside the scope of this assignment.
	Bugs - None known of at the time of submission.




