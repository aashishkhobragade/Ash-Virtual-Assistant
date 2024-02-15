import tkinter as tk
from tkinter import Scrollbar, Text, Entry, Button
import openai
from openai import OpenAI
import os
import speech_recognition as sr

# Insert your OpenAI API key here
openai.api_key = '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'

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Assistant - NEEL")
        self.root.geometry("800x600")
        self.root.configure(bg="#0174BE")

        self.chat_frame = Text(root, wrap=tk.WORD, font=("Arial", 12))
        self.chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.scrollbar = Scrollbar(self.chat_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_frame.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.chat_frame.yview)

        self.message_input = Entry(root)
        self.message_input.pack(padx=10, pady=10, fill=tk.BOTH, expand=False)

        send_button = Button(root, text="Send", command=self.send_message)
        send_button.pack()

        self.microphone_button = Button(root, text="Microphone", command=self.start_listening)
        self.microphone_button.pack()

        self.recognizer = sr.Recognizer()

    def send_message(self):
        user_message = self.message_input.get()
        if user_message:
            self.display_user_message(user_message)
            self.message_input.delete(0, tk.END)

            bot_response = self.chat_with_gpt3(user_message)
            self.display_bot_message(bot_response)

    def start_listening(self):
        with sr.Microphone() as source:
            self.display_bot_message("Listening...")
            self.microphone_button.configure(state="disabled")

            audio = self.recognizer.listen(source)

            try:
                user_message = self.recognizer.recognize_google(audio)
                self.display_user_message(user_message)
                bot_response = self.chat_with_gpt3(user_message)
                self.display_bot_message(bot_response)
            except sr.UnknownValueError:
                self.display_bot_message("Sorry, I couldn't understand the audio.")
            except sr.RequestError as e:
                self.display_bot_message(f"Speech recognition request failed: {e}")

            self.microphone_button.configure(state="active")

    def chat_with_gpt3(self, user_message):
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            prompt=f"Ashish: {user_message}\nNeel:",
            max_tokens=100
        )
        return response.choices[0].text

    def display_user_message(self, message):
        self.display_message("You: " + message, "blue")

    def display_bot_message(self, message):
        self.display_message("Neel: " + message, "red")
        say(message)

    def display_message(self, message, color):
        self.chat_frame.configure(state='normal')
        self.chat_frame.insert(tk.END, message + "\n", color)
        self.chat_frame.tag_add(color, f"{self.chat_frame.index(tk.END)}-2c", tk.END)
        self.chat_frame.tag_config(color, foreground=color)
        self.chat_frame.configure(state='disabled')
        self.chat_frame.see(tk.END)

def main():
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()

def say(text):
    os.system(f'say "{text}"')

if __name__ == "__main__":
    main()
