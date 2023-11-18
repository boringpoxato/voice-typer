import customtkinter
from subprocess import call
import playsound
import pyttsx3
# from voicetyper import main_voice

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"




engine = pyttsx3.init('sapi5')
vioces = engine.getProperty("voices")
engine.setProperty("voice" , vioces[1].id)


#Fun to speak

def speak (audio):
     engine.say(audio)
     engine.runAndWait()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        self.root = customtkinter.CTk()
        self.geometry(f"{650}x{450}")
        self.title("voice typer")


        engine = pyttsx3.init('sapi5')
        voices= engine.getProperty('voices') #getting details of current voice
        engine.setProperty('voice', voices[0].id)

        def start():
            file = open('TEXT FILES\Running_Status.txt' , "w")
            file.write('Running')
            file.close()
            speak('voice typer has started')
            call(['python' , 'main.py'])


        def english():    
            file = open('TEXT FILES\Language_Status.txt' , "w")
            file.write("English")
            file.close()
            speak("english")

        def gujrati():
            file = open('TEXT FILES\Language_Status.txt' , "w")
            file.write("Gujrati")
            file.close()
            speak('gujarati')

        def Hindi():
            file = open('TEXT FILES\Language_Status.txt' , "w")
            file.write("Hindi")
            file.close()
            speak('hindi')

        def stop():
            file = open('TEXT FILES\Running_Status.txt' , "w")
            file.write('Stoped')
            file.close()
            file = open("TEXT FILES\Language_Status.txt")
            file.write('none')
            file.close()

        frame = customtkinter.CTkFrame(master=self)
        frame.pack(pady=20 , padx = 60 , fill='both' , expand = True)

        lable = customtkinter.CTkLabel(master=frame, text='voice typer'  )
        lable.pack(pady= 15  , padx = 10)

        button = customtkinter.CTkButton(master=frame , text="English" ,  command=english)
        button.pack(pady = 15 , padx = 10 )

        button = customtkinter.CTkButton(master=frame , text="Gujarati" ,  command=gujrati)
        button.pack(pady = 15 , padx = 10 )

        button = customtkinter.CTkButton(master=frame , text="Hindi" ,  command=Hindi)
        button.pack(pady = 15 , padx = 10 )

        button = customtkinter.CTkButton(master=frame , text="Start" ,  command=start)
        button.pack(pady = 15 , padx = 10 )

        button = customtkinter.CTkButton(master=frame , text="Stop" ,  command=stop)
        button.pack(pady = 15 , padx = 10 )







if __name__ == "__main__":
    app = App()
    app.mainloop()

