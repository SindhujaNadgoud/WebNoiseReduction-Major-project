import os

topic = 'News'
l = ['News_1','News_2','News_3','News_4','News_5','News_6','News_7','News_8','News_9','News_10','News_11','News_12','News_13','News_14','News_15','News_16','News_17','News_18','News_19']
if not os.path.isdir('./project/main/templates/main/'+topic):
	os.mkdir('./project/main/templates/main/'+topic)

for i in range(1,len(l)+1):
	with open('./project/main/templates/main/'+topic+'/'+topic.lower()+str(i)+'.html','w') as o:
		o.write('\n{% load static %}\n<body>\n<center>\n<img src=\"{% static \''+topic+'/'+str(i)+'.jpg\' %}\" scale=\"0\" width=\"50%\" height=\"60%\">\n</center>\n</body>')