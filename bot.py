from simpletelegrambot import telegrambot
def on_message_receive(bot, message):
    msg_text = message['text']
    if msg_text=="Hii":
        bot.send_message("HELLO")
    print(msg_text)
def main():
    bot = telegrambot.TelegramBot('')
    bot.set_message_handler(on_message_receive)
    bot.wait_for_messages()
if __name__ == '__main__':
    main()
