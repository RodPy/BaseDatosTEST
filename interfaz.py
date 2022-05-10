import Tkinter as tk
from Tkinter import *

def holi():
	print ("Holii")


app = tk.TK()
alabra= tk.StringVar(app)
entrada=tk.StringVar(app)
tk.Wm.wm_title(app,"Monitoreo Ambiental")

tk.Entry(
    app,
    # fg="white",
    # bg="black",
    justify="center",
    textvariable=entrada
).pack(
    fill=tk.BOTH,
    expand=False
)

tk.Label(
    app,
    text=" Nombre",
    textvariable=palabra,
    justify="center"
).pack(
    fill=tk.BOTH,
    expand=False
)

tk.Button(
    app,
    text= "Aceptar ",
    bg="#00a8e8",
    command= holi(),
    relief="flat"
).pack(
    fill=tk.BOTH,
    expand=False
)


app.mainloop() # Refresca la app

