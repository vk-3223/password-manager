from secrets import choice
from tkinter import *
from tkinter import messagebox
import pyperclip
import random

font_name = "courier"

def password_genrate():
    letters  = ['a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbol = ['!','#','$','%','^','&','*','()','*','+']

    

    password_letters = [choice(letters) for _ in range(random.randint(8,10))]
    password_symbol = [choice(symbol) for _ in range(random.randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(random.randint(2,4))]
    password_list = password_letters+password_symbol+password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
    
def save():
    website = len(websit_entery.get())
    email = email_entery.get()
    password = len(password_entry.get())
    if password==0 and website==0:
        messagebox.showerror(title="oops something was wrong")
    else:    
        is_okay = messagebox.askokcancel(f"are you write email:{email}\n & password:{password} is right ?")
   
    if is_okay:
        with open("data.txt","a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            websit_entery.delete(0,END)
            password_entry.delete(0,END)



window = Tk()
window.title("password manger")
window.config(padx=550,pady=200) 
canvas = Canvas(width=200,height=200,highlightthickness=0)
canvas.grid()

logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

websit_label = Label(text="website")
websit_label.grid(row=1,column=0)
email_label = Label(text="email")
email_label.grid(row=2,column=0)
password_label = Label(text="passowrd")
password_label.grid(row=3,column=0)

## Entry are use for for take entry any text ##
websit_entery = Entry(width=35)
websit_entery.grid(row=1,column=1)
websit_entery.focus()
email_entery = Entry(width=35)
email_entery.grid(row=2,column=1)
## insert are for add some text in email ##
email_entery.insert(0,"venilkhunt3223@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3,column=1)
## insert random password ##


genrate_password = Button(text="genrate password",highlightthickness=2,command=password_genrate)
genrate_password.grid(row=3,column=2)

add_button = Button(text="Add",highlightthickness=0,width=20,command=save)
add_button.grid(row=4,column=1)

window.mainloop()