from tkinter import *
import random

names = []
asked = []
score = 0

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
        self.heading_label = Label(self.quiz_frame, text="MRGS School Map", font = ("Helvetica","18","bold"),bg="DarkSeaGreen2")
        self.heading_label.grid(row = 0, padx = 20) 
        self.var1 = IntVar() #holds value of radio buttons
        
        #label for username
        self.user_label = Label(self.quiz_frame, text = "Enter your name below to get started", font = ("Helvtica","16"),bg = "DarkSeaGreen2")
        self.user_label.grid(row = 1, padx = 20, pady = 20) 

        self.error_label= Label(self.quiz_frame, bg = background_color)
        self.error_label.grid(row = 6, padx = 20, pady =20)
        
        #entry box
        self.entry_box = Entry(self.quiz_frame, bg = 'DarkSeaGreen2')
        self.entry_box.grid(row=3,padx=20, pady=20)

        self.exit_button = Button (self.quiz_frame, text = "Exit", font = ("Helvetica", "13", "bold"), bg="IndianRed1", command=self.quiz_frame.destroy)
        self.exit_button.grid(row=5, padx=5, pady=5)

        #continue button
        self.continue_button = Button(self.quiz_frame, text="Enter", font =("Helvetica", "13", "bold"), bg = "DarkSeaGreen2", command = self.name_collection)
        self.continue_button.grid(row=4,  padx = 20)  


        
        #image
        #logo = PhotoImage(file="road.gif")
        #self.logo = Label(self.quiz_frame, image=logo)  
        #self.logo.grid(row=4,padx=20, pady=20) 
       

    def name_collection(self):
        name = self.entry_box.get()
        if name.strip() != "" and len(name) <= 15:
          names.append(name) #
          print(names)
          self.quiz_frame.destroy()
          Quiz(root)
        elif len(name)  >15:
          self.error_label.config(text="Please enter a name that is not more than 15 characters", fg="IndianRed1")
        elif len(name) ==0:
          self.error_label.config(text="Please enter a name", fg="IndianRed1")
       

class Quiz:    
  def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
        #Dictionary has key of number (for each question number) and : the value for each is a list that has 7 items, so index 0 to 6
        self.questions_answers = {
          1: ["What is the name of the hall?", #item 1, index 0 will be the question
          'Watson Hall', # Item 2, index 1 will be the first choice
          'Ball Hall', # Item 3, index 2 will be the second choice
          'Butler Hall', # Item 4, index 3 will be the third choice
          'School Hall', # Item 5, index 4 will be the fourth choice
          'Cathedral Hall'# Item 6, index 5 will be the write statement we need to dsiplay the right stetment if the user enters the wrong choice
          ,3], # Item 7, index 6 will be the postion of the right answer (ubdex where right answer sits), this will be our check if answer is correct or no
          2: ["1Lorem ipsum dolor sit amet, consectetur adipiscing?",
          'Lorem ipsum dolor sit amet, consectetur adipiscing1',
          'Lorem ipsum dolor sit amet, consectetur adipiscing2',
          'Lorem ipsum dolor sit amet, consectetur adipiscing3',
          'Lorem ipsum dolor sit amet, consectetur adipiscing4',
          'Lorem ipsum dolor sit amet, consectetur adipiscing5'
          ,1],
          3: ["2Lorem ipsum dolor sit amet, consectetur adipiscing?",
          'Lorem ipsum dolor sit amet, consectetur adipiscing1',
          'Lorem ipsum dolor sit amet, consectetur adipiscing2',
          'Lorem ipsum dolor sit amet, consectetur adipiscing3',
          'Lorem ipsum dolor sit amet, consectetur adipiscing4',
          'Lorem ipsum dolor sit amet, consectetur adipiscing5'
          ,2],
          4: ["3Lorem ipsum dolor sit amet, consectetur adipiscing?",
          'Lorem ipsum dolor sit amet, consectetur adipiscing1',
          'Lorem ipsum dolor sit amet, consectetur adipiscing2',
          'Lorem ipsum dolor sit amet, consectetur adipiscing3',
          'Lorem ipsum dolor sit amet, consectetur adipiscing4',
          'Lorem ipsum dolor sit amet, consectetur adipiscing5'
          ,2],
          5: ["4Lorem ipsum dolor sit amet, consectetur adipiscing?",
          'Lorem ipsum dolor sit amet, consectetur adipiscing1',
          'Lorem ipsum dolor sit amet, consectetur adipiscing2',
          'Lorem ipsum dolor sit amet, consectetur adipiscing3',
          'Lorem ipsum dolor sit amet, consectetur adipiscing4',
          'Lorem ipsum dolor sit amet, consectetur adipiscing5'
          ,5],
          6: ["5Lorem ipsum dolor sit amet, consectetur adipiscing?",
          'Lorem ipsum dolor sit amet, consectetur adipiscing1',
          'Lorem ipsum dolor sit amet, consectetur adipiscing2',
          'Lorem ipsum dolor sit amet, consectetur adipiscing3',
          'Lorem ipsum dolor sit amet, consectetur adipiscing4',
          'Lorem ipsum dolor sit amet, consectetur adipiscing5'
          ,3],
          7: ["6Lorem ipsum dolor sit amet, consectetur adipiscing?",
          'Lorem ipsum dolor sit amet, consectetur adipiscing1',
          'Lorem ipsum dolor sit amet, consectetur adipiscing2',
          'Lorem ipsum dolor sit amet, consectetur adipiscing3',
          'Lorem ipsum dolor sit amet, consectetur adipiscing4',
          'Lorem ipsum dolor sit amet, consectetur adipiscing5'
          ,4],
          8: ["7Lorem ipsum dolor sit amet, consectetur adipiscing?",
          'Lorem ipsum dolor sit amet, consectetur adipiscing1',
          'Lorem ipsum dolor sit amet, consectetur adipiscing2',
          'Lorem ipsum dolor sit amet, consectetur adipiscing3',
          'Lorem ipsum dolor sit amet, consectetur adipiscing4',
          'Lorem ipsum dolor sit amet, consectetur adipiscing5'
          ,1],
          9: ["8Lorem ipsum dolor sit amet, consectetur adipiscing?",
          'Lorem ipsum dolor sit amet, consectetur adipiscing1',
          'Lorem ipsum dolor sit amet, consectetur adipiscing2',
          'Lorem ipsum dolor sit amet, consectetur adipiscing3',
          'Lorem ipsum dolor sit amet, consectetur adipiscing4',
          'Lorem ipsum dolor sit amet, consectetur adipiscing5'
          ,3],
          10:["9Lorem ipsum dolor sit amet, consectetur adipiscing?",
          'Lorem ipsum dolor sit amet, consectetur adipiscing1',
          'Lorem ipsum dolor sit amet, consectetur adipiscing2',
          'Lorem ipsum dolor sit amet, consectetur adipiscing3',
          'Lorem ipsum dolor sit amet, consectetur adipiscing4',
          'Lorem ipsum dolor sit amet, consectetur adipiscing5'
          ,5],
        }

        background_color = "DarkSeaGreen1"#

        #frame set up
        self.quiz_frame = Frame (parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()#

        randomiser() #randomiser will randomly pick a question number which is qnum  
               
        #widgets goes below
        self.question_label = Label (self.quiz_frame, text = self.questions_answers[qnum][0], font = ("Helvetica","18","bold"), bg="DarkSeaGreen2")
        self.question_label.grid(row = 0, padx = 10) 

        self.var1 = IntVar() #holds value of radio buttons

        #first radio button to hold first choice answer 
        
        #Radiobutton 1
        self.rb1 = Radiobutton (self.quiz_frame, text = self.questions_answers[qnum][1], font = ("Helvetica", "14"), bg = background_color, value = 1, variable = self.var1, padx = 10, pady = 10)
        
        self.rb1.grid(row = 1, sticky = W)

        #Radiobutton 2
        
        self.rb2 = Radiobutton (self.quiz_frame, text = self.questions_answers[qnum][2], font = ("Helvetica", "14"), bg = background_color, value = 2, variable = self.var1, padx = 10, pady = 10)

        self.rb2.grid (row = 2, sticky = W)

        #Radiobutton 3
        self.rb3 = Radiobutton (self.quiz_frame, text = self.questions_answers[qnum][3], font = ("Helvetica", "14"), bg = background_color, value = 3, variable = self.var1, padx = 10, pady=10)

        self.rb3.grid (row = 3, sticky = W)

        #Radiobutton 4
        self.rb4 = Radiobutton (self.quiz_frame, text = self.questions_answers[qnum][4], font = ("Helvetica", "14"), bg = background_color, value = 4, variable = self.var1, padx = 10, pady = 10)

        self.rb4.grid (row = 4, sticky = W)

        #Radiobutton 5
        self.rb5 = Radiobutton (self.quiz_frame, text = self.questions_answers[qnum][5], font = ("Helvetica", "14"), bg = background_color, value = 5, variable = self.var1, padx = 10, pady = 10)

        self.rb5.grid (row = 5, sticky = W)


        #Confirm button
        self.confirm_button = Button (self.quiz_frame, text = "Confirm", font = ("Helvetica", "13", "bold"), bg = background_color, command = self.test_progress)

        self.confirm_button.grid (row = 6, padx = 5, pady = 5)

        #Score label
        self.score_label = Label (self.quiz_frame, text = "SCORE", font = ("Helvetica", "15"), bg = background_color,)

        self.score_label.grid (row = 7, padx = 10, pady = 1)

        #Quit Button
        self.quit= Button(self.quiz_frame, text="Quit", font=("Helvetica", "13", "bold"), bg="IndianRed1", command=self.end_screen)
        self.quit.grid(row=8, sticky=E, padx=10, pady=20)

        

        #Method showing the next questions data
  def questions_setup (self):
    randomiser()
    self.var1.set(0)
    self.question_label.config(text = self.questions_answers[qnum][0])
    self.rb1.config(text = self.questions_answers[qnum][1])
    self.rb2.config(text = self.questions_answers[qnum][2])
    self.rb3.config(text = self.questions_answers[qnum][3])
    self.rb4.config(text = self.questions_answers[qnum][4])
    self.rb5.config(text = self.questions_answers[qnum][5])

  #This is the method that would get invoked with confrim answer button is clicked, to take care of test_progress

  def test_progress(self):
    global score
    scr_label = self.score_label
    choice = self.var1.get()
    if len(asked)>9: #if the question is last
      if choice == self.questions_answers[qnum][6]: #if the last question is the correct answer
        score+=1 
        scr_label.configure(text = score)
        self.confirm_button.config(text="Confirm")
        self.end_screen()
      else: #if the last question is the incorrect answer
        print(choice)
        score+=0
        scr_label.configure(text = " The correct answer was " + self.questions_answers[qnum][5])
        self.confirm_button.config(text="Confirm")
        self.end_screen()
    else: #if it is not the last question
      if choice==0: #checks if the user has made a choice
        self.confirm_button.config(text="Try again please, you didnt select anyhting")
        choice=self.var1.get()
      else: #if a choice was made and its not the last question
        if choice == self.questions_answers[qnum][6]: #if thier choice is correct
          score+=1
          scr_label.configure(text = score)
          self.confirm_button.config(text="Confirm")
          self.questions_setup() #execute the method to move on to the next question 
        else: #if the choice was wrong
          print(choice)
          score+=0
          scr_label.configure(text="The correct answer was: " + self.questions_answers[qnum][5])
          self.confirm_button.configure(text="Confirm")
          self.questions_setup() 


  def end_screen(self):
      root.withdraw()
      name=names[0]
      file=open("leaderBoard.txt", "a")

      file.write(str(score))
      file.write(" - ")
      file.write(name+"\n")
      file.close()

      inputFile= open("leaderBoard.txt", "r")
      lineList = inputFile.readlines()
      lineList.sort()
      top=[]
      top5=(lineList[-5:])

      for line in top5:
          point=line.split(" - ")
          top.append((int(point[0]), point[1]))
      file.close()
      top.sort()
      top.reverse()
        
      return_string = ""
      for i in range (len(top)):
          return_string +="{} - {}\n".format(top[i][0], top[i][1])
      print(return_string)

      open_end_screen=End()
      open_end_screen.listLabel.config(text=return_string)


class End:
  def __init__(self):
    background = "DarkSeaGreen1"
    self.end_box = Toplevel(root)
    self.end_box.title("End Box")

    self.end_frame = Frame (self.end_box, width=1000, height=1000, bg=background)
    self.end_frame.grid()

    self.listLabel = Label (self.end_frame, text="1st Place Avaliable", font = ("Helvetica", "18"), width = 40, bg = background, padx=10, pady=10)
    self.listLabel.grid(column=0, row=2)

    end_heading = Label (self.end_frame, text = "Well Done", font=("Helvetica", "22", "bold"), bg=background, pady=15)
    end_heading.grid(row=0)

    exit_button = Button (self.end_frame, text="Exit", width=10, bg="IndianRed1", font=("Helvetica", "12", "bold"), command=self.close_end)
    exit_button.grid(row = 4, pady = 20)

   
  def close_end(self):
    self.end_box.destroy()
    root.destroy()

randomiser()
if __name__ == "__main__":
    root = Tk()
    root.title("Health Survey") 
    quizStarter_object = QuizStarter(root) #instantiation, making an instance of the class Quiz
    root.mainloop() #so the frame doesnt dissapear