#Add path of video in line 679
#Add path of image in line 305 and 376
#Add path of quit icon in line 470
#Add path of retry button in line 465

import random
import tkinter
import customtkinter as ctk
import time
import math
import turtle
from PIL import Image, ImageTk
from tkVideoPlayer import TkinterVideo

#new comment
WindowWidth = 1200
WindowHeight = 600
FrameHeight = 500


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def Question():
    word_list=['ARYAN','PARIS', 'AMERICA', 'APPLE', 'DOG', 'CAT', 'WOOD', 'YOYO', 'HANGMAN', 'RANDOM', 'TERMINATOR', 'LAPTOP']
    word=random.choice(word_list)
    return " ".join(word)

def generate_blank(word):
    ToBeStored=''
    for i in word:
        if i!=' ':
            ToBeStored=ToBeStored+'_'+' '
    return ToBeStored

def generate_print(ToBePrinted,word,letter):
    length=len(ToBePrinted)
    TemporaryString=''
    for i in range(length):
        if ToBePrinted[i] != ' ':
            if word[i]==letter and ToBePrinted[i]=='_':
                TemporaryString=TemporaryString+letter+''
            if ToBePrinted[i]!='_' and ToBePrinted[i]!='':
                TemporaryString=TemporaryString+ToBePrinted[i]
            elif word[i]!=letter:
                TemporaryString=TemporaryString+'_'
        elif ToBePrinted[i]==' ':
            TemporaryString=TemporaryString+' '
    
    if TemporaryString[-1] == ' ':
        TemporaryString = TemporaryString[0:len(TemporaryString)-1]

    return TemporaryString

def LetterIsPresent(word,letter):
    IsPresent=False
    for i in word:
        if i==letter:
            IsPresent=True
            break
    return IsPresent
            
            
def update_keys(key, key_color):
    global KeyText, TopRow, MiddleRow, BottomRow
    if key >= 'A' and key <= 'Z':
        if key in "QWERTYUIOP":
            row = 1
            for KeyInRow in range(len(TopRow)):
                if key == TopRow[KeyInRow]:
                    index = KeyInRow
                    break
        if key in "ASDFGHJKL":
            row = 2
            for KeyInRow in range(len(MiddleRow)):
                if key == MiddleRow[KeyInRow]:
                    index = KeyInRow
        if key in "ZXCVBNM":
            row = 3
            for KeyInRow in range(len(BottomRow)):
                if key == BottomRow[KeyInRow]:
                    index = KeyInRow
                    
        start = float(str(row)+'.'+str(index))
        end = float(str(row)+'.'+str(index+1))
        
        KeyText.configure(state="normal")
        KeyText.tag_add("color"+key, start, end)
        KeyText.tag_config("color"+key, foreground=key_color)
        KeyText.configure(state="disabled")
    
    
def DrawHangman():
    global count, Draw, GuessEntry, SubmitButton
    
    StartingPointX, StartingPointY = -200, -150
    BaseLength = 100
    PoleHeight = 300
    PoleWidth = 180
    StickDistance = 120
    RopeLength = 50
    StickManRadius = 25
    ArmLength = 40
    StickManLength = 95
    LegLength = 50
    DrawSpeed = 3
    
    if count == 11:
        GuessEntry.configure(state = "disabled")
        SubmitButton.configure(state = "disabled")
        Draw.penup()
        Draw.goto(StartingPointX,StartingPointY)
        Draw.pendown()
        Draw.speed(DrawSpeed)
        Draw.forward(BaseLength)
        Draw.speed(0)
        Draw.penup()
        Draw.back(BaseLength/2)
        GuessEntry.configure(state = "normal")
        SubmitButton.configure(state = "normal")
    elif count == 10:
        GuessEntry.configure(state = "disabled")
        SubmitButton.configure(state = "disabled")
        Draw.pendown()
        Draw.speed(DrawSpeed)
        Draw.left(90)
        Draw.forward(PoleHeight)
        Draw.speed(0)
        Draw.penup()
        Draw.right(90)
        GuessEntry.configure(state = "normal")
        SubmitButton.configure(state = "normal")
    elif count == 9:
        GuessEntry.configure(state = "disabled")
        SubmitButton.configure(state = "disabled")
        Draw.pendown()
        Draw.speed(DrawSpeed)
        Draw.forward(PoleWidth)
        Draw.speed(0)
        Draw.penup()
        Draw.back(StickDistance)
        GuessEntry.configure(state = "normal")
        SubmitButton.configure(state = "normal")
    elif count == 8:
        GuessEntry.configure(state = "disabled")
        SubmitButton.configure(state = "disabled")
        Draw.left(180+45)
        Draw.pendown()
        Draw.speed(DrawSpeed)
        Draw.forward((PoleWidth-StickDistance)/math.cos(math.pi/4))
        Draw.speed(0)
        Draw.penup()
        Draw.back((PoleWidth-StickDistance)/math.cos(math.pi/4))
        Draw.right(180+45)
        GuessEntry.configure(state = "normal")
        SubmitButton.configure(state = "normal")
    elif count == 7:
        GuessEntry.configure(state = "disabled")
        SubmitButton.configure(state = "disabled")
        Draw.forward(StickDistance)
        Draw.right(90)
        Draw.pendown()
        Draw.speed(DrawSpeed)
        Draw.forward(RopeLength)
        Draw.speed(0)
        Draw.penup()
        Draw.right(90)
        Draw.forward(StickManRadius)
        GuessEntry.configure(state = "normal")
        SubmitButton.configure(state = "normal")
    elif count == 6:
        GuessEntry.configure(state = "disabled")
        SubmitButton.configure(state = "disabled")
        Draw.left(90)
        Draw.forward(StickManRadius)
        Draw.pendown()
        Draw.speed(DrawSpeed)
        Draw.circle(StickManRadius)
        Draw.speed(0)
        Draw.penup()
        Draw.forward(StickManRadius)
        Draw.left(90)
        Draw.forward(StickManRadius)
        Draw.right(90)
        GuessEntry.configure(state = "normal")
        SubmitButton.configure(state = "normal")
    elif count == 5:
        GuessEntry.configure(state = "disabled")
        SubmitButton.configure(state = "disabled")
        Draw.right(45)
        Draw.pendown()
        Draw.speed(DrawSpeed)
        Draw.forward(ArmLength)
        Draw.speed(0)
        Draw.penup()
        Draw.back(ArmLength)
        GuessEntry.configure(state = "normal")
        SubmitButton.configure(state = "normal")
    elif count == 4:
        GuessEntry.configure(state = "disabled")
        SubmitButton.configure(state = "disabled")
        Draw.left(90)
        Draw.pendown()
        Draw.speed(DrawSpeed)
        Draw.forward(ArmLength)
        Draw.speed(0)
        Draw.penup()
        Draw.back(ArmLength)
        Draw.right(45)
        GuessEntry.configure(state = "normal")
        SubmitButton.configure(state = "normal")
    elif count == 3:
        GuessEntry.configure(state = "disabled")
        SubmitButton.configure(state = "disabled")
        Draw.pendown()
        Draw.speed(DrawSpeed)
        Draw.forward(StickManLength)
        Draw.speed(0)
        Draw.penup()
        Draw.left(45)
        GuessEntry.configure(state = "normal")
        SubmitButton.configure(state = "normal")
    elif count == 2:
        GuessEntry.configure(state = "disabled")
        SubmitButton.configure(state = "disabled")
        Draw.pendown()
        Draw.speed(DrawSpeed)
        Draw.forward(LegLength)
        Draw.speed(0)
        Draw.penup()
        Draw.back(LegLength)
        GuessEntry.configure(state = "normal")
        SubmitButton.configure(state = "normal")
    elif count == 1:
        GuessEntry.configure(state = "disabled")
        SubmitButton.configure(state = "disabled")
        Draw.right(90)
        Draw.pendown()
        Draw.speed(DrawSpeed)
        Draw.forward(LegLength)
        GuessEntry.configure(state = "normal")
        SubmitButton.configure(state = "normal")
    
    
            
            
def playing():
    global word, GuessingLabel, GuessEntry, TriesLabel, KeyText, count
    
    
    PrintStatement = GuessingLabel.cget("text")
    if count > 0:
        if not PrintStatement == word:
            letter = GuessEntry.get()
            if not LetterIsPresent(word, letter):
                DrawHangman()
                count = count-1
                TriesLabel.configure(text=str(count))
                if count <= 4 and count >= 3:
                    TriesLabel.configure(text_color = "yellow")
                if count <3:
                    TriesLabel.configure(text_color = "red")
                update_keys(letter, "red")
            if LetterIsPresent(word, letter):
                update_keys(letter, "green")
            PrintStatement = generate_print(PrintStatement, word, letter)
            if PrintStatement == word:
                GuessingLabel.configure(text = PrintStatement)
                passed()
            GuessingLabel.configure(text=PrintStatement)
            if count == 0:
                GuessingLabel.configure(text="Game Over")
                game_over()
        else:
            GuessingLabel.configure(text="GGWP")
    
    GuessEntry.delete(0,tkinter.END)
    
            

def StartScreen():
    SplashScreen.destroy()
    time.sleep(0.5)
    
    
    global WindowWidth, WindowHeight, x, y, window
    
    WindowWidth = 1200
    WindowHeight = 600
    
    #Window properties
    window = ctk.CTk()
    window.title("HANGMAN")
    window.geometry(f'{WindowWidth}x{WindowHeight}+{int(x)}+{int(y)}')
    window.resizable(False, False)


    #Image Frame properties
    ImageFrame = ctk.CTkFrame(master=window, height=1100, width=600, corner_radius=15)
    ImageFrame.grid(row=0, column=0,sticky="n")


    #Image properties
    ImageToBeDisplayed = ctk.CTkImage(dark_image = Image.open("/home/aryan_chopra/Downloads/image.png"),size=(600,600))
    ImageLabel = ctk.CTkLabel(master=ImageFrame, text='', image=ImageToBeDisplayed)
    ImageLabel.grid(pady=20,padx=20)


    #Frame containing button and text properties
    ButtonFrame = ctk.CTkFrame(master=window, height=1100, width=600, corner_radius=15)
    ButtonFrame.grid(row=0, column=1, padx=10)
    ButtonFrame.grid_propagate(0)


    #Text Frame properties
    SecondaryTextFrame = ctk.CTkFrame(master = ButtonFrame)
    SecondaryTextFrame.grid(padx=40, pady=(140,80))


    #Text properties
    Text = ctk.CTkLabel(master = SecondaryTextFrame, text="HANGMAN", font=("bold", 70))
    Text.grid(padx=5,pady=5)


    #Frame containing buttons properties
    SecondaryButtonFrame = ctk.CTkFrame(master = ButtonFrame)
    SecondaryButtonFrame.grid(padx=10)


    #Start button properties
    StartButton = ctk.CTkButton(master = SecondaryButtonFrame, text="Start", width=300, height=50, font=("Arial",25), command=loading)
    StartButton.grid(row=1,pady=7, padx=7)
    
    
    QuitButton = ctk.CTkButton(master = SecondaryButtonFrame, text="Quit", width=300, height=50, font=("Arial", 25), command=quit_main)
    QuitButton.grid(row=3, pady=7)


    window.mainloop()
    
    
def loading():
    global window, loading_window, window_switch
    window_switch="loading"
    window.destroy()
    
    time.sleep(0.5)
    
    
    WindowWidth = 700
    WindowHeight = 400
    
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    
    loading_window = ctk.CTk()
    
    
    ScreenWidth = loading_window.winfo_screenwidth()
    ScreenHeight = loading_window.winfo_screenheight()


    x = (ScreenWidth / 2) - (WindowWidth / 2)
    y = (ScreenHeight / 2) - (WindowHeight / 2)
        
    
    loading_window.title("HANGMAN")
    loading_window.geometry(f'{WindowWidth}x{WindowHeight}+{int(x)}+{int(y)}')
    loading_window.resizable(False, False)
    loading_window.overrideredirect(1)
    
    
    ImageToBeDisplayed = ctk.CTkImage(dark_image = Image.open("/home/aryan_chopra/Downloads/image.png"),size=(700,350))
    ImageLabel = ctk.CTkLabel(master=loading_window, text='', image=ImageToBeDisplayed)
    ImageLabel.grid(row=0, column=0,pady=20,padx=20)
    
    
    ProgressBar = ctk.CTkProgressBar(master = loading_window, progress_color="white", width = 700, height=2)
    ProgressBar.place(relx=0, rely=0.98)
    ProgressBar.set(0.25)
    loading_window.update_idletasks()
    time.sleep(0.4)
    ProgressBar.set(0.4)
    loading_window.update_idletasks()
    time.sleep(0.25)
    ProgressBar.set(0.8)
    loading_window.update_idletasks()
    time.sleep(1)
    ProgressBar.set(1)
    loading_window.update_idletasks()
    
    loading_window.after(1000,main_game)
    
    
    loading_window.mainloop()


def main_game():
    global loading_window, main_window, word, GuessingLabel, GuessEntry, TriesLabel, KeyText, count, TopRow, MiddleRow, BottomRow, window_switch, over_window, passed_window, Draw, SubmitButton
    
    
    word = Question()
    count = 11
    
    
    if window_switch == "loading":
        loading_window.destroy()
    if window_switch == "gameover":
        over_window.destroy()
    if window_switch == "passed":
        passed_window.destroy()
        
    WindowWidth = 1500
    WindowHeight = 800
    FrameHeight = 500


    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")


    main_window = ctk.CTk()


    ScreenWidth = main_window.winfo_screenwidth()
    ScreenHeight = main_window.winfo_screenheight()


    x = (ScreenWidth / 2) - (WindowWidth / 2)
    y = (ScreenHeight / 2) - (WindowHeight / 2)
        
    
    main_window.title("HANGMAN")
    main_window.geometry(f'{WindowWidth}x{WindowHeight}+{int(x)}+{int(y)}')
    main_window.resizable(False, False)


    UpperFrame = ctk.CTkFrame(master = main_window, height = FrameHeight, width = WindowWidth)
    UpperFrame.grid(row=0, column=0)


    FrameHangman = ctk.CTkFrame(master = UpperFrame, height = FrameHeight, width = 500)
    FrameHangman.grid(row=0, column=0)
    FrameHangman.grid_propagate(0)
    
    
    HangmanCanvas = tkinter.Canvas(master = FrameHangman, height = FrameHeight, width = 500, background = "black")
    turtle_screen = turtle.TurtleScreen(HangmanCanvas)
    turtle_screen.bgcolor("black")
    HangmanCanvas.grid()
    Draw = turtle.RawTurtle(turtle_screen)
    Draw.hideturtle()
    Draw.pencolor("white")
    Draw.speed(0)
    

    MainFrame = ctk.CTkFrame(master = UpperFrame, height = FrameHeight, width = 1000)
    MainFrame.grid(row=0, column=1, padx=10)
    MainFrame.grid_propagate(0)
    
    
    RetryButtonImage = ctk.CTkImage(dark_image = Image.open("/home/aryan_chopra/Downloads/reload.png"), size=(35,35))
    RetryButton = ctk.CTkButton(master = MainFrame, image = RetryButtonImage, width=0, height=0, text="", fg_color="transparent", command = restart, hover_color="black", corner_radius=15)
    RetryButton.place(relx=0.942, rely=0.08, anchor="center")
    
    
    QuitButtonImage = ctk.CTkImage(dark_image = Image.open("/home/aryan_chopra/Downloads/quit.png"), size=(35,35))
    QuitButton = ctk.CTkButton(master = MainFrame, image = QuitButtonImage, width=0, height=0, text="", fg_color="transparent", command = quit, hover_color="black", corner_radius=15)
    QuitButton.place(relx=0.947, rely=0.2, anchor="center")


    HangmanText = ctk.CTkLabel(master = MainFrame, text="HANGMAN", font=("Arial bold", 40))
    HangmanText.place(relx=0.5, rely=0.15, anchor="center")


    GuessingLabel = ctk.CTkLabel(master = MainFrame, text="", font=("Arial bold", 40))
    GuessingLabel.place(relx=0.5, rely=0.5, anchor="center")
    GuessingLabel.configure(text = generate_blank(word))
    


    GuessEntry = ctk.CTkEntry(master = MainFrame, height = 50, width=30, fg_color = "transparent", text_color = "white", insertborderwidth = 0, font = ("Aeriel", 20))
    GuessEntry.focus()
    GuessEntry.place(relx=0.5, rely=0.7, anchor="center")
    
    
    SubmitButton = ctk.CTkButton(master = MainFrame, text="Submit", width = 250, height = 50, font = ("Ariel", 19), command = playing)
    SubmitButton.place(relx=0.5, rely=0.9, anchor="center")


    TriesLabel = ctk.CTkLabel(master = MainFrame, text="11", text_color="WHITE", font = ("Arial", 35))
    TriesLabel.place(relx=0.95, rely=0.9, anchor="center")


    KeyFrame = ctk.CTkFrame(master = main_window, height = WindowHeight-FrameHeight, width = 1500)
    KeyFrame.grid(row=1, column=0, pady=10)
    KeyFrame.grid_propagate(0)


    KeyText = ctk.CTkTextbox(KeyFrame, width=1500, height= 300, font=("Ariel", 35))
    KeyText.tag_config("properties", justify="center", spacing3=30)
    TopRow = "Q         W       E        R        T        Y        U        I        O        P "
    MiddleRow = "A         S       D        F        G        H        J        K        L"
    BottomRow = "Z         X       C        V        B        N        M"
    KeyText.insert(ctk.INSERT, TopRow+"\n", "properties",)
    KeyText.insert(ctk.INSERT, MiddleRow+"\n", "properties")
    KeyText.insert(ctk.INSERT, BottomRow+"\n", "properties")
    KeyText.configure(state="disabled")
    KeyText.place(relx=0.0)


    main_window.mainloop()
    
    
def game_over():
    global main_window, word, window_switch, over_window
    window_switch="gameover"
    
    
    WindowWidth = 500
    WindowHeight = 300
    FrameHeight = 500


    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")


    over_window = ctk.CTk()


    ScreenWidth = over_window.winfo_screenwidth()
    ScreenHeight = over_window.winfo_screenheight()


    x = (ScreenWidth / 2) - (WindowWidth / 2)
    y = (ScreenHeight / 2) - (WindowHeight / 2)
        
    
    over_window.overrideredirect(True)
    over_window.geometry(f'{WindowWidth}x{WindowHeight}+{int(x)}+{int(y)}')
    over_window.resizable(False, False)
    
    
    InfoLabel = ctk.CTkLabel(master=over_window, text="THE WORD WAS:", font=("Aeriel", 20))
    InfoLabel.place(relx=0.5, rely=0.1, anchor="center")
    
    
    WordLabel = ctk.CTkLabel(master=over_window, text=word, font=("Aeriel", 20), text_color="red")
    WordLabel.place(relx=0.5, rely=0.253, anchor="center")
    
    
    RestartButton = ctk.CTkButton(master=over_window, text="RETRY", width=250, height=40, font=("Aeriel", 15), command=restart_over)
    RestartButton.place(relx=0.5, rely=0.5, anchor="center")
    
    
    QuitButton = ctk.CTkButton(master=over_window, text="QUIT", width=250, height=40, font=("Aeriel", 15), command=quit_over)
    QuitButton.place(relx=0.5, rely=0.72, anchor="center")
    
    
    
    
    
    over_window.mainloop()


def restart_over():
    global over_window, main_window
    main_window.destroy()
    main_game()
    
    
def quit_over():
    global over_window, main_window
    over_window.destroy()
    main_window.destroy()
    
    
def restart():
    global main_window, window_switch
    main_window.destroy()
    window_switch = "ab"
    main_game()
    
    
def quit():
    global main_window
    main_window.destroy()
    
    
def quit_passed():
    global main_window, passed_window
    print("here")
    passed_window.destroy()
    main_window.destroy()
    
    
def passed():
    global main_window, word, window_switch, passed_window
    window_switch="passed"
    
    
    WindowWidth = 500
    WindowHeight = 300
    FrameHeight = 500


    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")


    passed_window = ctk.CTk()


    ScreenWidth = passed_window.winfo_screenwidth()
    ScreenHeight = passed_window.winfo_screenheight()


    x = (ScreenWidth / 2) - (WindowWidth / 2)
    y = (ScreenHeight / 2) - (WindowHeight / 2)
        
    
    passed_window.overrideredirect(True)
    passed_window.geometry(f'{WindowWidth}x{WindowHeight}+{int(x)}+{int(y)}')
    passed_window.resizable(False, False)
    
    
    InfoLabel = ctk.CTkLabel(master=passed_window, text="YOU PASSED", font=("Aeriel", 20))
    InfoLabel.place(relx=0.5, rely=0.1, anchor="center")
    
    
    WordLabel = ctk.CTkLabel(master=passed_window, text=word, font=("Aeriel", 20), text_color="green")
    WordLabel.place(relx=0.5, rely=0.253, anchor="center")
    
    
    RestartButton = ctk.CTkButton(master=passed_window, text="PLAY AGAIN", width=250, height=40, font=("Aeriel", 15), command=restart_over)
    RestartButton.place(relx=0.5, rely=0.5, anchor="center")
    
    
    QuitButton = ctk.CTkButton(master=passed_window, text="QUIT", width=250, height=40, font=("Aeriel", 15), command=quit_passed)
    QuitButton.place(relx=0.5, rely=0.72, anchor="center")
    
    
    
    
    
    passed_window.mainloop()
    
    
def quit_main():
    global window
    window.destroy()
    


SplashScreen = ctk.CTk()


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


ScreenWidth = SplashScreen.winfo_screenwidth()
ScreenHeight = SplashScreen.winfo_screenheight()


x = (ScreenWidth / 2) - (WindowWidth / 2)
y = (ScreenHeight / 2) - (WindowHeight / 2)


SplashScreen.geometry(f'{WindowWidth}x{WindowHeight}+{int(x)}+{int(y)}')
SplashScreen.overrideredirect(True)


videoplayer = TkinterVideo(master=SplashScreen, scaled=True)
videoplayer.load("./hangman.mp4")
videoplayer.pack(expand=True, fill="both")
videoplayer.play()


SplashScreen.after(5000, StartScreen)
SplashScreen.mainloop()

