balance = 10000
USSD = '*555#'
options = '1. Buy Airtime.\n2. Buy Data.\n3. Borrow.\n4. Check Balance.\n5. Stop.'
Code = input('Enter *555# to buy or borrow airtime:\n>>>')
#if Code == USSD:
while Code == USSD:
	print(options)
	option = int(input('Enter option:\n>>>'))
	if option == 1:
		print('1. Buy for self.\n2. Buy for a friend.')
		option = int(input('Enter option:\n>>>'))
		if option == 1:
			amount_for_self = float(input('Enter amount:\n>>>'))
			if amount_for_self <= balance:
				balance -= amount_for_self
				print('AIRTIME PURCHASE SUCCESSFUL!')
			elif amount_for_self > balance:
				print('INSUFFICIENT FUNDS!')
			else:
				print('INVALID INPUT!')
		elif option == 2:
			reciver_number = int(input('Enter reciver number:\n>>>'))
			amount_for_frnd = float(input('Enter amount:\n>>>'))
			if amount_for_frnd <= balance:
				balance -= amount_for_frnd
				print('PURCHASE FOR FRIEND SUCCESSFUL!')
			elif amount_for_frnd > balance:
				print('INSUFFICIEN FUNDS!')
			else:
				print('INVALID INPUT!')
	elif option == 2:
		print('1. Buy for self.\n2. Buy for a friend.')
		option = int(input('Enter option:\n>>>'))
		if option == 1:
			print('1. 1GB=500\n2. 2GB=800\n3. 3GB=1000')
			option = int(input('Enter option:\n>>>'))
			if option == 1:
				if balance >= 500 or balance == 500:
					balance -= 500
					print('1GB DATA PURCHASE SUCCESSFUL!')
				else:
					print('INSUFFICEINT FUNDS!')
			elif option == 2:
				if balance >= 800 or balance == 800:
					balance -= 800
					print('2GB DATA PURCHASE SUCCESSFUL!')
				else:
					print('INSUFFICEINT FUNDS!')
			elif option == 3:
				if balance >= 1000 or balance == 1000:
					balance -= 1000
					print('3GB DATA PURCHASE SUCCESSFUL!')
				else:
					print('INSUFFICEINT FUNDS!')
			else:
				print('INVALID INPUT!')
		elif option == 2:
			print('1. 1GB=500\n2. 2GB=800\n3. 3GB=1000')
			option = int(input('Enter option:\n>>>'))
			if option == 1:
				reciver_number = int(input('Enter recivers number:\n>>>'))
				if balance >= 500 or balance == 500:
					balance -= 500
					print('1GB DATA PURCHASE SUCCESSFUL!')
				else:
					print('INSUFFICEINT FUNDS!')
			elif option == 2:
				reciver_number = int(input('Enter recivers number:\n>>>'))
				if balance >= 800 or balance == 800:
					balance -= 800
					print('2GB DATA PURCHASE SUCCESSFUL!')
				else:
					print('INSUFFICEINT FUNDS!')
			elif option == 3:
				reciver_number = int(input('Enter recivers number:\n>>>'))
				if balance >= 1000 or balance == 1000:
					balance -= 1000
					print('3GB DATA PURCHASE SUCCESSFUL!')
				else:
					print('INSUFFICEINT FUNDS!')
			else:
				print('INVALID INPUT!')

		
	elif option == 3:
		print('1. Borrow airtime\n2. Borrow data')	
		option = int(input('Enter option:\n>>>'))	
		if option == 1:
			amount_to_borrow = float(input('Enter amount:\n>>>'))
			print('AIRTIME BORROW SUCCESSFUL!')
		elif option == 2:
			print('1. 1GB=500\n2. 2GB=800\n3. 3GB=1000')
			option = int(input('Enter option:\n>>>'))
			if option == 1:
				print('1GB DATA BORROW SUCCESSFUL!')
			elif option == 2:
				print('2GB DATA BORROW SUCCESSFUL!')
			elif option == 3:
				print('3GB DATA BORROW SUCCESSFUL!')
			else:
				print('INVALID OPTION!')
		else:
			print('INVALID INPUT!')
	elif option == 4:
		print(f'YOUR BALANCE IS {balance}')
	elif option == 5:
		print('BYE BYE!')
		break
	else:
		print('INVALID INPUT!')
else:
	print('INVALID OPTION!')


