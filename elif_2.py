'''
a customer comes to the shop to buy Python books
demo the concept of stacked if else / ladder if else 
'''
book1 = "code 1 : Python Programming: Using Problem Solving Approach "
author1 ="Reema Thareja"

book2 = "code 2 : Python Programming: A Practical Approach "
author2 = "Vijay Kumar Sharma"

book3 = "code 3 : You Can Win "
author3 = "Shiv Khera"

book4 = "code 4 : Stay Hungry Stay Foolish "
author4 = "Rasgmi Bansal"

book5 = "code 5 : Wings of Fire"
author5 = "Dr.APJ Abdul Kalam"

book6 = "code 6 : The Story of My Experiments with Truth "
author6 = "M.K.Gandhi"

Genre1 = 'Education'
Genre2 = 'Self-Help'
Genre3 = 'Autobiography'

print ('Book avilable with us is as following ')
print()
print (book1)
print (book2)
print (book3)
print (book4)
print (book5)
print (book6)
print()
print (' ================================================= ')
choice = int(input('enter the book code of your choice '))
if choice == 1:
   print (' ***************************************** ')
   print (book1)
   print ('author is ',author1)
   print ('Genre:', Genre1)
   print ('Price is Rs 750 ')
   print ('how many quantities you wish to buy ? ')
   qty=int(input())
   bill = qty * 750
   print ('Your bill amount is Rs ',bill)
   print (' ***************************************** ')
elif choice == 2:
   print (book2)
   print ('author is ',author2)
   print ('Genre:', Genre1)
   print ('Price is Rs 650 ')
   print ('how many quantities your wish to buy ? ')
   qty=int(input())
   bill = qty * 650
   print ('Your bill amount is Rs ',bill)
elif choice == 3:
   print (book3)
   print ('author is ',author3)
   print ('Genre:', Genre2)
   print ('Price is Rs 300 ')
   print ('how many quantities your wish to buy ? ') 
   qty=int(input())
   bill = qty * 300
   print ('Your bill amount is Rs ',bill)
elif choice == 4:
   print (book4)
   print ('author is ',author4)
   print ('Genre:', Genre2)
   print ('Price is Rs 225 ')
   print ('how many quantities your wish to buy ? ')
   qty=int(input())
   bill = qty * 225
   print ('Your bill amount is Rs ',bill)
elif choice == 5:
   print (book5)
   print ('author is ',author5)
   print ('Genre:', Genre3)
   print ('Price is Rs 290 ')
   print ('how many quantities you wish to buy ? ') 
   qty=int(input())
   bill = qty * 290
   print ('Your bill amount is Rs ',bill)
elif choice == 6:
   print (book6)
   print ('author is ',author6)
   print ('Genre:', Genre3)
   print ('Price is Rs 550')
   print ('how many quantities your wish to buy ? ')
   qty=int(input())
   bill = qty * 550
   print ('Your bill amount is Rs ',bill)
else:
   print ('presently this book is NOT availble with us ')
   print('we will get it for you soon')
print ()
print ('--thank you Please visit again ---- ')

