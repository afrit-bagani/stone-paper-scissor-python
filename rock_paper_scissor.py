from tkinter import *
import ttkbootstrap as tb
import random

root = tb.Window()
root.title('Rock Paper Scissors')
root.geometry('1000x700')
#root.iconbitmap('')

# load the images
user_rock_image = tb.PhotoImage(file='user_rock_image.png')
user_paper_image = tb.PhotoImage(file='user_paper_image.png')
user_scissor_image = tb.PhotoImage(file='user_scissor_image.png')
com_rock_image = tb.PhotoImage(file='com_rock_image.png')
com_paper_image = tb.PhotoImage(file='com_paper_image.png')
com_scissor_image = tb.PhotoImage(file='com_scissor_image.png')

# create a dict for saving score
score = {
   'win' : 0,
   'loss' : 0,
   'tie' : 0,
}

# function defination
def play_game(choice):
   # user_icon change based on button click
   user_choice = choice
   if user_choice == 'rock':
      user_icon.config(image=user_rock_image)
   elif user_choice == 'paper':
      user_icon.config(image=user_paper_image)
   else:
      user_icon.config(image=user_scissor_image)     

   # com_icon change based on button click
   choices = ['rock', 'paper', 'scissor']
   com_choice = random.choice(choices)
   if com_choice == 'rock':
      com_icon.config(image=com_rock_image)
   elif com_choice == 'paper':
      com_icon.config(image=com_paper_image)
   else:
      com_icon.config(image=com_scissor_image)     

   # wining statement decide and showing score
   if user_choice == com_choice:
      wining_statement.config(text="It's a Tie")
      score['tie'] += 1
   elif (user_choice == 'rock' and com_choice == 'scissor') or (user_choice == 'paper' and com_choice == 'rock') or (user_choice == 'scissor' and com_choice == 'paper'):
      wining_statement.config(text='You Won')
      score['win'] += 1
      user_score.config(text=f'{score["win"]}')
   else:
      wining_statement.config(text='You Loss')
      score['loss'] += 1
      com_score.config(text=f'{score["loss"]}')

#heading 
heading = tb.Label(root, text='Rock Paper Scissors', font=('Helvetica', 36), foreground='red')
heading.pack(pady=(20,50))

# 2 frame => i) play_ground_container ii) button container
play_ground_container = tb.Frame(root)
play_ground_container.pack()
button_container = tb.Frame(root)
button_container.pack(pady=(50,0))

# 3 frame into play_ground_container => i) user container ii) score container iii) com container
user_container = tb.Frame(play_ground_container)
user_container.grid(row=1, column=1)
score_container = tb.Frame(play_ground_container)
score_container.grid(row=1, column=2, padx=120)
com_container = tb.Frame(play_ground_container)
com_container.grid(row=1, column=3)

# user, computer photo
user_icon = tb.Label(user_container, image=user_rock_image)
com_icon = tb.Label(com_container, image=com_rock_image)
user_icon.grid(row=1, column=1)
com_icon.grid(row=1, column=5)

# score 
user_score = tb.Label(score_container, text=0, font=('Helvetica', 36))
dash = tb.Label(score_container, text=' - ', font=('Helvetica', 36))
com_score = tb.Label(score_container, text=0, font=('Helvetica', 36))
user_score.grid(row=1, column=2)
dash.grid(row=1, column=3,)
com_score.grid(row=1, column=4)

# user computer text labeling 
user_label = tb.Label(user_container, text='User', font=('Helvetica', 18))
user_label.grid(row=2, column=1, pady=(7,0))
com_label = tb.Label(com_container, text='Computer', font=('Helvetica', 18))
com_label.grid(row=2, column=5, pady=(7,0))

# wining statement(Win, Loss, Tie)
wining_statement = tb.Label(play_ground_container, text="Let's Play", font=('Helvetica', 28), foreground='yellow')
wining_statement.grid(row=3, column=2, padx=(10,10), pady=(7, 0))
 
# adding style as width and style do not support by Button
my_style = tb.Style()
my_style.configure('danger.TButton', font=('Helvetica', 22), width=7)
my_style = tb.Style()
my_style.configure('success.TButton', font=('Helvetica', 22), width=7)
my_style = tb.Style()
my_style.configure('warning.TButton', font=('Helvetica', 22), width=7)

# rock paper scissor button
rock_button = tb.Button(button_container, text='Rock', style='danger.TButton', command=lambda:play_game('rock'))
rock_button.grid(row=4, column=1)
paper_button = tb.Button(button_container, text='Paper', style='success.TButton', command=lambda:play_game('paper'))
paper_button.grid(row=4, column=2, padx=20)
scissor_button = tb.Button(button_container, text='Scissor', style='warning.TButton', command=lambda:play_game('scissor'))
scissor_button.grid(row=4, column=3)

root.mainloop()