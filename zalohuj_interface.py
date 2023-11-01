import tkinter
from tkinter import messagebox
def prva_obrazovka():
    
    window = tkinter.Tk()
    window.title("Login PET Flaše")
    window.geometry('400x700')
    window.configure(bg='lightblue')
    
    canvas = tkinter.Canvas(window,width=400,height=700,bg="lightblue")
    canvas.pack()
    canvas.create_text(200,150,text='Zalohujeme.sk',font=("Times New Roman", 50),tags='login')
    canvas.create_rectangle(50,400,350,450,tags='login')
    canvas.create_text(200,425,text='log in',font=("Times New Roman", 35),tags='login')
    canvas.create_rectangle(50,500,350,550,tags='signup')
    canvas.create_text(200,525,text='sign up',font=("Times New Roman", 35),tags='signup')
    def mys(s):
        x=s.x
        y=s.y
        if x>50 and x<350 and y>400 and y<450:
            window.destroy()
            looogin()                            #PREPOJIT A VYTVORIT NOVY CANVAS, KDE POJDU DALSIE OBRAZOVKY
        if x>50 and x<350 and y>500 and y<550:
            window.destroy()
            signin()
    canvas.bind('<Button-1>',mys)
    tkinter.mainloop()

def posledna_obrazovka():

    window = tkinter.Tk()
    window.title("Login PET Flaše")
    window.geometry('400x700')
    window.configure(bg='lightblue')
    
    canvas = tkinter.Canvas(window,width=400,height=700,bg="lightblue")
    canvas.pack()
    canvas.create_line(0,50,400,50,width=4,tags='d')
    canvas.create_line(200,50,200,0,width=4,tags='d')
    canvas.create_text(100,25,text='domov',font=("Times New Roman", 15),tags='d')
    canvas.create_text(300,25,text='graf',font=("Times New Roman", 15),tags='d')
    canvas.create_text(200,100,text='meno',font=("Times New Roman", 15),tags='d') #SEM POTOM DAT PREMENNU Z LOGINU
    canvas.create_text(200,300,text='BALANCE:',font=("Times New Roman", 30),tags='d')
    canvas.create_text(200,350,text='',font=("Times New Roman", 30),tags='d') #MAM PENAAZE MAM PENAAAZE GRINDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEER
    def mys(s):
        x=s.x
        y=s.y
        if x<150 and y<50:
                window.destroy()
                posledna_obrazovka()
        if x>150 and y<50:
                window.destroy()
                #graf()
    
    canvas.bind('<Button-1>',mys)




    tkinter.mainloop()



def looogin():

    window = tkinter.Tk()
    window.title("Login PET Flaše")
    window.geometry('400x700')
    window.configure(bg='lightblue')


    def login():
        username = "makeuseof"
        password = "muo"

        if username_entry.get()==username and password_entry.get()==password:
            window.destroy()
            posledna_obrazovka()
        else:
            messagebox.showerror(title="Error", message="Nesprávne prihlasovacie údaje.")

    frame = tkinter.Frame(window,bg='lightblue')
    login_label = tkinter.Label(frame, text="PET Flaše - sign in", bg='lightblue', fg="cyan4", font=("Arial", 30))
    username_label = tkinter.Label(frame, text="Username", bg='cyan4', fg="white", font=("Arial", 16, 'bold'))
    password_label = tkinter.Label(frame, text="Password", bg='cyan4', fg="white", font=("Arial", 16, 'bold'))
    username_entry = tkinter.Entry(frame, font=("Arial", 16))
    password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
    login_button = tkinter.Button(frame, text="Login", bg="cyan4", fg="black", font=("Arial", 16), command=login)
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)
    frame.pack()
    window.mainloop()


def signin():
    window = tkinter.Tk()
    window.title("Registracia PET Flaše")
    window.geometry('400x700')
    window.configure(bg='lightblue')


    def signinin():
        a=len(username_entry.get())
        b=len(password_entry.get())
        if 3>a or a>15:
            messagebox.showinfo(title="Error", message="Použivatelské meno nespĺňa podmienky.(Min.3,Max.15 znakov)")
        ###elif (meno sa zhoduje s iným menom v databáze):
        ###    messagebox.showinfo(title="Error", message="Použivatelské meno sa už používa.")
        else:
            if b<1 or b>15:
                messagebox.showinfo(title="Error", message="Heslo nespĺňa podmienky.(Max.15 znakov)")
            else:
                if password_entry.get() == password2_entry.get():
                    messagebox.showinfo(title="Úspešné prihlásenie!", message="Registrácia prebehla úspešne. Vitajte")
                    print("Používatelské meno: " + username_entry.get())
                    print("Heslo: " + password_entry.get())
                    posledna_obrazovka()
                else:
                    messagebox.showinfo(title="Error", message="Heslá sa nezhodujú.")


    frame = tkinter.Frame(bg='lightblue')
    login_label = tkinter.Label(frame, text="PET Flaše - sign in", bg='lightblue', fg="cyan4", font=("Arial", 30))
    username_label = tkinter.Label(frame, text="Username", bg='cyan4', fg="white", font=("Arial", 16, 'bold'))
    password_label = tkinter.Label(frame, text="Password", bg='cyan4', fg="white", font=("Arial", 16, 'bold'))
    password2_label = tkinter.Label(frame, text="Repeat Password", bg='cyan4', fg="white", font=("Arial", 16, 'bold'))
    username_entry = tkinter.Entry(frame, font=("Arial", 16))
    password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
    password2_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
    login_button = tkinter.Button(frame, text="Sign in", bg="cyan4", fg="black", font=("Arial", 16), command=signinin)
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    password2_label.grid(row=3, column=0)
    password2_entry.grid(row=3, column=1, pady=20)

    login_button.grid(row=4, column=0, columnspan=2, pady=30)
    frame.pack()
    window.mainloop()

prva_obrazovka()
#posledna_obrazovka()
