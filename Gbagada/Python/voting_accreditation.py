#NAME: AZUNNA, AUGUSTINE UCHECHUKWU
#CENTRE: RCCG, MARANATHA, GBAGADA
#CLASS: PYTHON
#This is a voting machine for accreditation and voting process of an election
#This Machine is to allow voters to be accredited and cast their vote at once
Male=0
Female=0
APC=0
APGA=0
DPP=0
PDP=0
while True:
# This is accreditation for process for voters by the Presiding Officer
   PO=input("Any voter?\nYES\nNO\n")
#Presiding Officer ask the voter to input his/her details
   if (PO.lower ()=="yes"):
      print("please enter the last four (4) digits of your PVC number: ")
      pvc=input ()
      Voter=input ("please enter your sex\n(a)Male\n(b)Female\n")
      if(Voter.lower ()=="a"):
         Male+=1
      if(Voter.lower ()=="b"):
            Female+=1
#This is the voting 
      Party=input("Please chooose your candidate by selecting the Party HE/SHE represents\n(a)APC\n(b)APGA\n(c)DPP\n(d)PDP\n")
      if(Party.lower ()=="a"):
         APC+=1
      elif(Party.lower ()=="b"):
         APGA+=1
      elif(Party.lower ()=="c"):
         DPP+=1
      else:
         PDP+=1
   else:
     break
Total_of_voters=Male+Female
print("\n\nTotal Male voters=", Male)
print("\n\nTotal Female voters=",Female)
print("\n\nTotal votes for APC=",APC)
print("\n\nTotal votes for APGA=",APGA)
print("\n\nTotal votes for DPP=",DPP)
print("\n\nTotal votes for PDP=",PDP)
print("\n\nTotal number of voters",Total_of_voters)
#Declaration of Percentage vote
percentage_APC=(APC/Total_of_voters)*100
percentage_APGA=(APGA/Total_of_voters)*100
percentage_DPP=(DPP/Total_of_voters)*100
percentage_PDP=(PDP/Total_of_voters)*100
print("\n\nThe percentage of APC vote=",round(percentage_APC, 2))
print("\n\nThe percentage of APGA vote=",round(percentage_APGA, 2))
print("\n\nThe percentage of DPP vote=",round(percentage_DPP, 2))
print("\n\nThe percentage of PDP vote=",round(percentage_PDP, 2))
#Declaration of winner
if (percentage_APC>percentage_APGA and percentage_APC>percentage_DPP and percentage_APC>percentage_PDP and percentage_APC>=50):
   print("\n\nThe winner is APC")
elif(percentage_APGA>percentage_APC and percentage_APGA>percentage_DPP and percentage_APGA>percentage_PDP and percentage_APGA>=50):
   print("\n\nThe winner is APGA")
elif(percentage_DPP>percentage_APC and percentage_DPP>percentage_APGA and percentage_DPP>percentage_PDP and percentage_DPP>=50):
   print("\n\nThe winner is DPP")
elif(percentage_DPP>percentage_APC and percentage_DPP>percentage_APGA and percentage_DPP>percentage_PDP and percentage_DPP>=50):
    print("\n\nThe winner is PDP")
else:
   print("\n\nTHERE WILL BE A RERUN ELECTION")

     
        
      
         
   
   
   
          
