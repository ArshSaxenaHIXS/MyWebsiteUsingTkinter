from tkinter import*
from tkinter import ttk, filedialog


root =Tk()
root.title("Climate Change")
root.geometry('600x400')
root.configure(bg='snow')



notebook = ttk.Notebook(root)
notebook.pack(fill=BOTH, expand=TRUE)
def thankyou_message():
    thankyoumessage1=Tk()
    thankyoumessage1.title("Thank you")
    thankyoumessage1.geometry('400x50')
    Label(thankyoumessage1, text="Thank you so much .").pack(pady=10)

def feedback2():
    feedback1=Tk()
    feedback1.geometry('500x300')
    feedback1.title("Feedback")
    Label(feedback1, text="How did you like the app?").pack(pady=10)
    feedback3_entry = Entry(feedback1, width=70)
    feedback3_entry.insert(0,"")
    feedback3_entry.pack(pady=10)
    Label(feedback1, text="How much would you rate this app from 1-10?", bg='snow',fg='black').pack(pady=10)
    feedback3_entry= Entry(feedback1, width=10)
    feedback3_entry.insert(0,"")
    feedback3_entry.pack(pady=10)
    thankyou= Button(feedback1,text="End",command=thankyou_message)
    thankyou.pack(pady=10)

def submit():
    submit=Tk()
    submit.title("Climate Change")
    submit.geometry('400x100')
    Label(submit,text="Thank You You scored 3/3",bg='snow',fg='black').pack(pady=10)
    feedback= Button(submit, text="Feedback", command=feedback2)
    feedback.pack(pady=10)
def quizz():
    root=Tk()
    root.title("Quizz")
    root.geometry('600x400')
    Label(root, text="What is Climate Change",bg='snow',fg='black').pack(pady=10)
    question_entry = Entry(root, width=70)
    question_entry.insert(0,"")
    question_entry.pack(pady=10)
    Label(root, text="3 Causes for climate change",bg='snow',fg='black').pack(pady=10)
    question2_entry = Entry(root, width=70)
    
    question2_entry.insert(0,"")
    question2_entry.pack(pady=10)
    Label(root, text="3 Consequences for climate change",bg='snow',fg='black').pack(pady=10)
    question3_entry = Entry(root, width=70)
    
    question3_entry.insert(0,"")
    question3_entry.pack(pady=10)
    Label(root, text="How can you prevent Climate Change ?",bg='snow',fg='black').pack(pady=10)
    question3_entry = Entry(root, width=70)
    
    question3_entry.insert(0,"         ")
    question3_entry.pack(pady=10)
    

    btn=Button(root,text="Submit",command=submit)
    btn.pack(pady=10)


defination_frame = Frame(notebook, bg='light yellow')
notebook.add(defination_frame, text='Defination')
Label(defination_frame, text="Topc: Climate Change", bg="light yellow", fg="black").pack(pady=10)
Label(defination_frame, text=" A change in global or regional climate patterns, in particular a change apparent from the", bg="snow", fg='black').pack(pady=10)
Label(defination_frame, text= "mid to late 20th century onwards and attributed largely to the increased levels of", bg = 'snow', fg='black').pack(pady=10)
Label(defination_frame, text="atmospheric carbon dioxide produced by the use of fossil fuels.", bg='snow', fg='black').pack(pady=10)

causes_frame = Frame(notebook, bg='light blue')
notebook.add(causes_frame, text="Causes Of Climate Change")
Label(causes_frame, text="Causes For Climate change", bg='light yellow', fg='black').pack(pady=10)
Label(causes_frame, text="CO2 emissions are by far the largest cause of global warming and ocean acidification, and they are rising.", bg='snow', fg='black').pack(pady=10)
Label(causes_frame, text="Methane emissions are the second largest cause of warming, and they are rising.", bg='snow', fg='black').pack(pady=10)
Label(causes_frame, text="Since 1950 human activities have led to virtually all temperature rise.", bg='snow', fg='black').pack(pady=10)
Label(causes_frame, text=" Natural forces have caused virtually none of the temperature rise.", bg='snow', fg='black').pack(pady=10)


consequences_frame = Frame(notebook, bg='light green')
notebook.add(consequences_frame, text="Consequences Of Climate Change",)
Label(consequences_frame, text="Consequences for Climate Change.", bg='light yellow', fg='black').pack(pady=10)
Label(consequences_frame, text="Sea level is rising, and at an increasing pace.", bg='snow', fg='black').pack(pady=10)
Label(consequences_frame, text="Glaciers are melting, ice sheets are thinning, and Arctic sea ice is disappearing.", bg='snow',fg="black").pack(pady=10)
Label(consequences_frame, text="Permafrost is thawing.", bg='snow',fg='black').pack(pady=10)
Label(consequences_frame, text="The number of cold days and nights are decreasing.",bg='snow',fg='black').pack(pady=10)
Label(consequences_frame, text="The number of hot days and nights are increasing",bg='snow',fg='black').pack(pady=10)
Label(consequences_frame, text="Heat waves will occur more often and last longer.",bg='snow',fg='black').pack(pady=10)
Label(consequences_frame, text="Heavy rainstorms and snowstorms will become more intense and frequent..",bg='snow',fg='black').pack(pady=10)
Label(consequences_frame, text="Species are vanishing at an alarming and ever-increasing rate.",bg='snow',fg='black').pack(pady=10)
   

quizz_frame = Frame(notebook, bg='snow')
notebook.add(quizz_frame, text="Quizz")

button_quizz = Button(quizz_frame, text="Quizz", command= quizz,bg='snow')
button_quizz.pack()


root.mainloop()
