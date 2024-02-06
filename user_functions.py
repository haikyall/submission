def register_user():
	name1= input('Enter your first name:')
	name2= input('Enter your last name:')
	email= f'{name1}.{name2}@email.com'
	full= f'{name1} {name2}'
	created_user =({'user_name': full, 'email':email})


	print(f'Welcome {full}! Your email is {email}')

	return created_user

def edit_user(user):
	new1= input('Place your new first name:')
	new2= input('Place your new last name:')
	newmail= f'{new1}.{new2}@email.com'
	newfull= f'{new1} {new2}'
	updated_name=({'user_name': newfull, 'email':newmail})

	print(f'Your editted account is {newfull}')
	return updated_name
	