import xml.etree.ElementTree as ET

tree = ET.parse('../data/semcor.data.xml')
root = tree.getroot()#GET ROOT OF XML DOCUMENT

'''READ SENTENCES FROM XML FILE'''
sentence_list = []#LIST TO HOLD ALL SENTENCES
for sentence in root.iter('sentence'):#LOOP EACH SENTENCE TAG
	temp_sen = ''
	for child in sentence.iter():#LOOP EACH WORD OF A SENTENCE AND APPEND IN TEMPORARY SENTENCE
		text = child.text
		temp_sen+=text+' '
	
	temp_sen=temp_sen.translate(None, '!"#$%&()*+,\'-./:;<=>?@][\\^_`{|}~')#APPLY FILTERS
	temp_sen=temp_sen.lower()#CONVERT TO LOWERCASE
	temp_sen=" ".join(temp_sen.split())#REMOVE ALL TYPES OF WHITE SPACES
	sentence_list.append(temp_sen)

'''READ POS TAGS'''
pos_arr=[]#LIST TO HOLD ALL POS TAGS
for sentence in root.iter('sentence'):#LOOP EACH SENTENCE
	for child in sentence.iter():#LOOP EACH WORD OF A SENTENCE
		temp=child.get('pos')#GET POS TAG FOR CORRESPONDING WORD
		if temp is not None:
			pos_arr.append(temp)

'''WRITE SENTENCES TO EXTERNAL FILE'''
text_file_for_xml = open("sentences.txt", "w")
text_file_for_xml.write('{}'.format(sentence_list))
text_file_for_xml.close()

'''WRITE POS TAGS TO EXTERNAL FILE'''
text_file_for_pos_tags = open("pos_tags.txt", "w")
text_file_for_pos_tags.write('{}'.format(pos_arr))
text_file_for_pos_tags.close()