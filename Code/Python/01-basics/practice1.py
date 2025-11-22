#Taking user name and age

name=input("Enter User id: ")
age=int(input("Enter you age"))

print("My name is",name.title().rstrip(),"\nAge:",age+1)

# Question
print("If you apply 10V across a 1000Ω (1kohms) resistor,\nthe current flowing in the circuit will be:")

# Get voltage and resistance from user input
voltage = int(input("Enter the voltage: ").rstrip())  # Voltage in volts
ohms = int(input("Enter the resistance: ").rstrip())  # Resistance in ohms

# Calculate the current using Ohm's law: I = V / R
current = voltage / ohms

# Convert current to milliamps (1 A = 1000 mA)
current_mA = current * 1000

# Print the current in milliamps
print(f"The current flowing in the circuit will be {current_mA} mA.")
