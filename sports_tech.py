import os

topic = 'Sports'
l = ['Sports_1','Sports_2','Sports_3','Sports_4','Sports_5','Sports_6','Sports_7','Sports_8','Sports_9','Sports_10','Sports_11','Sports_12','Sports_13','Sports_14','Sports_15','Sports_16','Sports_17','Sports_18','Sports_19']
if not os.path.isdir('./project/main/templates/main/'+topic):
	os.mkdir('./project/main/templates/main/'+topic)

for i in range(1,len(l)+1):
	with open('./project/main/templates/main/'+topic+'/'+topic.lower()+str(i)+'.html','w') as o:
		o.write('\n{% load static %}\n<body>\n<center>\n<img src=\"{% static \''+topic+'/'+str(i)+'.jpg\' %}\" scale=\"0\" width=\"50%\" height=\"60%\">\n</center>\n</body>')
