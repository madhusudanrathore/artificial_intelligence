import xml.etree.ElementTree as ET

'''37176 SENTENCES'''
'''700201 WORDS AFTER REMOVING PUNCTUATIONS FROM EVERY SENTENCE'''
'''700201 POS TAGS FOR EACH WORD'''
'''802443 WORDS IF INCLUDING PUNCTUATION'''
'''43982 VOCABULARY'''
tree = ET.parse('../data/semcor.data.xml')
root = tree.getroot()#GET ROOT OF XML DOCUMENT

sentence_list=[]
pos_tags=[]

'''READ SENTENCES AND POS TAGS FOR WORDS FROM XML FILE'''
for sentence in root.iter('sentence'):#LOOP EACH SENTENCE TAG
	temp_sentence=[]
	for child in sentence.iter():#LOOP EACH WORD OF A SENTENCE
		temp_word=child.text
		temp_pos=child.get('pos')#GET POS TAG FOR CORRESPONDING WORD
		if temp_pos is not None and temp_pos != '.' and temp_word is not '\n':#PRE CONDITIONS, REMOVES PUNCTUATIONS
		#if temp_pos is not None and temp_word is not '\n':#PRE CONDITIONS, DOESN'T REMOVES PUNCTUATIONS
			temp_word=temp_word.translate(None, '!"#$%&()*+,\'-./:;<=>?@][\\^_`{|}~')#APPLY FILTERS
			temp_word=temp_word.lower()#CONVERT TO LOWERCASE
			temp_word=" ".join(temp_word.split())#REMOVE ALL TYPES OF WHITE SPACES
			temp_sentence.append(temp_word)
			pos_tags.append(temp_pos)
	sentence_list.append(temp_sentence)

'''WRITE WORDS TO EXTERNAL FILE'''
xml_words = open("stored_data/sentences.txt", "w")
xml_words.write("{}".format(sentence_list))
xml_words.close()

'''WRITE POS TAGS TO EXTERNAL FILE'''
xml_pos = open("stored_data/pos.txt", "w")
xml_pos.write("{}".format(pos_tags))
xml_pos.close()
