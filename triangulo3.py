import tkinter as tk

def triangulo():
   base = int(entrada_prim.get())
   altura = int(entrada_seg.get())
   areatriangulo = base*altura/2
   etiqueta_resultado.config(text=f"La base es {base}, la altura es {altura}, y su area es  {areatriangulo}") 


ventana = tk.Tk()
ventana.title("operacion de areas ")
ventana.geometry("500x400")



etiqueta = tk.Label(ventana, text="Ingresa tu base:")
etiqueta.pack()

entrada_prim = tk.Entry(ventana)
entrada_prim.pack()

etiqueta = tk.Label(ventana, text="ingresa tu altura: ")
etiqueta.pack()

entrada_seg = tk.Entry(ventana)
entrada_seg.pack()

boton = tk.Button(ventana, text="triangulo", command=triangulo)
boton.pack()

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()

