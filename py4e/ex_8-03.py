'''
 Open the file romeo.txt and read it line by line.
    For each line, split the line into a list of words using the split() method.
    The program should build a list of words. For each word on each line check 
    to see if the word is already in the list and if not append it to the list.
    When the program completes, sort and print the resulting words in python 
    sort() order as shown in the desired output.
'''

list_of_words = list()

#open the file:
fhandle = open('romeo.txt')

#split every line in a list of words
for lines in fhandle:
    words = lines.split()
   # print(words)
    for word in words:
        word.lower()
        if word not in list_of_words :
            list_of_words.append(word)

list_of_words.sort()
print(list_of_words)

