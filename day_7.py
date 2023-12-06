# # Python program to check whether the given character  
# # is a vowel or consonant  
  
# # Get an input character from the user  
# character = input("Enter a character: ")  
  
# # Creating a list of vowels  
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
  
# # Check if the character is a vowel or not  
# if character in vowels:  
#     print(f"The character '{character}' is a vowel!")  
# else:  
#     print(f"The character '{character}' is a consonant!")  


# # Python Program to check character is Alphabet Digit or Special Character
# ch = input("Please Enter Your Own Character : ")

# if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
#     print("The Given Character ", ch, "is an Alphabet") 
# elif(ch >= '0' and ch <= '9'):
#     print("The Given Character ", ch, "is a Digit")
# else:
#     print("The Given Character ", ch, "is a Special Character")



# # Python3 program to check if three 
# # sides form a  triangle or not  
  
# # function to check if three sides  
# # form a triangle or not  
# a = int(input("1st side:"))
# b = int(input("2nd side:"))
# c = int(input("3rd side:"))
# if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
#     print("Valid")
#     if (a==b==c):
#         print("equlatrel") 
#     if((a==b) or (b==c)or (c==a)):
#         print("isosecles")
#     else:
#         print("scalene")    
# else: 
#     print("Invalid")  
      


#counting notes
total_amount = int(input("Enter your total amount: "))

list_of_notes = [1000, 500, 100, 50, 20, 10, 5]

for i in list_of_notes:
    number_of_notes = total_amount // i
    total_amount %= i
    if number_of_notes != 0:
        print(f"The number of notes of {i} is {number_of_notes}")