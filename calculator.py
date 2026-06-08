while True :
    try :
	       a= int ( input ( "enter first number:"))
	       b= int (input ( "enter second number :"))   
	       op = input ( "enter operator ( + , - , * , / , // , **, %  ) ")
	       if op == "+" :
	       	print ("the addition of the numbers is :", a + b)
	       elif op == "-" :
	       	print ( "the subtraction of the numbers is :", a - b)
	       elif op == "*" :
	       	print ( "the multiplication of the numbers is :" , a * b)
	       elif op == "/" :
	              if b == 0 :
	              	print ( "cannot division by 0 ")
	              else :
	              	print ( "the division of the numbers is :" , a / b)
	       elif op == "//" :
	       	   if b == 0 :
	       	   	print ( "floor division of 0 cannot possible ")
	       	   else:
	       	   	print ( "the floor division of the numbers is :" , a // b)
	       elif op == "**" :
	           print ( "the exponential value of the numbers is :" , a ** b)
	       else :
	       	print ( "invalid ")
    except ValueError :
    	print ( " Error : enter valid number : ")
    	
    again =  input ( "continue ? ( yes / no )").strip().lower()
    if again == "no" :
    	print ( " thank you \"byee\"")
    	break