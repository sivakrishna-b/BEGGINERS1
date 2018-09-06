sd = raw_input()
siva = ['a','e','i','o','u','A','E','I','O','U']
anu = ['b','c','d','f','g','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
if (sd in siva):
	print("Vowel")
elif (sd in anu):
	print("Consonant")
else:
	print("Invalid")
	
	
