########################################################################
#Code: Python Code for Jira ticket creation using azure cognitive services.
#Date: 25-05-2023
#Version: 1.0
#Modified by: Chandravdan
##########################################################################

import tkinter as tk
import speech_recognition as sr
#from speech_recognition1 import *
import pyttsx3
import os
import azure.cognitiveservices.speech as speechsdk
from Jira_ticket import Rest_api_jira_call
import json

speech_config = speechsdk.SpeechConfig(subscription='f1ffa1eaaa674d92931a17ed09ac4094', region='eastus2')


r = sr.Recognizer()
engine = pyttsx3.init()

def send_message():
    user_message = entry_box.get()
    chat_log.insert(tk.END, "You: " + user_message + "\n")
    process_response(user_message)

flag = "False"

def process_response(message):
    # Implement your chatbot logic here to generate a response
    
    #response = "Hello, I'm a chatbot! How can i help you"
    #chat_log.insert(tk.END, "Bot: " + response + "\n")
    #speak(response)
    print ("Inside the response")
    

    if (message == "hello." or message == "Hello." or message == "Hey."):
        print("Inside if condition");
        response = "Hello, I'm a chatbot! How can i help you!"
        chat_log.insert(tk.END, "Bot: " + response + "\n")
        speak(response)

    elif (message == "Hi." or message == "hi." or message == "Good morning."):
	    response = "Hello, I'm a chatbot! How can i help you in this early morning!"
	    chat_log.insert(tk.END, "Bot: " + response + "\n")
	    speak(response)

    elif (message == "How are you?" or message == "How are you." or message == "How r u?"):
        response = "fine! and you?"
        chat_log.insert(tk.END, "Bot: " + response + "\n")
        speak(response)

    elif (message == "Fine." or message == "I am good." or message == "I am doing good." or message == "I'm good."):
	    response = "Great! how can I help you"
	    chat_log.insert(tk.END, "Bot: " + response + "\n")
	    speak(response)
        
    elif (message == "I want to create a JIRA ticket." or message == "Create JIRA ticket." or message == "Could you please help me to create jira ticket." or message == "Could you please help me to create jira ticket?."):
        response = "Ok.Sure, Could please let me know the exact issue to report?"
        chat_log.insert(tk.END, "Bot: " + response + "\n")
        speak(response)
        #flag = True

    elif ("I have an issue" in message) or ("I am working on" in message) or ("I am facing issue" in message):
        print("matched! for creating jira ticket using description")
        description1 = message
        summary1 = "TestfromPython"
        print(description1,summary1)
        import json
        result1,result2 =Rest_api_jira_call(summary1, description1)
        print("result1:", result1)
        print("result2:",result2)
        success = 0

        if(success == 0):
            #elif (message == "No. You can proceed with the same." or message == "No.You can proceed with the same." or message == "You can proceed with the same." or message == "Issue type is fine." or message == "Go ahead." or message == "No problem. Go ahead." or message == "No problem Go ahead."):
                response = "Sure. Please allow me sometime to generate JIRA ticket. I will update soon."
                chat_log.insert(tk.END, "Bot: " + response + "\n")
                speak(response)

                response = "Jira Ticket created successfully"
                chat_log.insert(tk.END, "Bot: " + response + "\n")
                speak(response)
                response = result1
                chat_log.insert(tk.END, "Bot: Please find Jira Ticket:" + response + "\n")
                speak(response)

                response = result2
                chat_log.insert(tk.END, "Bot: You can also use below link to check the created ticket:" + response + "\n")
                speak(response)

                print(response)
                #response = "Sure. Please allow me sometime to generate JIRA ticket. I will update soon."
                #chat_log.insert(tk.END, "Bot: Please find Jira Ticket:" + str(response) + ".\nYou can also use below link to check the created ticket:")
                #speak(str(response))




        

    elif (message == "yes." or message == "Yes." or message == "YES." or message == "I want to create a JIRA Ticket."):
        response = " Could you please tell me the project name?"
        chat_log.insert(tk.END, "Bot: " + response + "\n")
        speak(response)

    elif (message == "ecova support." or message == "support." or message == "Support." or message == "Ecova Support."):
        response = " Thanks. I am selecting the issue type as Bug for now. Would you like to modify it?"
        chat_log.insert(tk.END, "Bot: " + response + "\n")
        speak(response)

    elif (message == "No. You can proceed with the same." or message == "No.You can proceed with the same." or message == "You can proceed with the same." or message == "Issue type is fine." or message == "Go ahead." or message == "No problem. Go ahead." or message == "No problem Go ahead."):
        response = "Sure. Please allow me sometime to generate JIRA ticket. I will update soon."
        chat_log.insert(tk.END, "Bot: " + response + "\n")
        speak(response)
        flag = true

        if(flag == "true"):
            print("Flag true! for creating jira ticket now")
            Jira_ticket.Rest_api_jira_call(summary1, description1)

    
    elif (message == "Yes make it story." or message == "Yes." or message == "Use story"):
        response = " Sure, Modified. Please allow me sometime to generate JIRA ticket. I will update soon."
        chat_log.insert(tk.END, "Bot: " + response + "\n")
        speak(response)
        

    elif (message == "Thanks." or message == "Thank You." or message == "Thank you." or message == "Thank you so much" or message == "Thank you very much."):
        response = "Welcome!. Do you want to create new ticket?"
        chat_log.insert(tk.END, "Bot: " + response + "\n")
        speak(response)

    elif (message == ""):
        response = " Sorry! I didn't understand that. I am in Testing Phase. Could you please speak again! or you can use editor as well"
        chat_log.insert(tk.END, "Bot: " + response + "\n")
        speak(response)
    



    else:
	    response = " Sorry! I didn't understand that. Are you asking for jira ticket creation? Could you please speak again! or you can use editor as well ;) "
	    chat_log.insert(tk.END, "Bot: " + response + "\n")
	    speak(response)
    



    

def speak(text):

#####################Azure cognitive service-text-to-speech#########################

    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='en-US-JennyNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    #engine.say(text)
    engine.runAndWait()

def voice_input():
    #####################Azure cognitive service-speech-to-text#########################

    with sr.Microphone() as source:
        
        #audio = r.listen(source)
        speech_config = speechsdk.SpeechConfig(subscription='f1ffa1eaaa674d92931a17ed09ac4094', region='eastus2')
        speech_config.speech_recognition_language="en-US"

        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        print("Listening...")
        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("{}".format(speech_recognition_result.text))
    try:
        #text = r.recognize_google(audio)
        text=print("{}".format(speech_recognition_result.text))
        entry_box.delete(0, tk.END)
        entry_box.insert(tk.END, (speech_recognition_result.text))
        send_message()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
    except sr.RequestError as e:
        print("Error occurred: {0}".format(e))


root = tk.Tk()
root.title("Voice Chatbot")

chat_log = tk.Text(root, width=80, height=25)
entry_box = tk.Entry(root, width=50)
send_button = tk.Button(root, text="Send", command=send_message)

voice_input_button = tk.Button(root, text="Speak", command=voice_input)


chat_log.pack()
entry_box.pack()
send_button.pack()

voice_input_button.pack()

entry_box.focus_set()



if __name__ == "__main__":
    root.mainloop()
