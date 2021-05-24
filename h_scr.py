import os

topic = 'Art'
l = ['Florals','Cherry_Blossoms','Giraffe','Ocean','Lemons','Landscape_1','Watercolor_1','Daisey','Acrylic_Woman','Watercolour_Landscape','Watercolour_Landscape_Blue','Daisy_2','Acrylic_Trees','Ocean_1','Acrylic_Landscape_1','Abstract_1','Watercolour_Landscape_1','Watercolour_Landscape_2','Acrylic_Landscape_2']
if not os.path.isdir('./project/main/templates/main/'+topic):
	os.mkdir('./project/main/templates/main/'+topic)

for i in range(1,len(l)+1):
	with open('./project/main/templates/main/'+topic+'/'+topic.lower()+str(i)+'.html','w') as o:
		o.write('\n{% load static %}\n<body>\n<center>\n<img src=\"{% static \''+topic+'/'+str(i)+'.jpg\' %}\" scale=\"0\" width=\"50%\" height=\"60%\">\n</center>\n</body>')
