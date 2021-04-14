import re


#text = "First sentence. Second one! Third one? Last one."
text = """First sentence. 
Second one! 
Third one? Last one."""

#sentences = text.split(". ")
#sentences = re.split("[\?\!\.]", text)
sentences = re.split("\n", text)
#one_line_text = " ".join(sentences)
one_line_text = text.replace("\n","|")
#print(sentences)
print(one_line_text)