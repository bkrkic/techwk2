
#Open the text file
file = open('test.txt', 'r')

#Create a ditionary
dic = dict()
for line in file:
    line = line.strip()
    words = line.split(" ")

    for word in words:
        if word in dic:
            dic[word] = dic[word] + 1
        else:
            dic[word] = 1

dic_sum = sum(dic.values())
print(dic_sum)
#Print the contents of the dictionary in sorted order by value using lambda
for key, value in sorted(dic.items(), key=lambda p:p[1], reverse=True):
    #Formatting output and printing a histogram
    print(f"{key.upper():10s} [{'*' *(dic.get(key)*2)}] {round(value/dic_sum*100)}%")





