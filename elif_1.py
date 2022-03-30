'''
PROBLEM STATEMENT .....
demo the concept of STACKED IF ELSE .....ladder if else ...
customer....ask for a dish...
price of the dish is like this:
INPUT      OUTPUT
.....      .....
Iddli      35/plate
Dosa       55 for 1
Sandwich   50 for 1 piece
Juice      50 for 1 glass
Tea/Coffee 20 for 1 cup

otherwise ....this item is not available in our resturant
'''

print('welcome to the resturant ')
print('-------------------------')
print('Dish available are : Iddli,  Dosa, Sandwich, Juice, Tea/Coffee')
print('--------------------------------------------------------------')
dish = input('enter the dish of your choice ')
if dish == 'Iddli':
    print('the plate of iddli has 2 pieces ')
    print('cost is 35/plate')
elif dish == 'Dosa':
    print('this is served with chutney and sambar')
    print('cost of Dosa 1 piece is Rs 55 ')
elif dish == 'Sandwich':
    print('cost of Sandwich Rs 50 for 1 piece ')
elif dish == 'Juice':
    print('cost of Juice Rs 50 for 1 glass ')
elif dish == 'Tea/Coffee':
    print('Enjoy your Tea/Coffee with Rs 20 per cup')
else:
    print('this item ', dish, ' is not available in our resturant ')
print()
print('<-----------Thank You------------>')
