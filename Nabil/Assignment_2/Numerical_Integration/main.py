from single_segment_trapezoidal import Single_Segment_Trapezoidal
from Multi_segment_trapezoidal import Multiple_Segment_Trapezoidal_Rule
from basis_simpsons import Basis_Of_Simpson
from Multi_segment_simpson import Multiple_Segment_Simpson

print("Which integration method do you want to use?:")
print("1) Single Segment Trapezoidal Rule")
print("2) Multiple Segment Trapezoidal Rule")
print("3) 2 Segment Simpson's 1/3rd Rule")
print("4) Multiple Segment Simpson's 1/3rd Rule")

option = int(input("Enter your option: "))

if option == 1:
    Single_Segment_Trapezoidal()
elif option == 2:
    Multiple_Segment_Trapezoidal_Rule()
elif option == 3:
    Basis_Of_Simpson()
elif option == 4:
    Multiple_Segment_Simpson()
else:
    raise Exception('Input Error.')
