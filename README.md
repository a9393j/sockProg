# sockProg

SockProg is a basic python code for socket programming. It implements server code for both TCP/UDP sockets. Client can connect to the server using telnet(TCP) or ncat(UDP) and share messages. Initially the server replies with the same message but one can modify the reply and can even create a chat server using the same.

##Usage
```
python cli.py -h
```
This will guide you to the usage of the code.

If we create a server with port 8888 then client can communicate as mentioned below.

###TCP
In case of a TCP client connection, Use
```
telnet localhost 8888
```
This will connect to the TCP server and we can communicate through messages.

### UDP
In case of a UDP client connection, use

```
ncat -vv localhost 8888 -u
```
**Note#** As of now we aren't using any python library but as this code is server deployable so I have used virtualenv. It is possible that more functionalities may require some additoinal python libraries.
