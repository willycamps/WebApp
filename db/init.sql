CREATE TABLE `club` (
    `id` INT(11) PRIMARY KEY AUTO_INCREMENT,
    `club` VARCHAR(512) NOT NULL,
    `club_country` VARCHAR(100),
    `club_points` VARCHAR(100),
    `created` DATETIME DEFAULT CURRENT_TIMESTAMP(),
    `updated` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP()
);

INSERT INTO `club` (`club`, `club_country`, `club_points`)
VALUES ('TSV 1860 Munich', 'Deutschland', '7');

INSERT INTO `club` (`club`, `club_country`, `club_points`)
VALUES ('VfR Aalen', 'Deutschland', '5');

INSERT INTO `club` (`club`, `club_country`, `club_points`)
VALUES ('VfL 07 Bremen', 'Deutschland', '4');

INSERT INTO `club` (`club`, `club_country`, `club_points`)
VALUES ('Blau-Weiss 1890 Berlin', 'Deutschland', '3');