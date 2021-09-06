

chatbot = ChatBot(
    'Mr. Bot',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    logic_adapters = [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ],
    database_uri = 'sqlite:///database.sqlite3'
)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english"
)

print(chatbot.get_response("how are you"))
# Create a new trainer for the chatbot


# Train the chatbot based on the english corpus



# Get a response to an input statement


# trainer = ListTrainer(chatbot)

# Train the chat bot with a few responses
# trainer.train([
#     'How can I help you?',
#     'I want to create a chat bot',
#     'No, I have not'
#
# ])
