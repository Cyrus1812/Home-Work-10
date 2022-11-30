from tkinter import *
def support():
    

    with open("User_question.txt",'r',encoding="utf-8") as data:        #колличество вопросов
        column = data.readlines()
        quest = []
        for i in range(len(column)):
            if i%2!=0:   
                quest.append(column[i]) 

    def btn_click_save():                                       #запись вопроса
        Answers = answer.get()
        with open("Answer.txt",'a+',encoding="utf-8") as data:
            data.writelines(Answers+'\n')

    with open("Answer.txt",'r',encoding="utf-8") as rop:                    #Удаление вопросов на которые дали ответ
        line = rop.readlines()
        
    if len(quest) == len(line):
        with open("User_question.txt",'w+',encoding="utf-8") as remove:
            remove.read()

    root = Tk()

    canvas = Canvas(root,height=500,width=500)
    canvas.pack


    frm = Frame(root, bg='white')
    frm.pack()

    if len(quest)>=1:                   # Вывод вопросов техподдержке
        question_number = Label(frm, text=f'У вас {len(quest)} непрочитанных вопросов.')
        question_number.pack()
        for i in range(len(quest)):
            if i<len(quest):
                question = Label(frm, text=f'Вопрос {i+1}: {quest[i]}')
                question.pack()
            else:
                question = Label(frm, text='Вопросов нет')
                question.pack()

    answer = Entry(frm)
    answer.pack()

    send = Button(frm, text="Send", command=btn_click_save)
    send.pack()

    exit = Button(frm, text="Quit", command=root.destroy)
    exit.pack()

    root.mainloop()

