alien = {'color':'green','points':5}

print (alien['points'])


#Looping in Dictionary

user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }

for key,value in user_0.items():
    print(key +": " + value),

#List of Dictionary

aliens = []

for alien_numbers in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for value in aliens[:5]:
    print(value)

print ("...")

print("Total number of aliens: " + str(len(aliens)))