# Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) 
# in the list sports.
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports.insert(2, 'horseback riding')

# Write code to take ‘London’ out of the list trav_dest.
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
trav_dest.pop(7)

# Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method.
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
trav_dest.append('Guadalajara')

# For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing.
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = [ ]
for verb in verbs:
    ing.append(verb+"ing")
print(ing)

# Given the list of numbers, numbs, create a new list of those same numbers increased by 5. 
# Save this new list to the variable newlist.
numbs = [5, 10, 15, 20, 25]
newlist = [ ]
for i in range(len(numbs)):
   newlist.append(numbs[i]+5)
print(newlist)

# Given the list of numbers, numbs, modifiy the list numbs so that each of the original numbers are 
# increased by 5. Note this is not an accumulator pattern problem, but its a good review.
numbs = [5, 10, 15, 20, 25]
x=0
for numb in numbs:
    numbs[x]=numb+5
    x+=1
print(numbs)

# For each number in lst_nums, multiply that number by 2 and append it to a new list called larger_nums.
lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]
larger_nums=[]
for i in range(len(lst_nums)):
    larger_nums.append(lst_nums[i]*2)
print(larger_nums) 

# For each character in the string already saved in the variable str1, add each character to a 
# list called chars.
str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars = []
for i in str1:
    chars.append(i)

# Assign an empty string to the variable output. Using the range function, 
# write code to make it so that the variable output has 35 a s inside it 
# (like "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"). Hint: use the accumulation pattern!
output=""

for i in range(35):
    output=output+'a'
print(output)

# Currently there is a string called str1. Write code to create a list called chars which should contain 
# the characters from str1. Each character in str1 should be its own element in the list chars.
str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars = []
for i in str1:
    chars.append(i)

# For each character in the string saved in ael, append that character to a list that should be 
# saved in a variable app.
ael = "python!"
app = []
for i in ael:
    app.append(i)

# For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). 
# Save these past tense words to a list called past_wrds.
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []
for i in wrds:
    i = i + "ed"
    past_wrds.append(i)

# Below are a set of scores that students have received in the past semester. 
# Write code to determine how many are 90 or above and assign that result to the value a_scores.
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
scores_split = scores.split(" ")
a_scores = 0
for x in scores_split:
    x = float(x)
    if x >= 90:
        a_scores += 1

print(a_scores)

# Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. 
# Only the first letter of each word should be used, each letter in the acronym should be a capital letter, 
# and there should be nothing to separate the letters of the acronym. Words that should not be included in 
# the acronym are stored in the list stopwords. For example, if org was assigned the string “hello to world” 
# then the resulting acronym should be “HW”.
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

stopwords = set(w.upper() for w in stopwords)
acro = ''.join(i[0] for i in org.upper().split(' ') if i not in stopwords)

# Write code that uses the string stored in sent and creates an acronym which is assigned to the variable 
# acro. The first two letters of each word should be used, each letter in the acronym should be a capital 
# letter, and each element of the acronym should be separated by a “. ” (dot and space). 
# Words that should not be included in the acronym are stored in the list stopwords. For example, 
# if sent was assigned the string “height and ewok wonder” then the resulting acronym should be 
# “HE. EW. WO”.
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = '. '.join(word[:2].upper() for word in sent.split() if word not in stopwords)
print(acro)

# A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase 
# is a palindrome by reversing it and then checking if the reversed version is equal to the original. 
# Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.
p_phrase = "was it a car or a cat I saw"
r_phrase = p_phrase[::-1]

# Provided is a list of data about a store’s inventory where each item in the list represents the name 
# of an item, how much is in stock, and how much it costs. Print out each item in the list with the same 
# formatting, using the .format method (not string concatenation). For example, the first print statment 
# should read The store has 12 shoes, each for 29.99 USD.
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for item in inventory:
    item_desc, number, cost = item.split(", ")
    print("The store has {} {}, each for {} USD.".format(number, item_desc, cost))
