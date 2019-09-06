from chatterbot  import ChatBot
from chatterbot.trainers import ListTrainer
 
bot = ChatBot('AI')

trainer = ListTrainer(bot)
 
conversation = list(open('chats.txt','r').readlines())
 
trainer.train(conversation)

while True:
    message = input('You:')
    if message.strip()!= 'Bye':
     reply = bot.get_response(message)
    print('ChatBot:',reply)
    if message.strip()=='Bye':
        print('ChatBot:Bye')
        break