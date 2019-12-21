"""
def calTotal(num1, num2=0):
    return (num1+num2)

print(calTotal(3))
"""

"""lstName = ["Jahanzeb", "Ali", "Rehan", "Dawood"]
#lstName.append("Dawood")
#lstName.pop(3)
#print(lstName.count("Dawood"))
lstName.pop()
print(lstName)"""

from collections import deque
lstName = deque(["Jahanzeb", "Ali", "Rehan", "Dawood"])
lstName.popleft()
print(lstName)
