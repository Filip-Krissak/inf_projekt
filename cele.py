import tkinter
from tkinter import messagebox
import bcrypt
import json

file_name = "data.json"

# Read data from the JSON file or initialize it as an empty dictionary
try:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    data = {"data": []}

# Function to check if a user is registered
def check_user_registration(username, password):
    with open("user_database.txt", "r") as file:
        for line in file:
            stored_username, stored_password_hash = line.strip().split(",")
            if username == stored_username and bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
                return True
    return False

# Function to register a new user
def register_user(username, password):
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    with open("user_database.txt", "a") as file:
        file.write(f"{username},{password_hash.decode('utf-8')}\n")

# Function to create the initial screen
def create_initial_screen():
    window = tkinter.Tk()
    window.title("PET Flaše")
    window.geometry('400x700')
    window.configure(bg='lightblue')

    canvas = tkinter.Canvas(window, width=400, height=700, bg="lightblue")
    canvas.pack()

    canvas.create_text(200, 150, text='Zalohujeme.sk', font=("Times New Roman", 50), tags='login')

    canvas.create_rectangle(50, 400, 350, 450, tags='login')
    canvas.create_text(200, 425, text='log in', font=("Times New Roman", 35), tags='login')

    canvas.create_rectangle(50, 500, 350, 550, tags='signup')
    canvas.create_text(200, 525, text='sign up', font=("Times New Roman", 35), tags='signup')

    def click_handler(event):
        x, y = event.x, event.y
        if 50 < x < 350 and 400 < y < 450:
            window.destroy()
            login_screen()
        if 50 < x < 350 and 500 < y < 550:
            window.destroy()
            signup_screen()

    canvas.bind('<Button-1>', click_handler)
    tkinter.mainloop()

# Function to create the final screen
def create_final_screen(username):
    window = tkinter.Tk()
    window.title("PET Flaše")
    window.geometry('400x700')
    window.configure(bg='lightblue')

    canvas = tkinter.Canvas(window, width=400, height=700, bg="lightblue")
    canvas.pack()

    canvas.create_line(0, 50, 400, 50, width=4, tags='d')
    canvas.create_line(200, 50, 200, 0, width=4, tags='d')

    canvas.create_text(100, 25, text='domov', font=("Times New Roman", 15), tags='d')
    canvas.create_text(300, 25, text='graf', font=("Times New Roman", 15), tags='d')

    # Display the username on the final screen
    canvas.create_text(200, 125, text=f'Logged in as: {username}', font=("Times New Roman", 15), tags='d')

    canvas.create_text(200, 300, text='BALANCE:', font=("Times New Roman", 30), tags='d')
    canvas.create_text(200, 350, text='', font=("Times New Roman", 30), tags='d')

    def click_handler(event):
        x, y = event.x, event.y
        if x < 150 and y < 50:
            window.destroy()
            create_final_screen(username)
        if x > 150 and y < 50:
            window.destroy()

    canvas.bind('<Button-1>', click_handler)
    tkinter.mainloop()

# Function to create the login screen
def login_screen():
    window = tkinter.Tk()
    window.title("PET Flaše")
    window.geometry('400x700')
    window.configure(bg='lightblue')

    def login():
        username = username_entry.get()
        password = password_entry.get()

        if check_user_registration(username, password):
            window.destroy()
            create_final_screen(username)  # Pass the username to the final screen

            # Store the action under the corresponding username
            date = "2023-07-04"
            bottle_can = True
            amount = 7
            store_user_action(username, date, bottle_can, amount)
        else:
            messagebox.showerror(title="Error", message="Invalid login credentials.")

    frame = tkinter.Frame(window, bg='lightblue')
    login_label = tkinter.Label(frame, text="PET Flaše - log in", bg='lightblue', fg="cyan4", font=("Arial", 30))
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

# Function to create the sign-up screen
def signup_screen():
    window = tkinter.Tk()
    window.title("PET Flaše")
    window.geometry('400x700')
    window.configure(bg='lightblue')

    def sign_up():
        username = username_entry.get()
        password = password_entry.get()
        password2 = password2_entry.get()

        if check_user_registration(username, password):
            messagebox.showerror(title="Error", message="A user with this name already exists.")
        else:
            if len(username) < 3 or len(username) > 15:
                messagebox.showerror(title="Error", message="Username does not meet the requirements. (Min. 3, Max. 15 characters)")
            elif len(password) < 1 or len(password) > 15:
                messagebox.showerror(title="Error", message="Password does not meet the requirements. (Max. 15 characters)")
            elif password != password2:
                messagebox.showerror(title="Error", message="Passwords do not match.")
            else:
                register_user(username, password)
                messagebox.showinfo(title="Successful Registration", message="Registration successful. Welcome.")
                window.destroy()
                create_final_screen(username)  # Pass the username to the final screen

                # Store the action under the corresponding username
                date = "2023-07-04"
                bottle_can = True
                amount = 7
                store_user_action(username, date, bottle_can, amount)

    frame = tkinter.Frame(bg='lightblue')
    signup_label = tkinter.Label(frame, text="PET Flaše - sign up", bg='lightblue', fg="cyan4", font=("Arial", 30))
    username_label = tkinter.Label(frame, text="Username", bg='cyan4', fg="white", font=("Arial", 16, 'bold'))
    password_label = tkinter.Label(frame, text="Password", bg='cyan4', fg="white", font=("Arial", 16, 'bold'))
    password2_label = tkinter.Label(frame, text="Repeat Password", bg='cyan4', fg="white", font=("Arial", 16, 'bold'))
    username_entry = tkinter.Entry(frame, font=("Arial", 16))
    password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
    password2_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
    signup_button = tkinter.Button(frame, text="Sign up", bg="cyan4", fg="black", font=("Arial", 16), command=sign_up)

    signup_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    password2_label.grid(row=3, column=0)
    password2_entry.grid(row=3, column=1, pady=20)
    signup_button.grid(row=4, column=0, columnspan=2, pady=30)
    frame.pack()
    window.mainloop()

# Function to store the user's action in the JSON file
def store_user_action(username, date, bottle_can, amount):
    new_data = {
        "user": username,
        "date": date,
        "bottle_can": bottle_can,
        "amount": amount
    }
    data["data"].append(new_data)

    # Save the updated data back to the JSON file
    with open(file_name, "w") as json_file:
        json.dump(data, json_file)

# Main program
username = None
create_initial_screen()
