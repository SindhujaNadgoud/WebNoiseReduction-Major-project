
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages #import messages
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.forms import AuthenticationForm #add this
from django.shortcuts import redirect
from django.urls import reverse


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("main:homepage")
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
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:welcome")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form":form})


# Create your views here.
def homepage(request):
    return render(request=request, template_name='main/home.html')

def welcome(request):
    if request.method == 'POST':
    #   form = WelcomeForm(request.POST)
        choice = request.POST.get('topic_id')
        print(choice)
        #return render(request=request, template_name='main/view_project/'+str(choice)+'.html')
        return redirect('/view_project/'+choice)
    return render(request=request, template_name='main/welcome.html')   

def view_project(request, topic_id, link_id = 'Default'):
    '''if request.method == 'POST':
        topic_id = request.POST.get('topic_id');print(topic_id);return redirect(reverse('view_project', args=(topic_id)))'''
    if request.method == 'GET':
        if link_id == 'Default':
            d = {'News':1, 'Covid_Resources':2, 'Cinema':3, 'Sports':4, 'Education':5, 'Mental_Health':6, 'Art':7, 'Technology':8}
            return render(request=request, template_name='main/view_project/'+str(d[topic_id])+'.html')
        else:
            if topic_id == 'Cinema':
                l = ['Aishwarya_Rai' ,'Madhuri_Dixit', 'Alia_Bhatt', 'Rani_Mukerjee', 'Deepika_Ranveer', 'Jahnvi', 'Virat_Anushka', 'Sara', 'Ananya', 'Tara', 'Pooja', 'Deepika_Saree', 'Saif', 'Alia_Bhatt_1', 'Director', 'Tabu', 'Deepika_Ranveer_1', 'Deepika', 'Sonam', 'Disha']
                return render(request=request, template_name='main/'+topic_id+'/'+topic_id.lower()+str(l.index(link_id)+1)+'.html')

            if topic_id == 'Sports':
                l = ['Sports_1','Sports_2','Sports_3','Sports_4','Sports_5','Sports_6','Sports_7','Sports_8','Sports_9','Sports_10','Sports_11','Sports_12','Sports_13','Sports_14','Sports_15','Sports_16','Sports_17','Sports_18','Sports_19']
                return render(request=request, template_name='main/'+topic_id+'/'+topic_id.lower()+str(l.index(link_id)+1)+'.html')

            if topic_id == 'News':
                l = ['News_1','News_2','News_3','News_4','News_5','News_6','News_7','News_8','News_9','News_10','News_11','News_12','News_13','News_14','News_15','News_16','News_17','News_18','News_19']
                return render(request=request, template_name='main/'+topic_id+'/'+topic_id.lower()+str(l.index(link_id)+1)+'.html')

            if topic_id == 'Covid_Resources':
                l = ['CovidResources','Covid_Resources','Safety_Measures','CommunityResources','Sanitation','CovidVaccine','Covid_Vaccine','StayHome','SafetyInstructions','Safety_Instructions','TollNumber','WhatsappHelp','VerifiedHelpline','BedAvailability','HelpLine','Treatment','DoctorProtection','TeleConsultation','ImmunityBooster','Immunity_Booster']
                return render(request=request, template_name='main/'+topic_id+'/'+topic_id.lower()+str(l.index(link_id)+1)+'.html')

            if topic_id == 'Education':
                l = ['Education_1','Education_2','Education_3','Education_4','Education_5','Education_6','Education_7','Education_8','Education_9','Education_10','Education_11','Education_12','Education_13','Education_14','Education_15','Education_16','Education_17','Education_18','Education_19']
                return render(request=request, template_name='main/'+topic_id+'/'+topic_id.lower()+str(l.index(link_id)+1)+'.html')

            if topic_id == 'Mental_Health':
                l = ['MenthaHealth','MenthaHealthDay','Talk','WorldMenthaHealth','BeKind','Myths','MenthaHealthMyths','MalasyisStats','ChildMenthaHealth','Child_MenthaHealth','Happiness','Bullying','BeingDifferent','CyberBullying','Help','Psychology','Causes','Elderly','ContactHelp','CovidImpact']
                return render(request=request, template_name='main/'+topic_id+'/'+topic_id.lower()+str(l.index(link_id)+1)+'.html')

            if topic_id == 'Art':
                l = ['Florals','Cherry_Blossoms','Giraffe','Ocean','Lemons','Landscape_1','Watercolor_1','Daisey','Acrylic_Woman','Watercolour_Landscape','Watercolour_Landscape_Blue','Daisy_2','Acrylic_Trees','Ocean_1','Acrylic_Landscape_1','Abstract_1','Watercolour_Landscape_1','Watercolour_Landscape_2','Acrylic_Landscape_2']
                return render(request=request, template_name='main/'+topic_id+'/'+topic_id.lower()+str(l.index(link_id)+1)+'.html')

            if topic_id == 'Technology':
                l = ['Technology_1','Technology_2','Technology_3','Technology_4','Technology_5','Technology_6','Technology_7','Technology_8','Technology_9','Technology_10','Technology_11','Technology_12','Technology_13','Technology_14','Technology_15','Technology_16','Technology_17','Technology_18','Technology_19']
                return render(request=request, template_name='main/'+topic_id+'/'+topic_id.lower()+str(l.index(link_id)+1)+'.html')
                
    return render(request=request, template_name='main/welcome.html')   


