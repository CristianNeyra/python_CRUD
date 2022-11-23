# Import Segment
from tkinter import *
from tkinter import messagebox as MessageBox
import conexcion

# Global and Class definitions Segment
global rs
rs = list()

# Main program Segment
"""Funcion para recuperar los datos de un paciente"""
def buscapaciente(rut):
    try:

        sql= "SELECT * FROM paciente WHERE rut='"+str(rut)+"';"
        conexcion.cur.execute(sql)
        rs=conexcion.cur.fetchone()
        return rs

    except:
        MessageBox.showinfo("Error", "La consulta no ha retornado valores o el criterio de busqueda no es el correco.")
        conexcion.miconexion.rollback()

"""Funcion para recuperar los datos de un doctor"""
def buscardoctor(iddoctor):
    try:

        sql="SELECT * FROM doctor where iddoctor='"+str(iddoctor)+"';"
        conexcion.cur.execute(sql)
        rs=conexcion.cur.fetchone()
        return rs

    except:
        MessageBox.showinfo("Error", "La consulta no ha retornado valores o el criterio de busqueda no es el correco.")
        conexcion.miconexion.rollback()

"""Funcion para recuperar todos los pacientes y medicos"""
def buscartodo():
    try:

        sql="SELECT p.rut, p.nombre, p.apellido, d.nombre_doctor, d.profesion, d.apodo FROM paciente AS p, doctor AS d WHERE p.rut=d.rut_paciente;"
        conexcion.cur.execute(sql)
        rs=conexcion.cur.fetchall()
        return rs

    except:
        MessageBox.showinfo("Error", "La consulta no ha retornado valores o el criterio de busqueda no es el correco.")
        conexcion.miconexion.rollback()

""" Funcion para buscar todos los pacientes """
def buscarpacientesfull():
    try:

        sql="SELECT * FROM paciente;"
        conexcion.cur.execute(sql)
        rs=conexcion.cur.fetchall()
        return rs
    
    except:
        MessageBox.showerror("Error", "No se ha podido recueperar la información solicitada, favor intente más tarde.")

""" Funcion para buscar todos los doctores"""
def buscarmedicosfull():
    try:

        sql="SELECT * FROM doctor;"
        conexcion.cur.execute(sql)
        rs=conexcion.cur.fetchall()
        return rs
    
    except:
        MessageBox.showerror("Error", "No se ha podido recueperar la información solicitada, favor intente más tarde.")

"""Insertar un nuevo paciente"""
def insertpaciente(rut, nombre, apellido, email, telefono):
    try:

        sql="INSERT INTO paciente VALUES('"+str(rut)+"','"+str(nombre)+"','"+str(apellido)+"','"+str(email)+"',"+telefono+");"
        conexcion.cur.execute(sql)
        conexcion.miconexion.commit()
        MessageBox.showinfo("Correcto", "El nuevo Paciente ha sido algregado exitosamente")

    except:
        MessageBox.showerror("Error", "Los datos no se han podido almacenar en el sistema.")
        conexcion.miconexion.rollback()

"""Insertar nuevo doctor"""
def insertdoctor(iddoctor, nombre_doctor, profesion, apodo, rut):
    try:

        sql="INSERT INTO doctor VALUES('"+str(iddoctor)+"','"+str(nombre_doctor)+"','"+str(profesion)+"','"+str(apodo)+"','"+str(rut)+"');"
        conexcion.cur.execute(sql)
        conexcion.miconexion.commit()
        MessageBox.showinfo("Correcto", "El nuevo Doctor ha sido algregado exitosamente")

    except:
        MessageBox.showerror("Error", "Los datos no se han podido almacenar en el sistema.")
        conexcion.miconexion.rollback()

"""Actualizar un paciente"""
def updatepaciente(rut, nombre, apellido, email, telefono):
    try:

        sql="UPDATE paciente SET nombre='"+str(nombre)+"', apellido='"+str(apellido)+"', email='"+str(email)+"', telefono="+telefono+" WHERE rut='"+str(rut)+"';"
        conexcion.cur.execute(sql)
        conexcion.miconexion.commit()
        MessageBox.showinfo("Correcto","Datos del Paciente se han actualizados exitosamente")

    except:
        MessageBox.showerror("Error", "Error al actualizar el registro en el sistema.")
        conexcion.miconexion.rollback()

"""Actualizar un medico"""
def updatedoctor(iddoctor, nombre_doctor, profesion, apodo, rut):
    try:

        sql="UPDATE doctor SET nombre_doctor='"+str(nombre_doctor)+"',profesion='"+str(profesion)+"', apodo='"+str(apodo)+"', rut_paciente='"+str(rut)+"' WHERE iddoctor='"+str(iddoctor)+"';"
        conexcion.cur.execute(sql)
        conexcion.miconexion.commit()
        MessageBox.showinfo("Correcto","Datos del Doctor se han actualizados exitosamente")


    except:
        MessageBox.showinfo("Error", "Error al actualizar el registro en el sistema.")
        conexcion.miconexion.rollback()

"""Eliminar un paciente"""
def deletepaciente(rut):
    try:

        sql="DELETE FROM paciente WHERE rut='"+str(rut)+"';"
        conexcion.cur.execute(sql)
        conexcion.miconexion.commit()
        MessageBox.showinfo("Correcto", "El Paciente ha sido eliminado del sistema.")

    except:
        MessageBox.showinfo("Error", "Error al eliminar el Paciente en el sistema.")
        conexcion.miconexion.rollback()

"""Eliminar un doctor"""
def deletedoctor(iddoctor):
    try:

        sql="DELETE FROM doctor WHERE iddoctor='"+str(iddoctor)+"';"
        conexcion.cur.execute(sql)
        conexcion.miconexion.commit()
        MessageBox.showinfo("Correcto", "El Doctor ha sido eliminado del sistema.")

    except:
        MessageBox.showinfo("Error", "Error al eliminar el registro en el sistema.")
        conexcion.miconexion.rollback()