from tkinter import *
from tkinter import filedialog

def AskFile():
    global path
    path = filedialog.askopenfilename()
    npath = path.split('.')[0]
    from model import EnDeCoder
    model = EnDeCoder()
    if mode.get() == 0:
        newPath = npath + '.' + 'nbg'
        model.file_encode(input_path=path, output_path=newPath)
        tp['text'] = 'Файл зашифрован'
    elif mode.get() == 1:
        newPath = npath + '.' + 'dbg'
        model.file_decode(input_path=path, output_path=newPath)
        tp['text'] = 'Файл расшифрован'
    elif mode.get() == 2:
        newPath = npath + '.' + 'nbg'
        key = flk.get()
        model.file_encode_by_new_key(input_path=path, output_path=newPath, key=key)
        tp['text'] = f'Файл зашифрован c геоключом - {key}'


#vars
path = ''

#app
root = Tk()
root.geometry('300x150')
root.resizable(False, False)
root.title('Шифровщик / Расшифровщик файлов')

mode = IntVar()
mode.set(0)

fndflbttn = Button(root, text='Выбрать файл', command=AskFile)

flk = Entry(root)

ncd = Radiobutton(root, text='Зашифровать файл', variable=mode, value=0)
dcd = Radiobutton(root, text='Расшифровать файл', variable=mode, value=1)
ncdfltsnd = Radiobutton(root, text='Зашифровать файл для отправки', variable=mode, value=2)

tp = Label(text='Режим')



#pack

ncd.pack()
dcd.pack()
ncdfltsnd.pack()
flk.pack()
fndflbttn.pack()
tp.pack()
root.mainloop()