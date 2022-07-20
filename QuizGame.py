import os
import random
import sys
import webbrowser
from tkinter import *
from tkinter import messagebox as mess
import requests
from PIL import ImageTk, Image


class AskingAboutProgramExecution:
    def submit_button_command(self):
        self.total_question = int(self.total_number_of_question_scale.get())
        self.which_quiz = self.type_menu_variable.get()
        if self.which_quiz == 'Options':
            mess.showerror(
                title='Null Selection',
                message='Options Field is Compulsory please choose one :)')
        else:
            self.window.destroy()

    def __init__(self):
        self.which_quiz = None
        self.total_question = None
        self.window = Tk()
        self.window.geometry("600x400")
        self.window.title("Quiz Game")
        self.window.configure(bg="#ffffff")
        canvas = Canvas(
            self.window,
            bg="#ffffff",
            height=400,
            width=600,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"Program Images/background_0.png")
        canvas.create_image(
            297.5, 198.0,
            image=background_img)

        self.type_menu_variable = StringVar()
        self.type_menu_variable.set('Options')
        self.type_menu = OptionMenu(
            self.window,
            self.type_menu_variable,
            'General Knowledge',
            'Books',
            'Films',
            'Music',
            'Television',
            'Video Games',
            'Nature',
            'Computer',
            'Sports',
            'Geography',
            'History',
            'Cartoon And Animation'
        )

        self.type_menu.place(
            x=50,
            y=165
        )

        self.total_number_of_question_scale = Scale(
            canvas,
            from_=5,
            to=20,
            tickinterval=5,
            orient=HORIZONTAL,
            background='#FFFFFF',
            width=10,
            length=120,
            highlightthickness=0,
            font=('DomesticManners', 13))

        self.total_number_of_question_scale.place(
            x=40,
            y=280)

        img1 = PhotoImage(file=f"Program Images/img1_0.png")
        self.submit_button = Button(

            image=img1,
            borderwidth=0,
            cursor='pencil',
            bg='#FFFFFF',
            activebackground='#FFFFFF',
            highlightthickness=0,
            # border=1,
            command=lambda: self.submit_button_command(),
            relief=RAISED)

        self.submit_button.place(
            x=335, y=148,
            width=108,
            height=35)

        img0 = PhotoImage(file=f"Program Images/img0_0.png")
        self.help_button = Button(
            image=img0,
            borderwidth=0,
            cursor='pencil',
            bg='#FFFFFF',
            activebackground='#FFFFFF',
            highlightthickness=0,
            relief=RAISED,
            command=lambda: self.about_programmer_command())

        self.help_button.place(
            x=335, y=212,
            width=108,
            height=33)

        self.window.bind('<Control-h>', lambda a: self.about_programmer_command())
        self.window.bind('<Return>', lambda a: self.submit_button_command())
        self.window.bind('a', lambda a: self.type_menu_variable.set('General Knowledge'))
        self.window.bind('b', lambda a: self.type_menu_variable.set('Books'))
        self.window.bind('c', lambda a: self.type_menu_variable.set('Films'))
        self.window.bind('d', lambda a: self.type_menu_variable.set('Music'))
        self.window.bind('e', lambda a: self.type_menu_variable.set('Television'))
        self.window.bind('f', lambda a: self.type_menu_variable.set('Video Games'))
        self.window.bind('g', lambda a: self.type_menu_variable.set('Nature'))
        self.window.bind('h', lambda a: self.type_menu_variable.set('Computer'))
        self.window.bind('i', lambda a: self.type_menu_variable.set('Sports'))
        self.window.bind('j', lambda a: self.type_menu_variable.set('Geography'))
        self.window.bind('k', lambda a: self.type_menu_variable.set('History'))
        self.window.bind('l', lambda a: self.type_menu_variable.set('Cartoon And Animation'))
        self.window.protocol('WM_DELETE_WINDOW', lambda: quit())

        self.window.resizable(False, False)
        self.window.mainloop()

    def about_programmer_command(self):
        self.window.destroy()
        HelpClass()
        os.execl(sys.executable, sys.executable, *sys.argv)


class Quiz:

    def answer_checking_button_command(self, ques_no=400, button=1, btn_str=''):
        green = '#68fc5c'
        red = '#ff6464'
        if btn_str == self.correct_options_list[ques_no]:
            self.winning_game_list.append(ques_no)
            if button == 1:
                self.first_option_button.config(background=green, activebackground=green)
                self.second_option_button.config(background=red, activebackground=red)
                self.third_option_button.config(background=red, activebackground=red)
                self.forth_option_button.config(background=red, activebackground=red)
            elif button == 2:
                self.first_option_button.config(background=red, activebackground=red)
                self.second_option_button.config(background=green, activebackground=green)
                self.third_option_button.config(background=red, activebackground=red)
                self.forth_option_button.config(background=red, activebackground=red)
            elif button == 3:
                self.first_option_button.config(background=red, activebackground=red)
                self.second_option_button.config(background=red, activebackground=red)
                self.third_option_button.config(background=green, activebackground=green)
                self.forth_option_button.config(background=red, activebackground=red)
            elif button == 4:
                self.first_option_button.config(background=red, activebackground=red)
                self.second_option_button.config(background=red, activebackground=red)
                self.third_option_button.config(background=red, activebackground=red)
                self.forth_option_button.config(background=green, activebackground=green)
            mess.showinfo(title='you win', message='congrats you won this one')
        else:
            correct_option = None
            for index, item in enumerate(self.option_list[ques_no]):
                if item == self.correct_options_list[ques_no]:
                    correct_option = index + 1

            if correct_option == 1:
                self.first_option_button.config(background=green, activebackground=green)
                self.second_option_button.config(background=red, activebackground=red)
                self.third_option_button.config(background=red, activebackground=red)
                self.forth_option_button.config(background=red, activebackground=red)
            elif correct_option == 2:
                self.first_option_button.config(background=red, activebackground=red)
                self.second_option_button.config(background=green, activebackground=green)
                self.third_option_button.config(background=red, activebackground=red)
                self.forth_option_button.config(background=red, activebackground=red)
            elif correct_option == 3:
                self.first_option_button.config(background=red, activebackground=red)
                self.second_option_button.config(background=red, activebackground=red)
                self.third_option_button.config(background=green, activebackground=green)
                self.forth_option_button.config(background=red, activebackground=red)
            elif correct_option == 4:
                self.first_option_button.config(background=red, activebackground=red)
                self.second_option_button.config(background=red, activebackground=red)
                self.third_option_button.config(background=red, activebackground=red)
                self.forth_option_button.config(background=green, activebackground=green)

        self.first_option_button.config(state=DISABLED, disabledforeground='black')
        self.second_option_button.config(state=DISABLED, disabledforeground='black')
        self.third_option_button.config(state=DISABLED, disabledforeground='black')
        self.forth_option_button.config(state=DISABLED, disabledforeground='black')
        self.ans_button.config(state=DISABLED)

    def question_number_label_changer_command(self, text='Question / '):
        self.canvas.itemconfig(self.f1, text=text)

    def next_button_command(self):
        def command():
            self.ans_button.config(state=NORMAL)
            global total_question_from_ask_class, which_quiz_type_from_ask_class
            yellow = '#ffff99'
            self.current_question_from_0 += 1
            self.current_question_from_1 += 1
            if self.current_question_from_1 == self.total_question + 1:
                if len(self.winning_game_list) >= 1:
                    mess.showinfo(
                        title='Results',
                        message=f'Congrats You won {len(self.winning_game_list)}/{self.total_question} matches.')
                else:
                    mess.showinfo(title='Results', message=f'Oops!!, no win :(\nBetter Luck Next Time.')
                self.ans_button.config(state=DISABLED)
                self.next_button.config(state=DISABLED)
                ask_to_rerun = mess.askyesno(title='Replay Asking', message='Do you want to replay the game.')
                if ask_to_rerun:
                    self.window.destroy()
                    total_question_from_ask_class, which_quiz_type_from_ask_class = rerun_from_begin()
                    Quiz()
                else:
                    quit()

            self.first_option_button.config(state=NORMAL)
            self.second_option_button.config(state=NORMAL)
            self.third_option_button.config(state=NORMAL)
            self.forth_option_button.config(state=NORMAL)

            self.question_number_label_changer_command(
                text=f'Question {self.current_question_from_1}/{self.total_question}')
            self.canvas.itemconfig(self.question_label, text=self.question_list[self.current_question_from_0])
            self.forth_option_button.config(
                text=f'4) {self.option_list[self.current_question_from_0][3]}',
                background='white',
                activebackground=yellow)
            self.third_option_button.config(
                text=f'3) {self.option_list[self.current_question_from_0][2]}',
                background='white',
                activebackground=yellow)
            self.second_option_button.config(
                text=f'2) {self.option_list[self.current_question_from_0][1]}',
                background='white',
                activebackground=yellow)
            self.first_option_button.config(
                text=f'1) {self.option_list[self.current_question_from_0][0]}',
                background='white',
                activebackground=yellow)

        if self.current_question_from_1 == 1:
            ask = mess.askyesno(
                title='Warning',
                message='This question can be viewed only once, you cant go back\n\n'
                        ''
                        'Did You Want to view next question?')

            if ask:
                is_disable = mess.askyesno(
                    title='Disable Notification Alert',
                    message='Do you want to stop warning notification?')

                if is_disable:
                    self.ok_disabled_message_warning_of_next = True
                command()
                return

        if self.ok_disabled_message_warning_of_next:
            command()

        else:
            ask = mess.askyesno(
                title='Warning',
                message='This question can be viewed only once, you cant go back\n'
                        '\n'
                        'Did You Want to view next question?')

            if ask: 
                command()

    def ans_button_command(self):
        def command():
            green = '#68fc5c'
            red = '#ff6464'
            correct_answer_str = ''
            button = None
            self.first_option_button.config(state=DISABLED, disabledforeground='black')
            self.second_option_button.config(state=DISABLED, disabledforeground='black')
            self.third_option_button.config(state=DISABLED, disabledforeground='black')
            self.forth_option_button.config(state=DISABLED, disabledforeground='black')

            for index, answer in enumerate(self.correct_options_list):
                if index == self.current_question_from_0:
                    correct_answer_str = answer
            for index_is, answer_is in enumerate(self.option_list[self.current_question_from_0]):
                if answer_is == correct_answer_str:
                    button = index_is + 1

            if button == 1:
                self.first_option_button.config(background=green, activebackground=green)
                self.second_option_button.config(background=red, activebackground=red)
                self.third_option_button.config(background=red, activebackground=red)
                self.forth_option_button.config(background=red, activebackground=red)
            elif button == 2:
                self.first_option_button.config(background=red, activebackground=red)
                self.second_option_button.config(background=green, activebackground=green)
                self.third_option_button.config(background=red, activebackground=red)
                self.forth_option_button.config(background=red, activebackground=red)
            elif button == 3:
                self.first_option_button.config(background=red, activebackground=red)
                self.second_option_button.config(background=red, activebackground=red)
                self.third_option_button.config(background=green, activebackground=green)
                self.forth_option_button.config(background=red, activebackground=red)
            elif button == 4:
                self.first_option_button.config(background=red, activebackground=red)
                self.second_option_button.config(background=red, activebackground=red)
                self.third_option_button.config(background=red, activebackground=red)
                self.forth_option_button.config(background=green, activebackground=green)

            self.question_number_label_changer_command(
                text=f'Question {self.current_question_from_1}/{self.total_question}')
            self.ans_button.config(state=DISABLED)

        if self.current_question_from_1 == 1:
            ask = mess.askyesno(
                title='Warning',
                message='If you saw the answer of this question then you cant reappear this question.'
                        '\n'
                        '\nAre you sure ?')

            if ask:
                is_disable = mess.askyesno(
                    title='Disable Notification Alert',
                    message='Do you want to stop warning notification?')

                if is_disable:
                    self.ok_disabled_message_warning_of_ans = True
                command()
                return

        if self.ok_disabled_message_warning_of_ans:
            command()

        else:
            ask = mess.askyesno(
                title='Warning',
                message='This question can be viewed only once, you cant go back\n\n'
                        ''
                        'Did You Want to view next question?')

            if ask: 
                command()

    def data_giving(self):
        self.question_list = []
        self.option_list = []
        self.correct_options_list = []
        for i in range(self.total_question):
            self.question_list.append(self.dict_of_response['results'][i]['question'])
            self.correct_options_list.append(self.dict_of_response['results'][i]['correct_answer'])
            temp = [self.correct_options_list[i]]
            for item in self.dict_of_response['results'][i]['incorrect_answers']:
                temp.append(item)
            random.shuffle(temp)
            self.option_list.append(temp)
            # break

    def __init__(self):
        try:
            self.total_question, self.dict_of_response, self.cate = api_refresh()
            self.data_giving()
        except:
            Errors().server_side_error()
        else:
            self.window = Tk()
            self.window.geometry("700x500")
            self.window.title('Quiz Game by Prashant Singh.')
            self.window.configure(bg="#4696af")

            self.current_question_from_0 = 0
            self.current_question_from_1 = 1
            self.winning_game_list = []
            self.ok_disabled_message_warning_of_next = False
            self.ok_disabled_message_warning_of_ans = False

            self.canvas = Canvas(
                self.window,
                bg="#4696af",
                height=500,
                width=700,
                bd=0,
                highlightthickness=0,
                relief="ridge")
            self.canvas.place(x=0, y=0)

            background_img = PhotoImage(file=f"Program Images/background.png")
            self.canvas.create_image(
                318.0, 250.0,
                image=background_img)

            img0 = PhotoImage(file=f"Program Images/img0.png")
            self.next_button = Button(
                image=img0,
                borderwidth=0,
                highlightthickness=0,
                background='#EDEEF1',
                activebackground='#EDEEF1',
                command=lambda: self.next_button_command(),
                relief="flat")

            self.next_button.place(
                x=239, y=437,
                width=78,
                height=32)

            img1 = PhotoImage(file=f"Program Images/img1.png")
            self.ans_button = Button(
                image=img1,
                borderwidth=0,
                background='#EDEEF1',
                activebackground='#EDEEF1',
                highlightthickness=0,
                command=lambda: self.ans_button_command(),
                relief="flat")

            self.ans_button.place(
                x=35, y=437,
                width=78,
                height=32)

            self.question_label = self.canvas.create_text(
                175, 350,
                width=260,
                justify=LEFT,
                text=self.question_list[self.current_question_from_0],
                fill="#000000",
                font=("LatinModernRomanDunhill", int(12.0), 'bold'))

            self.f1 = self.canvas.create_text(
                181.0, 54.5,
                text=f"Question {self.current_question_from_0 + 1}/{self.total_question}",
                fill="#25c3f4",
                font=("Judson-Regular", int(28.0)))

            self.forth_option_button = Button(
                background='white',
                activebackground='#ffff99',
                justify='left',
                text=f'4) {self.option_list[self.current_question_from_0][3]}',
                highlightthickness=0,
                command=lambda: self.answer_checking_button_command(
                    button=4,
                    btn_str=self.option_list[self.current_question_from_0][3],
                    ques_no=self.current_question_from_0),
                relief="flat")

            self.forth_option_button.place(
                x=394, y=357,
                width=267,
                height=55)

            self.third_option_button = Button(
                background='white',
                activebackground='#ffff99',
                justify='left',
                text=f'3) {self.option_list[self.current_question_from_0][2]}',
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.answer_checking_button_command(
                    button=3,
                    btn_str=self.option_list[self.current_question_from_0][2],
                    ques_no=self.current_question_from_0),
                relief="flat")

            self.third_option_button.place(
                x=394, y=286,
                width=267,
                height=55)

            self.second_option_button = Button(
                background='white',
                activebackground='#ffff99',
                justify='left',
                text=f'2) {self.option_list[self.current_question_from_0][1]}',
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.answer_checking_button_command(
                    button=2,
                    btn_str=self.option_list[self.current_question_from_0][1],
                    ques_no=self.current_question_from_0),
                # command = lambda: self.data_giving(),
                relief="flat")

            self.second_option_button.place(
                x=394, y=215,
                width=267,
                height=55)

            self.first_option_button = Button(
                background='white',
                activebackground='#ffff99',
                justify='left',
                text=f'1) {self.option_list[self.current_question_from_0][0]}',
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.answer_checking_button_command(
                    button=1,
                    btn_str=self.option_list[self.current_question_from_0][0],
                    ques_no=self.current_question_from_0),
                relief="flat")

            self.first_option_button.place(
                x=394, y=144,
                width=267,
                height=55)

            self.window.bind('<Control-h>', lambda a: self.about_programmer_command())
            self.window.bind('<Return>', lambda a: self.next_button_command())
            self.window.bind('<space>', lambda a: self.ans_button_command())
            self.window.bind('1', lambda i: self.answer_checking_button_command(
                button=1,
                btn_str=self.option_list[self.current_question_from_0][0],
                ques_no=self.current_question_from_0))
            self.window.bind('2', lambda i: self.answer_checking_button_command(
                button=2,
                btn_str=self.option_list[self.current_question_from_0][1],
                ques_no=self.current_question_from_0))
            self.window.bind('3', lambda i: self.answer_checking_button_command(
                button=3,
                btn_str=self.option_list[self.current_question_from_0][2],
                ques_no=self.current_question_from_0))
            self.window.bind('4', lambda i: self.answer_checking_button_command(
                button=4,
                btn_str=self.option_list[self.current_question_from_0][3],
                ques_no=self.current_question_from_0))
            # self.data_filler()
            self.window.resizable(False, False)
            self.window.mainloop()

    def about_programmer_command(self):
        ask = mess.askyesno(title='Warning', message='Opening Help Page will delete current quiz progress.\n\n'
                                                     'Are You Still Want to Open Help Page ?')
        if ask:
            self.window.destroy()
            HelpClass()
            os.execl(sys.executable, sys.executable, *sys.argv)


class HelpClass:
    def __init__(self):
        self.run_next_program = False
        self.programmer_description_string = '''(#)This Program is made on July 21, 2022
by Prashant Ranjan Singh.


(#) It is an Online Quiz Game :) 


(#) Linkedin Profile of mine :-'''
        self.working_of_program_explain_str = '''\t\t\t     Shortcuts are :-

Main Menu :-
\t1) a/b/c/d/e/f/g/h/i/j/k/l --> Selecting Type from 1/12
\t2) Enter --> Submit Button Shortcut.

Shortcut Of Game :-
\t1) 1/2/3/4 --> Selecting Option 1/2/3/4.
\t2) Enter --> Next Button Shortcut.
\t3) Space key --> Answer Button Shortcut.

Universal Shortcuts :-
\t1) ctrl+h / ctrl+H --> For Opening Help Menu
\t2) alt+f4 --> Exiting application.'''
        background = 'white'

        # Screen
        self.screen = Tk()
        self.screen.geometry('600x620')
        self.screen.minsize(600, 620)
        self.screen.maxsize(600, 620)
        self.screen.title('Quiz Game By Prashant Ranjan Singh')
        self.screen.config(bg=background, padx=50, pady=50)
        self.screen.resizable(False, False)

        # image
        self.password_image = ImageTk.PhotoImage(Image.open("Program Images/Mine_photo.jpg"))
        self.image = Label(width=250, height=250, image=self.password_image, borderwidth=0)

        # Label
        self.text = Label()
        self.about_programmer = Label(text='About Programmer', font=('LatinModernRomanDunhill', 12, 'bold'),
                                      background=background)
        self.text.configure(text=self.programmer_description_string, bg='white', justify=LEFT)
        self.link = Label(text="www.linkedin.com", fg="blue", cursor="hand2", bg=background)
        self.link.bind("<Button-1>", lambda e: self.callback("www.linkedin.com/in/prashant-ranjan-singh-b9b6b9217"))
        self.working_heading = Label(text='Working of Program', font=('LatinModernRomanDunhill', 12, 'bold'),
                                     bg=background)
        self.working_of_program_explain = Label(text=self.working_of_program_explain_str, bg='white', justify=LEFT)

        # Create a Label to display the link
        self.image.grid(column=0, row=0)
        self.about_programmer.grid(column=1, row=0, sticky=NE, padx=70)
        self.text.grid(column=1, row=0, sticky=NW, pady=50, padx=10)
        self.link.grid(column=1, row=0, sticky=SW, padx=35, pady=30)
        self.working_heading.grid(column=0, row=1, padx=50, columnspan=2, pady=5)
        self.working_of_program_explain.grid(column=0, row=2, columnspan=3, sticky=W)
        self.screen.mainloop()

    @staticmethod
    def callback(url):
        webbrowser.open_new_tab(url)


class Errors:
    def __init__(self):
        self.background = None
        self.error = None
        self.what_to_do = None
        self.link = None
        self.L1 = None

    def file_missing(cls,
                     url='https://github.com/Prashant-ranjan-singh-123/MyAllProgramsInOneRepo/tree/main/'
                         '4)%20Python%20Language/GUI%20Program/Library%20Management',
                     show_name_of_url='www.github.com'):
        def callback(url_is):
            webbrowser.open_new_tab(url_is)

        root = Tk()
        cls.background = 'white'
        root.geometry('500x310')
        root.resizable(False, False)
        root.title('Quiz Game by Prashant Singh')
        root.config(background=cls.background, borderwidth=30)

        def exit_command():
            nonlocal root
            root.destroy()

        # Heading Label
        cls.L1 = Label(root, text='Prashant\'s Quiz Game', font='LatinModernRomanDunhill 20 bold',
                       background=cls.background)
        cls.L1.pack(anchor='center')

        # Label
        cls.error = Label(root, text='Error', foreground='red', font='arial 30 bold', justify=CENTER,
                          background=cls.background)
        cls.error.pack(anchor='center', pady=20)

        cls.what_to_do = Label(root, text=f'You wont have essential component\'s for proper \n'
                                          f'execution of program please download it from \n'
                                          f'official github repository from below link :-',
                               font=('arial', 12, 'bold'), justify=CENTER, bg=cls.background)
        cls.what_to_do.pack()

        cls.link = Label(text=show_name_of_url, fg="blue", cursor="hand2", bg=cls.background,
                         font=('arial', 12, 'bold'))
        cls.link.bind("<Button-1>", lambda e: callback(url))
        cls.link.pack(anchor='center')

        # Button
        exit_button = Button(text='Previous Menu', bg='#ff4d4d', padx=40, borderwidth=2, highlightbackground='black',
                             activebackground='#ff0000', command=exit_command)
        exit_button.place(x=480, y=300)
        root.mainloop()

    def server_side_error(cls,
                          url=f"https://opentdb.com/api.php?amount=20&category=22&difficulty=easy&type=multiple",
                          show_name_of_url='www.opentdb.com'):
        def callback(url_is):
            webbrowser.open_new_tab(url_is)

        root = Tk()
        cls.background = 'white'
        root.geometry('500x310')
        root.resizable(False, False)
        root.title('Quiz Game by Prashant Singh')
        root.config(background=cls.background, borderwidth=30)

        def exit_command():
            nonlocal root
            root.destroy()

        # Heading Label
        cls.L1 = Label(root, text='Prashant\'s Quiz Game', font='LatinModernRomanDunhill 20 bold',
                       background=cls.background)
        cls.L1.pack(anchor='center')

        # Label
        cls.error = Label(root, text='Error', foreground='red', font='arial 30 bold', justify=CENTER,
                          background=cls.background)
        cls.error.pack(anchor='center', pady=20)

        cls.what_to_do = Label(root, text=f'You wont have essential component\'s for proper \n'
                                          f'execution of program please download it from \n'
                                          f'official github repository from below link :-',
                               font=('arial', 12, 'bold'), justify=CENTER, bg=cls.background)

        cls.what_to_do = Label(root, text=f'Our Program is Trying To Connect With API but\n'
                                          f'there are some Problem While Connecting to it\n'
                                          f'You can manually try by clicking on given Link.',
                               font=('arial', 12, 'bold'), justify=CENTER, bg=cls.background)
        cls.what_to_do.pack()

        cls.link = Label(text=show_name_of_url, fg="blue", cursor="hand2", bg=cls.background,
                         font=('arial', 12, 'bold'))
        cls.link.bind("<Button-1>", lambda e: callback(url))
        cls.link.pack(anchor='center')

        # Button
        exit_button = Button(text='Previous Menu', bg='#ff4d4d', padx=40, borderwidth=2, highlightbackground='black',
                             activebackground='#ff0000', command=exit_command)
        exit_button.place(x=480, y=300)
        root.mainloop()


if __name__ == '__main__':
    def api_refresh():
        total_question = None
        dict_of_response = None
        category = 9
        if which_quiz_type_from_ask_class == 'General Knowledge':
            category = 9
        elif which_quiz_type_from_ask_class == 'Books':
            category = 10
        elif which_quiz_type_from_ask_class == 'Films':
            category = 11
        elif which_quiz_type_from_ask_class == 'Music':
            category = 12
        elif which_quiz_type_from_ask_class == 'Television':
            category = 14
        elif which_quiz_type_from_ask_class == 'Video Games':
            category = 15
        elif which_quiz_type_from_ask_class == 'Nature':
            category = 17
        elif which_quiz_type_from_ask_class == 'Computer':
            category = 18
        elif which_quiz_type_from_ask_class == 'Sports':
            category = 21
        elif which_quiz_type_from_ask_class == 'Geography':
            category = 22
        elif which_quiz_type_from_ask_class == 'History':
            category = 23
        elif which_quiz_type_from_ask_class == 'Cartoon And Animation':
            category = 32
        r = requests.get(
            f'https://opentdb.com/api.php?'
            f'amount={total_question_from_ask_class}&'
            f'category={category}&'
            f'difficulty=easy&'
            f'type=multiple')
        if r.status_code == 200:
            dict_of_response = r.json()
            total_question = len(dict_of_response['results'])
        else:
            Errors().server_side_error()
        return total_question, dict_of_response, category


    def rerun_from_begin():
        ask = AskingAboutProgramExecution()
        total_question_from_ask_class = ask.total_question
        which_quiz_type_from_ask_class = ask.which_quiz
        return total_question_from_ask_class, which_quiz_type_from_ask_class


    if os.path.exists('Program Images') and \
            os.path.exists('Program Images/background.png') and \
            os.path.exists('Program Images/background_0.png') and \
            os.path.exists('Program Images/img0.png') and \
            os.path.exists('Program Images/img1.png') and \
            os.path.exists('Program Images/img0_0.png') and \
            os.path.exists('Program Images/img1_0.png') and \
            os.path.exists('Program Images/Mine_photo.jpg'):
        total_question_from_ask_class, which_quiz_type_from_ask_class = rerun_from_begin()
        Quiz()

    else:
        Errors().file_missing()
