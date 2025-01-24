create table IF NOT EXISTS demo1 (
    id serial primary key,
    username varchar(255) not null,
    email varchar(255) not null
);

INSERT into demo1 values 
(12345,'Name1','john1@gmai.com'),
(12346,'Name2','john2@gmai.com'),
(12347,'Name3','john3@gmai.com');
