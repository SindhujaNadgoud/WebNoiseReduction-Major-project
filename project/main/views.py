
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages #import messages
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.forms import AuthenticationForm #add this
from django.shortcuts import redirect
from django.urls import reverse
import os
import datetime
import json

def gen_log(username, access_page, datetime):
    if not os.path.isdir('./log'):
        os.mkdir('./log')
    if not os.path.isfile('./log/weblog.csv'):
        with open('./log/weblog.csv', 'w') as o:
            o.write('server_ip,User_id,Access_page,Date_Time,URL'+'\n')
    with open('./log/weblog.csv', 'a') as o:
        o.write('http://127.0.0.1:8000/'+','+username+','+access_page+','+datetime+','+'http://127.0.0.1:8000'+access_page+'\n')

def inc_views(path):
    d = {}
    if os.path.isfile('./log/views.json'):
        with open('./log/views.json') as f:
            d = json.load(f)
    if path not in d.keys():
        d[path] = 1
    else:
        d[path] += 1
    with open('./log/views.json', 'w') as json_file:
        json.dump(d, json_file)
    return d[path]

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = request.POST['username']#Added
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("main:login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                return redirect("main:welcome")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form":form})


# Create your views here.
def homepage(request):
    username = request.user.username
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    gen_log(username, '/', dt)
    return render(request=request, template_name='main/home.html')

def welcome(request):
    username = request.user.username
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    gen_log(username, '/welcome', dt)
    if request.method == 'POST':
    #   form = WelcomeForm(request.POST)
        choice = request.POST.get('topic_id')
        print(choice)
        #return render(request=request, template_name='main/view_project/'+str(choice)+'.html')
        return redirect('/view_project/'+choice)
    return render(request=request, template_name='main/welcome.html')   

def view_project(request, topic_id, link_id = 'Default'):
    if request.method == 'POST':
    #   form = WelcomeForm(request.POST)
        choice = request.POST.get('topic_id')
        print(choice)
        #return render(request=request, template_name='main/view_project/'+str(choice)+'.html')
        return redirect('/view_project/'+choice)
    '''if request.method == 'POST':
        topic_id = request.POST.get('topic_id');print(topic_id);return redirect(reverse('view_project', args=(topic_id)))'''
    username = request.user.username
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    context = {}
    if link_id == 'Default':
        gen_log(username, '/view_project/'+topic_id, dt)
    else:
        gen_log(username, '/view_project/'+topic_id+'/'+link_id, dt)
        context['views_no'] = inc_views('/view_project/'+topic_id+'/'+link_id)
    if request.method == 'GET':
        if link_id == 'Default':
            d = {'News':1, 'Covid_Resources':2, 'Cinema':3, 'Sports':4, 'Education':5, 'Mental_Health':6, 'Art':7, 'Technology':8}
            return render(request=request, template_name='main/view_project/'+str(d[topic_id])+'.html')
        else:
            if topic_id == 'Cinema':
                l = ['Aishwarya_Rai' ,'Madhuri_Dixit', 'Alia_Bhatt', 'Rani_Mukerjee', 'Deepika_Ranveer', 'Jahnvi', 'Virat_Anushka', 'Sara', 'Ananya', 'Tara', 'Pooja', 'Deepika_Saree', 'Saif', 'Alia_Bhatt_1', 'Director', 'Tabu', 'Deepika_Ranveer_1', 'Deepika', 'Sonam', 'Disha']
                return render(request=request, template_name='main/'+topic_id+'/'+topic_id.lower()+str(l.index(link_id)+1)+'.html', context = context)

            if topic_id == 'Sports':
                l = ['FootBall','Sports','Sports Importance','Rugby','Importance of Football','Running','VolleyBall','BasketBall','Sports importance in Children','Hockey','Cricket','Gaelic football','Golf','Table tennis','Badminton','Handball','Wrestling','Ball badminton','Fives','Basketball']
                return render(request=request, template_name='main/'+topic_id+'/'+topic_id.lower()+str(l.index(link_id)+1)+'.html', context = context)

            if topic_id == 'News':
                l = ['News anchor','Tronc buys the news','Krystal profit','New York times','Bhopal gas tragedy','BBC','FOX News','Child Friendly news','Birmingham','The Hindu','Census','President poll','Australia Dam','NASA','World News','Hitler death','Massacred','Weather report','Hawaii Exclusive','Cricket News']
                return render(request=request, template_name='main/'+topic_id+'/'+topic_id.lower()+str(l.index(link_id)+1)+'.html', context = context)

            if topic_id == 'Covid_Resources':
                l = ['CovidResources','Covid_Resources','Safety_Measures','CommunityResources','Sanitation','CovidVaccine','Covid_Vaccine','StayHome','SafetyInstructions','Safety_Instructions','TollNumber','WhatsappHelp','VerifiedHelpline','BedAvailability','HelpLine','Treatment','DoctorProtection','TeleConsultation','ImmunityBooster','Immunity_Booster']
                return render(request=request, template_name='main/'+topic_id+'/'+topic_id.lower()+str(l.index(link_id)+1)+'.html', context = context)

            if topic_id == 'Education':
                l = ['Education','ClassRoom','Books','Graduate','MBBS','Advantages Of Education','Robotics','Artificial Intelligence','Botany','Zoology','Mathematics','English','Physics','Chemistry','Python','Java','Library','Smart classrooms','Online courses','Online platforms']
                return render(request=request, template_name='main/'+topic_id+'/'+topic_id.lower()+str(l.index(link_id)+1)+'.html', context = context)

            if topic_id == 'Mental_Health':
                l = ['MenthaHealth','MenthaHealthDay','Talk','WorldMenthaHealth','BeKind','Myths','MenthaHealthMyths','MalasyisStats','ChildMenthaHealth','Child_MenthaHealth','Happiness','Bullying','BeingDifferent','CyberBullying','Help','Psychology','Causes','Elderly','ContactHelp','CovidImpact']
                return render(request=request, template_name='main/'+topic_id+'/'+topic_id.lower()+str(l.index(link_id)+1)+'.html', context = context)

            if topic_id == 'Art':
                l = ['Florals','Cherry_Blossoms','Giraffe','Ocean','Lemons','Landscape_1','Watercolor_1','Daisey','Acrylic_Woman','Watercolour_Landscape','Watercolour_Landscape_Blue','Daisy_2','Acrylic_Trees','Ocean_1','Acrylic_Landscape_1','Abstract_1','Acrylic_Landscape_2','Watercolour_Landscape_1','Watercolour_Landscape_2','Acrylic_Landscape_3']
                return render(request=request, template_name='main/'+topic_id+'/'+topic_id.lower()+str(l.index(link_id)+1)+'.html', context = context)

            if topic_id == 'Technology':
                l = ['Artificial intelligence','Internet of Things','Robotics','Intelligent Apps','Blockchain','5G','Machine Learning','Robotic Process Automation','Cognitive Computing','VR','Edge computing','Internet of Behaviors','DevSecOps','Tactile Virtual Reality','Big Data Analytics','Human Augmentation1','Everything-as-a-Service (XaaS)','Cybersecurity','Edge computing']
                return render(request=request, template_name='main/'+topic_id+'/'+topic_id.lower()+str(l.index(link_id)+1)+'.html', context = context)
                
    return render(request=request, template_name='main/welcome.html')   


