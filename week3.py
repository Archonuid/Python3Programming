# Write code to assign the string "You can apply to SI!" to output if the string "SI 106" is in the list 
# courses. If it is not in courses, assign the value "Take SI 106!" to the variable output.
courses = ["ENGR 101", "SI 110", "ENG 125", "SI 106", "CHEM 130"]
if "SI 106" in courses:
    output = "You can apply to SI!"
else: 
    output = "Take SI 106"

# Create a variable, b, and assign it the value of 15. Then, write code to see if the value b is greater 
# than that of a. If it is, a’s value should be multiplied by 2. If the value of b is less than or equal 
# to a, nothing should happen. Finally, create variable c and assign it the value of the sum of a and b.
a = 20
b = 15
if b > a:
   a = a*2
c = b + a
print(c)

# Create one conditional to find whether “false” is in string str1. If so, assign variable output 
# the string “False. You aren’t you?”. Check to see if “true” is in string str1 and if it is then assign 
# “True! You are you!” to the variable output. If neither are in str1, assign “Neither true nor false!” 
# to output.
str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"
if 'false' in str1:
    output = "False. You aren't you?"
elif "true" in str1:
    output = "True! You are you!"
else:
    output = "Neither true nor false"

# Create an empty list called resps. Using the list percent_rain, for each percent, 
# if it is above 90, add the string ‘Bring an umbrella.’ to resps, otherwise if it is above 80, 
# add the string ‘Good for the flowers?’ to resps, otherwise if it is above 50, add the string 
# ‘Watch out for clouds!’ to resps, otherwise, add the string ‘Nice day!’ to resps. 
# Note: if you’re sure you’ve got the problem right but it doesn’t pass, then check that you’ve matched 
# up the strings exactly.
percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = []
for i in percent_rain:
    if i > 90:
        resps.append("Bring an umbrella.")
    elif i >80:
        resps.append("Good for the flowers?")                   
    elif i > 50:
        resps.append("Watch out for clouds!")
    else:
        resps.append("Nice day!")

# For each string in the list words, find the number of characters in the string. 
# If the number of characters in the string is greater than 3, add 1 to the variable num_words so 
# that num_words should end up with the total number of words with more than 3 characters.
words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0
for i in words:
    if len(i) > 3:
        num_words += 1

# Challenge For each word in words, add ‘d’ to the end of the word if the word ends in “e” to 
# make it past tense. Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a 
# list called past_tense.
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for i in words:
    if(i[len(i)-1] == 'e'):
        i += 'd'
    else:
        i += 'ed'
    past_tense.append(i)

# rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month 
# (in inches) with every month separated by a comma. Write code to compute the number of months that have 
# more than 3 inches of rainfall. Store the result in the variable num_rainy_months. In other words, count 
# the number of items with values > 3.0.
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rainfall_mi_split = rainfall_mi.split(",")
num_rainy_months = 0
for x in rainfall_mi_split:
    x = float(x)
    if x > 3.0:
        num_rainy_months += 1

print(num_rainy_months)

# The variable sentence stores a string. Write code to determine how many words in sentence start and 
# end with the same letter, including one-letter words. Store the result in the variable same_letter_count.
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
same_letter_count = sum(w[0] == w[-1] for w in sentence.split())
print(same_letter_count)

# Write code to count the number of strings in list items that have the character w in it. 
# Assign that number to the variable acc_num.
# HINT 1: Use the accumulation pattern!
# HINT 2: the in operator checks whether a substring is present in a string.
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
count = 0
for i in items:
    if 'w' in i:
        count += 1
acc_num = count

# Write code that counts the number of words in sentence that contain either an “a” or an “e”. 
# Store the result in the variable num_a_or_e.
# Note 1: be sure to not double-count words that contain both an a and an e.
# HINT 1: Use the in operator.
# HINT 2: You can either use or or elif.
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e = 0
for i in sentence.split():
    if ('a' in i) or ('e' in i):
        num_a_or_e += 1

print(num_a_or_e)

# Write code that will count the number of vowels in the sentence s and assign the result to the variable 
# num_vowels. For this problem, vowels are only a, e, i, o, and u. Hint: use the in operator with vowels.
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
# Write your code here.
num_vowels = sum([1 for i in s if i in vowels])
print(num_vowels)