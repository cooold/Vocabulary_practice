from functools import partial
from PIL import ImageTk, Image
import pygame,random,webbrowser,tkinter as tk

#初值
rand2=0
sign=7
url=""
timebool=False
hidebool=False
pygame.init()
pygame.mixer.init()

window = tk.Tk()
window.title('單字練習程式')
window.geometry('750x600')

with open('vocabularyDir/lev1.txt', 'r' ,encoding="utf-8") as file:
  save1 =file.readlines()
  len1=len(save1)

with open('vocabularyDir/lev2.txt', 'r' ,encoding="utf-8") as file:
  save2 =file.readlines()
  len2=len(save2)

with open('vocabularyDir/lev3.txt', 'r' ,encoding="utf-8") as file:
  save3 =file.readlines()
  len3=len(save3)

with open('vocabularyDir/lev4.txt', 'r' ,encoding="utf-8") as file:
  save4 =file.readlines()
  len4=len(save4)

with open('vocabularyDir/lev5.txt', 'r' ,encoding="utf-8") as file:
  save5 =file.readlines()
  len5=len(save5)

with open('vocabularyDir/lev6.txt', 'r' ,encoding="utf-8") as file:
  save6 =file.readlines()
  len6=len(save6)

len7=len(save1+save2+save3+save4+save5+save6)

#label
#單字
lbl_1 = tk.Label(window, width=20,text="", font=('Microsoft JhengHei', 28))
lbl_1.place(x=140, y=100)

lbl_2 = tk.Label(window,width=20, text="", font=('Microsoft JhengHei', 23))
lbl_2.place(x=170, y=200)

lbl_3 = tk.Label(window,width=40, text="", font=('Microsoft JhengHei', 23))
lbl_3.place(x=-20, y=290)

#顯示等級
lbl_11 = tk.Label(window,width=30, text="現在level"+str(sign), font=('Microsoft JhengHei', 15))
lbl_11.place(x=-115, y=80)
lbl_12 = tk.Label(window,width=20, text="", fg='#263238', font=('Microsoft JhengHei', 15))
lbl_12.place(x=-60, y=130)

#開網站
def web():
  webbrowser.get('windows-default').open_new(url)

#button 
button3 = tk.Button(window, text="到網址看看", height=3 ,width=10,font=('Microsoft JhengHei', 10),command=web)
button3.place(x=550, y=470)

# set lv
def setlv(number):
  global sign
  sign=number
  showlev()
  showcount(sign)

def showcount(num):
  global len1,len2,len3,len4,len5,len6,len7,lbl_12
  if(num==1):
    lbl_12['text']=len1
  if(num==2):
    lbl_12['text']=len2
  if(num==3):
    lbl_12['text']=len3
  if(num==4):
    lbl_12['text']=len4
  if(num==5):
    lbl_12['text']=len5
  if(num==6):
    lbl_12['text']=len6
  if(num==7):
    lbl_12['text']=len7


#顯示狀態
def showlev():
  global sign,lbl_11
  if(sign!=7):
    lbl_11['text']="現在level"+str(sign)
  if(sign==7):
    lbl_11['text']="現在level"+str(sign)+"--"+str(rand2)

#播放聲音
def playsounds():
  pygame.mixer.music.play()


#下一題
def change():
  
  global lbl_1,lbl_2,lbl_3,now,intro,rand,rand2

  if sign==1:
    rand=random.randint(0,len1-1)
    now=save1[rand].split()
  if sign==2:
    rand=random.randint(0,len2-1)
    now=save2[rand].split()
  if sign==3:
    rand=random.randint(0,len3-1)
    now=save3[rand].split()
  if sign==4:
    rand=random.randint(0,len4-1)
    now=save4[rand].split()  
  if sign==5:
    rand=random.randint(0,len5-1)
    now=save5[rand].split()  
  if sign==6:
    rand=random.randint(0,len6-1)
    now=save6[rand].split()  
  if sign==7:
    rand2=random.randint(1,6)
    if(rand2==1):
      rand=random.randint(0,len1-1)
      now=save1[rand].split()
    if(rand2==2):
      rand=random.randint(0,len2-1)
      now=save2[rand].split()
    if(rand2==3):
      rand=random.randint(0,len3-1)
      now=save3[rand].split()
    if(rand2==4):
      rand=random.randint(0,len4-1)
      now=save4[rand].split()
    if(rand2==5):
      rand=random.randint(0,len5-1)
      now=save5[rand].split()
    if(rand2==6):
      rand=random.randint(0,len6-1)
      now=save6[rand].split()
    
  if(sign!=7):
    with open('vocabularyDir/lev'+str(sign)+'/'+now[0]+'.txt', 'r' ,encoding="utf-8") as file:
      intro=file.readlines()
    
    pygame.mixer.music.load('vocabularyDir/lev'+str(sign)+'/'+now[0]+'.mp3')
    pygame.mixer.music.play()
  if(sign==7):
    with open('vocabularyDir/lev'+str(rand2)+'/'+now[0]+'.txt', 'r' ,encoding="utf-8") as file:
      intro=file.readlines()
    
    pygame.mixer.music.load('vocabularyDir/lev'+str(rand2)+'/'+now[0]+'.mp3')
    pygame.mixer.music.play()


  
  lbl_1['text']=now[0]
  lbl_2['text']=now[1]
  lbl_3['text']=intro

  #隱藏中文
  if(hidebool):
    lbl_3['fg']='#F0F0F0'
  #顯示級別
  showlev()

  #網址
  global url
  url='https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/'+now[0]
  
  if(timebool):
    window.after(5000, change)
  

  

#lv1~7 button
buttons1 = tk.Button(window,text="Level 1",height=3 ,width=10,font=('Microsoft JhengHei', 10),command=partial(setlv, 1))
buttons1.place(x=0, y=0)
buttons2 = tk.Button(window, text="Level 2", height=3 ,width=10,font=('Microsoft JhengHei', 10),command=partial(setlv, 2))
buttons2.place(x=100, y=0)
buttons3 = tk.Button(window, text="Level 3", height=3 ,width=10,font=('Microsoft JhengHei', 10),command=partial(setlv, 3))
buttons3.place(x=200, y=0)
buttons4 = tk.Button(window, text="Level 4", height=3 ,width=10,font=('Microsoft JhengHei', 10),command=partial(setlv, 4))
buttons4.place(x=300, y=0)
buttons5 = tk.Button(window, text="Level 5", height=3 ,width=10,font=('Microsoft JhengHei', 10),command=partial(setlv, 5))
buttons5.place(x=400, y=0)
buttons6 = tk.Button(window, text="Level 6", height=3 ,width=10,font=('Microsoft JhengHei', 10),command=partial(setlv, 6))
buttons6.place(x=500, y=0)
buttons7 = tk.Button(window, text="Level ALL", height=3 ,width=10,font=('Microsoft JhengHei', 10),command=partial(setlv, 7))
buttons7.place(x=600, y=0)

#hide開關
def hideinfo():
  global hidebool
  if(hidebool):
    hidebool=False
    button098['text']="Hide(關)"
    lbl_3['fg']='black'
    
  elif(hidebool==False):
    hidebool=True
    button098['text']="Hide(開)"
    lbl_3['fg']='#F0F0F0'



#next button
button199 = tk.Button(window, text="Click", height=3 ,width=10,font=('Microsoft JhengHei', 10),command=change)
button199.place(x=315, y=470)
#Hide button
button098 = tk.Button(window, text="Hide", height=3 ,width=10,font=('Microsoft JhengHei', 10),command=hideinfo)
button098.place(x=315, y=380)

#自動執行
def stillDo():
  global timebool
  if(timebool):
    timebool=False
    button0['text']="自動執行(關)"
    
  elif(timebool==False):
    timebool=True
    button0['text']="自動執行(開)"
    change()
  



#自動執行
#next button
button0 = tk.Button(window, text="自動執行", height=3 ,width=10,font=('Microsoft JhengHei', 10),command=stillDo)
button0.place(x=100, y=470)
#sound button
img= ImageTk.PhotoImage(file='speaker.jpg')
button2 = tk.Button(window, image=img, height=25 ,width=25,font=('Microsoft JhengHei', 10),command=playsounds)
button2.place(x=700, y=90)




window.mainloop()
