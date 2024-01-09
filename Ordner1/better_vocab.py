from tkinter import Tk, Label, StringVar, Entry, Button, Radiobutton

class Vocabulary:
    def __init__(self):
        self.words = {}
        self.load_words()

    def load_words(self):
        with open(file='wörter_vocabulary', mode='r') as file:
            for line in file:
                line = line.strip()
                mapping = line.split(' bedeutet ')
                if len(mapping) == 2:
                    self.words[mapping[0]] = mapping[1]

    def add_word(self, word, translation):
        self.words[word] = translation
        with open(file='wörter_vocabulary', mode='w') as file:
            for key, value in self.words.items():
                file.write(f'{key} bedeutet {value}\n')

    def translate_word(self, word):
        return self.words.get(word, 'Wort nicht gefunden')

def add_word_window(vocabulary):
    window = Tk()
    window.geometry('200x130')
    word_entry = Entry(master=window)
    translation_entry = Entry(master=window)
    
    def add_word():
        word = word_entry.get()
        translation = translation_entry.get()
        vocabulary.add_word(word, translation)
        window.destroy()
    word_entry.configure(width=150)
    translation_entry.configure(width=150)
    button = Button(master=window, command=add_word, text='Bestätigen')
    button.pack(side='bottom')
    Label(master=window,text='Wort: ').pack()
    word_entry.pack()
    Label(master=window,text='Übersetzung: ').pack()
    translation_entry.pack()
    
    window.mainloop()

def translate_word_window(vocabulary):
    window = Tk()
    entry = Entry(master=window)
    label = Label(master=window, text='Geben Sie das Wort ein')

    def translate():
        word = entry.get()
        result = vocabulary.translate_word(word)
        label.config(text=result)

    button = Button(master=window, command=translate, text='übersetzen')

    entry.pack()
    label.pack()
    button.pack()
    
    window.mainloop()
vocabulary = Vocabulary()
fenster = Tk('Menü')
fenster.geometry('200x100')
hinzufügen_radiobutton = Radiobutton(master=fenster, command=lambda: add_word_window(vocabulary), text='Wörter hinzufügen')
nutzen_radiobutton = Radiobutton(master=fenster, command=lambda: translate_word_window(vocabulary), text='Wörterübersetzung')
hinzufügen_radiobutton.pack()
nutzen_radiobutton.pack()
fenster.mainloop()
