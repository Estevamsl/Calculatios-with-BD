use python;

create table Soma(
	id int primary key not null unique auto_increment,
    number1 int not null,
    number2 int not null,
    
    Soma int not null
);

create table Subtracao(
	id int primary key not null unique auto_increment,
    number1 int not null,
    number2 int not null,
    
    Subtracao int not null
);

create table Produto(
	id int primary key not null unique auto_increment,
    number1 int not null,
    number2 int not null,
    
    Produto int not null
);

create table Divisao(
	id int primary key not null unique auto_increment,
    number1 int not null,
    number2 int not null,
    
    Divisao dec
(10, 2) not null
);

drop table Soma;
drop table Subtracao;
drop table Produto;
drop table Divisao;

select *
from Soma;
select *
from Subtracao;
select *
from Produto;
select *
from Divisao;

insert into Soma
    (number1, number2, Soma)
values
    (1, 2, 3);
insert into Subtracao
    (number1, number2, Subtracao)
values
    (1, 2, -1);
insert into Produto
    (number1, number2, Produto)
values
    (1, 2, 2);
insert into Divisao
    (number1, number2, Divisao)
values
    (1, 2, 0.5);

select *
from Soma __s__
    left join Subtracao __sub__
    on __s__.id = __sub__.id
    left join Divisao __d__
    on __s__.id = __d__.id
    left join Produto __p__
    on __s__.id = __p__.id