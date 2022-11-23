create database prueba2;
use prueba2;
create table Paciente(
rut nvarchar(15) not null,
nombre nvarchar(100) not null,
apellido nvarchar(100) not null,
email nvarchar(250) not null,
telefono int not null,
PRIMARY KEY(rut)
);

create table Doctor(
iddoctor nvarchar(15) not null,
nombre_doctor nvarchar(100) not null,
profesion nvarchar(100) not null,
apodo nvarchar(100) not null,
rut_paciente nvarchar(15) not null, 
primary key(iddoctor),
foreign key (rut_paciente) references Paciente(rut) 
on delete cascade on update cascade
);