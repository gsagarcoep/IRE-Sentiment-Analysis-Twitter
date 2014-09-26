import sys

def fv_cluster():
	cluster_dict={}
	#load the cluster dictionary
	f=open('cluster_IDS.txt','r')
	line=f.readline()
	while(line):
		arr=line.split()
		cluster_dict[arr[0]]=arr[1]
		line=f.readline()
	f.close()

	#form the list for each input tweet
	f=open(sys.argv[1],'r')
	line=f.readline()
	while(line):
		fv_list=[]
		line=line[:-1]
		line=line.lower()
		tem=line.split()
		for item in tem:
			if item in cluster_dict:
				if cluster_dict[item] not in fv_list:
					fv_list.append(int(cluster_dict[item]))
		fv_list=sorted(set(fv_list))
		for ijk in fv_list:
			print ijk,
		print
		line=f.readline()
	f.close()


#tweet='wehn life gives your lamon, make lamonade and surprise good !!!!!!!!'
fv_cluster()
