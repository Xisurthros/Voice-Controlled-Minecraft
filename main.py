import speech_recognition as sr  # pip install SpeechRecognition
import os
from gtts import gTTS  # pip install gTTS    ALSOOOOO pip install pipwin AND THEN pipwin install pyaudio
import warnings
import pydirectinput
import time

warnings.filterwarnings('ignore')


def recordAudio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say something!')
        audio = r.listen(source)

    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:  # Checks for unknown errors
        print('Google Speech Recognition could not understand the audio, unknown error')
    except sr.RequestError as e:
        print('Request results from google speech recognition service error' + e)

    return data


while True:
    try:
        text = recordAudio()

        if 'break' in text:
            pydirectinput.mouseDown()
            time.sleep(3.1)
            pydirectinput.mouseUp()

        if 'place' in text:
            pydirectinput.mouseDown(button='right')
            pydirectinput.mouseUp(button='right')

        if 'walk' in text:
            if 'left' in text:
                pydirectinput.keyDown('a')
                time.sleep(2)
                pydirectinput.keyUp('a')
            elif 'right' in text:
                pydirectinput.keyDown('d')
                time.sleep(2)
                pydirectinput.keyUp('d')
            elif 'backwards' in text:
                pydirectinput.keyDown('s')
                time.sleep(2)
                pydirectinput.keyUp('s')
            else:
                pydirectinput.keyDown('w')
                time.sleep(2)
                pydirectinput.keyUp('w')

        if 'run' in text:
            if 'jump' in text:
                x1 = 5
                x2 = 0
                pydirectinput.keyDown('ctrl')
                pydirectinput.keyDown('w')

                while x2 != x1:
                    pydirectinput.press('space')
                    time.sleep(0.3)
                    x2 += 1

                pydirectinput.keyUp('ctrl')
                pydirectinput.keyUp('w')
            else:
                pydirectinput.keyDown('ctrl')
                pydirectinput.keyDown('w')
                time.sleep(2)
                pydirectinput.keyUp('ctrl')
                pydirectinput.keyUp('w')

        if 'look' in text:
            if 'right' in text:
                pydirectinput.move(298, 0)

            elif 'left' in text:
                pydirectinput.move(-298, 0)

            elif 'up' in text:
                pydirectinput.move(0, -298)

            elif 'down' in text:
                pydirectinput.move(0, 298)

            elif 'backward' in text:
                pydirectinput.move(298, 0)
                time.sleep(0.5)
                pydirectinput.move(298, 0)
                time.sleep(0.5)
                pydirectinput.move(298, 0)
                time.sleep(0.5)
                pydirectinput.move(298, 0)

        if 'turn' in text:
            pydirectinput.move(298, 0)
            time.sleep(0.25)
            pydirectinput.move(298, 0)
            time.sleep(0.25)
            pydirectinput.move(298, 0)
            time.sleep(0.25)
            pydirectinput.move(298, 0)

        if 'say' in text:
            pydirectinput.press('t')
            pydirectinput.write(text[4:])
            pydirectinput.press('enter')

    except:
        print('Unexpected Error')