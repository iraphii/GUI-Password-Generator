import tkinter as tk
import random

root = tk.Tk()
root.title('Password Generator')
root.attributes('-alpha', 1)
root.geometry('420x120')
root.resizable(width=0, height=0)

label_hello = tk.Label(root, text='Choose Number of characters')
label_hello.pack()

slider_length = tk.Scale(root, from_=1, to=55, orient='horizontal', length=250)
slider_length.pack(side='top')

generated_password = tk.Text(root, height=1, width=60)
generated_password.pack(side='bottom', pady=5)

var_alpha = tk.IntVar()
var_special = tk.IntVar()
var_numbers = tk.IntVar()


def draw_password(password: str):
	generated_password.delete('1.0', tk.END)
	generated_password.insert(tk.END, password)
	

def generate_password(length: int) -> str:
	password = ''	
	data_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	data_numb = '1234567890'
	data_special = '@#+*-!§$%&?€'
	
	if var_alpha.get() == 0 and var_numbers.get() == 0 and var_special.get() == 0:
		draw_password('Choose a specification (Alphabetical, Numbers, Special).')

	if var_alpha.get() == 1 and var_numbers.get() == 0 and var_special.get() == 0:
		for i in range(length):
			password += random.choice(data_alpha)
		draw_password(password)	

	if var_alpha.get() == 0 and var_numbers.get() == 1 and var_special.get() == 0:
		for i in range(length):
			password += random.choice(data_numb)
		draw_password(password)

	if var_alpha.get() == 0 and var_numbers.get() == 0 and var_special.get() == 1:
		for i in range(length):
			password += random.choice(data_special)		
		draw_password(password)

	if var_alpha.get() == 1 and var_numbers.get() == 1 and var_special.get() == 0:
		data = data_alpha + 3 * data_numb
		for i in range(length):
			password += random.choice(data)
		draw_password(password)

	if var_alpha.get() == 1 and var_numbers.get() == 0 and var_special.get() == 1:
		data = data_alpha + data_special
		for i in range(length):
			password += random.choice(data)
		draw_password(password)

	if var_alpha.get() == 0 and var_numbers.get() == 1 and var_special.get() == 1:
		data = data_numb + data_special
		for i in range(length):
			password += random.choice(data)
		draw_password(password)
	
	if var_alpha.get() == 1 and var_numbers.get() == 1 and var_special.get() == 1:
		data = data_alpha + 2 * data_numb + 3 *  data_special
		for i in range(length):
			password += random.choice(data)
		draw_password(password)


def get_length():
	length = slider_length.get()
	generate_password(length)


alpha = tk.Checkbutton(root, text='Alphabetical', variable=var_alpha)
alpha.pack(side='left')

numbers = tk.Checkbutton(root, text='Numbers', variable=var_numbers)
numbers.pack(side='left')

special = tk.Checkbutton(root, text='Special (#*@€..)', variable=var_special)
special.pack(side='left')

slider_button = tk.Button(root, text='GENERATE', command=get_length)
slider_button.pack(side='top')

root.mainloop()
