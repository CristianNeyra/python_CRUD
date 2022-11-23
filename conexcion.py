# Import Segment
import pymysql

# Main program Segment
miconexion=pymysql.connect(host='localhost',db='prueba2',user='cneyra',passwd='Asternax12543')
cur=miconexion.cursor()