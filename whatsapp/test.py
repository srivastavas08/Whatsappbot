''' Just ChatterBot with a tkinter gui, with a trained conversation, no ELIZA yet implemented. '''

import tkinter as tk

try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText
import time

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer


class TkinterGUIExample(tk.Tk):

    def __init__(self, *args, **kwargs):
        '''
        Create & set window variables.
        '''
        tk.Tk.__init__(self, *args, **kwargs)

        self.chatbot = ChatBot("No Output",
                               storage_adapter = "chatterbot.adapters.storage.JsonFileStorageAdapter",
                               silence_performance_warning = True,
                               logic_adapters = [
                                   "chatterbot.adapters.logic.ClosestMatchAdapter",
                                   "chatterbot.adapters.logic.TimeLogicAdapter"
                               ],
                               input_adapter = "chatterbot.adapters.input.VariableInputTypeAdapter",
                               output_adapter = "chatterbot.adapters.output.OutputFormatAdapter",
                               database = "../database.db"
                               )
        self.chatbot.set_trainer(ListTrainer)
        my_name = [
            "What is your name?",
            "My name is Gideon."]
        self.chatbot.train(my_name)

        self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        self.chatbot.train("chatterbot.corpus.english")
        self.title("Chatterbot")

        self.initialize()

    def initialize(self):
        '''
        Set window layout.
        '''
        self.grid()

        self.usr_input = ttk.Entry(self, state = 'normal')
        self.usr_input.grid(column = 0, row = 0, sticky = 'nesw', padx = 3, pady = 3)

        self.respond = ttk.Button(self, text = 'Get Response', command = self.get_response)
        self.respond.grid(column = 1, row = 0, sticky = 'nesw', padx = 3, pady = 3)

        self.conversation_lbl = ttk.Label(self, anchor = tk.E, text = 'Conversation:')
        self.conversation_lbl.grid(column = 0, row = 1, sticky = 'nesw', padx = 3, pady = 3)

        self.conversation = ScrolledText.ScrolledText(self, state = 'disabled')
        self.conversation.grid(column = 0, row = 2, columnspan = 2, sticky = 'nesw', padx = 3, pady = 3)

    def get_response(self):
        '''
        Get a response from the chatbot &
        display it.
        '''
        user_input = self.usr_input.get()
        self.usr_input.delete(0, tk.END)

        response = self.chatbot.get_response(user_input)

        self.conversation['state'] = 'normal'
        self.conversation.insert(
            tk.END, "Human: " + user_input + "\n" + "Gideon: " + str(response.text) + "\n"
        )
        self.conversation['state'] = 'disabled'

        time.sleep(0.5)


gui_example = TkinterGUIExample()
gui_example.mainloop()
