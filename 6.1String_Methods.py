str = 'avara\t kedavara'
print (str)

p = str.capitalize()  # capitalize first letter
print ('capitalize:', p)

p = str.casefold() # does lowercase but more aggressive
print ('casefold: ', p)

p = str.center(21,'t') # makes str centre of 21 and fills with 't'
print('center: ', p)

p = str.count('a',0,5) # counts no. of 'a' from 0 to 5
print ('count-a: ', p)

p = str.encode() # utf-8 encoding with strict errors
print('encode: ', p)

p = str.endswith('a',0,len(str)) # checks wether ends with 'a' in range
print ('endswith-a: ', p)

p = str.expandtabs(1) #\t expanded with default 8 spaces
print ('expandtabs: ', p)

p = str.find('a',0,10) # finds 'a' in range; return -1 if not found
print ('find-a: ', p)

p = 'The sum of 1 + 2 is {0}'.format('three') # for replacement of text in curly brackets
print ('format: ', p)

# format_mapping later

p = str.index('a',0,20) # tells index of letter; different from find as if string not find raise error not -1
print ('index-a: ', p)

p = str.isalnum() # true if string is alphanumeric
print ('isalnum: ', p)

p = str.isalpha() # true if string is alphabetic
print ('isalpha: ', p)

p = str.isascii() # true if string ascii
print ('isascii: ', p)

p = str.isdecimal() # true if string decimal
print ('isdecimal: ', p)

p = str.isdigit() # true if string digit
print ('isdigit: ', p)

p = str.isidentifier() # if keyword then true
print ('isidentifier: ', p)

p = str.islower() # even if one uppercase then false
print ('islower: ', p)

p = str.isnumeric() # if even one non-numeric then false
print ('isnumeric: ', p)

# isprintable later

p = str.isspace() # checks if all spaces
print ('isspace: ', p)

p = str.istitle() # if first letter of all words upper then true
print ('istitle: ', p)

p = str.isupper() # even if one lowercase then false
print ('isupper: ', p)

p = '#'.join(str) # It is reverse of split
print ('join: ', p)

p = str.ljust(20,'t') #left align instead of center
print ('ljust: ', p)

p = str.lower() # returns lowercase string
print ('lower: ', p)

p = str.lstrip('av') #removes 'a''v' letters from leading
print ('lstrip: ', p)

# marketrans later

p = str.expandtabs().partition('av') # split str at first occurence of 'ke'
print ('partition: ', p)

p = str.replace('av','##',4) # replace av with ## in 4 counts
print ('replace: ', p)

p = str.rfind('av',0,20) # find highest index of 'av'
print ('rfind: ', p)

p = str.rindex('av',0,20) # similar to rfind but if not present then error
print ('rindex: ', p)

p = str.rjust(25) # align right in 25 chars
print ('rjust: ', p)

p = str.rpartition('av') # partition at last occurence of 'ava'
print ('rpartition: ', p)

p = str.split('a', maxsplit = 5) # splits the string at 'av' (if no mention then space is delimitor) (if maxsplit not mention or -1 then all splits)
print ('split: ', p)

p = str.rsplit('a', maxsplit = 3) # similar to partition but can do more than 1
print ('rsplit: ', p)

p = str.strip('ar') # removes 'a' and 'r' from trailing and leading
print ('strip: ', p)

p = str.rstrip('ra') #removes 'r''a' letters from trailing
print ('rstrip: ', p)

p = str.splitlines() # splits at \n \r etc. if keepends = true in brackets then split but keep \n \r etc.
print ('splitlines: ', p)

p = str.startswith('a') # check startswith 'a' then true
print ('startswith: ', p)

p = str.swapcase() # swaps cases
print ('swapcase: ', p)

p = str.title() # First letter uppercase rest lower
print ('title: ', p)

# translate later

p = str.upper() # converts to upper case
print ('upper: ', p)

p = str.zfill(20) # in left fill with 0s
print ('zfill: ', p)
