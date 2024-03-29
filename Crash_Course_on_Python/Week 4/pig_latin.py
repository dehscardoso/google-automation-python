# Let's create a function that turns text into pig latin: a simple text transformation 
# that modifies each word moving the first character to the end and appending "ay" to 
# the end. For example, python ends up as ythonpay.

def pig_latin(text):
  say = ""
  temp = []
  words = text.split()
  for word in words:
    temp.append(word[1:] + word[0] + "ay")
    say = " ".join(temp)
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"