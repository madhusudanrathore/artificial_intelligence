import xml.etree.ElementTree as ET

'''THIS FILE DOES THE FOLLOWING'''
'''1)	READ DATA FROM XML FILE'''
'''2)	SAVE LIST OF TOKENIZED SENTENCES IN TXT FILE'''
'''3)	SAVE WORDS WITH THEIR POS TAGS IN A CSV FILE'''

'''37176 SENTENCES'''
'''700201 WORDS AFTER REMOVING PUNCTUATIONS FROM EVERY SENTENCE'''
'''700201 POS TAGS FOR EACH WORD'''
'''43982 VOCABULARY'''

tree = ET.parse('../data/semcor.data.xml')
root = tree.getroot()#GET ROOT OF XML DOCUMENT

sentence_list=[]

pos_word_csv_file_writer = open("stored_train_data/word_pos.csv", "w")
'''READ SENTENCES AND POS TAGS FOR WORDS FROM XML FILE'''
for sentence in root.iter('sentence'):#LOOP EACH SENTENCE TAG
	temp_sentence=[]
	for child in sentence.iter():#LOOP EACH WORD OF A SENTENCE
		temp_word=child.text#GET WORD
		temp_pos=child.get('pos')#GET POS TAG FOR CORRESPONDING WORD
		if temp_pos is not None and temp_pos != '.' and temp_word is not '\n':#PRE CONDITIONS, REMOVES PUNCTUATIONS
		#if temp_pos is not None and temp_word is not '\n':#PRE CONDITIONS, DOESN'T REMOVES PUNCTUATIONS
			temp_word=temp_word.translate(None, '!"#$%&()*+,\'-./:;<=>?@][\\^_`{|}~')#APPLY FILTERS
			temp_word=temp_word.lower()#CONVERT TO LOWERCASE
			temp_word=" ".join(temp_word.split())#REMOVE ALL TYPES OF WHITE SPACES
			temp_sentence.append(temp_word)
			pos_word_csv_file_writer.write("{},{}\n".format(temp_word,temp_pos))#WRITE WORDS AND POS TAGS
	sentence_list.append(temp_sentence)
pos_word_csv_file_writer.close()

'''WRITE TOKENIZED SENTENCES TO EXTERNAL FILE'''
tokenized_sentences = open("stored_train_data/sentences.txt", "w")
tokenized_sentences.write("{}".format(sentence_list))
tokenized_sentences.close()
