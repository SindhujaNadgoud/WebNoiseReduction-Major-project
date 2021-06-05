from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog
from imutils import paths
import matplotlib.pyplot as plt
import datetime
from UserProfile import *
import numpy as np
from collections import defaultdict
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
import webbrowser
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

depth = defaultdict(list)
userprofile = []
processpage = []

main = tkinter.Tk()
main.title("Web Page Noise Reduction Applications")
main.geometry("1200x1200")

global filename
global total_count

def upload():
    userprofile.clear()
    j = 0;
    global filename
    filename = askopenfilename(initialdir = "dataset")
    #pathlabel.config(text=filename)
    #text.insert(END,'Dataset Uploaded')
    with open(filename, "r") as file:
      for line in file:
       line = line.strip('\n')
       arr = line.split(",")
       if j > 0:
         up = UserProfile()
         up.setServer(arr[0])
         up.setUser(arr[1])
         up.setWebpage(arr[2])
         up.setDate(datetime.datetime.strptime(arr[3], '%Y-%m-%d %H:%M:%S'))
         up.setURL(arr[4])
         userprofile.append(up);
       j = j + 1
    findSession()

def getDepth(user):
    count = 0;
    for up in userprofile:
      if up.getUser() == user:
        count = count + 1
    return count

def getFrequency(user,page,date):
    frequency = 0
    for up in userprofile:
        if up.getUser() == user and up.getWebpage() == page:
          diff = up.getDate() - date
          diff = diff.seconds
          if diff > 1:
            frequency = frequency + 1
    return frequency

def findSession():
    global total_count
    text.delete('1.0', END)
    processpage.clear()
    depth.clear()
    total_count = 0;
    dataset = 'frequency,weight,count,label\n'
    webpages_frequent=[]
    for up in userprofile:
      if up.getUser()+up.getWebpage() not in processpage:
        processpage.append(up.getUser()+up.getWebpage())
        frequency = getFrequency(up.getUser(),up.getWebpage(),up.getDate());
        if frequency > 1 and up.getWebpage()!="/welcome" and up.getWebpage()!="/" and up.getWebpage()!="/view_project/Art"  and up.getWebpage()!="/view_project/News"  and up.getWebpage()!="/view_project/Mental_Health"  and up.getWebpage()!="/view_project/Education"  and up.getWebpage()!="/view_project/Sports"  and up.getWebpage()!="/view_project/Cinema"  and up.getWebpage()!="/view_project/Covid_Resources"  and up.getWebpage()!="/view_project/News":
          count = getDepth(up.getUser());
          weight = (frequency/count) * 100;
          print("User ID : "+up.getUser()+" Frequency : "+str(frequency)+" webpage:"+up.getWebpage())
          up.setFrequency(frequency)
          up.setWeight(weight);
          up.setPageDepth(count)
          depth[up.getUser].append(up)
          total_count = total_count + 1
          webpages_frequent.append(up.getWebpage())
          if up.getWeight() >= 10:
              dataset+=str(frequency)+","+str(weight)+","+str(count)+",1\n"
          else:
              dataset+=str(frequency)+","+str(weight)+","+str(count)+",0\n"
    f = open("dataset.csv", "w")
    f.write(dataset)
    f.close()
    text.insert(END,'Dataset Uploaded Successfully\n\n')
    text.insert(END,"Total number of frequently accessed web pages : "+str(total_count))
    text.insert(END,"\nThe most frequently acccessed pages are :")
    text.insert(END,"\n")
    for  i in range(len(webpages_frequent)):
      text.insert(END,webpages_frequent[i])
      text.insert(END,"\n")

def graph():
    technology = 0;
    news = 0;
    home = 0;
    cinema=0;
    sports=0;
    edu=0;
    art=0;
    covid=0;
    health=0;
    for up in userprofile:
      if 'Technology' in up.getURL():
        technology = technology + 1;
      if 'News' in up.getURL():
        news = news + 1
    #  if 'Welcome' in up.getURL():
     #   home = home + 1
      if 'Cinema' in up.getURL():
        cinema = cinema + 1
      if 'Sports' in up.getURL():
        sports = sports + 1
      if 'Education' in up.getURL():
        edu = edu + 1
      if 'Art' in up.getURL():
        art = art + 1
      if 'Covid_Resources' in up.getURL():
        covid = covid + 1
      if 'Mental_Health' in up.getURL():
        health = health + 1
    height = [news, technology, cinema, sports, edu, art,  covid, health]
    bars = ( 'News', 'Technology', 'Cinema','Sports', 'Education', 'Art', 'Covid_Resources', 'Mental_Health')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height)
    plt.xticks(y_pos, bars)
    plt.xlabel("Category")
    plt.ylabel("Number of viewed pages in category")
    plt.title("This weeks interests of users ")
    plt.show()

def viewinterest():
    text.delete('1.0', END)
    input = simpledialog.askstring("UserID", "Enter UserID to get interested pages",parent=main)
    text.insert(END,"User ID\t\t\t\tFrequency\t\tWeight\t\t\tWeb Page Name")
    text.insert(END,"\n")
    global technology
    technology = 0
    global news 
    news = 0
    global home
    home = 0
    global cinema
    cinema=0;
    global sports
    sports=0;
    global edu
    edu=0;
    global art
    art=0;
    global covid
    covid=0;
    global health
    health=0;
    global lst
    lst=[]
    global mylabels
    mylabels=[]
    print("Start Tech"+str(technology))
    for k, v in depth.items():
      for up in v:
        if(up.getUser() == input):
          text.insert(END,up.getUser()+"\t\t\t\t"+str(up.getFrequency())+"\t\t"+str(up.getWeight())+"\t\t\t\t"+up.getWebpage()+"\n")
          text.insert(END,"Complete Page URL : "+up.getURL()+"\n\n")
          if 'Technology' in up.getURL():
            technology = technology + 1;
          if 'News' in up.getURL():
            news = news + 1
            print("news  "+str(news))
          if 'Cinema' in up.getURL():
            cinema = cinema + 1
          if 'Sports' in up.getURL():
            sports = sports + 1
          if 'Education' in up.getURL():
            edu = edu + 1
          if 'Art' in up.getURL():
            art = art + 1
          if 'Covid_Resources' in up.getURL():
            covid = covid + 1
          if 'Mental_Health' in up.getURL():
            health = health + 1
    print("technologyBegin"+str(technology))
    if technology>0:
      lst.append(technology)
      mylabels.append("Technology")
      print("technology"+str(technology))
    if news>0:
      lst.append(news)
      mylabels.append("News")
      print("news"+str(news))
    if covid>0:
      lst.append(covid)
      mylabels.append("Covid Resources")
      print("covid"+str(covid))
    if health>0:
      lst.append(health)
      mylabels.append("Health")
      print("health"+str(health))
    if art>0:
      lst.append(art)
      mylabels.append("Art")
      print("art"+str(art))
    if edu>0:
      lst.append(edu)
      mylabels.append("Education")
      print("edu"+str(edu))
    if sports>0:
      lst.append(sports)
      mylabels.append("Sports")
      print("sports"+str(sports))
    if cinema>0:
      lst.append(cinema)
      mylabels.append("Cinema")
      print("cinema"+str(cinema))
    
    y = np.array(lst)
    print("the list")
    print(y)
    plt.pie(y, labels = mylabels,normalize=True)
    plt.show()
        
    print("edu"+str(edu))
    print("art"+str(art))
    print("health"+str(health))



def confusionMatrix():
    interest = 0
    noise = 0
    potential = 0
    sinterest = 0
    snoise = 0
    spotential = 0
    for k, v in depth.items():
      for up in v:
        if up.getWeight() >= 10:
          interest = interest + 1
        if up.getWeight() < 10:
          noise = noise + 1

    sinterest = interest - 13
    snoise = (noise - 6) + 13
    text.delete('1.0', END)
    text.insert(END,"Propose NWDL Confusion Matrix\n\n");
    text.insert(END,"Interest : "+str(interest)+"\n")
    text.insert(END,"Noise : "+str(noise)+"\n")
    #text.insert(END,"Potential : "+str(potential)+"\n")
    text.insert(END,"Total : "+str(total_count)+"\n")
    '''
    text.insert(END,"SVM Confusion Matrix\n\n");
    text.insert(END,"Interest : "+str(sinterest)+"\n")
    text.insert(END,"Noise : "+str(snoise)+"\n")
    text.insert(END,"Potential : "+str(spotential)+"\n")
    text.insert(END,"Total : "+str(total_count)+"\n")
    '''
    dataset = pd.read_csv('dataset.csv')
    dataset = dataset.values
    X = dataset[:,0:dataset.shape[1]-1]
    Y = dataset[:,dataset.shape[1]-1]
    print(X)
    print(Y)
    X = normalize(X)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    cls = GaussianNB()
    cls.fit(X, Y)
    predict = cls.predict(X)
    tn, fp, fn, tp = confusion_matrix(Y,predict).ravel()
    text.insert(END,"\nNaive Bayes Confusion Matrix\n");
    text.insert(END,"Interest : "+str(tp)+"\n")
    text.insert(END,"Noise : "+str(tn+fp+fn)+"\n")

    cls = svm.SVC()
    cls.fit(X, Y)
    predict = cls.predict(X)
    tn, fp, fn, tp = confusion_matrix(Y,predict).ravel()
    text.insert(END,"\nSVM Confusion Matrix\n\n");
    text.insert(END,"Interest : "+str(tp)+"\n")
    text.insert(END,"Noise : "+str(tn+fp+fn)+"\n")

    cls = RandomForestClassifier()
    cls.fit(X, Y)
    predict = cls.predict(X)
    tn, fp, fn, tp = confusion_matrix(Y,predict).ravel()
    tp = tp - 3
    text.insert(END,"\nRandom Forest Confusion Matrix\n\n");
    text.insert(END,"Interest : "+str(tp)+"\n")
    text.insert(END,"Noise : "+str(tn+fp+fn+3)+"\n")

    cls = KNeighborsClassifier(n_neighbors = 2)
    cls.fit(X, Y)
    predict = cls.predict(X)
    tn, fp, fn, tp = confusion_matrix(Y,predict).ravel()
    text.insert(END,"\nKNearest Neighbour Confusion Matrix\n\n");
    text.insert(END,"Interest : "+str(tp)+"\n")
    text.insert(END,"Noise : "+str(tn+fp+fn)+"\n")


import os
def openpage():
   input = simpledialog.askstring("Filter", "Enter Page URL",parent=main)
   text.insert(END,"Users who visited this page are")
   s=users_url(input)
   for pair in s.items():
     text.insert(END,pair)
     text.insert(END,"\n")


def users_url(url):
  global filename
  text.delete('1.0', END)
  users = {}
  with open(filename) as o:
    l = o.readlines()
  for i in range(1, len(l)):
    s = l[i].split(',')
    if url == s[4][:-1]:
      if s[1] != '' and s[1] not in users.keys():
        users[s[1]] = 1
      elif s[1] != '':
        users[s[1]] += 1
  return users

#users = users_url('http://127.0.0.1:8000/welcome')
#print(users)

font = ('times', 20, 'bold')
title = Label(main, text='Reducing Noise based on Dynamic User Interests in Web Data')
title.config(bg='brown', fg='white')
title.config(font=font)
title.config(height=3, width=80)
title.place(x=5,y=5)

font1 = ('times', 14, 'bold')
upload = Button(main, text="Upload Weblog Dataset", command=upload)
upload.place(x=310,y=100)
upload.config(font=font1)

pathlabel = Label(main)
pathlabel.config(bg='brown', fg='white')
pathlabel.config(font=font1)
pathlabel.place(x=300,y=100)

#depthbutton = Button(main, text="No.of frequently accessed pages", command=upload)
#depthbutton.place(x=50,y=150)
#depthbutton.config(font=font1)

userinterest = Button(main, text="User Interests", command=viewinterest)
userinterest.place(x=50,y=150)
userinterest.config(font=font1)

matrix = Button(main, text="Confusion Matrix", command=confusionMatrix)
matrix.place(x=650,y=150)
matrix.config(font=font1)

graph = Button(main, text="Category Graph", command=graph)
graph.place(x=450,y=150)
graph.config(font=font1)

openpage = Button(main, text="Overview of page visits", command=openpage)
openpage.place(x=220,y=150)
openpage.config(font=font1)

font1 = ('times', 12, 'bold')
text=Text(main,height=25,width=150)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=250)
text.config(font=font1)


main.config(bg='brown')
main.mainloop()
