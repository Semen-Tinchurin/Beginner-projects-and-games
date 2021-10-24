from tkinter import *
from tkinter import messagebox
import pickle


root = Tk()
root.geometry("400x500")
root.title("Вход в систему")


def registration():
    text = Label(text="Для входа в систему зарегестрируйтесь!")
    text_log = Label(text="Введите логин: ")
    registr_login = Entry()
    text_password = Label(text="Введите пароль: ")
    registr_password = Entry()
    text_password2 = Label(text="Введите пароль еще раз: ")
    registr_password2 = Entry(show="*")
    button_reg = Button(text="Зарегистрироваться", command=lambda: save())

    text.pack()
    text_log.pack()
    registr_login.pack()
    text_password.pack()
    registr_password.pack()
    text_password2.pack()
    registr_password2.pack()
    button_reg.pack()

    def save():
        login_pass_save = {registr_login.get(): registr_password.get()}
        f = open("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()


def login():
    text_log = Label(text="Зарегестрировано...")
    text_enter_login = Label(text="Введите логин:")
    enter_login = Entry()
    text_enter_pass = Label(text="Введите пароль:")
    enter_pass = Entry(show="*")
    button_enter = Button(text="Войти", command=lambda: log_pass())

    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_pass.pack()
    button_enter.pack()

    def log_pass():
        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_pass.get() == a[enter_login.get()]:
                messagebox.showinfo("Вход выполнен")
            else:
                messagebox.showerror("Ошибка доступа")




registration()

root.mainloop()
