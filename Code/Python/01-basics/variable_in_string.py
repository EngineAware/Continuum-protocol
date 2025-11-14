# Using variables in stings

# Using variable value insde  a string "its like connecting to one"

half_0='kilo' #value1
half_1='bytes'# value2
Bytes=f'{half_0}{half_1}'#f used for string are called f-string " '{}' are called placeholders" when you  write variable inside its.Its places by the value of that variable
# print(Bytes) output kilobytes
#why dont we use  string casting or case in it.
print(Bytes.title()) 
print(Bytes.lower()) #it will show the same ouput cause it already in lowercase
print(Bytes.upper())

terminal_0='ohms'
terminal_1='law'
omega=f"sysmbol of {terminal_0} {terminal_1} is derived  by greek letter called omega"
print(omega.title())
#you can put title lower upper anywhere you want output is same 

particles_0='nucleus'
particles_1='electrons'
charge=f"Postively charged  centre called:{particles_0}, Negatively charged called:{particles_1}"
#Atoms=f'Atoms={charge.title()}'
Atoms=f'Atoms={charge}'
print(Atoms.title()) # but still this wrong what if  Atoms was small letter it change that so i still learn you can put title in particles_0 or 1