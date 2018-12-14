#program to determine the grade point of Auchi polytechnic,Auchi Edo state
print("program to determine the Grade of com302 introduction to pascal")
Name= input("enter your name please:   ")
matric_no=input("enter your matric_no:   ")
course=input("enter the course you are studying:    ")
department=input("what department are you from:     ")
level=input("what level are you:         ")

course_work=int(input("enter the value for course_work:     "))
Exam_score=int(input("enter the value for exam_score:       "))
Total =course_work+Exam_score
print("The Totalmark is",Total)
          
if(Total>=75 and Total<=100):
              print("A")
              
elif(Total>=70 and Total<=74):
              print("AB")
elif(Total>=65 and Total<=69):
              print("B")
elif(Total>=60 and Total<=64):
              print("BC")
elif(Total>=55 and Total<=59):
              print("C")
elif(Total>=50 and Total<=54):
              print("CD")
elif(Total>=45 and Total<=49):
              print("D")
elif(Total>=40 and Total<=44):
              print("E")
else:
                  print("F")

if(Total>=50 and Total<=100):
                      print( "excellent result")
elif (Total>=44 and Total<=49):
                      print ("you can do better")
else:
                      print("poor result")



                  
          
          
          
