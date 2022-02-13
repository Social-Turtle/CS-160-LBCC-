print("Hello! My name is Legalbot, and I'm here to tell you your driving eligibility status according to your age.")
print("Please note that any criminal records, restrictions, or probations will not be taken into account here.")
print("Unfortunately, I am not quite smart enough for that.")
# a pleasant greeting to improve user experience and explain the capacity of the system

# provide instructions to user
age = int(input("What is your age? "))

# respond according to their input, barring impossibly high numbers.
if age >= 122:
    print("Okay, now that's just unreasonable. I may not be smart, but I'm certainly not that dumb.")
elif age == 15:
    print("You are eligible to take the Driver's Permit Exam.")
elif age >= 16:
    print("You are eligible to take the Driver's License Exam.")
else:
    print("You can walk, run, ride a bike, skateboard, etc: BUT YOU CAN NOT DRIVE LEGALLY")
