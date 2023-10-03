import tkinter as tk

def guardar():
    nombre = tb_nombre.get()
    apellido = tb_apellido.get()
    edad = tb_edad.get()
    estatura = tb_estatura.get()
    telefono = tb_telefono.get()
    
    genero = ""
    if var_genero.get() == 1:
        genero= "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"    

    datos = f"Nombres: {nombre}\nApellidos: {apellido}\nTeléfono: {telefono} kg\nEstatura: {estatura} cm\nEdad: {edad} años\nGénero: {genero}"
    with open("Datosformulario.txt","a") as archivo:
        archivo.write(datos + "\n\n")
        
    tk.messagebox.showinfo("Información", "Datos guardados correctamente:\n\n" + datos)
    
    tb_nombre.delete(0,"end")
    tb_apellido.delete(0,"end")
    tb_edad.delete(0,"end")
    tb_estatura.delete(0,"end")
    tb_telefono.delete(0,"end")
    var_genero.set(None)

def borrarCampos():
    cancelar()
    
def cancelar():
    tb_nombre.delete(0,"end")
    tb_apellido.delete(0,"end")
    tb_edad.delete(0,"end")
    tb_estatura.delete(0,"end")
    tb_telefono.delete(0,"end")
    var_genero.set(None)
    
ventana = tk.Tk()
ventana.title("Practica 4")

lbl_nombre = tk.Label(ventana, text="Nombre:")
lbl_nombre.pack()
tb_nombre = tk.Entry(ventana)
tb_nombre.pack()

lbl_apellido = tk.Label(ventana, text="Apellido:")
lbl_apellido.pack()
tb_apellido = tk.Entry(ventana)
tb_apellido.pack()

lbl_edad = tk.Label(ventana, text="Edad:")
lbl_edad.pack()
tb_edad = tk.Entry(ventana)
tb_edad.pack()

lbl_estatura = tk.Label(ventana, text="Estatura:")
lbl_estatura.pack()
tb_estatura = tk.Entry(ventana)
tb_estatura.pack()

lbl_telefono = tk.Label(ventana, text="Teléfono:")
lbl_telefono.pack()
tb_telefono = tk.Entry(ventana)
tb_telefono.pack()

var_genero = tk.IntVar()
lbl_genero = tk.Label(ventana, text="Género:")
lbl_genero.pack()

radbtn_hombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
radbtn_hombre.pack()

radbtn_mujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
radbtn_mujer.pack()

btn_guardar = tk.Button(ventana,text="Guardar",command = guardar)
btn_guardar.pack()

btn_cancelar = tk.Button(ventana,text="Cancelar",command = cancelar)
btn_cancelar.pack()


ventana.mainloop()
