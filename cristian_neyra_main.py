# Import Segment
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pymysql import NULL
import funciones
import pdf
import csv

# Global and Class definitions Segment
global lis
lis = list()

# Main program Segment
""" Se define el area de trabajo de la ventana """
ventana = Tk()
ventana.title("Ventana")
ventana.geometry("650x400")

""" Segmento de codigo que define la ventana emergente para ingresar nuevos Pacientes """
def nuevopaciente():
    #limpia los campos de texto
    def limpiar():
        txtRut.delete(0,'end')
        txtNombre.delete(0,'end')
        txtApellido.delete(0,'end')
        txtEmail.delete(0,'end')
        txtTelefono.delete(0,'end')
    
    #Agrega a la BD los datos ingresados en el formulario
    def agregar():
        funciones.insertpaciente(txtRut.get(),txtNombre.get(),txtApellido.get(),txtEmail.get(),txtTelefono.get())
        limpiar()
    
    #Se define el area de trabajo de la ventana para ingresar nuevos Pacientes
    
    nuevopa = Toplevel(ventana)
    nuevopa.title("Agregar Paciente")
    nuevopa.geometry("300x500")
    lblTitulo = Label(nuevopa, text='Agregar Nuevo Paciente', font='Calibri 18').pack()
    lblrut = Label(nuevopa, text='Rut', font='Calibri 18').pack()
    rut = StringVar()
    txtRut=Entry(nuevopa, font='Calibri 16', textvariable=rut)
    txtRut.pack()
    lblnombre = Label(nuevopa, text='Nombre', font='Calibri 18').pack()
    nombre = StringVar()
    txtNombre=Entry(nuevopa, font='Calibri 16', textvariable=nombre)
    txtNombre.pack()
    lblapellido = Label(nuevopa, text='Apellido', font='Calibri 18').pack()
    apellido = StringVar()
    txtApellido=Entry(nuevopa, font='Calibri 16', textvariable=apellido)
    txtApellido.pack()
    lblemail = Label(nuevopa, text='Email', font='Calibri 18').pack()
    email = StringVar()
    txtEmail=Entry(nuevopa, font='Calibri 16', textvariable=email)
    txtEmail.pack()
    lbltelefono = Label(nuevopa, text='Teléfono', font='Calibri 18').pack()
    telefono = StringVar()
    txtTelefono=Entry(nuevopa, font='Calibri 16', textvariable=telefono)
    txtTelefono.pack()
    lblsalto3 = Label(nuevopa, text='', font='Calibri 5').pack()
    btnAgregar = Button(nuevopa, text='Agregar Paciente', font='Calibri 16', command=agregar).pack()

""" Segmento de codigo que define la ventana emergente para CRUD de Pacientes """
def crudpaciente():
    # Limpia los campos de Texto
    def limpiar():
        txtRut.delete(0,'end')
        txtNombre.delete(0,'end')
        txtApellido.delete(0,'end')
        txtEmail.delete(0,'end')
        txtTelefono.delete(0,'end')
    
    # Busca los datos de un paciente y los asocia a los Entry
    def buscarpaciente():
        rut=txtRut.get()
        infopaciente = funciones.buscapaciente(rut)
        # Valida que el Result Set no sea nulo y asosia los Entry con los datos de la consulta
        if infopaciente:
            nombre.set(str(infopaciente[1]))
            apellido.set(str(infopaciente[2]))
            email.set(str(infopaciente[3]))
            telefono.set(str(infopaciente[4]))
        else:
            messagebox.showinfo("Error", "La consulta no ha retornado valores o el criterio de busqueda no es el correco.")
            limpiar()
        

    def actualizarpaciente():
        # Actualización de los datos de un paciente
        try:
            funciones.updatepaciente(rut.get(),nombre.get(),apellido.get(),email.get(),telefono.get())
            limpiar()
        except:
            return
    
    def eliminarpaciente():
        # Eliminar datos de un paciente
        try:
            funciones.deletepaciente(rut.get())
            limpiar()
        except:
            return

    # Se define la ventana de trabajo para el CRUD Paciente
    crudpa=Toplevel(ventana)
    crudpa.title("CRUD de Paciente")
    crudpa.geometry("300x550")

    lblTitulo = Label(crudpa, text='Administración de Pacientes', font='Calibri 18').pack()
    lblrut = Label(crudpa, text='Rut', font='Calibri 18').pack()
    rut = StringVar()
    txtRut=Entry(crudpa, font='Calibri 16', textvariable=rut)
    txtRut.pack()
    lblnombre = Label(crudpa, text='Nombre', font='Calibri 18').pack()
    nombre = StringVar()
    txtNombre=Entry(crudpa, font='Calibri 16', textvariable=nombre)
    txtNombre.pack()
    lblapellido = Label(crudpa, text='Apellido', font='Calibri 18').pack()
    apellido = StringVar()
    txtApellido=Entry(crudpa, font='Calibri 16', textvariable=apellido)
    txtApellido.pack()
    lblemail = Label(crudpa, text='Email', font='Calibri 18').pack()
    email = StringVar()
    txtEmail=Entry(crudpa, font='Calibri 16', textvariable=email)
    txtEmail.pack()
    lbltelefono = Label(crudpa, text='Teléfono', font='Calibri 18').pack()
    telefono = StringVar()
    txtTelefono=Entry(crudpa, font='Calibri 16', textvariable=telefono)
    txtTelefono.pack()
    lblsalto4 = Label(crudpa, text='', font='Calibri 5').pack()
    btnBuscar = Button(crudpa, text='Buscar Paciente', font='Calibri 16', command=buscarpaciente).pack()
    lblsalto5 = Label(crudpa, text='', font='Calibri 5').pack()
    btnActualizar = Button(crudpa, text='Actualizar Paciente', font='Calibri 16', command=actualizarpaciente).pack()
    lblsalto6 = Label(crudpa, text='', font='Calibri 5').pack()
    btnEliminar = Button(crudpa, text='Eliminar Paciente', font='Calibri 16', command=eliminarpaciente).pack()

""" Segmento de codigo que define la ventana emergente para ingresar nuevos Doctores """
def nuevodoctor():
    #limpia los campos de texto
    def limpiar():
        txtIddoctor.delete(0,'end')
        txtNombredoc.delete(0,'end')
        txtProfesion.delete(0,'end')
        txtApodo.delete(0,'end')
        txtRutpaciente.delete(0,'end')
    
    #Agrega a la BD los datos ingresados en el formulario
    def agregar():
        paciente=funciones.buscapaciente(txtRutpaciente.get())
        # Valida que el paciente exista en el sistems, en caso contrario no almacena la información asociada
        if paciente:
            funciones.insertdoctor(txtIddoctor.get(),txtNombredoc.get(),txtProfesion.get(),txtApodo.get(),txtRutpaciente.get())
            limpiar()
        else:
            messagebox.showerror("Error de Sistema", "Debe ingresar el RUT de un Paciente que exista en el sistema, favor de revisar los datos ingresados, en caso contrario primero debe crear al Paciente")
    
    #Se define el area de trabajo de la ventana para ingresar nuevos Pacientes
    
    nuevodoc = Toplevel(ventana)
    nuevodoc.title("Agregar Doctor")
    nuevodoc.geometry("300x500")
    lblTitulo = Label(nuevodoc, text='Agregar Nuevo Doctor', font='Calibri 18').pack()
    lblIddoctor = Label(nuevodoc, text='ID Doctor', font='Calibri 18').pack()
    iddoctor = StringVar()
    txtIddoctor=Entry(nuevodoc, font='Calibri 16', textvariable=iddoctor)
    txtIddoctor.pack()
    lblNombredoc = Label(nuevodoc, text='Nombre Doctor', font='Calibri 18').pack()
    nombredoc = StringVar()
    txtNombredoc=Entry(nuevodoc, font='Calibri 16', textvariable=nombredoc)
    txtNombredoc.pack()
    lblProfesion = Label(nuevodoc, text='Profesión', font='Calibri 18').pack()
    profesion = StringVar()
    txtProfesion=Entry(nuevodoc, font='Calibri 16', textvariable=profesion)
    txtProfesion.pack()
    lblApodo = Label(nuevodoc, text='Apodo', font='Calibri 18').pack()
    apodo = StringVar()
    txtApodo=Entry(nuevodoc, font='Calibri 16', textvariable=apodo)
    txtApodo.pack()
    lblRutpaciente = Label(nuevodoc, text='RUT Paciente', font='Calibri 18').pack()
    rutpaciente = StringVar()
    txtRutpaciente=Entry(nuevodoc, font='Calibri 16', textvariable=rutpaciente)
    txtRutpaciente.pack()
    lblsalto7 = Label(nuevodoc, text='', font='Calibri 5').pack()
    btnAgregar = Button(nuevodoc, text='Agregar Doctor', font='Calibri 16', command=agregar).pack()

""" Segmento de codigo que define la ventana emergente para CRUD de Doctores """
def cruddoctor():
    # Limpia los campos de Texto
    def limpiar():
        txtIddoctor.delete(0,'end')
        txtNombre.delete(0,'end')
        txtProfesion.delete(0,'end')
        txtApodo.delete(0,'end')
        txtRutpaciente.delete(0,'end')
    
    # Busca los datos de un paciente y los asocia a los Entry
    def buscarmedico():
        iddoc=txtIddoctor.get()
        infodoctor = funciones.buscardoctor(iddoc)
        # Valida que el Result Set no sea nulo y asosia los Entry con los datos de la consulta
        if infodoctor:
            nombredoctor.set(str(infodoctor[1]))
            profesion.set(str(infodoctor[2]))
            apodo.set(str(infodoctor[3]))
            rutpaciente.set(str(infodoctor[4]))
        else:
            messagebox.showinfo("Error", "La consulta no ha retornado valores o el criterio de busqueda no es el correco.")
            limpiar()
        

    def actualizarmedico():
        # Actualización de los datos de un paciente
        try:
            funciones.updatedoctor(iddoctor.get(),nombredoctor.get(),profesion.get(),apodo.get(),rutpaciente.get())
            limpiar()
        except:
            return
    
    def eliminarmedico():
        # Eliminar datos de un paciente
        try:
            funciones.deletedoctor(iddoctor.get())
            limpiar()
        except:
            return

    # Se define la ventana de trabajo para el CRUD Paciente
    cruddoc=Toplevel(ventana)
    cruddoc.title("CRUD de Doctor")
    cruddoc.geometry("300x550")

    lblTitulo = Label(cruddoc, text='Administración de Doctores', font='Calibri 18').pack()
    lbliddoctor = Label(cruddoc, text='ID Doctor', font='Calibri 18').pack()
    iddoctor = StringVar()
    txtIddoctor=Entry(cruddoc, font='Calibri 16', textvariable=iddoctor)
    txtIddoctor.pack()
    lblnombre = Label(cruddoc, text='Nombre', font='Calibri 18').pack()
    nombredoctor = StringVar()
    txtNombre=Entry(cruddoc, font='Calibri 16', textvariable=nombredoctor)
    txtNombre.pack()
    lblprofesion = Label(cruddoc, text='Profesión', font='Calibri 18').pack()
    profesion = StringVar()
    txtProfesion=Entry(cruddoc, font='Calibri 16', textvariable=profesion)
    txtProfesion.pack()
    lblApodo = Label(cruddoc, text='Apodo', font='Calibri 18').pack()
    apodo = StringVar()
    txtApodo=Entry(cruddoc, font='Calibri 16', textvariable=apodo)
    txtApodo.pack()
    lblrutpaciente = Label(cruddoc, text='RUT Paciente', font='Calibri 18').pack()
    rutpaciente = StringVar()
    txtRutpaciente=Entry(cruddoc, font='Calibri 16', textvariable=rutpaciente)
    txtRutpaciente.pack()
    lblsalto4 = Label(cruddoc, text='', font='Calibri 5').pack()
    btnBuscar = Button(cruddoc, text='Buscar Doctor', font='Calibri 16', command=buscarmedico).pack()
    lblsalto5 = Label(cruddoc, text='', font='Calibri 5').pack()
    btnActualizar = Button(cruddoc, text='Actualizar Doctor', font='Calibri 16', command=actualizarmedico).pack()
    lblsalto6 = Label(cruddoc, text='', font='Calibri 5').pack()
    btnEliminar = Button(cruddoc, text='Eliminar Doctor', font='Calibri 16', command=eliminarmedico).pack()

""" Limpia la grilla de datos """
def limpiagrilla():
    for i in grilla.get_children():
        grilla.delete(i)
    ventana.update()

""" Segmento de codigo que define el proceso de llenado de la grilla con los datos requeridos """
def llenargrilla():
    # Si existen datos llena la grilla con la informacion contenida en la BD
    try:
        limpiagrilla()
        lis = funciones.buscartodo()
        i=0
        # Valida que el set de datos no sea nulo
        if lis:
            # Ciclo que llena la grilla con la información
            for datos in lis:
                grilla.insert('',i,text="",values=(datos[0], datos[1], datos[2], datos[3], datos[4],datos[5]))
                i=i+1
            btnExportar['state']=NORMAL

        else:
            messagebox.showinfo("Sin Datos","No se cuenta con datos en el sistema que permitan llenar la Grilla")
    except:
        messagebox.showerror("Error", "Error al cargar los datos, intente nuevamente.")

""" Segmento de codigo para la exportación de la grilla a CSV"""
def exportarcsv():
    try:
        # se llena la lista con el resultado de la consulta sql y se exporta a archivo CSV
        lis = funciones.buscartodo()
        miarchivo= open('exportdata.csv','w')
        with miarchivo:
            escribir = csv.writer(miarchivo)
            escribir.writerows(lis)
        
        messagebox.showinfo("CSV", "Exportación de los datos del Treeview a CSV realizado de manera exitosa.")
    
    except:
        messagebox.showerror("Error", "No es posible el poder exportar los datos del Treeview a un archivo CSV, asegurese de cargar el Treeview antes de realizar esta acción.")

""" Se define el menu de la aplicación """

menubar = Menu(ventana)
ventana.config(menu=menubar)
doctormenu = Menu(menubar,tearoff=0)
pacientemenu =  Menu(menubar,tearoff=0)
pacientemenu.add_command(label="Nuevo Paciente",command=nuevopaciente)
pacientemenu.add_command(label="CRUD Paciente",command=crudpaciente)
pacientemenu.add_command(label='Informe de Pacientes', command=pdf.exportapacientespdf)
pacientemenu.add_separator()
pacientemenu.add_command(label="Salir", command=ventana.quit)
menubar.add_cascade(label="Pacientes", menu=pacientemenu)

doctormenu.add_command(label="Nuevo Doctor",command=nuevodoctor)
doctormenu.add_command(label="CRUD Doctor",command=cruddoctor)
doctormenu.add_command(label='Informe de Doctores', command=pdf.exportarmedicopdf)
doctormenu.add_separator()
doctormenu.add_command(label="Salir", command=ventana.quit)
menubar.add_cascade(label="Doctor", menu=doctormenu)

""" Se define la estructura de la Grilla de datos """

lblsalto0 = Label(ventana, text='', font='Calibri 16').pack()
    
grilla = ttk.Treeview(ventana)
grilla['show'] = 'headings'
grilla['columns'] = ("rut", "nombre", "apellido", "nombre_doctor", "profesion","apodo")

grilla.column("rut", width=100, minwidth=100, anchor=tk.CENTER)
grilla.column("nombre", width=100, minwidth=100, anchor=tk.CENTER)
grilla.column("apellido", width=100, minwidth=100, anchor=tk.CENTER)
grilla.column("nombre_doctor", width=100, minwidth=100, anchor=tk.CENTER)
grilla.column("profesion", width=100, minwidth=100, anchor=tk.CENTER)
grilla.column("apodo", width=100, minwidth=100, anchor=tk.CENTER)

grilla.heading("rut", text="RUT Paciente", anchor=tk.CENTER)
grilla.heading("nombre", text='Nombre Paciente', anchor=tk.CENTER)
grilla.heading("apellido", text="Apellido Paciente", anchor=tk.CENTER)
grilla.heading("nombre_doctor", text="Nombre Doctor", anchor=tk.CENTER)
grilla.heading("profesion", text="Profesión", anchor=tk.CENTER)
grilla.heading("apodo", text="Apodo", anchor=tk.CENTER)

grilla.pack()

lblsalto1 = Label(ventana, text='', font='Calibri 5').pack()
btnCargar = Button(ventana, text="Cargar TreeView", font="Calibri 14", command=llenargrilla)
btnCargar.pack()
lblsalto2 = Label(ventana, text='', font='Calibri 5').pack()
btnExportar = Button(ventana, text="Guardar en CSV", font="Calibri 14", command=exportarcsv)
btnExportar.pack()
btnExportar['state']=tk.DISABLED


ventana.mainloop()