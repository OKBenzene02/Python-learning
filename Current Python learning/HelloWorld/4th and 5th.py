# # ===========================================================
# ASCII to Characters and Characters to ASCII

# # Characters to ascii
# def index(a: str):
#       i = 0
#       for i in range(len(character)):
#             if a == character[i]:
#                   break
#       return i
#
# character = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
# charEnter = input("Enter the character to convert to ascii number: ")
#
# if (charEnter == 'A'):
#       print(f"{charEnter} ascii value is 65.")
# else:
#       print(f"{charEnter} ascii value is {65 + index(charEnter)}")

# # Ascii to characters
# character = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
# AsciiValue = int(input("Enter the number to convert in the ascii character: "))
#
# index = 65
# if AsciiValue == 65:
#     print(f"{AsciiValue} ascii character is A.")
#
# else:
#     index = AsciiValue - 65
#     print(f"{AsciiValue} ascii character is {character[index]}")

# # ===========================================================
#  Bit Stuffing and De-stuffing

# Bit stuffing
# bit = '111111001'
# bitList = list(bit)
#
# i = 0
# count = 0
#
# while i < len(bit):
#     if bitList[i] == '1':
#         count += 1
#     else:
#         count = 0
#     if count == 6:
#         bitList.insert(i, '0')
#         count = 0
#     i += 1
#
# print(bit)
# print("".join(bitList))

# Bit De-stuffing
# bit = "101011111001"
# bitLst = list(bit)
# i = 0
# count = 0
#
# while i < len(bitLst):
#     if bitLst[i] == '1':
#         count += 1
#     else: count = 0
#
#     if count == 5:
#         bitLst.__delitem__(i+1)
#         count = 0
#
#     i += 1
#
# print(bit)
# print("".join(bitLst))