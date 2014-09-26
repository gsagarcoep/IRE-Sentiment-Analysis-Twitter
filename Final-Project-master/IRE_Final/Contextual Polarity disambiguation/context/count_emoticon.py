import sys
import re

####################
#	For normalizing - url , username , emoticons
#
###################
#emoticons_dict={':-)':'pos_POL', ':)':'pos_POL', ':o)':'pos_POL', ':]':'pos_POL' ,':3':'pos_POL',':c)':'pos_POL' , ':D':'Extpos_POL', 'C:':'Extpos_POL', 'D8':'ExtNEG_POL', 'D;':'ExtNEG_POL', 'D=':'ExtNEG_POL', 'DX':'ExtNEG_POL', 'v.v':'ExtNEG_POL', ':|':'Neut_POL'}



elt = ['Ext_pos_POL', 'neg_POL', 'pos_POL', 'neut_POL', 'Ext_neg_POL', 'surprise_POL', 'cheeky_POL']
f = open(sys.argv[1], "r")
entire_emo = []

for line in f:
	tem = line[:-1]
	tem = tem.split()

	tw = []

	for_emo = {'pos_POL': 0, 'Ext_pos_POL' : 0, 'neg_POL' : 0, 'Ext_neg_POL': 0, 'surprise_POL' : 0, 'cheeky_POL':0 , 'neut_POL' : 0};


	for i in tem:
		n  = i	
		if n in elt:
			for_emo[n] += 1
			
	temlist = []
	for i in sorted(for_emo.keys()):
		temlist.append(str(for_emo[i]))
	
	entire_emo.append(" ".join(temlist))

f.close()

f = open('count_emoticon_class.txt', 'w')
for i in entire_emo:
        f.write(i + "\n")
f.close()

