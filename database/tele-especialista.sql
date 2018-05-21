CREATE SCHEMA teleespecialista;

CREATE TABLE teleespecialista.login(
    id INT,
    username VARCHAR(64) UNIQUE NOT NULL,
	password VARCHAR(64) NOT NULL
)

CREATE TABLE teleespecialista.users(
	id INT PRIMARY KEY AUTO_INCREMENT,
    crm VARCHAR(255),
    fullname VARCHAR(255),
    birthdate DATE,
    birthcity VARCHAR(255),
    birthstate VARCHAR(2),
    rg VARCHAR(11),
    CPF VARCHAR(12),
    cep INT,
    place VARCHAR(255),
    address VARCHAR(255),
    neighborhood VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    phone1 INT,
    phone2 INT,
    specially  VARCHAR(255)
);

CREATE TABLE teleespecialista.clinics(
	id INT PRIMARY KEY AUTO_INCREMENT,
    bussinessname VARCHAR(255),
    companyname VARCHAR(255),
    cep INT,
    place VARCHAR(255),
    address VARCHAR(255),
    neighborhood VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    phone1 INT,
    phone2 INT,
    email VARCHAR(255),
    cnpj INT,
    stateinscription VARCHAR
);

CREATE TABLE teleespecialista.specialities(
    id INT,
    name VARCHAR
);

CREATE TABLE teleespecialista.appointments(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_specialisty INT,
    id_specially VARCHAR,
    msr_date DATE,
	msr_time TIME,
	confirmed BOOLEAN DEFAULT 0
);



CREATE TABLE teleespecialista.jclinicuser(
    id INT,
    id_user INT,
    id_clinic INT,
);

CREATE TABLE teleespecialista.histories(
    id INT,
    id_user INT,
    id_clinic INT,
);

-- INSERT INTO teleespecialista.users(fullname, contact, username, password) VALUES
-- ('Telemedicina Tele-especialista', 'telemed@telemed.com', 'telemed@telemed.com', 'telemd');

-- SELECT * FROM teleespecialista.users;
-- ALTER TABLE teleespecialista.users MODIFY COLUMN contact VARCHAR(256) NULL;
-- ALTER TABLE teleespecialista.users MODIFY COLUMN contact VARCHAR(64) NULL;
-- INSERT INTO teleespecialista.users(username, password) VALUES ('teleespecialista@telemed.com', 'teleespecialista');


CREATE TABLE teleespecialista.users_appointments(

);
