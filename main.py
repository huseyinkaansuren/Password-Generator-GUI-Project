import tkinter
from tkinter import messagebox
import random
import pyperclip
# PASSWORD GENERATOR
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for l in range(nr_letters)]
    password_symbols = [random.choice(symbols) for s in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for n in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# SAVE PASSWORD
def save_to_file():
    website = website_input.get()
    mail = mail_input.get()
    password = password_input.get()

    if len(website) ==0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{mail} "
                                                      f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {mail} | {password}\n")
                website_input.delete(0, tkinter.END)
                password_input.delete(0, tkinter.END)


# UI SETUP
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

# Canvas
canvas = tkinter.Canvas(width=200, height=200)
logo=tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1,row=0)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0,row=1)

mail_label = tkinter.Label(text="Email/Username:")
mail_label.grid(column=0,row=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0,row=3)

# Entries
website_input = tkinter.Entry(width=52)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

mail_input = tkinter.Entry(width=52)
mail_input.grid(column=1, row=2, columnspan=2)

password_input = tkinter.Entry(width=33)
password_input.grid(column=1, row=3)


# Buttons
gen_pass_button=tkinter.Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3)

add_button= tkinter.Button(text="Add", width=44, command=save_to_file)
add_button.grid(column=1,row=4, columnspan=2)


window.mainloop()