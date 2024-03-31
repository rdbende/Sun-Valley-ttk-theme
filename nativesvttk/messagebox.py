import os
os.system("pip install Pillow")
from winsound import MessageBeep, MB_ICONHAND, MB_ICONASTERISK
from ctypes import windll, c_int, byref, sizeof, c_char_p
from tkinter import Toplevel,Tk, X, Y, LEFT, RIGHT, BOTTOM, Frame
from tkinter.ttk import Button, Label
from PIL import Image, ImageTk
from darkdetect import isDark
from sv_ttk import set_theme
from os import getenv

systemroot = getenv("SYSTEMROOT") + "\\System32\\"
class NormalModel(Toplevel):
	""" This is a class for Normal Messagebox Model """
	def __init__(self, mtitle, mtext, mcommand, mtype, mclick = "OK"):
		""" Init this model"""
		super().__init__()
		
		self.master = Tk()
		self.master.withdraw()
		self.mtitle = mtitle # Title
		self.mtext = mtext # Infomation
		self.mtype = mtype.lower()
		if self.mtype == "showwarning": # Type icon
			MessageBeep(eval("MB_ICONHAND"))
			self.icon = systemroot + "SecurityAndMaintenance_Alert.png"
		elif self.mtype == "showerror":
			MessageBeep(eval("MB_ICONHAND"))
			self.icon = systemroot + "SecurityAndMaintenance_Error.png"
		else:
			MessageBeep(eval("MB_ICONASTERISK"))
			self.icon = systemroot + "SecurityAndMaintenance.png"
		load = Image.open(self.icon)   # Open image
		load = load.resize((55, 55)) # Resize the image
		image = ImageTk.PhotoImage(load)  # Read opened image
		
		self.title(self.mtitle) # Icon will set by master window
		self.iconphoto(False, image)
		self.minsize(375, 175)
		self.resizable(False, False)
		self.transient(self.master)
		self.attributes("-topmost", True)

		self.show = Frame(self)
		if not mcommand: self.command = self.mcommand
		else: self.command = mcommand
		self.cilck = Button(self.show, text = mclick, command = self.command, style = "Accent.TButton", width = 7)
		
		self.show.pack(side = BOTTOM, fill = X)
		self.cilck.pack(side = RIGHT, fill = X)
		self.image = Label(self, image = image)
		self.image.pack(side = LEFT, fill = X, padx = 25, pady = 10)
		self.info = Label(self, text = self.mtext)
		self.info.pack(side = LEFT, fill = X, padx = 25, pady = 10)
		
		try:
			if isDark(): 
				self.darkmode()
				self.show["bg"] = "#1c1c1a"
			else: 
				set_theme("dark")
				self.show["bg"] = "#f5f5f5"
		except: pass # The master window had theme
		self.mainloop()
		
		del load, image
			
	def mcommand(self):
		""" Normal Button Command"""
		self.destroy()
		return True
	
	def darkmode(self):
		""" Set window into darkmode"""
		set_theme("dark")
		self.update()
		DWMWA_USE_IMMERSIVE_DARK_MODE = 20
		set_window_attribute = windll.dwmapi.DwmSetWindowAttribute
		get_parent = windll.user32.GetParent
		hwnd = get_parent(self.winfo_id())
		rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
		value = 2
		value = c_int(value)
		set_window_attribute(hwnd, rendering_policy, byref(value), sizeof(value))
		self.withdraw()
		self.deiconify()

def showinfo(mtitle, mtext, mcommand = None):
	""" Showinfo Messagebox """
	handle = NormalModel(mtitle, mtext, mcommand, mtype = "showinfo")
	return True

def showwarning(mtitle, mtext, mcommand = None):
	""" Showwarning Messagebox """
	handle = NormalModel(mtitle, mtext, mcommand, mtype = "showwarning")
	return True
	
def showerror(mtitle, mtext, mcommand = None):
	""" Showerror Messagebox """
	handle = NormalModel(mtitle, mtext, mcommand, mtype = "showerror")
	return True

