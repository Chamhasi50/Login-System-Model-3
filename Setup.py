from customtkinter import *
from tkinter import *
from tkinter import messagebox

from PIL import Image
import os
import sqlite3


class App(CTk):
  def __init__(self):
    super().__init__()
    self.title("Sign-in")
    self.geometry("1000x400+400+300")
    self.resizable(False, False)
    self.config(background="#18191c")
    self.file_path = os.path.dirname(os.path.relpath(__file__))

    def move_frame(frame, target_x, duration, step=1):
      current_x = frame.winfo_x()
      delta_x = (target_x - current_x) / (duration / step)

      def move_step():
        nonlocal current_x
        current_x += delta_x
        frame.place(x=current_x)
        if delta_x > 0 and current_x < target_x or delta_x < 0 and current_x > target_x:
          frame.after(step, move_step)
      move_step()

    def switch_frames_right_to_left(frame1, frame2, duration):
      current_x1, current_x2 = frame1.winfo_x(), frame2.winfo_x()
      if current_x1 < current_x2:
        move_frame(frame1, 5, duration)
        move_frame(frame2, 5, duration)
      else:
        move_frame(frame1, 5, duration)
        move_frame(frame2, 5, duration)
        signin_username.delete(0, END)
        signin_password.delete(0, END)

    def switch_frames_left_to_right(frame1, frame2, duration):
      current_x1, current_x2 = frame1.winfo_x(), frame2.winfo_x()
      if current_x1 > current_x2:
        move_frame(frame1, 990, duration)
        move_frame(frame2, 5, duration)
      else:
        move_frame(frame1, 5, duration)
        move_frame(frame2, -990, duration)
        signup_username.delete(0, END)
        signup_email.delete(0, END)
        signup_password.delete(0, END)

    self.signin_frame = CTkFrame(self, width=990, height=390, bg_color="#18191c", fg_color="#202225")
    self.signup_frame = CTkFrame(self, width=990, height=390, bg_color="#18191c", fg_color="#202225")

    duration = 300

    # --> Loging window + widget and frames.
    signin_tilte = CTkLabel(self.signin_frame, text="Sign-in", font=("Ariel", 30, "bold"), bg_color="#202225", fg_color="#202225").place(x=700, y=25)
    
    signin_username = CTkEntry(self.signin_frame, width=400, height=50, corner_radius=20, border_width=1, border_color="royalblue", placeholder_text="Username or Email", font=("Ariel", 17), bg_color="#202225", fg_color="#202225")
    signin_password = CTkEntry(self.signin_frame, width=400, height=50, corner_radius=20, border_width=1, border_color="royalblue", placeholder_text="Password", show="⁕", font=("Ariel", 17), bg_color="#202225", fg_color="#202225")

    signin_username.place(x=550, y=80)
    signin_password.place(x=550, y=140)

    signin_connect_btn = CTkButton(self.signin_frame, width=400, height=50, corner_radius=20, text="Signin", text_color="#222", font=("Ariel", 17, "bold"), bg_color="#202225", fg_color=("#fff", "royalblue"), hover_color="white", border_width=1, border_color="royalblue",).place(x=550, y=210)
    signin_option = CTkLabel(self.signin_frame, text="Or Sign in with social platforms", font=("Ariel", 15), bg_color="#202225", fg_color="transparent").place(x=645, y=270)

    lab_label_signin = CTkLabel(self.signin_frame, text='', width=600, height=395, corner_radius=50, bg_color="#202225", fg_color="royalblue").place(x=-100, y=0)

    facebook_img = CTkImage(Image.open(self.file_path + 'Icons/facebook.png'), size=(35, 35))
    face_lab = CTkButton(self.signin_frame, image = facebook_img, text='', corner_radius=50, width=10, fg_color='#202225', bg_color='#202225', hover_color='#f7f0fa').place(x=552, y=320)
    google_img = CTkImage(Image.open(self.file_path + 'Icons/google.png'), size=(35, 35))
    google_lab = CTkButton(self.signin_frame, image = google_img, text='', corner_radius=50, width=10, fg_color='#202225', bg_color='#202225', hover_color='#f7f0fa').place(x=660, y=320)
    apple_img = CTkImage(Image.open(self.file_path + 'Icons/apple.png'), size=(35, 35))
    apple_lab = CTkButton(self.signin_frame, image = apple_img, text='', corner_radius=50, width=10, fg_color='#202225', bg_color='#202225', hover_color='#f7f0fa').place(x=770, y=320)
    email_img = CTkImage(Image.open(self.file_path + 'Icons/internet.png'), size=(35, 35))
    email_lab = CTkButton(self.signin_frame, image = email_img, text='', corner_radius=50, width=10, fg_color='#202225', bg_color='#202225', hover_color='#f7f0fa').place(x=880, y=320)

    signup_btn = CTkButton(self.signin_frame, width=200, height=40, corner_radius=20, text="Signup", text_color="#222", font=("Ariel", 17, "bold"), bg_color="royalblue", fg_color="#fff", hover_color="royalblue", border_width=1, border_color="#fff", command=lambda: switch_frames_right_to_left(self.signin_frame, self.signup_frame, duration)).place(x=130, y=25)


    # --> Signup window + widget and frames.
    signup_title = CTkLabel(self.signup_frame, text="Sign-up", font=("Ariel", 30, "bold"), bg_color="#202225", fg_color="#202225").place(x=200, y=20)

    signup_username = CTkEntry(self.signup_frame, width=400, height=50, corner_radius=20, border_width=1, border_color="royalblue", placeholder_text="Username", font=("Ariel", 17), bg_color="#202225", fg_color="#202225")
    signup_email = CTkEntry(self.signup_frame, width=400, height=50, corner_radius=20, border_width=1, border_color="royalblue", placeholder_text="Email", font=("Ariel", 17), bg_color="#202225", fg_color="#202225")
    signup_password = CTkEntry(self.signup_frame, width=400, height=50, corner_radius=20, border_width=1, border_color="royalblue", placeholder_text="Password", show="⁕", font=("Ariel", 17), bg_color="#202225", fg_color="#202225")

    signup_username.place(x=50, y=70)
    signup_email.place(x=50, y=130)
    signup_password.place(x=50, y=190)

    signup_connect_btn = CTkButton(self.signup_frame, width=400, height=50, corner_radius=20, text="Signup", text_color=("black", "#fff"), font=("Ariel", 17, "bold"), bg_color="#202225", fg_color=("#fff", "royalblue"), hover_color=("white", "#444")).place(x=50, y=260)

    facebook_img = CTkImage(Image.open(self.file_path + 'Icons/facebook.png'), size=(35, 35))
    face_lab = CTkButton(self.signup_frame, image = facebook_img, text='', corner_radius=50, width=10, fg_color='#202225', bg_color='#202225', hover_color='#f7f0fa').place(x=50, y=330)
    google_img = CTkImage(Image.open(self.file_path + 'Icons/google.png'), size=(35, 35))
    google_lab = CTkButton(self.signup_frame, image = google_img, text='', corner_radius=50, width=10, fg_color='#202225', bg_color='#202225', hover_color='#f7f0fa').place(x=160, y=330)
    apple_img = CTkImage(Image.open(self.file_path + 'Icons/apple.png'), size=(35, 35))
    apple_lab = CTkButton(self.signup_frame, image = apple_img, text='', corner_radius=50, width=10, fg_color='#202225', bg_color='#202225', hover_color='#f7f0fa').place(x=270, y=330)
    email_img = CTkImage(Image.open(self.file_path + 'Icons/internet.png'), size=(35, 35))
    email_lab = CTkButton(self.signup_frame, image = email_img, text='', corner_radius=50, width=10, fg_color='#202225', bg_color='#202225', hover_color='#f7f0fa').place(x=380, y=330)

    lab_label_signup = CTkLabel(self.signup_frame, text='', width=600, height=395, corner_radius=50, bg_color="#202225", fg_color="royalblue").place(x=500, y=0)
    
    signin_btn = CTkButton(self.signup_frame, width=200, height=40, corner_radius=20, text="Signin", text_color="#222", font=("Ariel", 17, "bold"), bg_color="royalblue", fg_color="#fff", hover_color="royalblue", border_width=1, border_color="#fff", command=lambda: switch_frames_left_to_right(self.signin_frame, self.signup_frame, duration)).place(x=670, y=25)
    

     

    self.signin_frame.place(x=5, y=5)
    self.signup_frame.place(x=-990, y=5)

    self.mainloop()

App()