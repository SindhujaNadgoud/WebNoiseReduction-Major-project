import os

topic = 'Mental_Health'
# l = ['CovidResources','Covid_Resources','Safety_Measures','CommunityResources','Sanitation','CovidVaccine','Covid_Vaccine','StayHome','SafetyInstructions','Safety_Instructions','TollNumber','WhatsappHelp','VerifiedHelpline','BedAvailability','HelpLine','Treatment','DoctorProtection','TeleConsultation','ImmunityBooster','Immunity_Booster']
l = ['MenthaHealth','MenthaHealthDay','Talk','WorldMenthaHealth','BeKind','Myths','MenthaHealthMyths','MalasyisStats','ChildMenthaHealth','Child_MenthaHealth','Happiness','Bullying','BeingDifferent','CyberBullying','Help','Psychology','Causes','Elderly','ContactHelp','CovidImpact']
if not os.path.isdir('./project/main/templates/main/'+topic):
	os.mkdir('./project/main/templates/main/'+topic)

for i in range(1,len(l)+1):
	with open('./project/main/templates/main/'+topic+'/'+topic.lower()+str(i)+'.html','w') as o:
		o.write('\n{% load static %}\n<body>\n<center>\n<img src=\"{% static \''+topic+'/'+str(i)+'.jpg\' %}\" scale=\"0\" width=\"50%\" height=\"60%\">\n</center>\n</body>')
