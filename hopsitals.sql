CREATE TABLE HOSPITALS (
OrganisationID INT NOT NULL,
OrganisationCode VARCHAR(30) NOT NULL,
Sector VARCHAR(30) NOT NULL,
OrganisationName VARCHAR(30) NOT NULL,
Address1 VARCHAR(30) NOT NULL,        
Address2 VARCHAR(30) NOT NULL,         
Address3 VARCHAR(30) NOT NULL,         
City     VARCHAR(30) NOT NULL,        
County   VARCHAR(30) NOT NULL,         
Postcode VARCHAR(30) NOT NULL,         
Latitude  FLOAT NOT NULL,       
Longitude FLOAT NOT NULL
);
SELECT * FROM HOSPITALS ;