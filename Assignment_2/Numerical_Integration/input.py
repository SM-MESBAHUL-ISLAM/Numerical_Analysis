from Single_Segment import Single_Segment_Trapezoidal
from Multiple_segment_Trapezoidal import Multiple_Segment_Trapezoidal_Rule
from basis_simpsons import Basis_Of_Simpson
from Multiple_Segment_Simpson import Multiple_Segment_Simpson

print("Which integration method do you want to use?:")
print("1) Single Segment Trapezoidal Rule")
print("2) Multiple Segment Trapezoidal Rule")
print("3) 2 Segment Simpson's 1/3rd Rule")
print("4) Multiple Segment Simpson's 1/3rd Rule")

choice = int(input("Enter your choice: "))

if choice == 1:
    Single_Segment_Trapezoidal()
elif choice == 2:
    Multiple_Segment_Trapezoidal_Rule()
elif choice == 3:
    Basis_Of_Simpson()
elif choice == 4:
    Multiple_Segment_Simpson()
else:
    raise Exception('Input Error.')
