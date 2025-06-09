from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot( # create chatbot instance
    'TerminalBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3'
)

trainer = ChatterBotCorpusTrainer(chatbot) 
trainer.train('chatterbot.corpus.english') # train chatbot for english