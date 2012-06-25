from pattern.en import tag
import sys
fname = ""
if len(sys.argv) < 2:
	print "supply a filename numbnuts"
	exit(1)

f = open (sys.argv[1],"r")

s = f.readlines()

f.close()

output = []
for line in s:
	line = line.strip()
	interestingList = []
	if line != "":
		for word, tg in tag(line):
			if tg == "JJ" and len(word) > 5:
				print word
				secondVowelPos = 0
				vowelCount = 0
				
				for i, letter in enumerate(reversed(word)):
					if letter in "aeiou" and vowelCount < 2:
						vowelCount += 1
						secondVowelPos = i + 1

				secondVowelPos = len(word) - secondVowelPos
				hehword = "smurf-" + word[secondVowelPos:]
				
				line = line.replace(word, hehword)						
					
				interestingList.append( hehword)
		output.append(line)
	else :
		output.append("\n")
for a in output:
	print a


