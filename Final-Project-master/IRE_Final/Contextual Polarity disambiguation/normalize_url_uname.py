import sys
import re

####################
#	For normalizing - url , username , emoticons
#
###################
#emoticons_dict={':-)':'pos_POL', ':)':'pos_POL', ':o)':'pos_POL', ':]':'pos_POL' ,':3':'pos_POL',':c)':'pos_POL' , ':D':'Extpos_POL', 'C:':'Extpos_POL', 'D8':'ExtNEG_POL', 'D;':'ExtNEG_POL', 'D=':'ExtNEG_POL', 'DX':'ExtNEG_POL', 'v.v':'ExtNEG_POL', ':|':'Neut_POL'}



emoticons_dict={'>.<': 'neg_POL', ':(': 'neg_POL', ':)': 'pos_POL', ':c)': 'pos_POL', 'B^D': 'Ext_pos_POL', ':<': 'neg_POL', 'v.v': 'Ext_neg_POL', ':>': 'pos_POL', ':/': 'neg_POL', 'd:': 'cheeky_POL', ':3': 'pos_POL', '=]': 'pos_POL', '=\\': 'neg_POL', '=D': 'Ext_pos_POL', '=L': 'neg_POL', ':o': 'surprise_POL', '=3': 'Ext_pos_POL', 'O-O': 'surprise_POL', ':b': 'cheeky_POL', ':c': 'neg_POL', ':|': 'neut_POL', ':}': 'pos_POL', ':{': 'neg_POL', '=/': 'neg_POL', '=)': 'pos_POL', ':-p': 'cheeky_POL', ':L': 'neg_POL', ':O': 'surprise_POL', ':D': 'Ext_pos_POL', ':@': 'Ext_neg_POL', ":'(": 'Ext_neg_POL', ":')": 'Ext_pos_POL', "D-':": 'Ext_neg_POL', '*-)': 'cheeky_POL', '=-3': 'Ext_pos_POL', ':[': 'neg_POL', ':P': 'cheeky_POL', ':S': 'neg_POL', '8)': 'pos_POL', ':-O': 'surprise_POL', '8-D': 'Ext_pos_POL', ':-))': 'Ext_pos_POL', ':-D': 'Ext_pos_POL', ':-[': 'neg_POL', 'o_o': 'surprise_POL', ':\\': 'neg_POL', ':-o': 'surprise_POL', ':]': 'pos_POL', ':-b': 'cheeky_POL', ':-c': 'neg_POL', ';]': 'cheeky_POL', ':-|': 'neut_POL', ';D': 'cheeky_POL', 'o_O': 'surprise_POL', ":'-(": 'Ext_neg_POL', ":'-)": 'Ext_pos_POL', ';)': 'cheeky_POL', ';(': 'neg_POL', ':-(': 'neg_POL', ':-)': 'pos_POL', ':-.': 'neg_POL', ':-/': 'neg_POL', ':-,': 'cheeky_POL', 'X-D': 'Ext_pos_POL', '8D': 'Ext_pos_POL', ':-<': 'neg_POL', '8-0': 'surprise_POL', ':p': 'cheeky_POL', 'xp': 'cheeky_POL', ':-||': 'Ext_neg_POL', ':o)': 'pos_POL', '>:(': 'Ext_neg_POL', '>:/': 'neg_POL', 'xD': 'Ext_pos_POL', 'x-D': 'Ext_pos_POL', '>:O': 'surprise_POL', 'XD': 'Ext_pos_POL', '>:P': 'cheeky_POL', '=p': 'cheeky_POL', '>:[': 'neg_POL', 'XP': 'cheeky_POL', 'D:<': 'Ext_neg_POL', '>:\\': 'neg_POL', ':^)': 'pos_POL', 'x-p': 'cheeky_POL', 'o-o': 'surprise_POL', 'DX': 'Ext_neg_POL', 'O_O': 'surprise_POL', ':-P': 'cheeky_POL', 'O_o': 'surprise_POL', ';-)': 'cheeky_POL', '=-D': 'Ext_pos_POL', ';-]': 'cheeky_POL', '*)': 'cheeky_POL', ';^)': 'cheeky_POL', 'X-P': 'cheeky_POL', 'D=': 'Ext_neg_POL', 'D:': 'Ext_neg_POL', 'D;': 'Ext_neg_POL', 'D8': 'Ext_neg_POL'}



f = open(sys.argv[1], "r")

entire_emo = []

for line in f:
	tem = line[:-1]
	tem = tem.split()

	tw = []

	for_emo = {'pos_POL': 0, 'Ext_pos_POL' : 0, 'neg_POL' : 0, 'Ext_neg_POL': 0, 'surprise_POL' : 0, 'cheeky_POL':0 , 'neut_POL' : 0};


	for i in tem:
		n = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'http/URL', i)
		n = re.sub('@[^\s]+', '@someUSER', n)
		
		if n in emoticons_dict:
			tw.append(emoticons_dict[n])
			val = emoticons_dict[n]
			for_emo[val] += 1
			continue
			
		tw.append(n)

	temlist = []
	for i in sorted(for_emo.keys()):
		temlist.append(str(for_emo[i]))
	
	entire_emo.append(" ".join(temlist))

	print " ".join(tw)

f.close()


