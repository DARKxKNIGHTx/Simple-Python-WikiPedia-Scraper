from tkinter import *
import wikipedia
s=''
def btn_clicked(event=None):
    global s
    l.config(text="")
    er.config(text="")
    print(entry0.get())
    try :
     s=wikipedia.summary(entry0.get(),300)
    except wikipedia.DisambiguationError:
     er.config(text="Please try again by Specifying your topic more")
    except wikipedia.PageError:
     er.config(text="No details found")
    chk=0
    init = 0
    for i in range(len(s)):
        chk+=1
        if chk-init>90:
            if s[chk]==" ":
                s=s[0:chk+1] + "\n"+s[chk+1:]
                init+=90
    print(s)
    l.config(text=s)
    s=''
window = Tk()

window.geometry("1097x616")
window.configure(bg = "#ffb4b4")
canvas = Canvas(
    window,
    bg = "#ffb4b4",
    height = 616,
    width = 1097,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)



canvas.create_rectangle(
    0, 0, 0+364, 0+616,
    fill = "#ffffff",
    outline = "")


canvas.create_rectangle(
    371, 65, 371+717, 65+541,
    fill = "#ffffff",
    outline = "")

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")
b0.bind("<Return>",btn_clicked)

b0.place(
    x = 127, y = 308,
    width = 110,
    height = 87)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    178.5, 221.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffb4b4",
    highlightthickness = 0)
entry0.focus_set()

entry0.place(
    x = 55.0, y = 195,
    width = 247.0,
    height = 50)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    307.0, 569.5,
    image=background_img)

canvas.create_text(
    178.5, 268.0,
    text = "Report Bug",
    fill = "#000000",
    font = ("None", int(10.0)))

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    719.0, 33.5,
    image=background_img)
l=Label(text=s,bg = "#ffffff",font=("Arial",12))
l.place(x=371,y=65)
er=Label(text='',bg = "#ffffff",foreground="red")
er.place(x=55,y=170)

window.resizable(False, False)
window.mainloop()










