import Tkinter
from Tkinter import *
import tkMessageBox
import PIL
from PIL import Image
import tkFont
a=Tkinter.Tk()
a.title("CAR COMPARE")
tkMessageBox.showinfo("Welcome","Welcome to AUTOMOTO \n Compare cars \nEnjoy ;-)")
"""========================================================================================="""
img_cmp1=PhotoImage(file="cmp1.gif")#main page image 1
img_close=PhotoImage(file="close.gif")#close
img_search=PhotoImage(file="search.gif")
def abdev():#about developer Function
  c=Tkinter.Tk()
  c.title("About Software")#title about developer
  Tkinter.Button(c,command=c.destroy,text="X",background="red").pack(anchor="ne")
  text=Text(c)
  text.insert(INSERT,"\t \t \t Made By Arpit & Vishrant\n")
  text.insert(INSERT,"\t \t \t INSPIRED BY : CARDEKHO.COM \n")
  text.insert(INSERT,"\t \t \t VERSION:1.0 \n \n \n")
  text.insert(INSERT,"This program compares cars of some well known brands like \n")
  text.insert(INSERT,"\t \t MERCEDES;  AUDI;  LAMBOGHINI;  BMW;  PORSCHE; ROLLS ROYCE \n")
  text.insert(INSERT,"On the basis of :\n \t \t ENGINE; PRICE; TOP SPEED; MILEAGE \n ")
  text.insert(INSERT," \n")
  text.insert(INSERT,"With some UPCOMING CARS: \n  \n")
  text.insert(INSERT,"\tBENTLEY BENTAYGA \n\tJAGUAR F-PACE \n\tROLLS ROYCE DAWN \n\tFERRARI 488")
  text.insert(INSERT,"\tPORSCHE MISSION E \n\t LAMBORGHINI URUS \n\tMERCEDES IAA \n \n")
  text.insert(INSERT,"Any queries feel free to contact us at:\t carhdwallpaper.weebly.com/contact \n")
  text.insert(INSERT,"\t \t \t \t \t abc@gmail.com \n")
  text.pack()
  text.config(background="gold")
  c.config(background="black")
  c.mainloop()
#-------------------------------------------------------------------------------------------
def Upcoming(): # DROP DOWN MENU
  c=Tkinter.Tk()
  c.title("UPCOMING")
  Tkinter.Button(c,command=c.destroy,text="X",background="red").pack(anchor="ne")
  def upcoming_car():
    valcar=upcoming_cars.get()#taking value of upcoming cars
    if(valcar=="DAWN"):
      im=Image.open("dawn.jpg")
      im.show()
    if(valcar=="488 GTB"):
      im=Image.open("488.jpg")
      im.show() 
    if(valcar=="BENTAYGA"):
      im=Image.open("bentayga.jpg")
      im.show()
    if(valcar=="URUS"):
      im=Image.open("urus.jpg")
      im.show()
    if(valcar=="MISSION E"):
      im=Image.open("mission-e.jpg")
      im.show()
    if(valcar=="MERCEDES IAA"):
      im=Image.open("iaa.jpg")
      im.show()
    if(valcar=="F PACE"):
      im=Image.open("fpace.jpg")
      im.show()
  #------------------------------------------------------------------------------------------
  upcoming_cars=Tkinter.StringVar(c)
  upcoming_cars.set("UPCOMING CARS")
  choices=["DAWN","488 GTB","BENTAYGA","URUS","MISSION E","MERCEDES IAA","F PACE"]
  option=Tkinter.OptionMenu(c,upcoming_cars,*choices).pack(anchor="w")  Tkinter.Button(c,command=upcoming_car,text="Select",background="gold").pack(anchor="center")   c.config(background="black")
  c.mainloop()
def Facts():              #Facts
  c=Tkinter.Tk()
  c.title("Facts About Cars")
  Tkinter.Button(c,command=c.destroy,text="X",background="red").pack(anchor="ne")
  text=Text(c)
  text.insert(INSERT,"A}The Spirit Of Ecstasy On The Rolls Royce Is Worth $40 Million \n \n")
  text.insert(INSERT,"B} Rolls Royce Logo On Its Wheel Always Remains Upright \n \n")
  text.insert(INSERT,"C}Lamborghinis Murcielago Is The Real Batmobile \n \n")
  text.insert(INSERT,"D}Daniel Craig Has A Lifelong Access to Aston Martin Cars \n \n")
  text.insert(INSERT,"E}Lamborghini Initially Manufactured Tractors \n \n")
  text.insert(INSERT,"F}The Symbol Of Toyota Is Not Merely A T \n \n")
  text.insert(INSERT,"G}Aston Martin Has Been Owned By 11 Different Owners \n \n")
  text.insert(INSERT,"H}Volkswagen Isnt Called The Peoples Car For No Reason! \n \n")
  text.insert(INSERT,"I}The Name Of Lamborghini Countach Is Inspired From A Cuss Word \n \n")
  text.insert(INSERT,"J}The Mercedes Silver Arrow Was Initially Grey \n \n")
  text.pack()
  text.config(background="gold")
  c.config(background="black")
#-------------------------------------------------------------    #menubar
b=Menu(a)
Aboutmenu=Menu(b)
Aboutmenu.add_command(label="About Software",command=abdev)
b.add_cascade(label="About", menu=Aboutmenu)    
Upcomingmenu=Menu(b)                              #upcoming menu
Upcomingmenu.add_command(label="Upcoming",command=Upcoming)
b.add_cascade(label="Upcoming",menu=Upcomingmenu)    
Factsmenu=Menu(b)                                 #facts menu
Factsmenu.add_command(label="Facts About Cars",command=Facts)
b.add_cascade(label="Facts About Cars",menu=Factsmenu)
def Select_Brand():
  val_ddmenu=var.get()        #taking values of drop down menu
  if(val_ddmenu=="AUDI" or val_ddmenu=="MERCEDES" or val_ddmenu=="BMW" or 
     val_ddmenu=="LAMBORGHINI" or  val_ddmenu=="PORSCHE" or val_ddmenu=="ROLLS ROYCE"):
      tkMessageBox.showinfo("Error","Select a model not brand") 
  else :
    if(val_ddmenu=="   R8 SPYDER"):#r8spyder
      im=Image.open("r8spy.jpg")
      im.show()                                 #showing image
    if(val_ddmenu=="   RS7"):
      im=Image.open("rs7.jpg")
      im.show()                                     #showing imageRS7
    if(val_ddmenu=="   TT"):
      im=Image.open("tt.jpg")
      im.show()                                       #Showing image TT
#bmw
    if(val_ddmenu=="   BMW i8"):
        im=Image.open("i8.jpg")
        im.show()                                   #showing image hybrid
    if(val_ddmenu=="   M4"): 
        im=Image.open("m4.jpg")
        im.show()                                   #showing image M4
    if(val_ddmenu=="   7SERIES"):
        im=Image.open("7series.jpg")
        im.show()                                   #showing image 7series
    """----------------------------------------------porsche------------------------"""
    if(val_ddmenu=="   PORSCHE 918"):
      im=Image.open("918.jpg")
      im.show()                                   #showing image 918
    if(val_ddmenu=="   CAYMAN"):
      im=Image.open("cayman.jpg")
      im.show()                                   #showing image cayman
    if(val_ddmenu=="   911"):
      im=Image.open("911.jpg")
      im.show()                                   #showing image 911
    """---------------------------------------------mercedes---------------------"""
    if(val_ddmenu=="   G63"):
      im=Image.open("g63.jpg")
      im.show()                                   #showing image G63
   if(val_ddmenu=="   AMG GT"):
      im=Image.open("amggt.jpg")
      im.show()                                   #showing image AMG GT
    if(val_ddmenu=="   GL-63"):
      im=Image.open("gl63.jpg")
      im.show()
    """--------------------------------------------lamborghini-------------------"""
    if(val_ddmenu=="   HURACAN"):
      im=Image.open("huracan.jpg")
      im.show()
      #--------------------------------------------
    if(val_ddmenu=="   AVENTDOR"):
      im=Image.open("aventdor.jpg")
      im.show()
      #----------------------------------------------
    if(val_ddmenu=="   GALLARDO"):
      im=Image.open("gallardo.jpg")
      im.show()
    """-----------------------------------------rolls-royce--------------------"""
    if(val_ddmenu=="   GHOST"):
      im=Image.open("ghost.jpg")
      im.show()
      #---------------------------------------------
    if(val_ddmenu=="   WRAITH"):
      im=Image.open("wraith.jpg")
      im.show()
      #-------------------------------------------
    if(val_ddmenu=="   PHANTOM"):
      im=Image.open("phantom.jpg")
      im.show()
    b.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------------------------
var=Tkinter.StringVar(a)
var.set("S E L E C T   B R A N D ")
choices=["AUDI","   R8 SPYDER","   RS7","   TT","\n",
         "BMW","   BMW i8","   M4","   7SERIES","\n",
         "LAMBORGHINI","   HURACAN","   GALLARDO","   AVENTDOR","\n",
         "PORSCHE","   PORSCHE 918","   CAYMAN","   911","\n",
         "MERCEDES","   G63","   AMG GT","   GL-63","\n",
         "ROLLS ROYCE","   PHANTOM","   GHOST","   WRAITH"]
Tkinter.Button(a,command=a.destroy,image=img_close,background="black").pack(anchor="ne")
option=Tkinter.OptionMenu(a,var,*choices).pack(anchor="nw")
Tkinter.Button(a,command=Select_Brand,image=img_search).pack(anchor="n")
label=Label(image=img_cmp1,width=1360,height=600).pack()
a.config(background="black")
a.config(menu=b)
a.mainloop()
