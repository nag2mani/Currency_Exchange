import nagmani_a1
old=input('Enter original currency:')
new=input('Enter desired currency:')
amt=input('Enter original amount:')

# DO NOT modify the following code
# if the source currency is not valid, quit

if(not(nagmani_a1.is_currency(old))):
	print(old," is not a valid currency")
	quit()
# if the target currency is not valid, quit

if(not(nagmani_a1.is_currency(new))):
	print(new," is not a valid currency")
	quit()
else:
	print('You can exchange',amt,old,'for',nagmani_a1.exchange(old,new,amt),new)

	

