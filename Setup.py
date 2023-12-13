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

    # -> This line defines a function called move_frame that takes four parameters: frame (the Tkinter frame to be moved), 
    #target_x (the target x-coordinate to move the frame to), duration (the total duration of the animation in milliseconds), 
    #and an optional parameter step (the size of each movement step, with a default value of 1).
    def move_frame(frame, target_x, duration, step=1):
      current_x = frame.winfo_x() # This line gets the current x-coordinate of the frame using the winfo_x() method.
      delta_x = (target_x - current_x) / (duration / step) # This line calculates the distance to move the frame in each step (delta_x). 
      #It divides the total distance to travel (target_x - current_x) by the number of steps, which is determined by the duration and step size.

      # This line defines an inner function called move_step, which represents a single step of the animation.
      def move_step():
        nonlocal current_x # This line allows the move_step function to modify the current_x variable from the outer function.
        current_x += delta_x # This line allows the move_step function to modify the current_x variable from the outer function.
        frame.place(x=current_x) # This line updates the frame's x-coordinate using the place() method.
        if delta_x > 0 and current_x < target_x or delta_x < 0 and current_x > target_x:
          frame.after(step, move_step) # If the frame has not reached the target x-coordinate, this line schedules the move_step function to be called after the specified step milliseconds using the after() method.
      move_step() # This line initiates the first step of the animation.

    # -> Two frames (frame1 and frame2) are created with different background colors.
    # The switch_frames function is introduced, which checks the current x-coordinates of both frames and moves them accordingly to create the switching effect.
    # The button is configured to call the switch_frames function when clicked.
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

    # >>> The main frmaes of the app.
    self.signin_frame = CTkFrame(self, width=990, height=390, bg_color="#18191c", fg_color="#fff")
    self.signup_frame = CTkFrame(self, width=990, height=390, bg_color="#18191c", fg_color="#fff")

    duration = 300 # These lines set the target x-coordinate and the duration of the animation.

    # --> Loging window + widget and frames.
    signin_tilte = CTkLabel(self.signin_frame, text="Sign-in", text_color="#333", font=("Ariel", 30, "bold"), bg_color="#fff", fg_color="#fff").place(x=700, y=25)
    
    # --> Signin Entries widget.
    signin_username = CTkEntry(self.signin_frame, width=400, height=50, corner_radius=20, border_width=1, border_color="royalblue", placeholder_text="Username or Email", text_color="#333", font=("Ariel", 17), bg_color="#fff", fg_color="#fff")
    signin_password = CTkEntry(self.signin_frame, width=400, height=50, corner_radius=20, border_width=1, border_color="royalblue", placeholder_text="Password", text_color="#333", show="⁕", font=("Ariel", 17), bg_color="#fff", fg_color="#fff")

    signin_username.place(x=550, y=80)
    signin_password.place(x=550, y=140)

    # --> Signin Connection button and option label.
    signin_connect_btn = CTkButton(self.signin_frame, width=400, height=50, corner_radius=20, text="Signin", text_color="#111", font=("Ariel", 17, "bold"), bg_color="#fff", fg_color=("#fff", "royalblue"), hover_color="white", border_width=1, border_color="royalblue",).place(x=550, y=210)
    signin_option = CTkLabel(self.signin_frame, text="Or Sign in with social platforms", height=10, text_color="#333", font=("Ariel", 15, "underline"), bg_color="#fff", fg_color="#fff").place(x=645, y=270)

    # --> Signin blue label and the IMG of the window.
    lab_label_signin = CTkLabel(self.signin_frame, text='', width=600, height=395, corner_radius=50, bg_color="#fff", fg_color="royalblue").place(x=-100, y=0)
    signin_img = CTkImage(Image.open(self.file_path + 'Images/Secure_login.png'), size=(450, 320))
    signin_img_lab = CTkLabel(self.signin_frame, image = signin_img, text='', fg_color='royalblue', bg_color='transparent').place(x=20, y=90)

    # --> Social Media (Icons, Widget and layout) for the signin frame.
    facebook_img = CTkImage(Image.open(self.file_path + 'Icons/facebook.png'), size=(35, 35))
    face_lab = CTkButton(self.signin_frame, image = facebook_img, text='', corner_radius=50, width=10, fg_color='#fff', bg_color='#fff', hover_color='#f7f0fa').place(x=552, y=320)
    google_img = CTkImage(Image.open(self.file_path + 'Icons/google.png'), size=(35, 35))
    google_lab = CTkButton(self.signin_frame, image = google_img, text='', corner_radius=50, width=10, fg_color='#fff', bg_color='#fff', hover_color='#f7f0fa').place(x=660, y=320)
    apple_img = CTkImage(Image.open(self.file_path + 'Icons/apple.png'), size=(35, 35))
    apple_lab = CTkButton(self.signin_frame, image = apple_img, text='', corner_radius=50, width=10, fg_color='#fff', bg_color='#fff', hover_color='#f7f0fa').place(x=770, y=320)
    email_img = CTkImage(Image.open(self.file_path + 'Icons/internet.png'), size=(35, 35))
    email_lab = CTkButton(self.signin_frame, image = email_img, text='', corner_radius=50, width=10, fg_color='#fff', bg_color='#fff', hover_color='#f7f0fa').place(x=880, y=320)

    # --> This is the signup button whitch alowes you to switch between Signin and Signup frames.
    signup_btn = CTkButton(self.signin_frame, width=200, height=40, corner_radius=20, text="Signup", text_color="#222", font=("Ariel", 17, "bold"), bg_color="royalblue", fg_color="#fff", hover_color="royalblue", border_width=1, border_color="#fff", command=lambda: switch_frames_right_to_left(self.signin_frame, self.signup_frame, duration)).place(x=130, y=25)
    signin_msg_label = CTkLabel(self.signin_frame, text="Register with your personal details to completly use this app.\nThanks for signing up with us.", height=10, font=("",15), bg_color="royalblue", fg_color="transparent").place(x=40, y=80)


    # --> Signup window + widget and frames.
    signup_title = CTkLabel(self.signup_frame, text="Sign-up", text_color="#333", font=("Ariel", 30, "bold"), bg_color="#fff", fg_color="#fff").place(x=200, y=20)

    # --> Signup Entries widget.
    signup_username = CTkEntry(self.signup_frame, width=400, height=50, corner_radius=20, border_width=1, border_color="royalblue", placeholder_text="Username", text_color="#333", font=("Ariel", 17), bg_color="#fff", fg_color="#fff")
    signup_email = CTkEntry(self.signup_frame, width=400, height=50, corner_radius=20, border_width=1, border_color="royalblue", placeholder_text="Email", text_color="#333", font=("Ariel", 17), bg_color="#fff", fg_color="#fff")
    signup_password = CTkEntry(self.signup_frame, width=400, height=50, corner_radius=20, border_width=1, border_color="royalblue", placeholder_text="Password", text_color="#333", show="⁕", font=("Ariel", 17), bg_color="#fff", fg_color="#fff")

    signup_username.place(x=50, y=70)
    signup_email.place(x=50, y=130)
    signup_password.place(x=50, y=190)

    # --> This is the signup button to create an account.
    signup_connect_btn = CTkButton(self.signup_frame, width=400, height=50, corner_radius=20, text="Signup", text_color="#111", font=("Ariel", 17, "bold"), bg_color="#fff", fg_color="royalblue", hover_color="#fff", border_width=1, border_color="royalblue",).place(x=50, y=260)

    # --> Social Media (Icons, Widget and layout) for the signup frame.
    facebook_img = CTkImage(Image.open(self.file_path + 'Icons/facebook.png'), size=(35, 35))
    face_lab = CTkButton(self.signup_frame, image = facebook_img, text='', corner_radius=50, width=10, fg_color='#fff', bg_color='#fff', hover_color='#f7f0fa').place(x=50, y=330)
    google_img = CTkImage(Image.open(self.file_path + 'Icons/google.png'), size=(35, 35))
    google_lab = CTkButton(self.signup_frame, image = google_img, text='', corner_radius=50, width=10, fg_color='#fff', bg_color='#fff', hover_color='#f7f0fa').place(x=160, y=330)
    apple_img = CTkImage(Image.open(self.file_path + 'Icons/apple.png'), size=(35, 35))
    apple_lab = CTkButton(self.signup_frame, image = apple_img, text='', corner_radius=50, width=10, fg_color='#fff', bg_color='#fff', hover_color='#f7f0fa').place(x=270, y=330)
    email_img = CTkImage(Image.open(self.file_path + 'Icons/internet.png'), size=(35, 35))
    email_lab = CTkButton(self.signup_frame, image = email_img, text='', corner_radius=50, width=10, fg_color='#fff', bg_color='#fff', hover_color='#f7f0fa').place(x=380, y=330)

    # --> This is the blue color that is on left side (Signup Page).
    lab_label_signup = CTkLabel(self.signup_frame, text='', width=600, height=395, corner_radius=50, bg_color="#fff", fg_color="royalblue").place(x=500, y=0)
    
    # --> This is the signin button whitch alowes you to switch between Signin and Signup frames.
    signin_btn = CTkButton(self.signup_frame, width=200, height=40, corner_radius=20, text="Signin", text_color="#222", font=("Ariel", 17, "bold"), bg_color="royalblue", fg_color="#fff", hover_color="royalblue", border_width=1, border_color="#fff", command=lambda: switch_frames_left_to_right(self.signin_frame, self.signup_frame, duration)).place(x=670, y=25)
    
    # --> Signup IMG and text widget.
    signup_img = CTkImage(Image.open(self.file_path + 'Images/Sign_up.png'), size=(450, 300))
    signup_img_lab = CTkLabel(self.signup_frame, image = signup_img, text='', fg_color='royalblue', bg_color='transparent').place(x=530, y=100)
    signin_msg_label = CTkLabel(self.signup_frame, text="Already having an existing account, please ignore this page.\nThanks for signing up with us.", height=10, font=("",15), bg_color="royalblue", fg_color="transparent").place(x=540, y=80)

    self.signin_frame.place(x=5, y=5)
    self.signup_frame.place(x=-990, y=5)

    self.mainloop()


App()
