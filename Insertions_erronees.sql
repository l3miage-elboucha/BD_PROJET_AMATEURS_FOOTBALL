/*EQUIPE NON EXISTANTE*/
INSERT INTO Joueurs VALUES (2, "FC BARCILOUNA", "Anas", "Test", 6600000);

/*NUMERO DEJA EXISTANT*/
INSERT INTO Joueurs VALUES (88, "MANCHESTER CITY", "Keli", "Mor", 6600000);
INSERT INTO Joueurs VALUES (88, "MANCHESTER CITY", "Ilias", "Num", 6600000);

/*TROPHEE DEJA EXISTANT*/
INSERT INTO Trophees VALUES ("Champions Cup", 20, "collectif");
INSERT INTO Trophees VALUES ("Champions Cup", 29, "collectif");

/*CLUB AVEC MANAGER N'EXISTANT PAS*/
INSERT INTO Clubs VALUES ("FC TEST", "29/11/1899", 76, "TEST"); 

/*CREATION MANAGER DEJA EXISTANT*/
INSERT INTO Managers VALUES ("TEST", "un", 78400);
INSERT INTO Managers VALUES ("TEST", "un", 54100);

/*TROPHEE GAGNE N'EXISTANT PAS*/
/*IL FAUT EXECUTER LE FICHIER Insertion_trophees.sql AVANT*/
INSERT INTO Gagnes VALUES ("Messi", "Lionel","La Liga 2","20/03/2014");

/*JOUEUR N'EXISTANT PAS*/
INSERT INTO Gagnes VALUES ("Mexi", "Lionel","Champions League","20/03/2014");








