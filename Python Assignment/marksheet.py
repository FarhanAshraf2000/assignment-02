eng =int(input("Enter marks of English : "))
math = int(input ("Enter marks of Maths :"))
isl= int(input ("Enter marks of Islamiat :"))
total_marks = eng + math + isl
per = int ((total_marks / 300)* 100)
if (per > 100 or  per <0  ):
    print ("The marks that you have Entered are not valid :")
elif (per <=100 and per >=90 ):
    print ("your Grade is : A+\nyour percentage is:",(per), "\ntotal marks are :",(total_marks))   
elif (per <=90 and per >=80 ):
    print ("your Grade is A\nyour percentage is:",(per),"\ntotal marks are :",(total_marks))
elif (per <=80 and per >=70 ):
    print ("your Grade is B+ \nyour percentage is:",(per),"\ntotal marks are :",(total_marks))
elif (per <=70 and per >=60 ):
    print ("your Grade is B\nyour percentage is:",(per),"\ntotal marks are :",(total_marks))
elif (per <=60 and per >=50):
    print ("your Grade is C \nyour percentage is:",(per),"\ntotal marks are :",(total_marks))
elif (per <=50 and per >=40 ):
    print ("your Grade is D  \nyour percentage is:",(per),"\ntotal marks are :",(total_marks))
elif (per <=40 and per >=20 ):
    print ("you have failed this semester  \nyour percentage is :",(per),"\ntotal marks are :",(total_marks))    



