import nltk
from nltk import tokenize
from nltk.stem.wordnet import WordNetLemmatizer

# test

# string as input
text = str(raw_input())
#stext = text.split(" ")
#print stext[0]

#into multiple sentences
sentncs = tokenize.sent_tokenize(text)

moods = []

def checkfor_ind(arr):

	# checking for 0
	if arr[0][1] in ["PRP", "NNS", "NNP"]:
		# 0 for indicative
		return True
	if arr[0][1] == "EX" and arr[2][1] in ["CD","JJ"]:
		# 0 for indicative
		return True
	return False

def checkfor_imp(arr):
	#checking for 1
	if arr[0][1] == "NNP" and arr[1][1] == "VBP":
		print "NNP + VBP"
		return True

	if (arr[0][1] == "NNP" or arr[0][1] == "NN") and ( arr[len(arr)-2][1] == "NN" or arr[len(arr)-1][1] == "NN" ):
		print "NNp/NN...NN."
		return True
		
	if arr[0][1] == "VB" and arr[1][1] == "PRP":
		print "VB + PRB"
		return True
		
	if arr[0][1] == "VB" and ( arr[len(arr)-2][1] == "NN" or arr[len(arr)-1][1] == "NN" ):
		print "VB...NN."
		return True

	if arr[0][1] == "VB" and  arr[1][1] == "VB" and ( arr[len(arr)-2][1] == "NN" or arr[len(arr)-1][1] == "NN" ):
		print "VB+VB...NN."
		return True

	if arr[0][1] == "NNP" and (arr[1][1] == "RB" or arr[1][1] == "RP"):
		return True
	# checking for 1 over
	return False

def checkfor_sub(arr):
	# checking for 2
	hasword = False

	for i in arr:
		#print i[1]
		if i[1] in ["VBZ", "VBP", "VBD"]:
			v = WordNetLemmatizer().lemmatize(i[0],'v')
			if v in ["suggest", "wish", "recommend", "hope"]:
				hasword = True
				break;
		if i[1] in ["MD"]:
			return True

	if hasword == False:
		return False

	if arr[0][1] == "IN" and arr[1][1] == "PRP" and arr[2][1] in ["VBZ", "VBP", "VBD"]:
		return True
	if arr[0][1] == "DT" and arr[1][1] == "NN" and arr[2][1] in ["VBZ", "VBP", "VBD"]:
		return True
	if arr[0][1] == "PRP" and arr[1][1] in ["VBZ", "VBP", "VBD"]:
		return True

	# else
	return False


for s in sentncs:
	ptext = nltk.word_tokenize(s)
	arr_ptext = nltk.pos_tag(ptext)
	print arr_ptext
	if checkfor_sub(arr_ptext):
		moods.append(2)
		continue

	if checkfor_imp(arr_ptext):
		moods.append(1)
		continue

	if checkfor_ind(arr_ptext):
		moods.append(0)
		continue
	else:
		moods.append(-1)

print moods

print "..................\n total sentences: %d" % len(sentncs) 
print "Moods \n ......................"
print "Indicative mood: %d percent" % (moods.count(0) * 100 / len(sentncs))
print "Imperative mood: %d percent" % (moods.count(1) * 100 / len(sentncs))
print "Subjunctive mood: %d percent" % (moods.count(2) * 100 / len(sentncs))
if moods.count(-1) > 0:
	print "Unknown mood: %d" % (moods.count(-1) * 100 / len(sentncs))
#print "Subjunctive mood: %d%" % (moods.count(1) * 100 / len(arr_ptext))



