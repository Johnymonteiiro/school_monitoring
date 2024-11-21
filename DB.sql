-- Criação do Banco de Dados "teste"
CREATE DATABASE school;

-- Usar o Banco de Dados "teste"
USE teste;

/* Lógico_20.11: */

CREATE TABLE Aluno (
    id_aluno int PRIMARY KEY AUTO_INCREMENT,
    nome varchar(255),
    data_nascimento date,
    cpf varchar(14),
    endereco varchar(255),
    condicoes_saude text,
    fk_Presenca_id_presenca int
);

CREATE TABLE Responsavel (
    id_responsavel int PRIMARY KEY AUTO_INCREMENT,
    nome varchar(255),
    telefone varchar(20),
    email varchar(255),
    parentesco varchar(50),
    endereco varchar(255)
);

CREATE TABLE Professor (
    id_professor int PRIMARY KEY AUTO_INCREMENT,
    nome varchar(255),
    cpf varchar(14),
    email varchar(255),
    telefone varchar(20),
    especialidade varchar(250)
);

CREATE TABLE Disciplina (
    id_disciplina int PRIMARY KEY AUTO_INCREMENT,
    nome_disciplina varchar(255),
    descricao text,
    fk_Professor_id_professor int
);

CREATE TABLE Aula (
    id_aula int PRIMARY KEY AUTO_INCREMENT,
    data_aula date,
    hora_inicio time,
    hora_fim time,
    fk_Disciplina_id_disciplina int
);

CREATE TABLE Presenca (
    id_presenca int PRIMARY KEY AUTO_INCREMENT,
    status_presenca varchar(50),
    hora_chegada time,
    hora_saida time
);

CREATE TABLE Avaliacao (
    id_avaliacao int PRIMARY KEY AUTO_INCREMENT,
    tipo_avaliacao varchar(50),
    nota decimal,
    data_avaliacao date
);

CREATE TABLE Ocorrencia (
    id_ocorrencia int PRIMARY KEY AUTO_INCREMENT,
    descricao text,
    tipo varchar(50),
    data_ocorrencia date,
    fk_Professor_id_professor int
);

CREATE TABLE Aluno_Responsavel (
    fk_Aluno_id_aluno int,
    fk_Responsavel_id_responsavel int
);

CREATE TABLE Aula_Presenca (
    fk_Aula_id_aula int,
    fk_Presenca_id_presenca int
);

CREATE TABLE Avaliacao_Disciplina (
    fk_Disciplina_id_disciplina int,
    fk_Avaliacao_id_avaliacao int
);

CREATE TABLE Avaliacao_Aluno (
    fk_Aluno_id_aluno int,
    fk_Avaliacao_id_avaliacao int
);

CREATE TABLE Hitorico_Ocorrencia (
    id_historico_ocorrencia int PRIMARY KEY AUTO_INCREMENT,
    fk_Aluno_id_aluno int,
    fk_Ocorrencia_id_ocorrencia int
);

CREATE TABLE Usuarios (
    id_usuarios int PRIMARY KEY AUTO_INCREMENT,
    nome_usuario varchar(255),
    senha varchar(255),
    tipo_usuario varchar(50),
    ultimo_login datetime,
    data_criacao datetime,
	status varchar(50)
);
 
ALTER TABLE Aluno ADD CONSTRAINT FK_Aluno_2
    FOREIGN KEY (fk_Presenca_id_presenca)
    REFERENCES Presenca (id_presenca)
    ON DELETE RESTRICT;
 
ALTER TABLE Disciplina ADD CONSTRAINT FK_Disciplina_2
    FOREIGN KEY (fk_Professor_id_professor)
    REFERENCES Professor (id_professor)
    ON DELETE CASCADE;
 
ALTER TABLE Aula ADD CONSTRAINT FK_Aula_2
    FOREIGN KEY (fk_Disciplina_id_disciplina)
    REFERENCES Disciplina (id_disciplina)
    ON DELETE RESTRICT;
 
ALTER TABLE Ocorrencia ADD CONSTRAINT FK_Ocorrencia_2
    FOREIGN KEY (fk_Professor_id_professor)
    REFERENCES Professor (id_professor)
    ON DELETE RESTRICT;
 
ALTER TABLE Aluno_Responsavel ADD CONSTRAINT FK_Aluno_Responsavel_1
    FOREIGN KEY (fk_Aluno_id_aluno)
    REFERENCES Aluno (id_aluno);
 
ALTER TABLE Aluno_Responsavel ADD CONSTRAINT FK_Aluno_Responsavel_2
    FOREIGN KEY (fk_Responsavel_id_responsavel)
    REFERENCES Responsavel (id_responsavel);
 
ALTER TABLE Aula_Presenca ADD CONSTRAINT FK_Aula_Presenca_1
    FOREIGN KEY (fk_Aula_id_aula)
    REFERENCES Aula (id_aula);
 
ALTER TABLE Aula_Presenca ADD CONSTRAINT FK_Aula_Presenca_2
    FOREIGN KEY (fk_Presenca_id_presenca)
    REFERENCES Presenca (id_presenca);
 
ALTER TABLE Avaliacao_Disciplina ADD CONSTRAINT FK_Avaliacao_Disciplina_1
    FOREIGN KEY (fk_Disciplina_id_disciplina)
    REFERENCES Disciplina (id_disciplina);
 
ALTER TABLE Avaliacao_Disciplina ADD CONSTRAINT FK_Avaliacao_Disciplina_2
    FOREIGN KEY (fk_Avaliacao_id_avaliacao)
    REFERENCES Avaliacao (id_avaliacao);
 
ALTER TABLE Avaliacao_Aluno ADD CONSTRAINT FK_Avaliacao_Aluno_1
    FOREIGN KEY (fk_Aluno_id_aluno)
    REFERENCES Aluno (id_aluno);
 
ALTER TABLE Avaliacao_Aluno ADD CONSTRAINT FK_Avaliacao_Aluno_2
    FOREIGN KEY (fk_Avaliacao_id_avaliacao)
    REFERENCES Avaliacao (id_avaliacao);
 
ALTER TABLE Hitorico_Ocorrencia ADD CONSTRAINT FK_Hitorico_Ocorrencia_2
    FOREIGN KEY (fk_Aluno_id_aluno)
    REFERENCES Aluno (id_aluno);
 
ALTER TABLE Hitorico_Ocorrencia ADD CONSTRAINT FK_Hitorico_Ocorrencia_3
    FOREIGN KEY (fk_Ocorrencia_id_ocorrencia)
    REFERENCES Ocorrencia (id_ocorrencia);


    