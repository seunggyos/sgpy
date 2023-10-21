import tkinter as tk
import tkinter.ttk
import csv
from tkinter import *
import random
import tkinter.messagebox as msgbox
from tkintermapview import TkinterMapView
from Color import *

win = tk.Tk()
win.iconbitmap('ico/dksmsakszma.ico')
win.title("아는만큼보인다")
win.geometry("500x900")
win.resizable(False, False)

score = 0
m_score = 0
count = 0
ekdma = 0
lastanswp = 10
notebook = tk.ttk.Notebook(win, width=400, height=800)
notebook.pack()

frame1 = tk.Frame(win)
notebook.add(frame1, text="4지선다")
def scoree():
    win1 = Tk()
    win1.title("결과창")
    win1.geometry("300x500")
    win1.config(bg=BGCOLOR1)
    result1 = Label(win1, text="맞은 개수 ", highlightcolor='blue', highlightthickness=4,
                    font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR1, bd=4,
                    fg='white')
    result1.pack(pady=10)
    result2 = Label(win1, text="틀린 개수 ", highlightcolor='blue', highlightthickness=4,
                    font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR1, bd=4,
                    fg='white')
    xmfflsahdma = Label(win1, text="틀린 문제", font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR1, bd=4,
                        fg='white')
    result2.pack(pady=10)
    xmfflsahdma.pack(pady=5)
    result3 = Label(win1, text="틀린문제 나오는 곳", wraplength=220, highlightcolor='blue', highlightthickness=4,
                    font=("나눔바른펜", 10, "bold"), bg=BGCOLOR1, bd=4,
                    fg='white')
    result3.pack(pady=10)
    skrkwk = Button(win1, text="종료", command=win1.destroy, width=10, height=3)
    skrkwk.place(x=120, y=440)
##게임 2
ekqekq1 =[]
def game2():
    with open("threka.csv", "r", encoding="UTF-8-sig") as file:
        question2 = list(csv.reader(file))
    ekqekq1.clear()
    def next_question():
        global answer
        global cur_qustion
        global cur_qustion1
        global multi_choice
        for i in range(4):
            buttons[i].config(bg=THREKACOLOR2)

        multi_choice = random.sample(question2, 4)
        answer = random.randint(0, 3)
        cur_qustion = multi_choice[answer][0]
        cur_qustion1 = multi_choice[answer][1]

        question_label.config(text=cur_qustion)
        question_label.config(wraplength=300)
        for i in range(4):
            buttons[i].config(text=multi_choice[i][1])

    def hint():
        cur_qustion = multi_choice[answer][2]
        print(cur_qustion)
        msgbox.showinfo("힌트", f"{cur_qustion}입니다")

    def check_answer(idx):
        global score
        global m_score
        global count
        global lastanswp
        global ekqekq
        idx = int(idx)
        if answer == idx:
            buttons[idx].config(bg=Choicecolor)
            win.after(1000, next_question)
            score = score + 1
            count = count + 1
            lastanswp = lastanswp -1
            akwglsrottn3.config(text="맞힌 개수:" + str(score))
            akwglsrottn4.config(text="틀린 개수:" + str(m_score))
            skajwl2.config(text="남은 개수:"  + str(lastanswp))
            if count == 10:
                win1 = Tk()
                win1.title("결과창")
                win1.geometry("300x500")
                win1.config(bg=BGCOLOR3)
                result1 = Label(win1, text="맞은 개수는 " + str(score) + "개",highlightcolor='blue', highlightthickness=4,font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR3,bd=4,
                    fg='white')
                result1.pack(pady=10)
                result2 = Label(win1, text="틀린 개수는 " + str(m_score) + "개",highlightcolor='blue', highlightthickness=4,font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR3,bd=4,
                    fg='white')
                xmfflsahdma = Label(win1, text="틀린 문제",font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR3,bd=4,
                    fg='white')
                result2.pack(pady=10)
                xmfflsahdma.pack(pady=5)
                result3 = Label(win1, text=str(ekqekq1), wraplength=220,highlightcolor='blue', highlightthickness=4,font=("나눔바른펜", 10, "bold"),  bg=BGCOLOR3,bd=4,
                fg='white')
                result3.pack()
                skrkwk = Button(win1, text="종료" , command=win1.destroy,width=10, height=3,bg=NEXTBUTTON2)
                skrkwk.place(x=120, y=440)
                count = 0
                m_score = 0
                score = 0
                lastanswp = 10
                win.destroy()
        elif answer != idx:
            msgbox.showinfo("떙", "틀렸습니다")
            buttons[idx].config(bg=ChoicecolorX)
            win.after(1000, next_question)
            ekqekq1.append(cur_qustion1)
            m_score = m_score + 1
            count = count + 1
            lastanswp = lastanswp -1
            print(count)
            akwglsrottn3.config(text="맞힌 개수:" + str(score))
            akwglsrottn4.config(text="틀린 개수:" + str(m_score))
            skajwl2.config(text="남은 개수:" + str(lastanswp))
            if count == 10:
                win1 = Tk()
                win1.title("결과창")
                win1.config(bg=BGCOLOR3)
                win1.geometry("300x500")
                result1 = Label(win1, text="맞은 개수는 "+str(score)+"개" ,highlightcolor='blue', highlightthickness=4,font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR3,bd=4,
                    fg='white')

                result1.pack(pady=10)
                result2 = Label(win1, text="틀린 개수는 "+str(m_score)+"개" ,highlightcolor='blue', highlightthickness=4,font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR3,bd=4,
                    fg='white')
                xmfflsahdma = Label(win1, text="틀린 문제",font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR3,bd=4,
                    fg='white')
                result2.pack(pady=10)
                xmfflsahdma.pack(pady=5)
                result3 = Label(win1, text=str(ekqekq1),wraplength=220 ,highlightcolor='blue', highlightthickness=4,font=("나눔바른펜", 10, "bold"), bg=BGCOLOR3,bd=4,
                    fg='white')
                result3.pack()
                skrkwk = Button(win1, text="종료" , command=win1.destroy,width=10, height=3,bg=NEXTBUTTON2)
                skrkwk.place(x=120, y=440)
                count = 0
                m_score = 0
                score = 0
                lastanswp = 10
                win.destroy()

    def skrkrl():
        global score
        global m_score
        global count
        global lastanswp
        lastanswp = 10
        count = 0
        m_score = 0
        score = 0
        win.destroy()

    win = Tk()
    win.iconbitmap('ico/threka1.ico')
    win.title("속담퀴즈")
    win.resizable(False, False)
    win.config(padx=30, pady=10, bg=BGCOLOR3)
    skajwl2 = Label(win, text="남은 개수" + str(lastanswp), font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR3,bd=4,
                    fg='white')
    skajwl2.pack(anchor='se')

    question_label = Label(win, width=30, height=3, text='text', highlightcolor='blue', highlightthickness=4,
                           font=("나눔바른펜", 12, "bold"), bg=BGCOLOR7, fg="white")

    question_label.pack(pady=20)
    buttons = []
    for i in range(4):
        btn = Button(win, text="{i}번", width=35, height=2, font=("나눔바른펜", 15, "bold"),
                     bg=BTN_COLOR, command=lambda idx=i: check_answer(idx))
        btn.pack()
        buttons.append(btn)

    next_btn = Button(win, text="다음문제", width=15, height=2,
                      command=next_question,
                      font=("나눔바른펜", 15, "bold"), bg=NEXTBUTTON2)
    next_btn.pack(pady=30)
    akwglsrottn3 = Label(win, text="맞힌 개수:" + str(score), font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR3,
                         bd=4,
                         fg='white')
    akwglsrottn4 = Label(win, text="틀린 개수:" + str(m_score), font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR3,
                         fg='white', bd=4)

    exit_btn = Button(win, text="종료하기", width=15, height=2, command=skrkrl, bg=BGCOLOR7, )
    hint = Button(win, text="힌트", width=15, height=2, command=hint, bg=BGCOLOR7, )
    next_question()
    exit_btn.pack(side='left')
    hint.pack(side='right')
    akwglsrottn3.pack()
    akwglsrottn4.pack()

ekqekq2 =[]
##게임 3
def game3():
    with open("4ja.csv", "r", encoding="UTF-8-sig") as file:
        question3 = list(csv.reader(file))
    ekqekq2.clear()
    def next_question():
        global answer
        global cur_qustion
        global multi_choice
        global multi_choice
        for i in range(4):
            buttons[i].config(bg=TKWKCOLOR2)

        multi_choice = random.sample(question3, 4)
        answer = random.randint(0, 3)
        cur_qustion = multi_choice[answer][0]
        question_label.config(text=cur_qustion)

        for i in range(4):
            buttons[i].config(text=multi_choice[i][1])

    def hint():
        cur_qustion = multi_choice[answer][2]
        print(cur_qustion)
        msgbox.showinfo("힌트", f"{cur_qustion}입니다")

    def check_answer(idx):
        global score
        global m_score
        global count
        global lastanswp
        global ekqekq
        idx = int(idx)
        if answer == idx:
            buttons[idx].config(bg=Choicecolor)
            win.after(1000, next_question)
            score = score + 1
            count = count + 1
            lastanswp = lastanswp -1
            print(count)
            print(score)
            akwglsrottn5.config(text="맞힌 개수:" + str(score))
            akwglsrottn6.config(text="틀린 개수:" + str(m_score))
            skajwl3.config(text="남은 개수:" + str(lastanswp))
            if count == 10:
                win1 = Tk()
                win1.title("결과창")
                win1.geometry("300x500")
                win1.config(bg=BGCOLOR4)

                result1 = Label(win1, text="맞은 개수는 "+str(score)+"개" ,highlightcolor='blue', highlightthickness=4, font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR4,bd=4,
                    fg='white')
                result1.pack(pady=10)
                result2 = Label(win1, text="틀린 개수는 "+str(m_score)+"개" ,highlightcolor='blue', highlightthickness=4, font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR4,bd=4,
                    fg='white')
                xmfflsahdma = Label(win1, text="틀린 문제", font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR4,bd=4,
                    fg='white')
                result2.pack(pady=10)
                xmfflsahdma.pack(pady=5)
                result3 = Label(win1, text=str(ekqekq2),wraplength=220,highlightcolor='blue', highlightthickness=4, font=("나눔바른펜", 10, "bold"), bg=BGCOLOR4,bd=4,
                    fg='white' )
                result3.pack()
                skrkwk = Button(win1, text="종료" , command=win1.destroy,width=10, height=3,bg=TKWKCOLOR3)
                skrkwk.place(x=120, y=440)
                count = 0
                m_score = 0
                score = 0
                lastanswp = 10
                win.destroy()
        elif answer != idx:
            msgbox.showinfo("떙", "틀렸습니다")
            buttons[idx].config(bg=ChoicecolorX)
            win.after(1000, next_question)
            ekqekq2.append(cur_qustion)
            m_score = m_score + 1
            count = count + 1
            lastanswp = lastanswp -1
            akwglsrottn5.config(text="맞힌 개수:" + str(score))
            akwglsrottn6.config(text="틀린 개수:" + str(m_score))
            skajwl3.config(text="남은 개수:" + str(lastanswp))
            print(count)
            if count == 10:
                win1 = Tk()
                win1.title("결과창")
                win1.geometry("300x500")
                win1.config(bg=BGCOLOR4)

                result1 = Label(win1, text="맞은 개수는 " + str(score) + "개",highlightcolor='blue', highlightthickness=4, font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR4,bd=4,
                    fg='white')
                result1.pack(pady=10)
                result2 = Label(win1, text="틀린 개수는 " + str(m_score) + "개",highlightcolor='blue', highlightthickness=4, font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR4,bd=4,
                    fg='white')
                xmfflsahdma = Label(win1, text="틀린 문제", font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR4,bd=4,
                    fg='white')
                result2.pack(pady=10)
                xmfflsahdma.pack(pady=5)
                result3 = Label(win1, text=str(ekqekq2), wraplength=220,highlightcolor='blue', highlightthickness=4, font=("나눔바른펜", 10, "bold"),  bg=BGCOLOR4,bd=4,
                    fg='white')
                result3.pack()
                skrkwk = Button(win1, text="종료" , command=win1.destroy,width=10, height=3,bg=TKWKCOLOR3)
                skrkwk.place(x=120, y=440)
                count = 0
                m_score = 0
                score = 0
                lastanswp = 10
                win.destroy()

    def skrkrl():
        global score
        global m_score
        global count
        global lastanswp
        lastanswp = 10
        count = 0
        m_score = 0
        score = 0
        win.destroy()

    win = Tk()
    win.title("사자성어")
    win.iconbitmap('ico/tkwktjddj.ico')
    win.resizable(False, False)
    win.config(padx=30, pady=10, bg=BGCOLOR4)
    skajwl3 = Label(win, text="남은 개수" + str(lastanswp), font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR4,bd=4,
                    fg='white')
    skajwl3.pack(anchor='se')

    question_label = Label(win, width=30, height=3, text='text', highlightcolor='blue', highlightthickness=4,
                           font=("나눔바른펜", 15, "bold"), bg=BGCOLOR5, fg="white")

    question_label.pack(pady=20)
    buttons = []
    for i in range(4):
        btn = Button(win, text="{i}번", width=35, height=2, font=("나눔바른펜", 15, "bold"),
                     bg=BGCOLOR1, command=lambda idx=i: check_answer(idx))
        btn.pack()
        buttons.append(btn)

    next_btn = Button(win, text="다음문제", width=15, height=2,
                      command=next_question,
                      font=("나눔바른펜", 15, "bold"), bg=TKWKCOLOR3)
    next_btn.pack(pady=30)
    akwglsrottn5 = Label(win, text="맞힌 개수:" + str(score), font=("나눔바른펜", 15, "bold"), width=15, height=2,
                                 bg=BGCOLOR4, bd=4,
                                 fg='white')
    akwglsrottn6 = Label(win, text="틀린 개수:" + str(m_score), font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR4,
                         fg='white', bd=4)

    exit_btn = Button(win, text="종료하기", width=15, height=2, command=skrkrl, bg=BGCOLOR5)
    hint = Button(win, text="힌트", width=15, height=2, command=hint, bg=BGCOLOR5)
    next_question()
    exit_btn.pack(side='left')
    hint.pack(side='right')
    akwglsrottn5.pack()
    akwglsrottn6.pack()


def hint00():
    msgbox.showinfo("힌트", "이 문제의 힌트는 (     )입니다")


##게임 1 2 3 새창함수

photo = PhotoImage(file="tpwhd.png", ).subsample(2)

sg = tk.Label(frame1, image=photo, anchor='e')
sg.pack()
sg.config(padx=50, pady=50, bg=BGCOLOR4)

game2_btn = Button(frame1, text="속담\n퀴즈풀기", command=game2, bg=button1, width=10, height=3)
game2_btn.place(x=80, y=335)
game3_btn = Button(frame1, text="사자성어\n퀴즈풀기", command=game3, bg=button1, width=10, height=3)
game3_btn.place(x=220, y=335)
sssg = tk.LabelFrame(frame1, text="퀴즈 규칙", foreground="BLUE", width=385, height=400)
sg0014 = tk.Label(sssg, text="퀴즈는 속담, 사자성어 2개로 구성", fg='red', font=("나눔바른펜", 12, "bold"))
sg0001 = tk.Label(sssg, text="1. 퀴즈는 4지선다형이며, 랜덤한 10문제로 구성되어\n있어 풀때마다 새로운 문제가 등장한다.", font=
("나눔바른펜", 12, "bold"), )
sg0002 = tk.Label(sssg, text="2. 답을 클릭하여 문제를 맞추거나 틀리면 다음 문제\n로 넘어간다.", font=
("나눔바른펜", 12, "bold"), )
sg0003 = tk.Label(sssg, text="3. 답을 모를 경우 아래 힌트 버튼을 클릭하여 문제에\n 대한 힌트를 제공 받을 수 있다.", font=
("나눔바른펜", 12, "bold"), )
sg0004 = tk.Label(sssg, text="4. 게임 상단에는 남은 문제가 표시되고, 아래에는 \n맞은 개수와 틀린 개수를 확인 할 수 있다.", font=
("나눔바른펜", 12, "bold"), )
sg0005 = tk.Label(sssg, text="5. 문제를 푸는 도중에 정답을 모르겠으면 다음 문제\n 버튼을 클릭하여 넘어 갈 수 있다.", font=
("나눔바른펜", 12, "bold"), )
sg0006 = tk.Label(sssg, text="6. 퀴즈는 10문제를 다 풀면 종료 되면서 점수를 \n알려줍니다.", font=
("나눔바른펜", 12, "bold"), )

sssg.place(x=15, y=400)
sg0014.grid(row=0, column=0)
sg0001.grid(row=1, column=0)
sg0002.grid(row=2, column=0)
sg0003.grid(row=3, column=0)
sg0004.grid(row=4, column=0)
sg0005.grid(row=5, column=0)
sg0006.grid(row=6, column=0)
wjatnqhrl = Button(frame1, text='점수보기', width=15, height=2, command=scoree, bg=button1)
wjatnqhrl.place(x=35, y=730)
glsxmqhrl = Button(frame1, text='힌트보기', width=15, height=2, command=hint00, bg=button1)
glsxmqhrl.place(x=255, y=730)

#########################################
tneh1list = [] ##수도게임
def grammarQuizGame():
    with open("tneh1.csv", "r", encoding="UTF-8-sig") as file:
        grammarr = list(csv.reader(file))

    tneh1list.clear()
    global grammar
    def grammar_next():
        global grammaranswer
        global grammar_choice
        global grammar
        global tnehekq
        global grammar4
        for i in range(2):
            buttons[i].config(bg=TNEHCOLOR2)

        grammar_choice = random.choice(grammarr)
        grammar = grammar_choice[0]
        grammar1 = grammar_choice[1]
        grammar2 = grammar_choice[2]

        tnehekq = grammar_choice[6]
        grammaranswer = grammar_choice[3]
        if grammaranswer == '1':
            grammaranswer = 0
            print(grammaranswer)
        elif grammaranswer == '2':
            grammaranswer = 1
            print(grammaranswer)
        question_label.config(text=grammar)
        question_label.config(wraplength=400)
        btn.config(text=grammar1)
        btn.config(text=grammar2)
        #
        #
        for i in range(2):
            buttons[i].config(text=grammar_choice[1 + i])

    def hint():
        global tnehekq
        try:
            msgbox.showinfo("힌트", f"{tnehekq}")
        except NameError:
            msgbox.showinfo("힌트", f"{grammar_choice[6]}")
    def grammaranswer():
        global grammaranswer

        grammaranswer = grammar_choice[3]
        if grammaranswer == '1':
            grammaranswer = 0
            print(grammaranswer)
        elif grammaranswer == '2':
            grammaranswer = 1
            print(grammaranswer)

    def check_answer(idx):
        global score
        global m_score
        global count
        global grammar
        global lastanswp
        global tnehekq
        global grammaranswer
        idx = int(idx)
        if grammaranswer == idx:
            buttons[idx].config(bg=Choicecolor)
            win.after(1000, grammar_next)
            score = score + 1
            count = count + 1
            lastanswp = lastanswp -1
            akwglsrottn1.config(text="맞힌 개수:" + str(score))
            akwglsrottn2.config(text="틀린 개수:" + str(m_score))
            skajwl1.config(text="남은 개수:"+ str(lastanswp))
            if count == 10:
                win1 = Tk()
                win1.title("결과창")
                win1.geometry("300x500")
                win1.config(bg=BGCOLOR1)
                result1 = Label(win1, text="맞은 개수 " + str(score)+"개",highlightcolor='blue', highlightthickness=4,font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR1,bd=4,
                    fg='white')
                result1.pack(pady=10)
                result2 = Label(win1, text="틀린 개수 " + str(m_score)+"개",highlightcolor='blue', highlightthickness=4,font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR1,bd=4,
                    fg='white')
                xmfflsahdma = Label(win1, text="틀린 문제",font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR1,bd=4,
                    fg='white')
                result2.pack(pady=10)
                xmfflsahdma.pack(pady=5)
                result3 = Label(win1, text=str(tneh1list), wraplength=220,highlightcolor='blue', highlightthickness=4,font=("나눔바른펜", 10, "bold"),  bg=BGCOLOR1,bd=4,
                    fg='white')
                result3.pack(pady=10)
                skrkwk = Button(win1, text="종료" , command=win1.destroy,width=10, height=3)
                skrkwk.place(x=120, y=440)
                lastanswp = 10
                count = 0
                m_score = 0
                score = 0
                win.destroy()
        else:
            msgbox.showinfo("떙", "틀렸습니다")
            tneh1list.append(grammar)
            print(grammar)
            buttons[idx].config(bg=ChoicecolorX)
            win.after(1000, grammar_next)
            m_score = m_score + 1
            count = count + 1
            lastanswp = lastanswp - 1
            akwglsrottn1.config(text="맞은 개수:" + str(score))
            akwglsrottn2.config(text="틀린 개수:" + str(m_score))
            skajwl1.config(text="남은 개수:"  + str(lastanswp))
            print(count)
            if count == 10:
                win1 = Tk()
                win1.title("결과창")
                win1.geometry("300x500")
                win1.config(bg=BGCOLOR1)
                result1 = Label(win1, text="맞은 개수는 "+str(score)+"개" ,highlightcolor='blue', highlightthickness=4,font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR1,bd=4,
                    fg='white')
                result1.pack(pady=10)
                result2 = Label(win1, text="틀린 개수는 "+str(m_score)+"개" ,highlightcolor='blue', highlightthickness=4,font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR1,bd=4,
                    fg='white')
                xmfflsahdma = Label(win1, text="틀린 문제",font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR1,bd=4,
                    fg='white')
                result2.pack(pady=10)
                xmfflsahdma.pack(pady=5)
                result3 = Label(win1, text=str(tneh1list),wraplength=220,highlightcolor='blue', highlightthickness=4,font=("나눔바른펜", 10, "bold"), bg=BGCOLOR1,bd=4,
                    fg='white' )
                result3.pack(pady=10)
                skrkwk = Button(win1, text="종료" , command=win1.destroy,width=10, height=3,bg=NEXTBUTTON1)
                skrkwk.place(x=120, y=440)
                count = 0
                m_score = 0
                score = 0
                lastanswp = 10
                win.destroy()


    def skrkrl():
        global score
        global m_score
        global count
        global lastanswp
        count = 0
        m_score = 0
        score = 0
        lastanswp = 10
        win.destroy()

    grammar_choice = random.choice(grammarr)
    grammaranswer()
    tnehekq = grammar_choice[6]
    grammar = grammar_choice[0]
    win = Tk()
    win.iconbitmap('ico/tneh1.ico')
    win.title("수도 ox퀴즈")
    win.resizable(False, False)
    win.config(padx=30, pady=10, bg=BGCOLOR1)
    skajwl1 = Label(win, text="남은 개수" + str(lastanswp), font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR1,bd=4,
                    fg='white')
    skajwl1.pack(anchor='se')
    question_label = Label(win, width=40, height=3, text=grammar, highlightcolor='blue', highlightthickness=4,
                           font=("나눔바른펜", 15, "bold"), bg=BGCOLOR2, fg="white")
    question_label.pack(pady=20)
    ##
    buttons = []
    for i in range(2):
        btn = Button(win, text=grammar_choice[1 + i], width=15, height=5, font=("나눔바른펜", 15, "bold"),
        fg = 'white', bg=TNEHCOLOR2, command=lambda idx=i: check_answer(idx))

        btn.pack(pady=20)
        buttons.append(btn)
    root = Frame(win)
    root.pack()
    next_btn = Button(win, text="다음문제", width=15, height=2, bg=NEXTBUTTON1,
                      command=grammar_next,
                      font=("나눔바른펜", 15, "bold"), )
    next_btn.pack(pady=30)
    akwglsrottn1 = Label(win, text="맞힌 개수:" + str(score), font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=BGCOLOR1,bd=4,
                         fg='white')
    akwglsrottn2 = Label(win, text="틀린 개수:" + str(m_score),font=("나눔바른펜", 15, "bold"), width=15, height=2,bg=BGCOLOR1,fg='white',bd=4)
    exit_btn = Button(win, text="종료하기", width=15, height=2, command=skrkrl, bg=HINT1)
    hint = Button(win, text="힌트", width=15, height=2, bg=HINT1, command=hint)
    exit_btn.pack(side='left')
    hint.pack(side='right')
    akwglsrottn1.pack()
    akwglsrottn2.pack()



knowledgelist=[]
def knowledgeQuizGame():
    with open("wekorean.csv", "r", encoding="UTF-8-sig") as file:
        knowledgee = list(csv.reader(file))
    knowledgelist.clear()
    global knowledge
    def knowledge_next():
        global knowledgeanswer
        global knowledge
        global knowledge4
        for i in range(2):
            buttons[i].config(bg=TKDTLRCOLOR3)

        knowledge_choice = random.choice(knowledgee)
        knowledge = knowledge_choice[0]
        knowledge1 = knowledge_choice[1]
        knowledge2 = knowledge_choice[2]
        knowledge4 = knowledge_choice[4]
        knowledgeanswer = knowledge_choice[3]
        if knowledgeanswer == '1':
            knowledgeanswer = 0
            print(knowledgeanswer)
        elif knowledgeanswer == '2':
            knowledgeanswer = 1
            print(knowledgeanswer)
        question_label.config(text=knowledge)
        question_label.config(wraplength=400)
        btn.config(text=knowledge1)
        btn.config(text=knowledge2)

        for i in range(2):
            buttons[i].config(text=knowledge_choice[1 + i])

    def knowledgeanswer():
        global knowledgeanswer
        knowledgeanswer = knowledge_choice[3]
        if knowledgeanswer == '1':
            knowledgeanswer = 0
            print(knowledgeanswer)
        elif knowledgeanswer == '2':
            knowledgeanswer = 1
            print(knowledgeanswer)

    def check_answer(idx):
        global lastanswp
        global knowledge
        global score
        global m_score
        global count
        idx = int(idx)
        global knowledgeanswer
        if knowledgeanswer == idx:
            buttons[idx].config(bg=Choicecolor)
            win.after(1000, knowledge_next)
            score = score + 1
            count = count + 1
            lastanswp = lastanswp -1
            akwglsrottn8.config(text="맞힌 개수:" + str(score))
            akwglsrottn9.config(text="틀린 개수:" + str(m_score))
            skajwl8.config(text="남은 개수:"+ str(lastanswp))
            if count == 10:
                win1 = Tk()
                win1.title("결과창")
                win1.geometry("300x500")
                win1.config(bg=TKDTLRCOLOR2)
                result1 = Label(win1, text="맞은 개수 " + str(score) + "개", highlightcolor='blue', highlightthickness=4,
                                font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=TKDTLRCOLOR2, bd=4,
                                fg='white')
                result1.pack(pady=10)
                result2 = Label(win1, text="틀린 개수 " + str(m_score) + "개", highlightcolor='blue', highlightthickness=4,
                                font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=TKDTLRCOLOR2, bd=4,
                                fg='white')
                xmfflsahdma = Label(win1, text="틀린 문제", font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=TKDTLRCOLOR2,
                                    bd=4,
                                    fg='white')
                result2.pack(pady=10)
                xmfflsahdma.pack(pady=5)
                result3 = Label(win1, text=str(knowledgelist), wraplength=220, highlightcolor='blue', highlightthickness=4,
                                font=("나눔바른펜", 10, "bold"), bg=TKDTLRCOLOR2, bd=4,
                                fg='white')
                result3.pack(pady=10)
                skrkwk = Button(win1, text="종료", command=win1.destroy, width=10, height=3,bg=NEXTBUTTON1)
                skrkwk.place(x=120, y=440)
                count = 0
                m_score = 0
                score = 0
                lastanswp = 10
                win.destroy()

        else:
            msgbox.showinfo("떙", "틀렸습니다")
            print(knowledge)
            knowledgelist.append(knowledge)
            buttons[idx].config(bg=ChoicecolorX)
            win.after(1000, knowledge_next)
            m_score = m_score + 1
            count = count + 1
            lastanswp = lastanswp - 1
            akwglsrottn8.config(text="맞은 개수:" + str(score))
            akwglsrottn9.config(text="틀린 개수:" + str(m_score))
            skajwl8.config(text="남은 개수:"  + str(lastanswp))
            print(count)
            if count == 10:
                win1 = Tk()
                win1.title("결과창")
                win1.geometry("300x500")
                win1.config(bg=TKDTLRCOLOR2)
                result1 = Label(win1, text="맞은 개수는 " + str(score) + "개", highlightcolor='blue', highlightthickness=4,
                                font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=TKDTLRCOLOR2, bd=4,
                                fg='white')
                result1.pack(pady=10)
                result2 = Label(win1, text="틀린 개수는 " + str(m_score) + "개", highlightcolor='blue', highlightthickness=4,
                                font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=TKDTLRCOLOR2, bd=4,
                                fg='white')
                xmfflsahdma = Label(win1, text="틀린 문제", font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=TKDTLRCOLOR2,
                                    bd=4,
                                    fg='white')
                result2.pack(pady=10)
                xmfflsahdma.pack(pady=5)
                result3 = Label(win1, text=str(knowledgelist), wraplength=220, highlightcolor='blue', highlightthickness=4,
                                font=("나눔바른펜", 10, "bold"), bg=TKDTLRCOLOR2, bd=4,
                                fg='white')
                result3.pack(pady=10)
                skrkwk = Button(win1, text="종료", command=win1.destroy, width=10, height=3, bg=NEXTBUTTON1)
                skrkwk.place(x=120, y=440)
                count = 0
                m_score = 0
                score = 0
                lastanswp = 10
                win.destroy()

    def hint():
        global knowledge4
        try:
            msgbox.showinfo("힌트", f"{knowledge4}입니다")
        except NameError:
            msgbox.showinfo("힌트", f"{knowledge_choice[4]}")
    knowledge_choice = random.choice(knowledgee)
    knowledgeanswer()
    knowledge = knowledge_choice[0]
    win = Tk()
    win.iconbitmap('ico/tkdtlr.ico')
    win.title("상식 ox퀴즈")
    win.resizable(False, False)
    win.config(padx=30, pady=10, bg=TKDTLRCOLOR2)
    skajwl8 = Label(win, text="남은 개수" + str(lastanswp), font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=TKDTLRCOLOR2,bd=4,
                    fg='white')
    skajwl8.pack(anchor='se')
    question_label = Label(win, width=40, height=3, text=knowledge, highlightcolor='blue', highlightthickness=4,
                           font=("나눔바른펜", 15, "bold"), bg=TKDTLRCOLOR1, fg="white")
    question_label.pack(pady=20)
    ##
    buttons = []
    for i in range(2):
        btn = Button(win, text=knowledge_choice[1 + i], width=15, height=5, font=("나눔바른펜", 15, "bold"),
                     bg=TKDTLRCOLOR3, command=lambda idx=i: check_answer(idx), fg=TEXT_COLOR)

        btn.pack(pady=20)
        buttons.append(btn)

    ##
    root = Frame(win)
    root.pack()
    next_btn = Button(win, text="다음문제", width=15, height=2, bg=TKDTLRCOLOR4,
                      command=knowledge_next,
                      font=("나눔바른펜", 15, "bold"), )
    next_btn.pack(pady=30)
    akwglsrottn8 = Label(win, text="맞힌 개수:" + str(score), font=("나눔바른펜", 15, "bold"), width=15, height=2, bg=TKDTLRCOLOR2,bd=4,
                         fg='white')
    akwglsrottn9 = Label(win, text="틀린 개수:" + str(m_score),font=("나눔바른펜", 15, "bold"), width=15, height=2,bg=TKDTLRCOLOR2,fg='white',bd=4)
    exit_btn = Button(win, text="종료하기", width=15, height=2, command=win.destroy, bg=HINT1)
    hint = Button(win, text="힌트", width=15, height=2, bg=HINT1, command=hint)
    exit_btn.pack(side='left')
    hint.pack(side='right')
    akwglsrottn8.pack()
    akwglsrottn9.pack()


frame2 = tk.Frame(win)
notebook.add(frame2, text="OX 퀴즈")
oxox = PhotoImage(file="oxox.png", ).subsample(1)
oxoxsg = tk.Label(frame2, image=oxox)
oxoxsg.pack()
grammarquiz = Button(frame2, command=grammarQuizGame, text="수도\nOX풀기", width=10, height=3, bg=BGCOLOR3)
grammarquiz.place(x=80, y=345)

tkdtlrquiz = Button(frame2, command=knowledgeQuizGame, text="상식\nOX풀기", width=10, height=3, bg=BGCOLOR3)
tkdtlrquiz.place(x=240, y=345)
quizrbclr = tk.LabelFrame(frame2, text="퀴즈 규칙", foreground="BLUE", width=385, height=400)
sg0013 = tk.Label(quizrbclr, text="퀴즈는 속담 , 상식 2개로 구성", fg='red', font=
("나눔바른펜", 12, "bold"))
sg0007 = tk.Label(quizrbclr, text="1. 퀴즈는 O X 퀴즈이며, 랜덤한 10문제로 구성되어\n있어 풀 때 마다 새로운 문제가 등장한다.", font=
("나눔바른펜", 12, "bold"), )
sg0008 = tk.Label(quizrbclr, text="2. 답을 클릭하여 문제를 맞추거나 틀리면 다음 문제\n로 넘어간다. ", font=
("나눔바른펜", 12, "bold"), )
sg0009 = tk.Label(quizrbclr, text="3. 답을 모를 경우 아래 힌트 버튼을 클릭하여 문제에\n 대한 힌트를 제공 받을 수 있다.", font=
("나눔바른펜", 12, "bold"), )
sg0010 = tk.Label(quizrbclr, text="4. 게임 상단에는 남은 문제가 표시되고, 아래에는 \n맞은 개수와 틀린 개수를 확인 할 수 있다.", font=
("나눔바른펜", 12, "bold"), )
sg0011 = tk.Label(quizrbclr, text="5. 문제를 푸는 도중에 정답을 모르겠으면 다음 문제\n 버튼을 클릭하여 넘어 갈 수 있다.", font=
("나눔바른펜", 12, "bold"), )
sg0012 = tk.Label(quizrbclr, text="6. 퀴즈는 10문제를 다 풀면 종료 되면서 점수를 \n알려줍니다.", font=
("나눔바른펜", 12, "bold"), )
quizrbclr.place(x=15, y=400)

##
sg0013.grid(row=0, column=0)
sg0007.grid(row=1, column=0)
sg0008.grid(row=2, column=0)
sg0009.grid(row=3, column=0)
sg0010.grid(row=4, column=0)
sg0011.grid(row=5, column=0)
sg0012.grid(row=6, column=0)
oxwjatn = Button(frame2, text='점수보기', width=15, height=2, command=scoree, bg=BGCOLOR3)
oxwjatn.place(x=35, y=730)
oxglsxm = Button(frame2, text='힌트보기', width=15, height=2, command=hint00, bg=BGCOLOR3)
oxglsxm.place(x=255, y=730)

###############
frame3 = tk.Frame(win)
notebook.add(frame3, text="속담")
with open("threka.csv", "r", encoding="UTF-8-sig") as file:
    wethreka = list(csv.reader(file))
threkaData = wethreka
del(threkaData[-1])
threkalist =[]
for x in list(range(0,len(threkaData))):
    threkalist.append(threkaData[x][1])

def rkwudhrl1():
    dkssud5.config(text=str(ekqekq1), )
    dkssud5.config(wraplength=150, )


print(list)
varssv =StringVar(value= threkalist)
threkalistboxsg = Listbox(frame3, listvariable = varssv, width=30)
threkalistboxsg.place(x=15 , y=20)
dkssud11 = LabelFrame(frame3, text="틀린 문제")
dkssud11.place(x=240 , y=10)
dkssud5 = Label(dkssud11, text="문제를 풀고 와주세요",)
dkssud5.grid()
dkssud6 = Button(dkssud11, text="틀린 문제 가져오기",command=rkwudhrl1,bg=BGCOLOR2)
dkssud6.grid()
def threkaupdate1():
    try:
        threkaindex = threkalistboxsg.curselection()[0]
        brandlabel2sg.config(text=threkaData[threkaindex][1])
        stock2sg.config(text=threkaData[threkaindex][0])
        country2sg.config(text=threkaData[threkaindex][2])
        country2sg.config(wraplength=350)
        if threkaindex == 0:
            wall_label.configure(image=wall[0])
        elif threkaindex == 1:
            wall_label.configure(image=wall[1])
        elif threkaindex == 2:
            wall_label.configure(image=wall[2])
        elif threkaindex == 3:
            wall_label.configure(image=wall[3])
        elif threkaindex == 4:
            wall_label.configure(image=wall[4])
        elif threkaindex == 5:
            wall_label.configure(image=wall[5])
        elif threkaindex == 6:
            wall_label.configure(image=wall[6])
        elif threkaindex == 7:
            wall_label.configure(image=wall[7])
        elif threkaindex == 8:
            wall_label.configure(image=wall[8])
        elif threkaindex == 9:
            wall_label.configure(image=wall[9])
        elif threkaindex == 10:
            wall_label.configure(image=wall[10])
        elif threkaindex == 11:
            wall_label.configure(image=wall[11])
        elif threkaindex == 12:
            wall_label.configure(image=wall[12])
        elif threkaindex == 13:
            wall_label.configure(image=wall[13])
        elif threkaindex == 14:
            wall_label.configure(image=wall[14])
        elif threkaindex == 15:
            wall_label.configure(image=wall[15])
        elif threkaindex == 16:
            wall_label.configure(image=wall[16])
        elif threkaindex == 17:
            wall_label.configure(image=wall[17])
        elif threkaindex == 18:
            wall_label.configure(image=wall[18])
        elif threkaindex == 19:
            wall_label.configure(image=wall[19])
        elif threkaindex == 20:
            wall_label.configure(image=wall[20])
        elif threkaindex == 21:
            wall_label.configure(image=wall[21])
        elif threkaindex == 22:
            wall_label.configure(image=wall[22])
        elif threkaindex == 23:
            wall_label.configure(image=wall[23])
        elif threkaindex == 24:
            wall_label.configure(image=wall[24])
        elif threkaindex == 25:
            wall_label.configure(image=wall[25])
        elif threkaindex == 26:
            wall_label.configure(image=wall[26])
        elif threkaindex == 27:
            wall_label.configure(image=wall[27])
        elif threkaindex == 28:
            wall_label.configure(image=wall[28])
        elif threkaindex == 29:
            wall_label.configure(image=wall[29])
        elif threkaindex == 30:
            wall_label.configure(image=wall[30])
        elif threkaindex == 31:
            wall_label.configure(image=wall[31])
        elif threkaindex == 32:
            wall_label.configure(image=wall[32])
        elif threkaindex == 33:
            wall_label.configure(image=wall[33])
        elif threkaindex == 34:
            wall_label.configure(image=wall[34])
        elif threkaindex == 35:
            wall_label.configure(image=wall[35])
        elif threkaindex == 36:
            wall_label.configure(image=wall[36])
        elif threkaindex == 37:
            wall_label.configure(image=wall[37])
        elif threkaindex == 38:
            wall_label.configure(image=wall[38])
        elif threkaindex == 39:
            wall_label.configure(image=wall[39])
        print(threkaindex)
    except IndexError:
        msgbox.showwarning("경고", "속담을 선택하지 않았습니다")

wall = [PhotoImage(file="threkatkwls/threka61.png"),PhotoImage(file="threkatkwls/threka62.png"),PhotoImage(file="threkatkwls/threka63.png"),PhotoImage(file="threkatkwls/threka64.png")
        ,PhotoImage(file="threkatkwls/threka65.png"),PhotoImage(file="threkatkwls/threka66.png"),PhotoImage(file="threkatkwls/threka67.png"),PhotoImage(file="threkatkwls/threka68.png")
        ,PhotoImage(file="threkatkwls/threka69.png"),PhotoImage(file="threkatkwls/threka70.png"),PhotoImage(file="threkatkwls/threka71.png"),PhotoImage(file="threkatkwls/threka72.png")
        ,PhotoImage(file="threkatkwls/threka73.png"),PhotoImage(file="threkatkwls/threka74.png"),PhotoImage(file="threkatkwls/threka75.png"),PhotoImage(file="threkatkwls/threka76.png")
        ,PhotoImage(file="threkatkwls/threka77.png"),PhotoImage(file="threkatkwls/threka78.png"),PhotoImage(file="threkatkwls/threka79.png"),PhotoImage(file="threkatkwls/threka80.png")
        ,PhotoImage(file="threkatkwls/threka81.png"),PhotoImage(file="threkatkwls/threka82.png"),PhotoImage(file="threkatkwls/threka83.png"),PhotoImage(file="threkatkwls/threka84.png")
        ,PhotoImage(file="threkatkwls/threka85.png"),PhotoImage(file="threkatkwls/threka86.png"),PhotoImage(file="threkatkwls/threka87.png"),PhotoImage(file="threkatkwls/threka88.png")
        ,PhotoImage(file="threkatkwls/threka89.png"),PhotoImage(file="threkatkwls/threka90.png"),PhotoImage(file="threkatkwls/threka91.png"),PhotoImage(file="threkatkwls/threka92.png")
        ,PhotoImage(file="threkatkwls/threka93.png"), PhotoImage(file="threkatkwls/threka94.png"), PhotoImage(file="threkatkwls/threka95.png"), PhotoImage(file="threkatkwls/threka96.png")
        ,PhotoImage(file="threkatkwls/threka97.png"), PhotoImage(file="threkatkwls/threka98.png"), PhotoImage(file="threkatkwls/threka99.png"), PhotoImage(file="threkatkwls/threka100.png")]


segyo= LabelFrame(frame3, text="공부", width=50, height=20, bd=4, bg='lightgreen',)
segyo.place(x=20, y=260)
button1sg = Button(frame3,text= "설명보기" , command= threkaupdate1,width=10, height=2, bg=BGCOLOR2)
button1sg.place(x=75,y=200)

brandlabelsg = Label(segyo, text="속담", font=("나눔바른펜", 10, "bold"), bg='lightgreen',fg="red")
brandlabelsg.grid(row=1, column=0,)
stocksg = Label(segyo, text="뜻", font=("나눔바른펜", 10, "bold"), bg='lightgreen',fg="red")
stocksg.grid(row=3, column=0,)
countrysg = Label(segyo, text="예제", font=("나눔바른펜", 10, "bold"), bg='lightgreen',fg="red")
countrysg.grid(row=5, column=0,)


brandlabel2sg = Label(segyo, text="ex) 아는만큼 보인다 ", font=("나눔바른펜", 10, "bold"), bg='lightgreen')
brandlabel2sg.grid(row=2, column=0, )
stock2sg = Label(segyo, text="ex) 아는 것이 많을 수록 보이는 것도 많다", font=("나눔바른펜", 10, "bold"), bg='lightgreen')
stock2sg.grid(row=4, column=0, )
country2sg = Label(segyo, text="ex) 아는 것이 많을수록 새로운 생각과 지혜도 많아진다", font=("나눔바른펜", 10, "bold"), bg='lightgreen')
country2sg.grid(row=6, column=0, )
wall_frame= LabelFrame(frame3, text="사진 설명",width=100,height=100)
wall_frame.place(x=20, y=445)
threkadPwp = PhotoImage(file="threkatkwls/threkarhdqn.png", )
wall_label = Label(wall_frame,image=threkadPwp )
wall_label.grid()
##


###
frame4 = tk.Frame(win)
notebook.add(frame4, text="사자성어")

with open("4ja.csv", "r", encoding="UTF-8-sig") as file:
    dustmqanswp = list(csv.reader(file))
tkwkData = dustmqanswp
del (tkwkData[-1])
tnehlist = []
for x in list(range(0, len(tkwkData))):
    tnehlist.append(tkwkData[x][0])
def rkwudhrl():
    dkssud2.config(text=str(ekqekq2))
    dkssud2.config(wraplength=220)
print(list)
var1 = StringVar(value=str(tnehlist))
scrollbar = Scrollbar(frame4,)
scrollbar.place(x=190, y=20)
listbox1 = Listbox(frame4, listvariable=var1, selectbackground=BGCOLOR1, bd=4, bg="white")
listbox1.place(x=30 , y=20)
listbox1.config(yscrollcommand=scrollbar.set)
dkssud = LabelFrame(frame4, text="틀린 문제")
dkssud.place(x=230 , y=10)
dkssud2 = Label(dkssud, text="문제를 풀고 와주세요",)
dkssud2.grid()
dkssud1 = Button(dkssud, text="틀린 문제 가져오기",command=rkwudhrl ,bg=BGCOLOR2)
dkssud1.grid()
listbox1.config(yscrollcommand=scrollbar.set)



def update():
    try:
        index = listbox1.curselection()[0]
        brandlabel2.config(text=tkwkData[index][0])
        stock2.config(text=tkwkData[index][1])
        country2.config(text=tkwkData[index][2])
        if index == 0:
            wall1_label1.configure(image=wall1[0])
        elif index == 1:
            wall1_label1.configure(image=wall1[1])
        elif index == 2:
            wall1_label1.configure(image=wall1[2])
        elif index == 3:
            wall1_label1.configure(image=wall1[3])
        elif index == 4:
            wall1_label1.configure(image=wall1[4])
        elif index == 5:
            wall1_label1.configure(image=wall1[5])
        elif index == 6:
            wall1_label1.configure(image=wall1[6])
        elif index == 7:
            wall1_label1.configure(image=wall1[7])
        elif index == 8:
            wall1_label1.configure(image=wall1[8])
        elif index == 9:
            wall1_label1.configure(image=wall1[9])
        elif index == 10:
            wall1_label1.configure(image=wall1[10])
        elif index == 11:
            wall1_label1.configure(image=wall1[11])
        elif index == 12:
            wall1_label1.configure(image=wall1[12])
        elif index == 13:
            wall1_label1.configure(image=wall1[13])
        elif index == 14:
            wall1_label1.configure(image=wall1[14])
        elif index == 15:
            wall1_label1.configure(image=wall1[15])
        elif index == 16:
            wall1_label1.configure(image=wall1[16])
        elif index == 17:
            wall1_label1.configure(image=wall1[17])
        elif index == 18:
            wall1_label1.configure(image=wall1[18])
        elif index == 19:
            wall1_label1.configure(image=wall1[19])
        elif index == 20:
            wall1_label1.configure(image=wall1[20])
        elif index == 21:
            wall1_label1.configure(image=wall1[21])
        elif index == 22:
            wall1_label1.configure(image=wall1[22])
        elif index == 23:
            wall1_label1.configure(image=wall1[23])
        elif index == 24:
            wall1_label1.configure(image=wall1[24])
        elif index == 25:
            wall1_label1.configure(image=wall1[25])
        elif index == 26:
            wall1_label1.configure(image=wall1[26])
        elif index == 27:
            wall1_label1.configure(image=wall1[27])
        elif index == 28:
            wall1_label1.configure(image=wall1[28])
        elif index == 29:
            wall1_label1.configure(image=wall1[29])
        elif index == 30:
            wall1_label1.configure(image=wall1[30])
        elif index == 31:
            wall1_label1.configure(image=wall1[31])
        elif index == 32:
            wall1_label1.configure(image=wall1[32])
        elif index == 33:
            wall1_label1.configure(image=wall1[33])
        elif index == 34:
            wall1_label1.configure(image=wall1[34])
        elif index == 35:
            wall1_label1.configure(image=wall1[35])
        elif index == 36:
            wall1_label1.configure(image=wall1[36])
        elif index == 37:
            wall1_label1.configure(image=wall1[37])
        elif index == 38:
            wall1_label1.configure(image=wall1[38])
        elif index == 39:
            wall1_label1.configure(image=wall1[39])
        elif index == 40:
            wall1_label1.configure(image=wall1[40])
        elif index == 41:
            wall1_label1.configure(image=wall1[41])
        elif index == 42:
            wall1_label1.configure(image=wall1[42])
        elif index == 43:
            wall1_label1.configure(image=wall1[43])
        elif index == 44:
            wall1_label1.configure(image=wall1[44])
        elif index == 45:
            wall1_label1.configure(image=wall1[45])
        elif index == 46:
            wall1_label1.configure(image=wall1[46])
        elif index == 47:
            wall1_label1.configure(image=wall1[47])
        elif index == 48:
            wall1_label1.configure(image=wall1[48])
        elif index == 49:
            wall1_label1.configure(image=wall1[49])
        elif index == 50:
            wall1_label1.configure(image=wall1[50])
        elif index == 51:
            wall1_label1.configure(image=wall1[51])
        elif index == 52:
            wall1_label1.configure(image=wall1[52])
        elif index == 53:
            wall1_label1.configure(image=wall1[53])
        elif index == 54:
            wall1_label1.configure(image=wall1[54])
        elif index == 55:
            wall1_label1.configure(image=wall1[55])
        elif index == 56:
            wall1_label1.configure(image=wall1[56])
        print(index)
    except IndexError:
        msgbox.showwarning("경고", "사자성어를 선택을 하지 않았습니다")

# frame4.config(bg=BGCOLOR1)
seg = LabelFrame(frame4, text="공부", width=50, height=20, bd=4, bg='lightgreen', )
seg.place(x=30, y=260)
button1 = Button(frame4, text="설명 보기", command=update, width=10, height=2, bg=BGCOLOR2)
button1.place(x=75,y=200)
wall1 = [PhotoImage(file="4wk/tkwk0.png"),PhotoImage(file="4wk/tkwk1.png"),PhotoImage(file="4wk/tkwk2.png"),PhotoImage(file="4wk/tkwk3.png")
        ,PhotoImage(file="4wk/tkwk4.png"),PhotoImage(file="4wk/tkwk5.png"),PhotoImage(file="4wk/tkwk6.png"),PhotoImage(file="4wk/tkwk7.png")
        ,PhotoImage(file="4wk/tkwk8.png"),PhotoImage(file="4wk/tkwk9.png"),PhotoImage(file="4wk/tkwk10.png"),PhotoImage(file="4wk/tkwk11.png")
        ,PhotoImage(file="4wk/tkwk12.png"),PhotoImage(file="4wk/tkwk13.png"),PhotoImage(file="4wk/tkwk14.png"),PhotoImage(file="4wk/tkwk15.png")
        ,PhotoImage(file="4wk/tkwk16.png"),PhotoImage(file="4wk/tkwk17.png"),PhotoImage(file="4wk/tkwk18.png"),PhotoImage(file="4wk/tkwk19.png")
        ,PhotoImage(file="4wk/tkwk20.png"),PhotoImage(file="4wk/tkwk21.png"),PhotoImage(file="4wk/tkwk22.png"),PhotoImage(file="4wk/tkwk23.png")
        ,PhotoImage(file="4wk/tkwk24.png"),PhotoImage(file="4wk/tkwk25.png"),PhotoImage(file="4wk/tkwk26.png"),PhotoImage(file="4wk/tkwk27.png")
        ,PhotoImage(file="4wk/tkwk28.png"),PhotoImage(file="4wk/tkwk29.png"),PhotoImage(file="4wk/tkwk30.png"),PhotoImage(file="4wk/tkwk31.png")
        ,PhotoImage(file="4wk/tkwk32.png"), PhotoImage(file="4wk/tkwk33.png"), PhotoImage(file="4wk/tkwk34.png"), PhotoImage(file="4wk/tkwk35.png")
        ,PhotoImage(file="4wk/tkwk36.png"), PhotoImage(file="4wk/tkwk37.png"), PhotoImage(file="4wk/tkwk38.png"), PhotoImage(file="4wk/tkwk39.png")
         ,PhotoImage(file="4wk/tkwk40.png"), PhotoImage(file="4wk/tkwk41.png"), PhotoImage(file="4wk/tkwk42.png"), PhotoImage(file="4wk/tkwk43.png")
         ,PhotoImage(file="4wk/tkwk44.PNG"), PhotoImage(file="4wk/tkwk44.png"), PhotoImage(file="4wk/tkwk46.png"), PhotoImage(file="4wk/tkwk47.png")
         ,PhotoImage(file="4wk/tkwk48.png"), PhotoImage(file="4wk/tkwk49.png"), PhotoImage(file="4wk/tkwk50.png"), PhotoImage(file="4wk/tkwk51.png")
         ,PhotoImage(file="4wk/tkwk52.png"), PhotoImage(file="4wk/tkwk53.png"), PhotoImage(file="4wk/tkwk54.png"), PhotoImage(file="4wk/tkwk55.png")
         , PhotoImage(file="4wk/tkwk56.png")]
brandlabel = Label(seg, text="사자성어 ", font=("나눔바른펜", 10, "bold"), bg='lightgreen', fg="red")
brandlabel.grid(row=1, column=0,)
stock = Label(seg, text="뜻 ", font=("나눔바른펜", 10, "bold"), bg='lightgreen', fg="red")
stock.grid(row=3, column=0, )
country = Label(seg, text="한자 ", font=("나눔바른펜", 10, "bold"), bg='lightgreen', fg="red")
country.grid(row=5, column=0, )


brandlabel2 = Label(seg, text="ex) 박학독지", font=("나눔바른펜", 10, "bold"), bg='lightgreen')
brandlabel2.grid(row=2, column=0, )
stock2 = Label(seg, text="ex) 널리 공부하여 덕을 닦으려고 뜻을 굳건히 함", font=("나눔바른펜", 10, "bold"), bg='lightgreen')
stock2.grid(row=4, column=0, )
country2 = Label(seg, text="ex) 博:넓을 박 學:배울 학 篤:도타울 독 志:뜻 지", font=("나눔바른펜", 10, "bold"), bg='lightgreen')
country2.grid(row=6, column=0, )
# datelabel2 = Label(seg, text="", font=("나눔바른펜", 10, "bold"), bg='lightgreen')
# datelabel2.grid(row=7,column=0)
wall1_frame1= LabelFrame(frame4, text="사진 설명",width=100,height=100)
wall1_frame1.place(x=20, y=445)
threkadPwp1 = PhotoImage(file="tkwktkwk.PNG", )
wall1_label1 = Label(wall1_frame1,image=threkadPwp1 )
wall1_label1.grid()
# datelabel2.grid(row=8, column=0, )
###
frame5 = tk.Frame(win)
notebook.add(frame5, text="수도")
with open("tneh1.csv", "r", encoding="UTF-8-sig") as file:
    tnehdustmq = list(csv.reader(file))
    tnehData = tnehdustmq
    del (tnehData[0])
tnehlist = []
for x in list(range(0, len(tnehData))):
    tnehlist.append(tnehData[x][4])

def rkwudhrl3():
    dkssud3.config(text=str(tneh1list),)
    dkssud3.config(wraplength=210,)
dkssud = LabelFrame(frame5, text="틀린 문제")
dkssud.place(x=170 , y=650)
dkssud3 = Label(dkssud, text="문제를 풀고 와주세요",)
dkssud3.grid()
dkssud4 = Button(dkssud, text="틀린 문제 가져오기",command=rkwudhrl3,bg=BGCOLOR2)
dkssud4.grid()
print(list)
def tnehupdate():
    try:
        tnehindex = tnehlistbox.curselection()[0]
        tnehbrandlabel2sg.config(text=tnehData[tnehindex][4])
        tnehstock2sg.config(text=tnehData[tnehindex][5])
        tnehcountry2sg.config(text=tnehData[tnehindex][6])
        tnehcountry2sg.config(wraplength=200)
        # datelabel2.config(text=tnehData[ttnehindex][3])
        print(tnehindex)
    except IndexError:
        msgbox.showwarning("경고", "수도를 선택하지 않았습니다")

def address():
    map_widget.set_address(my_entry.get())

map_widget = TkinterMapView(frame5, width=100, height=300, corner_radius=0)
map_widget.set_zoom(13)
map_widget.pack(fill="both", padx=5, pady=5)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
                           max_zoom=15)
map_widget.set_address("seoul", marker=True, )

my_entry = Entry(frame5, width=30, bd=4, fg=Choicecolor)
# frame5.config(bg='blue')
my_entry.pack(pady=5, )
my_button = Button(frame5, text="검색", command=address, bg='pink', width=8, height=2)
my_button.pack(pady=5)
tnehvar = StringVar(value=tnehlist)
tnehlistbox = Listbox(frame5, listvariable=tnehvar, width=20, height=15)
tnehlistbox.place(x=10, y=400)

##
tnehsegyo = LabelFrame(frame5, text="수도 설명", width=50, height=20, bd=4, bg='lightgreen', )
tnehsegyo.place(x=170, y=400)
tnehbutton1sg = Button(frame5, text="설명", command=tnehupdate, width=7, height=2, bg=BGCOLOR2)
tnehbutton1sg.place(x=50, y=650)

tnehbrandlabelsg = Label(tnehsegyo, text="나라", font=("나눔바른펜", 10, "bold"), bg='lightgreen', fg="red")
tnehbrandlabelsg.grid(row=1, column=0, )
tnehstocksg = Label(tnehsegyo, text="수도", font=("나눔바른펜", 10, "bold"), bg='lightgreen', fg="red")
tnehstocksg.grid(row=3, column=0, )
tnehcountrysg = Label(tnehsegyo, text="설명", font=("나눔바른펜", 10, "bold"), bg='lightgreen', fg="red")
tnehcountrysg.grid(row=5, column=0, )

tnehbrandlabel2sg = Label(tnehsegyo, text="ex) 대한민국", font=("나눔바른펜", 10, "bold"), bg='lightgreen')
tnehbrandlabel2sg.grid(row=2, column=0, )
tnehstock2sg = Label(tnehsegyo, text="ex) 서울", font=("나눔바른펜", 10, "bold"), bg='lightgreen')
tnehstock2sg.grid(row=4, column=0, )
tnehcountry2sg = Label(tnehsegyo, text="ex) 한반도 중앙에 있다", font=("나눔바른펜", 10, "bold"), bg='lightgreen')
tnehcountry2sg.grid(row=6, column=0, )
##

##
frame6 = tk.Frame(win)
with open("wekorean.csv", "r", encoding="UTF-8-sig") as file:
    dustmqanswp = list(csv.reader(file))
tkdtlrlist =[]
tkdtlrData = dustmqanswp
for x in list(range(0,len(tkdtlrData))):
    tkdtlrlist.append(tkdtlrData[x][0])
notebook.add(frame6, text="상식",)
def next_study():
    global study_num
    study_num +=1
    if study_num >= len(study_list):
        study_num=0
    sutuyy1.config(text=study_list[study_num])
    sutuyy1.config(wraplength=400)
    sutuyy2.config(text=study_list1[study_num])
    sutuyy2.config(wraplength=400)

def pre_study():
    global study_num
    study_num -=1
    if study_num < 0:
        study_num= len(study_list)- 1

    sutuyy1.config(text=study_list[study_num])
    sutuyy1.config(wraplength=400)
    sutuyy2.config(text=study_list1[study_num])
    sutuyy2.config(wraplength=400)

with open("auddjs.csv", "r", encoding="UTF-8-sig") as file:
    auddjs = list(csv.reader(file))
auddjsData = auddjs

def showww1():
    if '우주' in ent1.get()  or '비행' in ent1.get() or '소연' in ent1.get():  # 입력한 값이 정답과 같으면
        lab4.config(text=dustmqanswp[18][4])
        lab4.config(wraplength=200)
    elif 'e' in ent1.get() or 'mail' in ent1.get() or 'el' in ent1.get() or '약자' in ent1.get():
        lab4.config(text=dustmqanswp[1][4])
        lab4.config(wraplength=200)
    elif '섭씨' in ent1.get() or '화씨' in ent1.get() or 'C' in ent1.get() or '온도' in ent1.get() or 'K' in ent1.get():
        lab4.config(text=dustmqanswp[0][4])
        lab4.config(wraplength=250)
    elif '100' in ent1.get() or '동전' in ent1.get() or '인물' in ent1.get() or '광개' in ent1.get():
        lab4.config(text=dustmqanswp[2][4])
        lab4.config(wraplength=200)
    elif '개천절' in ent1.get() or '독립' in ent1.get() or '날' in ent1.get():
        lab4.config(text=dustmqanswp[3][4])
        lab4.config(wraplength=200)
    elif '구기' in ent1.get() or '골프' in ent1.get() or '작은' in ent1.get() or '경기' in ent1.get():
        lab4.config(text=dustmqanswp[4][4])
        lab4.config(wraplength=200)
    elif '낙타' in ent1.get() or '혹' in ent1.get() or '물' in ent1.get() or '차' in ent1.get():
        lab4.config(text=dustmqanswp[5][4])
        lab4.config(wraplength=200)
    elif '남대' in ent1.get() or '흥인' in ent1.get() or '문' in ent1.get():
        lab4.config(text=dustmqanswp[6][4])
        lab4.config(wraplength=200)
    elif '입법' in ent1.get() or '사법' in ent1.get()  or '행정' in ent1.get()or '국가' in ent1.get()or '권력' in ent1.get():
        lab4.config(text=dustmqanswp[7][4])
        lab4.config(wraplength=200)
    elif '달' in ent1.get() or '빛' in ent1.get() or '스스로' in ent1.get():
        lab4.config(text=dustmqanswp[8][4])
        lab4.config(wraplength=200)
    elif '광역' in ent1.get() or '6' in ent1.get():
        lab4.config(text=dustmqanswp[9][4])
        lab4.config(wraplength=200)
    elif '바다' in ent1.get() or '상어' in ent1.get() or '부레' in ent1.get():
        lab4.config(text=dustmqanswp[10][4])
        lab4.config(wraplength=200)
    elif '대륙' in ent1.get() or '아프' in ent1.get() or '여섯' in ent1.get()or '땅' in ent1.get():
        lab4.config(text=dustmqanswp[11][4])
        lab4.config(wraplength=200)
    elif '긴' in ent1.get() or '건축' in ent1.get() or '만리' in ent1.get():
        lab4.config(text=dustmqanswp[12][4])
        lab4.config(wraplength=200)
    elif '소리' in ent1.get() or '측정' in ent1.get() or '단위' in ent1.get()or 'dB' in ent1.get()or '데시' in ent1.get():
        lab4.config(text=dustmqanswp[13][4])
        lab4.config(wraplength=200)
    elif '위' in ent1.get() or '없' in ent1.get() or '사람' in ent1.get():
        lab4.config(text=dustmqanswp[14][4])
        lab4.config(wraplength=200)
    elif '인구' in ent1.get() or '도' in ent1.get() or '제일' in ent1.get():
        lab4.config(text=dustmqanswp[15][4])
        lab4.config(wraplength=200)
    elif '일' in ent1.get() or '오늘' in ent1.get() or '말' in ent1.get():
        lab4.config(text=dustmqanswp[16][4])
        lab4.config(wraplength=200)
    elif '창덕' in ent1.get() or '유네' in ent1.get() or '세계' in ent1.get()or '유산' in ent1.get():
        lab4.config(text=dustmqanswp[17][4])
        lab4.config(wraplength=200)
    elif '영국' in ent1.get() or '섬' in ent1.get() or '나라' in ent1.get():
        lab4.config(text=dustmqanswp[19][4])
        lab4.config(wraplength=200)
    elif '허' in ent1.get() or '강' in ent1.get() or '아마' in ent1.get():
        lab4.config(text=dustmqanswp[20][4])
        lab4.config(wraplength=200)
    elif '전' in ent1.get() or 'V' in ent1.get() or '트' in ent1.get():
        lab4.config(text=dustmqanswp[21][4])
        lab4.config(wraplength=200)
    elif '태극' in ent1.get() or '건' in ent1.get() or '곤' in ent1.get()or\
            '감' in ent1.get()or '리' in ent1.get()or '하늘' in ent1.get()\
            or '불' in ent1.get()or '징' in ent1.get():
        lab4.config(text=dustmqanswp[22][4])
        lab4.config(wraplength=200)
    elif '태양' in ent1.get() \
        or '목' in ent1.get() or '해' in ent1.get():
        lab4.config(text=dustmqanswp[23][4])
        lab4.config(wraplength=200)
    elif '화력' in ent1.get() or '원료' in ent1.get() or '석유' in ent1.get():
        lab4.config(text=dustmqanswp[24][4])
        lab4.config(wraplength=200)
    elif '아임' in ent1.get() or 'I' in ent1.get() or '95' in ent1.get():
        lab4.config(text=dustmqanswp[25][4])
        lab4.config(wraplength=200)
    elif '15' in ent1.get() or '광복' in ent1.get() or '45' in ent1.get():
        lab4.config(text=dustmqanswp[26][4])
        lab4.config(wraplength=200)
    elif '노비' in ent1.get() or '상속' in ent1.get() or '증' in ent1.get()or '매' in ent1.get():
        lab4.config(text=dustmqanswp[27][4])
        lab4.config(wraplength=200)
    elif '법' in ent1.get() or '발' in ent1.get() or '상품' in ent1.get()or '폐' in ent1.get():
        lab4.config(text=dustmqanswp[28][4])
        lab4.config(wraplength=200)
    elif '건국' in ent1.get() or '홍인' in ent1.get() or '념' in ent1.get():
        lab4.config(text=dustmqanswp[29][4])
        lab4.config(wraplength=200)
    elif '대동' in ent1.get() or '정호' in ent1.get() or '작성' in ent1.get():
        lab4.config(text=dustmqanswp[30][4])
        lab4.config(wraplength=200)
    elif '미국' in ent1.get() or '컨' in ent1.get() or '령' in ent1.get():
        lab4.config(text=dustmqanswp[31][4])
        lab4.config(wraplength=200)
    elif '무늬' in ent1.get() or '토기' in ent1.get() or '시대' in ent1.get():
        lab4.config(text=dustmqanswp[32][4])
        lab4.config(wraplength=200)
    elif '선사' in ent1.get() or '구석' in ent1.get() or '청동' in ent1.get()or '신석' in ent1.get()or '철기' in ent1.get() or '순서' in ent1.get():
        lab4.config(text=dustmqanswp[33][4])
        lab4.config(wraplength=200)
    elif '수군' in ent1.get() or '의병' in ent1.get() or '정묘' in ent1.get():
        lab4.config(text=dustmqanswp[34][4])
        lab4.config(wraplength=200)
    elif '세종' in ent1.get() or '문' in ent1.get() or '연구' in ent1.get()or '현' in ent1.get():
        lab4.config(text=dustmqanswp[35][4])
        lab4.config(wraplength=200)
    elif '정조' in ent1.get() or '금난' in ent1.get() or '특권' in ent1.get()or '시전' in ent1.get():
        lab4.config(text=dustmqanswp[36][4])
        lab4.config(wraplength=200)
    elif '직지' in ent1.get() or '기원' in ent1.get() or '부처' in ent1.get()or '몽골' in ent1.get():
        lab4.config(text=dustmqanswp[37][4])
        lab4.config(wraplength=200)
    elif '몽주' in ent1.get() or '고려' in ent1.get() or '마음' in ent1.get()or '하여' in ent1.get() or '임금' in ent1.get():
        lab4.config(text=dustmqanswp[38][4])
        lab4.config(wraplength=200)
    else:
        lab4.config(text='없는 내용! \n 핵심단어를 잘 검색해주세요!')
study_list = []
study_list1 = []
for ddd in range(12):
    auddjsindex = auddjsData[ddd][0]
    auddjsindex1 = auddjsData[ddd][1]
    study_list.append(auddjsindex)
    study_list1.append(auddjsindex1)
    print(auddjsindex)

def tkdtlrdustmq4():
    tkdtlrdustmq1.config(text=str(knowledgelist),)
    tkdtlrdustmq1.config(wraplength=330,)
study_num=0
pagecount=1
sutuyy1= Label(frame6, text=study_list[study_num],font=("나눔바른펜", 15, "bold"),bd=4,
                    fg='black')
sutuyy1.pack(pady=20)
sutuyy2= Label(frame6, text=study_list1[study_num],font=("나눔바른펜", 10, "bold"),bd=4,
                    fg='black')
sutuyy2.pack()
nextbutton= Button(frame6, text='◀ 이전', command=pre_study,width=10,height=2, bg=BGCOLOR2)
nextbutton.place(x=10 ,y=150)
prebutton= Button(frame6, text='다음 ▶', command=next_study,width=10,height=2, bg=BGCOLOR2)
prebutton.place(x=310 ,y=150)

tkdtlrvar = StringVar(value=tkdtlrlist)
tkdtlrlist1= Listbox(frame6, height=10, width=54, listvariable= tkdtlrvar, state="disabled",)
tkdtlrlist1.place(x=10,y=200)
lab5 = Label(frame6, text="")
lab4 = Label(frame6, text="검색 결과가 없습니다! \n 문제의 핵심 단어를 검색해주세요! \n"
                          "ex) '우주' '낙타' '정조' '링컨' '광복'", font=("나눔바른펜", 12, "bold"))


ent1 = Entry(frame6)
ent2= Button(frame6, text="검색", command=showww1, bg=BGCOLOR2)
ent2.place(x=280, y=370)
ent1.place(x=125, y=375)
lab4.place(x=100, y=400)
lab5.place(x=105, y=400)
tkdtlrdustmq = LabelFrame(frame6, text="틀린 문제",)
tkdtlrdustmq.place(x=20,y=550)
tkdtlrdustmq1 = Label(tkdtlrdustmq, text="문제를 풀고 와주세요",)
tkdtlrdustmq1.grid()
tkdtlrdustmq4 = Button(tkdtlrdustmq, text="틀린 문제 가져오기",command=tkdtlrdustmq4,bg=BGCOLOR2)
tkdtlrdustmq4.grid()

win.mainloop()