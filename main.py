from tkinter import *
import random

names = []
global questions_answers
asked = []
score = 0

#Dictionary has key of number (for each question number) and : the value for each is a list that has 7 items, so index 0 to 6
questions_answers = {
  1: ["Lorem ipsum dolor sit amet, consectetur adipiscing?", #item 1, index 0 will be the question
  'Lorem ipsum dolor sit amet consectetur adipiscing1', # Item 2, index 1 will be the first choice
  'Lorem ipsum dolor sit amet, consectetur adipiscing2', # Item 3, index 2 will be the second choice
  'Lorem ipsum dolor sit amet, consectetur adipiscing3', # Item 4, index 3 will be the third choice
  'Lorem ipsum dolor sit amet, consectetur adipiscing4', # Item 5, index 4 will be the fourth choice
  'Lorem ipsum dolor sit amet, consectetur adipiscing5'# Item 6, index 5 will be the write statement we need to dsiplay th right stetment if the user enters the wrong choice
  ,3], # Item 7, index 6 will be the postion of the right answer (ubdex where right answer sits), this will be our check if answer is correct or no
  2: ["Lorem ipsum dolor sit amet, consectetur adipiscing?",
  'Lorem ipsum dolor sit amet, consectetur adipiscing1',
  'Lorem ipsum dolor sit amet, consectetur adipiscing2',
  'Lorem ipsum dolor sit amet, consectetur adipiscing3',
  'Lorem ipsum dolor sit amet, consectetur adipiscing4',
  'Lorem ipsum dolor sit amet, consectetur adipiscing5'
  ,1],
  3: ["Lorem ipsum dolor sit amet, consectetur adipiscing?",
  'Lorem ipsum dolor sit amet, consectetur adipiscing1',
  'Lorem ipsum dolor sit amet, consectetur adipiscing2',
  'Lorem ipsum dolor sit amet, consectetur adipiscing3',
  'Lorem ipsum dolor sit amet, consectetur adipiscing4',
  'Lorem ipsum dolor sit amet, consectetur adipiscing5'
  ,2],
  4: ["Lorem ipsum dolor sit amet, consectetur adipiscing?",
  'Lorem ipsum dolor sit amet, consectetur adipiscing1',
  'Lorem ipsum dolor sit amet, consectetur adipiscing2',
  'Lorem ipsum dolor sit amet, consectetur adipiscing3',
  'Lorem ipsum dolor sit amet, consectetur adipiscing4',
  'Lorem ipsum dolor sit amet, consectetur adipiscing5'
  ,2],
  5: ["Lorem ipsum dolor sit amet, consectetur adipiscing?",
  'Lorem ipsum dolor sit amet, consectetur adipiscing1',
  'Lorem ipsum dolor sit amet, consectetur adipiscing2',
  'Lorem ipsum dolor sit amet, consectetur adipiscing3',
  'Lorem ipsum dolor sit amet, consectetur adipiscing4',
  'Lorem ipsum dolor sit amet, consectetur adipiscing5'
  ,5],
  6: ["Lorem ipsum dolor sit amet, consectetur adipiscing?",
  'Lorem ipsum dolor sit amet, consectetur adipiscing1',
  'Lorem ipsum dolor sit amet, consectetur adipiscing2',
  'Lorem ipsum dolor sit amet, consectetur adipiscing3',
  'Lorem ipsum dolor sit amet, consectetur adipiscing4',
  'Lorem ipsum dolor sit amet, consectetur adipiscing5'
  ,3],
  7: ["Lorem ipsum dolor sit amet, consectetur adipiscing?",
  'Lorem ipsum dolor sit amet, consectetur adipiscing1',
  'Lorem ipsum dolor sit amet, consectetur adipiscing2',
  'Lorem ipsum dolor sit amet, consectetur adipiscing3',
  'Lorem ipsum dolor sit amet, consectetur adipiscing4',
  'Lorem ipsum dolor sit amet, consectetur adipiscing5'
  ,4],
  8: ["Lorem ipsum dolor sit amet, consectetur adipiscing?",
  'Lorem ipsum dolor sit amet, consectetur adipiscing1',
  'Lorem ipsum dolor sit amet, consectetur adipiscing2',
  'Lorem ipsum dolor sit amet, consectetur adipiscing3',
  'Lorem ipsum dolor sit amet, consectetur adipiscing4',
  'Lorem ipsum dolor sit amet, consectetur adipiscing5'
  ,1],
  9: ["Lorem ipsum dolor sit amet, consectetur adipiscing?",
  'Lorem ipsum dolor sit amet, consectetur adipiscing1',
  'Lorem ipsum dolor sit amet, consectetur adipiscing2',
  'Lorem ipsum dolor sit amet, consectetur adipiscing3',
  'Lorem ipsum dolor sit amet, consectetur adipiscing4',
  'Lorem ipsum dolor sit amet, consectetur adipiscing5'
  ,3],
  10:["Lorem ipsum dolor sit amet, consectetur adipiscing?",
  'Lorem ipsum dolor sit amet, consectetur adipiscing1',
  'Lorem ipsum dolor sit amet, consectetur adipiscing2',
  'Lorem ipsum dolor sit amet, consectetur adipiscing3',
  'Lorem ipsum dolor sit amet, consectetur adipiscing4',
  'Lorem ipsum dolor sit amet, consectetur adipiscing5'
  ,5],
}

def  randomiser():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()  


class QuizStarter:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color="DarkSeaGreen1"#

        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        #

        self.quiz_frame.grid()#
               
        #widgets goes below
        self.heading_label = Label(self.quiz_frame, text="Health Survey", font = ("Helvetica","18","bold"),bg="DarkSeaGreen2")
        self.heading_label.grid(row = 0, padx = 20) 
        self.var1 = IntVar() #holds value of radio buttons
        
        #label for username
        self.user_label = Label(self.quiz_frame, text = "Enter your name below to get started", font = ("Helvtica","16"),bg = "DarkSeaGreen2")
        self.user_label.grid(row = 1, padx = 20, pady = 20) 
        
        #entry box
        self.entry_box = Entry(self.quiz_frame, bg = 'DarkSeaGreen2')
        self.entry_box.grid(row=2,padx=20, pady=20)
        
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Enter", font =("Helvetica", "13", "bold"), bg = "DarkSeaGreen2", command = self.name_collection)
        self.continue_button.grid(row=3,  padx = 20)        
        
        #image
        #logo = PhotoImage(file="road.gif")
        #self.logo = Label(self.quiz_frame, image=logo)  
        #self.logo.grid(row=4,padx=20, pady=20) 
       

    def name_collection(self):
        name = self.entry_box.get()
        names.append(name) #
        print(names)
        self.quiz_frame.destroy()
        Quiz(root)

class Quiz:    
  def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color = "DarkSeaGreen1"#

        #frame set up
        self.quiz_frame = Frame (parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()#

        randomiser() #randomiser will randomly pick a question number which is qnum  
               
        #widgets goes below
        self.question_label = Label (self.quiz_frame, text = questions_answers[qnum][0], font = ("Helvetica","18","bold"), bg="DarkSeaGreen2")
        self.question_label.grid(row = 0, padx = 10) 

        self.var1 = IntVar() #holds value of radio buttons

        #first radio button to hold first choice answer 
        
        #Radiobutton 1
        self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font = ("Helvetica", "14"), bg = background_color, value = 1, variable = self.var1, padx = 10, pady = 10)
        
        self.rb1.grid(row = 1, sticky = W)

        #Radiobutton 2
        
        self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font = ("Helvetica", "14"), bg = background_color, value = 2, variable = self.var1, padx = 10, pady = 10)

        self.rb2.grid (row = 2, sticky = W)

        #Radiobutton 3
        self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font = ("Helvetica", "14"), bg = background_color, value = 3, variable = self.var1, padx = 10, pady=10)

        self.rb3.grid (row = 3, sticky = W)

        #Radiobutton 4
        self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font = ("Helvetica", "14"), bg = background_color, value = 4, variable = self.var1, padx = 10, pady = 10)

        self.rb4.grid (row = 4, sticky = W)

        #Radiobutton 5
        self.rb5 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][5], font = ("Helvetica", "14"), bg = background_color, value = 5, variable = self.var1, padx = 10, pady = 10)

        self.rb5.grid (row = 5, sticky = W)


        #Confirm button
        self.quiz_instance = Button (self.quiz_frame, text = "Confirm", font = ("Helvetica", "13", "bold"), bg = background_color)

        self.quiz_instance.grid (row = 6, padx = 5, pady = 5)

        #Score label
        self.score_label = Label (self.quiz_frame, text = "SCORE", font = ("Helvetica", "15"), bg = background_color,)

        self.score_label.grid (row = 7, padx = 10, pady = 1)

      

randomiser()
if __name__ == "__main__":
    root = Tk()
    root.title("Health Survey") 
    quizStarter_object = QuizStarter(root) #instantiation, making an instance of the class Quiz
    root.mainloop() #so the frame doesnt dissapear