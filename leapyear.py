#year = int(input("Please Enter the Year Number you wish: "))

#if year % 4 != 0:
 #   print("No")
#else:
 #   if year % 100 == 0:
  #      if year % 400 == 0:
   #         print("Yes")
    #    else:
     #       print("No")
    #else:
     #   print("Yes")

#year = int (input(" Please Enter the Year Numner ur wish : "))
#if year % 400 == 0:
 #   print("Yes")
#elif year % 100 == 0:
 #   print("No")
#elif year % 4 == 0:
 #   print("Yes")
#else:
 #   print("No")

year = int (input(" Please Enter the Year Numner ur wish : "))
if year % 100 != 0 and year % 4 == 0:
    print("Yes")
elif year % 100 == 0 and year % 400 == 0:
    print("Yes")
else:
    print("No")