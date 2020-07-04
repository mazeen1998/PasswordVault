from tkinter import * 
from tkinter import messagebox
from tkinter import scrolledtext as st
import pickle
import os



m=Tk()
m.title('Password Vault')
m.iconbitmap('cir.ico')
m.geometry('600x300')
m.resizable(0,0)
def add():
	domain=e6.get()
	username=e7.get()
	password=e8.get()
	e6.delete(0,'end')
	e7.delete(0,'end')
	e8.delete(0,'end')
	new={'domain':domain,'username':username,'password':password}
	# print('mm ',new)
	mfile=os.path.isfile('pass')
	if mfile:
		with open('pass','rb') as nn:
			my=pickle.load(nn)
			# print(my)
		my.append(new)
	with open('pass','wb') as nn:
		if mfile:
			pickle.dump(my,nn)
		else:
			nee=[]
			nee.append(new)
			new=nee
			# print(new)
			pickle.dump(new,nn)
def reset():
	pw=e9.get()
	with open('pas','rb') as nn:
		r_new=pickle.load(nn)
	r_new['pw']=pw
	with open('pas','wb') as nn:
		pickle.dump(r_new,nn)

def main():
	global e6,e7,e8,e9
	m.geometry('600x450')
	f2=Frame(m,borderwidth=5,height=300,width=580,bg='grey')
	f2.grid(rowspan=8,ipadx=300,ipady=280,columnspan=3)
	l=Label(f2,text='Welcome '+name+'!',fg='yellow',bg='white',font=('Verdana',26)).grid(ipadx=170,row=0,columnspan=4,ipady=5)
	e9=Entry(f2)
	e9.insert(0,'New Password')
	e9.grid(row=1,column=0,columnspan=2)
	b1=Button(f2,text='Reset Password',command=reset).grid(row=1,column=2,columnspan=2)
	l=Label(f2,text='Domain',bg='grey',font=('Ariel Bold',12)).grid(row=2,column=1,pady=5)
	e6=Entry(f2)
	e6.grid(row=2,column=2)
	l=Label(f2,text='Username',bg='grey',font=('Ariel Bold',12)).grid(row=3,column=1,pady=5)
	e7=Entry(f2)
	e7.grid(row=3,column=2)
	l=Label(f2,text='Password',bg='grey',font=('Ariel Bold',12)).grid(row=4,column=1,pady=5)
	e8=Entry(f2)
	e8.grid(row=4,column=2)
	b=Button(f2,text='Add',command=add).grid(row=5,column=2)
	s=st.ScrolledText(f2,bg='white',font=('Times New Roman',16),height=8,width=52)
	s.grid(row=6,columnspan=3)
	mfile=os.path.isfile('pass')
	if mfile:
		with open('pass','rb') as nn:
			store=pickle.load(nn)
		# print(store)
		for i in store:
			s.insert(INSERT,'\n')
			for k,v in i.items():
				s.insert(INSERT, k+' : '+v +'\n')
	s.configure(state='disabled')


def login():
	global e4,e5,f1,name
	name=e4.get()
	pw=e5.get()
	cont=pickle.load(open('pas','rb'))
	if cont['name']!=name:
		messagebox.showerror('Login Error','Incorrect User')
	if cont['pw']!=pw:
		messagebox.showerror('Login Error','Incorrect Password')
	else:
		f1.grid_forget()
		main()
	

def get():
	name=e1.get()
	pw=e2.get()
	cpw=e3.get()
	# print(name,pw,cpw)
	if pw!=cpw:
		messagebox.showerror('Password Error','Password doesnot match')
	if pw==cpw:
		cont=[{'name':name,'pw':pw}]
		pickle.dump(cont,open('pas','wb'))
		# print(cont)
		messagebox.showinfo('Registration','Success, Login now!')
		f.grid_forget()
		log()

def log():
	global f1,e4,e5
	f1=Frame(m,borderwidth=5,height=300,width=580,bg='grey')
	f1.grid(rowspan=8,ipadx=300,ipady=280,columnspan=3)
	l=Label(f1,text='Login',fg='yellow',bg='white',font=('Ariel Bold',26)).grid(ipadx=250,row=1,columnspan=4,ipady=5)
	l=Label(f1,text='Username',bg='grey',font=('Ariel Bold',12)).grid(row=3,column=1,pady=5)
	e4=Entry(f1)
	e4.grid(row=3,column=2)
	l=Label(f1,text='Password',bg='grey',font=('Ariel Bold',12)).grid(row=4,column=1,pady=5)
	e5=Entry(f1,show='*')
	e5.grid(row=4,column=2)
	b=Button(f1,text='Login',command=login).grid(row=5,column=2,pady=5)

file=os.path.isfile('pas')
if file:
	log()
else:
	f=Frame(m,borderwidth=5,height=300,width=580,bg='grey')
	f.grid(rowspan=8,ipadx=300,ipady=280,columnspan=3)
	l=Label(f,text='Registration Pannel',fg='yellow',bg='white',font=('Ariel Bold',20)).grid(ipadx=173,row=1,columnspan=4,ipady=5)
	l=Label(f,text='Username',bg='grey',font=('Ariel Bold',12)).grid(row=3,column=1,pady=5)
	e1=Entry(f)
	e1.grid(row=3,column=2)
	l=Label(f,text='Password',bg='grey',font=('Ariel Bold',12)).grid(row=4,column=1,pady=5)
	e2=Entry(f)
	e2.grid(row=4,column=2)
	l=Label(f,text='Confirm Password',bg='grey',font=('Ariel Bold',12)).grid(row=5,column=1,pady=5)
	e3=Entry(f)
	e3.grid(row=5,column=2)
	b=Button(f,text='Register',command=get).grid(row=6,column=2,pady=5)


mainloop()