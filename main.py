"""String Rotation
Write a method is_rotation that, given two strings, will determine if one string is a rotation of the other. e.g. is_rotation("doghouse", "usedogho") returns true You can rotate the letters of "usedogho" to create "doghouse" e.g. is_rotation("dog", "dgo") returns false This is not a rotation even though the same letters are used exactly. Note: This is not a permutation problem. I 

Clarifying Questions:

In progress in addressing in my code:
Do they need to be the same length?
Do they need to be same case?
okay numbers, symbols are okay 
empty strings & spaces okay
okay to keep spaces input will not have spaces

Edge case: 
assume yes they need to be the same length
assume okay to have mixed case - make all lower case
okay to have numbers and symbols 

Give an example on your own and clarifying question that can be edge case 


returns true or false
take length of variables and compare
if they are the same then continue else return false
loop length of array compare take first letter and move to the end of the word and compare to the 2nd array
#how do I know if it is the start 
"doghouse", "usedogho"   
"""
def string_rotation(string1,string2):
    string3 = string1
    if len(string1) != len(string2):
        return False
    for i in range(len(string1)):
        string3 = string3[1:]+string3[0]
        if string3 == string2:
            print(f"string3:{string3}")
            return True
            

string1 = "doghouse"
string2 = "usedogho"
print(string_rotation(string1,string2))

""" other examples to look at:
 https://leetcode.com/problems/rotate-string/ * """
        



    









