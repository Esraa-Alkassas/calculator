'''
واضح كدا ان موضوع الفانكشنز هنا سهل جدا ، مش فيه لا بروتوتايب ولا امبلمنتيشن ولا الكلام دا كله ، هذا رائع !

'''

# طبعا كما تعلمين ان انبوت دخلها ايا كان ف هو ديما استرينج ف لازم اعمله كاستنج لل انا عايزاه بقا

 # سيبك م الكلام ال فوق دا ، المهم ابقي كمليها زي م كريم كان بيقول هتبقا احلى 


'''
عندي سؤال، انا جربت اكتب اي حاجة غير حرف البي الكابيتال دا كان بيشتغل ف المود التاني ف دا كدا معناه ان لو كتبت حرف الاس هيتحقق ال بعد اف علطول 
اما لو كتبت اي حاجة غير حتى لو مش حرف البي ف هيتحقق المود التاني علطول ؟! 
طب م كدا ايه فايدة ان اكتب الحرف التاني دا ؟!
'''



mode = input ("please choose the mode you want; Scientific or programming? ")
result = "S" or "P"
if mode == result:
	x = input ("please enter the first number")
	y = input ("please enter the first number")
	
	x = int (x)
	y = int (y)
	
	print ("summation of the two variables = %d" % (x+y))
	print ("sub of the two variables = %d" % (x-y))
	print ("mul of the two variables = %d" % (x*y))
	print ("division of the two variables = %d" % (x/y))
	print ("floor division of the two variables = %d" % (x//y))
	print ("modulus of the two variables = %d" % (x%y))
	print ("Exponential of the two variables = %d" % (x**y))

else:
	z = input ("please enter your number in decimal")
	z = int (z)
	
	BIN = bin (z)
	HEX = hex(z)
	OCT = oct (z)
	print ("binary of your number is", BIN)
	print ("HEX of your number is" , HEX)
	print ("oct of your number is", OCT)