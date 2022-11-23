# Import Segment
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas as Canvas
from datetime import datetime
import funciones

# Global and Class definitions Segment

lis = list()
lismed = list()


""" Se definen los archivos de salida para los reportes en PDF """
reportepaciente = Canvas.Canvas("informe_paciente.pdf", pagesize=letter)
reportepaciente.setLineWidth(.3)
reportepaciente.setFont('Helvetica', 10)

reportedoctor = Canvas.Canvas("informe_doctor.pdf", pagesize=letter)
reportedoctor.setLineWidth(.3)
reportedoctor.setFont('Helvetica', 10)

#Exportar el conetido de la tabla paciente a un archivo PDF
def exportapacientespdf():
    lis=funciones.buscarpacientesfull()
    try:
        if lis:
            reportepaciente.drawString(30,750,'Informe de Prueba')
            reportepaciente.drawString(30,735,'CFT San Agustin')
            reportepaciente.drawString(500,750,datetime.today().strftime('%Y-%m-%d %H:%M'))
            reportepaciente.line(480,747,580,747)
            reportepaciente.drawString(275,725,'Estimado')
            reportepaciente.drawString(480,725,'Docente Pablo Vilches')
            reportepaciente.line(465,722,580,722)
            reportepaciente.drawString(30,715,'Asunto:')    
            reportepaciente.drawString(200,700,'Informe de los Pacientes Registrados')
            reportepaciente.line(30,697,580,697)
            reportepaciente.drawString(30,670,'RUT')
            reportepaciente.drawString(110,670,'Nombre')
            reportepaciente.drawString(190,670,'Apellido')
            reportepaciente.drawString(270,670,'Email')
            reportepaciente.drawString(450,670,'Teléfono')

            variableapo=650
            for i in lis:
                reportepaciente.drawString(30,variableapo,i[0])
                reportepaciente.drawString(110,variableapo,i[1])
                reportepaciente.drawString(180,variableapo,i[2])
                reportepaciente.drawString(270,variableapo,i[3])
                reportepaciente.drawString(450,variableapo,str(i[4]))
                variableapo = variableapo-15
            
            reportepaciente.showPage()
            reportepaciente.save()

            messagebox.showinfo("Reporte", "Se ha generado satisfactoriamente el reporte de Pacientes solicitado.")
        
        else:
            messagebox.showerror("Reporte", "No se puede generar el reporte solicitado.")
    
    except:
        messagebox.showerror("Reporte", "Se ha precentado un problema inesperado, intente nuevamente.")

#Exportar el conetenido de la tabla doctor a un archivo PDF
def exportarmedicopdf():
    lismed = funciones.buscarmedicosfull()
    try:
        if lismed:
            reportedoctor.drawString(30,750,'Informe de Prueba')
            reportedoctor.drawString(30,735,'CFT San Agustin')
            reportedoctor.drawString(500,750,datetime.today().strftime('%Y-%m-%d %H:%M'))
            reportedoctor.line(480,747,580,747)
            reportedoctor.drawString(275,725,'Estimado')
            reportedoctor.drawString(480,725,'Docente Pablo Vilches')
            reportedoctor.line(465,722,580,722)
            reportedoctor.drawString(30,715,'Asunto:')    
            reportedoctor.drawString(200,700,'Informe de los Pacientes Registrados')
            reportedoctor.line(30,697,580,697)
            reportedoctor.drawString(30,670,'RUT')
            reportedoctor.drawString(110,670,'Nombre')
            reportedoctor.drawString(190,670,'Apellido')
            reportedoctor.drawString(270,670,'Email')
            reportedoctor.drawString(450,670,'Teléfono')

            variableapo=650
            for i in lismed:
                reportedoctor.drawString(30,variableapo,i[0])
                reportedoctor.drawString(110,variableapo,i[1])
                reportedoctor.drawString(180,variableapo,i[2])
                reportedoctor.drawString(270,variableapo,i[3])
                reportedoctor.drawString(450,variableapo,i[4])
                variableapo = variableapo-15
            
            reportedoctor.showPage()
            reportedoctor.save()
            messagebox.showinfo("Reporte", "Se ha generado satisfactoriamente el reporte de Medicos solicitado.")
        
        else:
            messagebox.showerror("Reporte", "No se puede generar el reporte solicitado.")
    
    except:
        messagebox.showerror("Reporte", "Se ha precentado un problema inesperado, intente nuevamente.")