#NAME: OMOLE-ADEBOMI STEVEN
#PROJECT: Electronic Voting System using Server-Client Socket Communication in Python
#DOB:29th of July
#FIlETYPE: Client File which will be used by all voters to cast a vote
import socket as soc
ip = input("Enter The Poling Address to Vote to")
#ip = "127.0.0.1"
port = 8080
def serverSetUp(ip,port):
    socketCreate = soc.socket(soc.AF_INET,soc.SOCK_STREAM,0) #SocType,SocFamily,socProtocol
    print("Voter Set up\n")
    socConnect = socketCreate.connect((ip,port)) #To connect
    if(socketCreate):
        print("Connected To the Voting Pole @",soc.gethostbyaddr(ip)[0]) #soc.getservbyport
        vote = input("Which Do You Want to Cast Your Vote on?\n(1)APC\n(2)PDP\n")
        vote = vote.upper()
        name = soc.gethostname()
        if(vote == "1" or vote == "(1)" or vote == "(1)APC"):
            socketCreate.send(b'APC')
            print(str(socketCreate.recv(1024))[2::].replace('\'',''))

        elif(vote == "2" or vote == "(1)" or vote == "(1)APC"):
            socketCreate.send(b'PDP')
            print(str(socketCreate.recv(1024))[2::].replace('\'',''))
        else:
            print("wrong Vote")

try:
    serverSetUp(ip,port)
except:
    print("Unable to Connect to Poling Server")
