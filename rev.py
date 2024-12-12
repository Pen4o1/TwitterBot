text_file = open("tweet.txt","r")
str1 = text_file.read()
revstr = ""
revstr = (str1[::-1])
text_file.close()

f = open("rev_tweet.txt","w")
f.write(revstr)
f.close()


























