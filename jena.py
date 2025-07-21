from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox 

sir=Tk()


def handle_login():
    email =email_input.get()
    password =password_input.get()
    print(email,password)
    if email != password:
        messagebox.showinfo("sir","login successful")
    else:
        messagebox.showwarning("sir","login failed")
    
 
#sir = Tk()
#TAKING ALL FUNCTION FROM TKINTER

sir.minsize(350,500)
sir.maxsize(350,500)

sir.config(background='#A7FF87')

#img = Image.open("D:\Downloads\WhatsApp Image 2023-03-12 at 1.34.46 AM.jpeg")
#resized_img = img.resize((150,150))
#Inserteing image

#img = ImageTk.PhotoImage(resized_img)
#img_lable = Label(sir,image=img)
#ṇimg_lable.pack(pady=(10,20))
#adjucting image

Text_lable = Label(sir,text='Rana Institute Of Technology.',fg='#FF0000',bg='#A7FF87')
Text_lable.config(font=('italic',15))
Text_lable.pack()

email_lable = Label(sir,text='Enter your id :- ',fg='black',bg='#A7FF87')
email_lable.pack(pady=(30,10),padx=(10,170))
email_lable.config(font=('bold',15))

email_input = Entry(sir,width=50,border='5')
email_input.pack()

password_lable = Label(sir,text='Enter your password :- ',fg='black',bg='#A7FF87')
password_lable.pack(pady=(30,10),padx=(10,110))
password_lable.config(font=('bold',15))

password_input = Entry(sir,width=50,border='5')
password_input.pack()

login_btn =Button(sir,text='Login Here',fg='blue',bg='white',border='4',width=10,height=1,command=handle_login)
login_btn.config(font=('bold'))
login_btn.pack(pady=(10))
login_btn.pack(padx=(10))
login_btn.pack()


sir.mainloop()
