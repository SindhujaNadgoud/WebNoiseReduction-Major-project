import os

topic = 'Technology'
l = ['Technology_1','Technology_2','Technology_3','Technology_4','Technology_5','Technology_6','Technology_7','Technology_8','Technology_9','Technology_10','Technology_11','Technology_12','Technology_13','Technology_14','Technology_15','Technology_16','Technology_17','Technology_18','Technology_19']
if not os.path.isdir('./project/main/templates/main/'+topic):
	os.mkdir('./project/main/templates/main/'+topic)

for i in range(1,len(l)+1):
	with open('./project/main/templates/main/'+topic+'/'+topic.lower()+str(i)+'.html','w') as o:
		o.write('\n{% load static %}\n<body>\n<center>\n<img src=\"{% static \''+topic+'/'+str(i)+'.jpg\' %}\" scale=\"0\" width=\"50%\" height=\"60%\">\n</center>\n<h3> Number of views per page: {{views_no}}</h3>\n</body>')
