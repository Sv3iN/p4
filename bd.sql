CREATE DATABASE CURRICULO;

USE CURRICULO;

CREATE TABLE candidato(
    idUsuario INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nome CHAR(50),
    telefone VARCHAR(11),
    minibio CHAR(200),
    entrevista INT,
    teste_teorico INT,
    teste_pratico INT,
    soft_skill INT 
    
);

INSERT INTO candidato VALUES(0,"Ronaldinho","11-03425424","sei driblar",8,5,7,10);
INSERT INTO candidato VALUES(0,"Carles puyol","23-03454424","sei defender",4,7,9,8);
INSERT INTO candidato VALUES(0,"Nedved","11-03425232","joguei mt",2,3,5,6);
INSERT INTO candidato VALUES(0,"Puskas","11-03432464","sou brabo",8,9,9,10);
INSERT INTO candidato VALUES(0,"pelé","11-83255424","the goat",10,10,10,10);
INSERT INTO candidato VALUES(0,"Cruuyf","15-03963424","F",7,6,7,8);
INSERT INTO candidato VALUES(0,"Lucio","11-03535424","nunca trabalhei",8,4,3,0);
INSERT INTO candidato VALUES(0,"Pedro","11-23535424","nunca trabalhei",8,6,3,3);
INSERT INTO candidato VALUES(0,"Luis","11-03590424","nunca trabalhei",9,6,8,7);
INSERT INTO candidato VALUES(0,"Claudio","11-03512424","nunca trabalhei",1,6,1,10);
INSERT INTO candidato VALUES(0,"Guilherme","11-03535794","nunca trabalhei",7,3,5,2);
INSERT INTO candidato VALUES(0,"Jailson","11-03675424","nunca trabalhei",5,5,5,5);
INSERT INTO candidato VALUES(0,"Caique","11-03535424","nunca trabalhei",8,4,3,0);
INSERT INTO candidato VALUES(0,"Amaral","11-98535424","nunca trabalhei",2,2,4,5);
INSERT INTO candidato VALUES(0,"João","11-03536524","nunca trabalhei",10,7,2,2);
INSERT INTO candidato VALUES(0,"Mario","33-03535424","nunca trabalhei",1,7,1,8);
INSERT INTO candidato VALUES(0,"Leandro","21-03535424","nunca trabalhei",9,5,9,7);
INSERT INTO candidato VALUES(0,"Melo","11-03375424","nunca trabalhei",7,7,2,1);
INSERT INTO candidato VALUES(0,"Laura","11-03530894","nunca trabalhei",0,7,7,0);
INSERT INTO candidato VALUES(0,"Raquel","11-03537243","nunca trabalhei",6,6,6,6);

