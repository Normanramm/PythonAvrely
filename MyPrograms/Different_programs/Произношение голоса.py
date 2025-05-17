import pyttsx3


def golos():
    tts = pyttsx3.init()

    voices = tts.getProperty('voices')

    # Задать голос по умолчанию
    tts.setProperty('voice', 'ru')

    # Попробовать установить предпочтительный голос
    for voice in voices:
        if voice.name == 'Aleksandr':
            tts.setProperty('voice', voice.id)

    tts.say(input("Введите текст и он будет звучать: "))
    tts.runAndWait()


golos()
