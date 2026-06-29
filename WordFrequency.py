import sys

#check if user entered the arguments
if len(sys.argv) < 3:
    print("Usage: python <current file relative path> <full target file path> <N>")
    sys.exit()

#declare vars
file_path = sys.argv[1]
N = int(sys.argv[2])


#make into a word list
clean_word_list = []
with open(file_path, "r") as file:
    f = file.read() #read the content of the file
    word_list = f.split(" ") #seperate to words in a list
    clean_word_list = [word.strip('".,?!').lower() for word in word_list] # make it cleaner


#get a set of uniqe words
uniqe_words = set(clean_word_list)
word_dict = {}

for key in uniqe_words:
    word_dict[key] = 0 #restarting the values
    for word in clean_word_list:
        if key == word:
            word_dict[key] += 1

final_list = sorted(word_dict, key = lambda x: word_dict[x], reverse=True)

#final print
for n in range(N):
    print(f"the {n+1} frequent word is '{final_list[n]}' and it occured {word_dict[final_list[n]]}")


# my command:
# פייתון_למתקדמים\sys.argv_exrecise\sys.argv_exrecise.py C:\Users\yuval\OneDrive\אקדמיית_המתכנתים\פייתון_למתקדמים\sys.argv_exrecise\sys.argv_file.txt N