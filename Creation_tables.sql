DROP TABLE IF EXISTS Gagnes;
DROP TABLE IF EXISTS Joueurs;
DROP TABLE IF EXISTS Trophees;
DROP TABLE IF EXISTS Clubs;
DROP TABLE IF EXISTS Managers;



CREATE TABLE Joueurs(
	numero_joueur int NOT NULL,
	nom_club char(40) NOT NULL ,
	nom_joueur char(40) NOT NULL ,
	prenom_joueur char(40) NOT NULL ,
	salaire_joueur number(4,0) CHECK (salaire_joueur > 0) NOT NULL,
	CONSTRAINT pk_numJ_Club PRIMARY KEY (numero_joueur, nom_club),
	CONSTRAINT fk_nom_club FOREIGN KEY (nom_club) REFERENCES Clubs(nom_club),
	UNIQUE (nom_joueur, prenom_joueur)
);

CREATE TABLE Trophees (
	nom_trophee CHAR(50)NOT NULL,
	prix_trophee INTEGER CHECK (prix_trophee > 0) NOT NULL,
	type_trophee CHAR(50) CHECK (type_trophee IN ("individuel", "collectif")) NOT NULL,
	CONSTRAINT pk_nom_trophee PRIMARY KEY (nom_trophee)
);


CREATE TABLE Clubs (
	nom_club char(40) NOT NULL ,
	date_creation date NOT NULL,
	nombre_trophées int NOT NULL,
	nom_manager char(40) NOT NULL,
	CONSTRAINT pk_nom_club PRIMARY KEY (nom_club),
	CONSTRAINT fk_nom_manager FOREIGN KEY (nom_manager) REFERENCES Managers(nom_manager)
);

CREATE TABLE Managers (
	nom_manager char(40) NOT NULL,
	prenom_manager char(40) NOT NULL,
	salaire_manager int CHECK (salaire_manager > 0) NOT NULL,
	CONSTRAINT pk_nom_manager PRIMARY KEY (nom_manager)
);

CREATE TABLE Gagnes (
	nom_joueur char (40) NOT NULL,
	prenom_joueur char (40) NOT NULL,
	nom_trophee char (60) NOT NULL,
	date_gagne date NOT NULL,
	CONSTRAINT pk_nomJ_prenomJ_nomT_date PRIMARY KEY (nom_joueur, prenom_joueur, nom_trophee, date_gagne),
	CONSTRAINT fk_nom_prenom_joueur_ FOREIGN KEY (nom_joueur, prenom_joueur) REFERENCES Joueurs (nom_joueur, prenom_joueur),
	CONSTRAINT fk_nom_trophee FOREIGN KEY (nom_trophee) REFERENCES Trophees (nom_trophee)
);
