import customtkinter as ck
from tkinter import *


app = ck.CTk()
app.geometry("900x400+400+300")
app.config(background="#18191c")

# -> This line defines a function called move_frame that takes four parameters: frame (the Tkinter frame to be moved), target_x (the target x-coordinate to move the frame to), duration (the total duration of the animation in milliseconds), and an optional parameter step (the size of each movement step, with a default value of 1).
def move_frame(frame, target_x, duration, step=1):
    current_x = frame.winfo_x() # This line gets the current x-coordinate of the frame using the winfo_x() method.
    delta_x = (target_x - current_x) / (duration / step) # This line calculates the distance to move the frame in each step (delta_x). It divides the total distance to travel (target_x - current_x) by the number of steps, which is determined by the duration and step size.

    # This line defines an inner function called move_step, which represents a single step of the animation.
    def move_step():
        nonlocal current_x # This line allows the move_step function to modify the current_x variable from the outer function.
        current_x += delta_x # This line allows the move_step function to modify the current_x variable from the outer function.
        frame.place(x=current_x) # This line updates the frame's x-coordinate using the place() method.
        if delta_x > 0 and current_x < target_x or delta_x < 0 and current_x > target_x: # This line checks if the frame has not reached the target x-coordinate yet.
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


def switch_frames_left_to_right(frame1, frame2, duration):
    current_x1, current_x2 = frame1.winfo_x(), frame2.winfo_x()
    if current_x1 > current_x2:
        move_frame(frame1, 890, duration)
        move_frame(frame2, 5, duration)
    else:
        move_frame(frame1, 5, duration)
        move_frame(frame2, -890, duration)


login_frame = ck.CTkFrame(app, width=890, height=390, fg_color='#202225', bg_color='#18191c')
signup_frame = ck.CTkFrame(app, width=890, height=390, fg_color='#333', bg_color='#18191c')


duration = 300 # These lines set the target x-coordinate and the duration of the animation.


show_login_frame = ck.CTkButton(login_frame, width=30, corner_radius=8, text='Signup', bg_color='transparent', fg_color='royalblue', hover_color='#fff', command=lambda: switch_frames_right_to_left(login_frame, signup_frame, duration))
show_login_frame.place(x=400, y=5) # This line calls the move_frame function to start the animation of moving the frame from its initial position to the target position over the specified duration.

show_signup_frame = ck.CTkButton(signup_frame, width=30, corner_radius=8, text='Loging', bg_color='transparent', fg_color='royalblue', hover_color='#fff', command=lambda: switch_frames_left_to_right(signup_frame, signup_frame, duration))
show_signup_frame.place(x=400, y=5) # This line calls the move_frame function to start the animation of moving the frame from its initial position to the target position over the specified duration.



login_frame.place(x=5, y=5)
signup_frame.place(x=-890, y=5)


app.mainloop()