import telebot
import openai

bot = telebot.TeleBot("6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io")
openai.api_key = "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"

@bot.message_handler(content_types=["text"])
def handle_text(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message.text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    bot.send_message(message.chat.id, response.choices[0].text)

bot.polling()