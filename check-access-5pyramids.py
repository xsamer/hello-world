#! python3

import requests , os , sys , time

if sys.platform in ["linux","linux2"]:
	W = '\033[0m'
	G = '\033[32;1m'
	R = '\033[31;1m'
	
else:
	W = ''
	G = ''
	R = ''


print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++' )
print ('+                                 +                                   +' )
print ('+                                + +                                  +' )
print ('+                               + + +                                 +' )
print ('+                              + + + +                                +' )
print ('+                             ********+                               +' )
print ('+                            +********++                              +' )
print ('+                           + ** + + + ++                             +' )
print ('+                          ++ ** + + + + +                            +' )
print ('+                         + + ********  + +                           +' )
print ('+                        ++++ ******** +++++                          +' )
print ('+                       +++++++++++ ** ++++++                         +' )
print ('+                      ++++++++++++ ** +++++++                        +' )
print ('+                     +++++++ ******** ++++++++                       +' ) 
print ('+                    ++++++++ ******** +++++++++                      +' )
print ('+                   + + + + +  pyramid + + + +  +                     +' )
print ('+                  +ADMIN: MAHDAWY-3LAA-FALASTINY+                    +' )
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++' )
print()
print(G + 'FILE ACCESS NAME => ', end='' + W)
put = input()

file = open(put , 'r')
readfile = file.read()
lista = readfile.split('\n')

# lista = ['kjlahsflhas' , 'ajskhkgas']

file.close()
print()
print(G + 'Starting ...')
print()
live = []
die = []

print(W + 'the number of access tokens : ' , G + str(len(lista)))
print()
print('+'.center(40 , '+'))
print()
# def chk(access):
	

x = 1
x2 =  .5
for access in lista:
	if x == 6:
		time.sleep(x2)
		x = 1
		x2 += .1
	if not access.isalnum():
		continue
	
	try:
		res = requests.get('https://graph.facebook.com/me?access_token=' + access)
	except Exception as exc:
		print(R + 'Error ... Skipping and' + G + ' Continue ...')
	


	if 'Error validating access token' in res.text:
		print( G + '[*]' + ' Checking : ' + W + access  , end='')
		print(R + ' [!] DIE ...')
		die.append(access)
	elif 'The access token could not be decrypted' in res.text:
		print( G + '[*]' + ' Checking : ' + W + access  , end='')
		print(R + ' [!] DIE ...')
		die.append(access)
	elif 'Malformed access token' in res.text:
		print( G + '[*]' + ' Checking : ' + W + access  , end='')
		print(R + ' [!] DIE ...')
		die.append(access)

	else:
		print( G + '[*]' + ' Checking : ' + W + access  , end='')
		print(G + ' [!] LIVE ...')
		live.append(access)
	x +=1


print('LIVE = ', len(live))
print('DIE = ', len(die) )

os.makedirs('check-access-5pyramids' , exist_ok=True)

livefile = open(os.path.join('.','check-access-5pyramids','live.txt') , 'a')

for i in live:
	livefile.write(i + '\n')
livefile.close()

diefile = open(os.path.join('.','check-access-5pyramids','die.txt'), 'a')
for i in die:
	diefile.write(i + '\n')
diefile.close()
print('[*] The Results have been saved in the folder named'+ G + ' [check-access-5pyramids] ... Goodbye' +W )
