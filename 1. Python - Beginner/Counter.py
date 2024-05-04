text = """
Look, I was gonna go easy on you and not to hurt your feelings
But I'm only going to get this one chance (six minutes, six minutes)
Something's wrong, I can feel it (six minutes, six minutes, Slim Shady, you're on)
Just a feeling I've got, like something's about to happen, but I don't know what
If that means what I think it means, we're in trouble, big trouble

My pen'll go off when I half-cock it
Got a fat knot from that rap profit
Made a livin' and a killin' off it
Ever since Bill Clinton was still in office
With Monica Lewinsky feelin' on his nutsack

Hit the Earth like an asteroid, did nothin' but shoot for the moon since (pew)
Mc's get taken to school with this music
'Cause I use it as a vehicle to bus the rhyme
Now I lead a new school full of students
Me? I'm a product of Rakim
Lakim Shabazz, 2Pac, N.W.A, Cube, hey Doc, Ren, Yella, Eazy, thank you, they got Slim
Inspired enough to one day grow up, blow up and be in a position
""" 
# for long texts we use 3 double quotes --> """ string """

print(text.split())
print(len(text.split()))
# The 'len' helps us to count the characters
# but if we want to count the words we can use the split --> text.split() 
# this splits each word and makes a list of them
# and now we can count them with 'len'

text2 = """
a b c a a b b b x x x 
"""
print(text2.split())

word_count = {}

for count in text2.split(): # 'Word' is the counter in for loop, it could be Asghar or Akbar
    if count in word_count:
     word_count[count] += 1
    else:
       word_count[count] = 1
# we create a dictionary to list the words we have in 'text2'
# then we do a text2.slpit() to separate them as words
# now we count them with a for loop and set a 'if' to count the words
# if a word does not exists in the dictionary, then counter adds it,
# with a value of 1 as shown in 'else: word_count[count] = 1'
# but if it exists, then adds a value to it with the 
# ---> 'if count in word_count: word_count[count] += 1'
# So then by printing the dictionary we would have   a:3, b:2, c:1 # 
print(word_count)
