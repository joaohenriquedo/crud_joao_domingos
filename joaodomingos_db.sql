create date base joaodomingos__db


create table usuario(
     idusuario int not null ,
     nome text,
     telefine text,
     usuario text,
     senha text,
     primary key (idusuario)
);

#codigo para funcionar
#pib install mysql-conector-python