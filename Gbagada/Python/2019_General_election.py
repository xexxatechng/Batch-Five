#Name - Michael okubanjo
#Gender- Male
#topic - 2019 Genral election

#2019 Genral election
print ("welcome to 2019 General election")

# polling unit name

menu = int(input("\n select your polling unit\n \n1) gbagada polling unit\n2) shomolu polling unit\n3) Bariga polling unit\n>"))
if (menu==1):
            print("gbagada polling unit")

elif(menu==2):
            print("shomlu polling unit")

elif(menu==3):
            print("bariga polling unit")

            

 #ask voter's candidate party
    #print out the user's choice
menu = int(input("\nplease select candidate party\n1) PDP\n2) APC\n3) SDP\n"))
if (menu== 1):
        print("PDP")

elif (menu== 2):
        print("APC")
        
elif(menu==3):
        print("SDP")
        
else:
        print("invalid choice")

print("thanks for coming")

#accumulation for 3 polling units

#total number of registered voters =500
#total number of eligible voters=300
z="score for pdp in shomolu + bariga + gbagada unit is"
shomolu=130
bariga=40 
gbagada=30

print (z,shomolu,bariga,gbagada,)

z="score for apc in shomolu + bariga + gbagada unit is"
pdp=180
bariga=50 
gbagada=10

print (z,shomolu,bariga,gbagada,)

z="score for sdp in shomolu + bariga + gbagada unit is"
shomolu=110
bariga=80 
gbagada=20

print (z,shomolu,bariga,gbagada,)

u="winner sdp with"
f=110
d=80
r=20

print (u,f,d,r,)
print ("total score 220")












