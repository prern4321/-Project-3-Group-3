DROP TABLE hospitals;

CREATE TABLE hospitals (
organisationid INT NOT NULL,
organisationcode VARCHAR(30) NOT NULL,
sector VARCHAR(30) NOT NULL,
organisationname VARCHAR(30) NOT NULL,
address1 VARCHAR(30) NOT NULL,        
address2 VARCHAR(30) NOT NULL,         
address3 VARCHAR(30) NOT NULL,         
city     VARCHAR(30) NOT NULL,        
county   VARCHAR(30) NOT NULL,         
postcode VARCHAR(30) NOT NULL,         
latitude  FLOAT NOT NULL,       
longitude FLOAT NOT NULL
);

SELECT * FROM hospitals ;

