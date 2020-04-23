from tkinter import *
# pip install mypassmaker
from mypassmaker import Password
# pip install pyperclip
import pyperclip

# فانکشن برای کپی کردن در کلیپ بورد
def copy():
    return pyperclip.copy(password_entry.get())

# فانکشن ساختن پسورد با دکمه generate
def keep_generate():
    # اگر طول پسورد رو بهش ندادیم 10 در نظر بگیره
    if len(length_entry.get()) < 1:
        length = 10
    else:
        # در غیر این صورت طول که ما بهش دادیم درنظر میگیره
        length = int(length_entry.get())
    my_pass = Password.generate(length)
    new_text = my_pass
    # وقتی دکمه generate رو نزدیم entry پسورد ازاد باشه
    password_entry.config(state="normal")

    #  مقادیر قبلی رو حذف میکنه اگر delete نزاریم پسورد جدید و قدیمی قاطی میشه
    # از خونه 0 تا اخر(End) پاک میکنه
    password_entry.delete(0, END)

    # از خونه اول(0) تا اخر پسور جدید رو میزاره
    # در واقع باحث میشه با زدن دوباره دکمه (generate) پسورد جدید بده
    password_entry.insert(0, new_text)
    # وقتی دکمه رو زدیم پسورد قابل دیدن و کپی کردن بشه (غیر قابل تعغیر)
    password_entry.config(state="readonly")


root = Tk()
# بگراند صفحه bg
root["bg"] = "tan"
# سایز و موقعیت باز شدن صفحه روی مانیتور
root.geometry("448x270+400+200")
# title
root.title("random password")
# اندازه صفحه غیر قابل تعغیر باشه
root.resizable(False, False)

# فونت های مورد استفاده و سایزشون
label_font = ("time", 13, "bold")
entry_font = ("time", 13)
entry_font_2 = ("time", 10)
button_font = ("time", 10, "bold")

# از StringVar () معمولاً برای ویرایش متن ویجت خیلی سریع استفاده میشه
# متغیر برای ویجت password_entry
the_passWord = StringVar()
# ساخت ویجت (entry)برای پسورد
password_entry = Entry(root, bg="silver", font=entry_font, fg="green", bd=3, textvariable=the_passWord)
password_entry.grid(row=2, column=4)  # تعریف سطر و ستون
# ساخت لیبل پسورد
password_lbl = Label(root, text="password: ", font=label_font, fg="navy", bg="tan")
password_lbl.grid(row=2, column=3, padx=15)  # تعریف سطر و ستون و فاصله از محور x
# دکمه برای کپی کردن
# رنگ متن fg
# تابعت از فانکشهای که قبلا ساختیم با دستور (command)
button_copy = Button(root, text="copy", font=button_font, fg="navy", command=copy)
button_copy.grid(column=4, row=4, pady=5)  # تعریف سطر و ستون و فاصله از محور y
# دکمه generate
button_generate = Button(root, text="generate", font=button_font, fg="navy", command=keep_generate)
button_generate.grid(column=5, row=2, padx=10)

# لیبل طول
length_lbl = Label(root, text="length:", font=label_font, bg="tan", fg="navy")
length_lbl.grid(row=0, column=3, pady=60, padx=15)
# ویجتی که طول متن رو بهش میدیم
length_entry = Entry(root, bg="lightgrey", font=entry_font_2, fg="green", bd=3)
length_entry.grid(row=0, column=4)

# mainloop برنامه رو اماده اجرا میکنه
root.mainloop()
