CREATE TABLE `club` (
    `id` INT(11) PRIMARY KEY AUTO_INCREMENT,
    `club` VARCHAR(512) NOT NULL,
    `club_country` VARCHAR(100),
    `created` DATETIME DEFAULT CURRENT_TIMESTAMP(),
    `updated` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP()
);

INSERT INTO `club` (`club`, `club_country`)
VALUES ('TSV 1860 Munich', 'Deutschland');

INSERT INTO `club` (`club`, `club_country`)
VALUES ('VfR Aalen', 'Deutschland');

INSERT INTO `club` (`club`, `club_country`)
VALUES ('VfL 07 Bremen', 'Deutschland');

INSERT INTO `club` (`club`, `club_country`)
VALUES ('Blau-Weiss 1890 Berlin', 'Deutschland');

CREATE TABLE `match` (
    `id` INT(11) PRIMARY KEY AUTO_INCREMENT,
    `comment` VARCHAR(500),
    `date` DATETIME DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE `club_match` (
    `idclub_match` INT(11) PRIMARY KEY AUTO_INCREMENT,
    `idclub` INT(11) NOT NULL,
    `idmatch` INT(11) NOT NULL,
    `points` INT(11) NOT NULL,  
    `created` DATETIME DEFAULT CURRENT_TIMESTAMP(),
    `updated` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(),
    FOREIGN KEY (idclub) REFERENCES `club`(id),
    FOREIGN KEY (idmatch) REFERENCES `match`(id));

-- CREATE PROCEDURE
DELIMITER //
CREATE PROCEDURE `matchClubs`(IN `id1` INT(11), IN `point1` INT(11), IN `id2` INT(11), IN `point2` INT) NOT DETERMINISTIC CONTAINS SQL SQL SECURITY DEFINER BEGIN INSERT INTO `match` (`comment`) VALUES(''); SET @last_id = LAST_INSERT_ID(); INSERT INTO `club_match` (`idmatch`,`idclub`, `points`) VALUES(@last_id, id1, point1); INSERT INTO `club_match` (`idmatch`,`idclub`, `points`) VALUES(@last_id, id2, point2); END //

-- CALL STORE PROCEDURE
CALL matchClubs(1,3,2,0);
CALL matchClubs(3,1,4,1); 


