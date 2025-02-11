-- MySQL dump 10.13  Distrib 8.0.36, for macos14 (arm64)
--
-- Host: localhost    Database: UniStats
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `activities`
--

DROP TABLE IF EXISTS `activities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `activities` (
  `activity_id` int NOT NULL AUTO_INCREMENT,
  `activity_name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`activity_id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activities`
--

LOCK TABLES `activities` WRITE;
/*!40000 ALTER TABLE `activities` DISABLE KEYS */;
INSERT INTO `activities` VALUES (1,'Basketball'),(2,'Soccer'),(3,'Track and field'),(4,'Baseball'),(5,'Golf'),(6,'Tennis'),(19,'Volleyball'),(20,'Football'),(21,'Softball'),(22,'Swimming'),(23,'Lacrosse'),(24,'Wrestling'),(25,'Cross Country Running'),(26,'Water polo'),(27,'Hockey'),(28,'Cheerleading'),(29,'Gymnastics'),(30,'Piano'),(31,'Chess'),(33,'Violin');
/*!40000 ALTER TABLE `activities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `activity_records`
--

DROP TABLE IF EXISTS `activity_records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `activity_records` (
  `activity_record_id` int NOT NULL AUTO_INCREMENT,
  `student_id` int DEFAULT NULL,
  `activity_id` int DEFAULT NULL,
  PRIMARY KEY (`activity_record_id`),
  KEY `student_id` (`student_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `activity_records_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`),
  CONSTRAINT `activity_records_ibfk_2` FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activity_records`
--

LOCK TABLES `activity_records` WRITE;
/*!40000 ALTER TABLE `activity_records` DISABLE KEYS */;
INSERT INTO `activity_records` VALUES (1,2,2),(2,8,6),(3,6,3),(4,4,4),(5,5,5),(6,3,2),(7,3,3),(8,1,26),(9,16,5),(10,16,1),(11,16,2),(12,16,3),(13,22,29),(14,22,28),(18,24,22);
/*!40000 ALTER TABLE `activity_records` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `all_decisions1`
--

DROP TABLE IF EXISTS `all_decisions1`;
/*!50001 DROP VIEW IF EXISTS `all_decisions1`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `all_decisions1` AS SELECT 
 1 AS `full_name`,
 1 AS `university_name`,
 1 AS `major`,
 1 AS `year`,
 1 AS `status`,
 1 AS `from_state`,
 1 AS `gpa`,
 1 AS `test`,
 1 AS `test_score`,
 1 AS `international`,
 1 AS `high_school_name`,
 1 AS `activities`,
 1 AS `decision_comments`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `all_decisions2`
--

DROP TABLE IF EXISTS `all_decisions2`;
/*!50001 DROP VIEW IF EXISTS `all_decisions2`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `all_decisions2` AS SELECT 
 1 AS `decision_id`,
 1 AS `full_name`,
 1 AS `university_name`,
 1 AS `major`,
 1 AS `year`,
 1 AS `status`,
 1 AS `from_state`,
 1 AS `gpa`,
 1 AS `test`,
 1 AS `test_score`,
 1 AS `international`,
 1 AS `high_school_name`,
 1 AS `activities`,
 1 AS `decision_comments`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `decision_records`
--

DROP TABLE IF EXISTS `decision_records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `decision_records` (
  `decision_id` int NOT NULL AUTO_INCREMENT,
  `student_id` int DEFAULT NULL,
  `school_id` int DEFAULT NULL,
  `major_id` int DEFAULT NULL,
  `status` varchar(15) DEFAULT NULL,
  `comment` varchar(50) DEFAULT NULL,
  `year` year DEFAULT NULL,
  PRIMARY KEY (`decision_id`),
  KEY `school_id` (`school_id`),
  KEY `major_id` (`major_id`),
  KEY `student_index` (`student_id`),
  CONSTRAINT `decision_records_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`),
  CONSTRAINT `decision_records_ibfk_2` FOREIGN KEY (`school_id`) REFERENCES `schools` (`school_id`),
  CONSTRAINT `decision_records_ibfk_3` FOREIGN KEY (`major_id`) REFERENCES `majors` (`major_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `decision_records`
--

LOCK TABLES `decision_records` WRITE;
/*!40000 ALTER TABLE `decision_records` DISABLE KEYS */;
INSERT INTO `decision_records` VALUES (2,3,11,1,'Accepted',NULL,2024),(3,3,12,1,'Accepted',NULL,2024),(4,3,25,1,'Rejected',NULL,2024),(5,3,20,1,'Accepted',NULL,2024),(6,22,28,6,'Waitlisted',NULL,2024),(7,22,21,6,'Accepted',NULL,2024),(8,23,27,1,'Rejected','sad',2024),(9,23,20,1,'Waitlisted','thought I had this...',2024),(12,23,30,1,'Accepted',NULL,2024),(13,23,28,1,'Rejected',NULL,2024),(15,25,11,1,'Accepted',NULL,2024),(16,1,12,1,'Accepted',NULL,2024),(17,1,11,1,'Accepted',NULL,2024);
/*!40000 ALTER TABLE `decision_records` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `majors`
--

DROP TABLE IF EXISTS `majors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `majors` (
  `major_id` int NOT NULL AUTO_INCREMENT,
  `major_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`major_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `majors`
--

LOCK TABLES `majors` WRITE;
/*!40000 ALTER TABLE `majors` DISABLE KEYS */;
INSERT INTO `majors` VALUES (1,'Business'),(2,'Biology'),(3,'Communications'),(4,'Computer Science'),(5,'Education'),(6,'English'),(7,'Environmental Science'),(8,'Finance'),(9,'History'),(10,'Mathematics'),(11,'Political Science'),(12,'Psychology'),(13,'Sociology'),(14,'Film Production'),(15,'Anthropology'),(16,'Criminal Justice'),(20,'Screenwriting');
/*!40000 ALTER TABLE `majors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schools`
--

DROP TABLE IF EXISTS `schools`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schools` (
  `school_id` int NOT NULL AUTO_INCREMENT,
  `school_name` varchar(50) DEFAULT NULL,
  `state_id` int DEFAULT NULL,
  `level` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`school_id`),
  KEY `state_id` (`state_id`),
  CONSTRAINT `schools_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`state_id`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schools`
--

LOCK TABLES `schools` WRITE;
/*!40000 ALTER TABLE `schools` DISABLE KEYS */;
INSERT INTO `schools` VALUES (11,'Chapman University',1,'University'),(12,'University Of California, Irvine',1,'University'),(13,'Sage Hill School',1,'High school'),(14,'Arizona State University',4,'University'),(15,'Alabama State University',2,'University'),(16,'Cypress High School',1,'High school'),(17,'Mater Dei High School',1,'High school'),(18,'Arizona College Preparatory',4,'High school'),(19,'University of Southern California',1,'University'),(20,'Boston University',21,'University'),(21,'New York University',32,'University'),(22,'Emory University',10,'University'),(23,'DePaul University',13,'University'),(24,'University of California, Los Angeles',1,'University'),(25,'Columbia University',32,'University'),(26,'Florida State University',9,'University'),(27,'Stanford University',1,'University'),(28,'Harvard University',21,'University'),(29,'Carnegie Mellon University',38,'University'),(30,'Ohio State University',35,'University'),(31,'Purdue University',14,'University'),(32,'University Of California, Davis',1,'University'),(33,'University High School',1,'High school'),(34,'Irvine Valley College',1,'University'),(47,'Saddleback College',1,'University'),(49,'Biola University',1,'University'),(53,'Santa Ana College',1,'University'),(88,'Fullerton College',1,'University'),(114,'University Of Nevada, Las Vegas',28,'University'),(115,'Brown University',39,'University'),(118,'Yale University',7,'University'),(120,'Irvine High School',1,'High school');
/*!40000 ALTER TABLE `schools` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `states`
--

DROP TABLE IF EXISTS `states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `states` (
  `state_id` int NOT NULL AUTO_INCREMENT,
  `state_abb` varchar(3) DEFAULT NULL,
  `state_name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`state_id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `states`
--

LOCK TABLES `states` WRITE;
/*!40000 ALTER TABLE `states` DISABLE KEYS */;
INSERT INTO `states` VALUES (1,'CA','California'),(2,'AL','Alabama'),(3,'AK','Alaska'),(4,'AZ','Arizona'),(5,'AR','Arkansas'),(6,'CO','Colorado'),(7,'CT','Connecticut'),(8,'DE','Delaware'),(9,'FL','Florida'),(10,'GA','Georgia'),(11,'HI','Hawaii'),(12,'ID','Idaho'),(13,'IL','Illinois'),(14,'IN','Indiana'),(15,'IA','Iowa'),(16,'KS','Kansas'),(17,'KY','Kentucky'),(18,'LA','Louisiana'),(19,'ME','Maine'),(20,'MD','Maryland'),(21,'MA','Massachusetts'),(22,'MI','Michigan'),(23,'MN','Minnesota'),(24,'MS','Mississippi'),(25,'MO','Missouri'),(26,'MT','Montana'),(27,'NE','Nebraska'),(28,'NV','Nevada'),(29,'NH','New Hampshire'),(30,'NJ','New Jersey'),(31,'NM','New Mexico'),(32,'NY','New York'),(33,'NC','North Carolina'),(34,'ND','North Dakota'),(35,'OH','Ohio'),(36,'OK','Oklahoma'),(37,'OR','Oregon'),(38,'PA','Pennsylvania'),(39,'RI','Rhode Island'),(40,'SC','South Carolina'),(41,'SD','South Dakota'),(42,'TN','Tennessee'),(43,'TX','Texas'),(44,'UT','Utah'),(45,'VT','Vermont'),(46,'VA','Virginia'),(47,'WA','Washington'),(48,'WV','West Virginia'),(49,'WI','Wisconsin'),(50,'WY','Wyoming'),(51,'n/a','Outside of the US');
/*!40000 ALTER TABLE `states` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `student_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `state_id` int DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `international` tinyint(1) DEFAULT NULL,
  `gpa` float DEFAULT NULL,
  `test` varchar(5) DEFAULT NULL,
  `test_score` int DEFAULT NULL,
  `high_school` int DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  KEY `state_id` (`state_id`),
  KEY `high_school` (`high_school`),
  CONSTRAINT `students_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`state_id`),
  CONSTRAINT `students_ibfk_2` FOREIGN KEY (`high_school`) REFERENCES `schools` (`school_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Ariel','Kuo',1,'Female',1,3.9,'SAT',1500,17),(2,'Jessica','Luo',1,'Female',1,3.7,'SAT',1380,17),(3,'Maggie','Kuo',51,'Female',1,4,'SAT',1550,NULL),(4,'Josh','Medina',4,'Male',0,3.4,NULL,NULL,18),(5,'Adam','Smith',1,'Male',0,3.5,'ACT',32,13),(6,'Nathan','Slevcove',1,'Male',0,3.7,'SAT',1300,16),(7,'Steve','Sonsma',2,'Male',0,3.5,NULL,NULL,16),(8,'Chloe','Hu',1,'Female',0,3.9,'SAT',1580,17),(9,'Ryan','Brown',1,'Male',0,NULL,NULL,NULL,NULL),(10,'Lyla','Welsh',2,'Female',0,NULL,NULL,NULL,NULL),(11,'Nancy','Williams',2,'Female',0,NULL,NULL,NULL,NULL),(12,'Travis','Booth',2,'Male',0,NULL,NULL,NULL,NULL),(13,'Nikki','Vinh',4,'Female',0,NULL,NULL,NULL,NULL),(14,'John','Vergonio',1,'Non-binary',0,NULL,NULL,NULL,NULL),(15,'Selena','Johnson',5,'Female',0,NULL,NULL,NULL,NULL),(16,'Joe','White',13,'Male',0,NULL,NULL,NULL,NULL),(17,'Dakota','White',13,'Female',0,NULL,NULL,NULL,NULL),(18,'Nina','Lee',2,'Prefer not to say',0,NULL,NULL,NULL,13),(19,'Celine','Green',2,'Transgender',0,NULL,NULL,NULL,NULL),(20,'Rick','Green',7,'Male',0,NULL,NULL,NULL,NULL),(21,'Zoe','Lin',47,'Prefer not to say',0,3.4,'n/a',NULL,13),(22,'Grace','Jones',12,'Female',0,NULL,NULL,NULL,NULL),(23,'Amy','Vergonio',1,'Female',0,3.7,'SAT',1400,33),(24,'Sierra','Clibourne',28,'Female',0,NULL,NULL,NULL,NULL),(25,'Jerry','West',1,'Male',0,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `all_decisions1`
--

/*!50001 DROP VIEW IF EXISTS `all_decisions1`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `all_decisions1` AS select concat(`stu`.`first_name`,' ',`stu`.`last_name`) AS `full_name`,`uni`.`school_name` AS `university_name`,`major`.`major_name` AS `major`,`decision`.`year` AS `year`,`decision`.`status` AS `status`,`states`.`state_name` AS `from_state`,`stu`.`gpa` AS `gpa`,`stu`.`test` AS `test`,`stu`.`test_score` AS `test_score`,(case `stu`.`international` when 1 then 'Yes' else 'No' end) AS `international`,`hs`.`school_name` AS `high_school_name`,group_concat(distinct `act`.`activity_name` order by `act`.`activity_name` ASC separator ', ') AS `activities`,`decision`.`comment` AS `decision_comments` from (((((((`students` `stu` join `decision_records` `decision` on((`stu`.`student_id` = `decision`.`student_id`))) join `majors` `major` on((`decision`.`major_id` = `major`.`major_id`))) join `schools` `uni` on((`decision`.`school_id` = `uni`.`school_id`))) join `states` on((`stu`.`state_id` = `states`.`state_id`))) left join `schools` `hs` on((`stu`.`high_school` = `hs`.`school_id`))) left join `activity_records` `actrec` on((`stu`.`student_id` = `actrec`.`student_id`))) left join `activities` `act` on((`actrec`.`activity_id` = `act`.`activity_id`))) group by `stu`.`first_name`,`stu`.`last_name`,`uni`.`school_name`,`major`.`major_name`,`decision`.`year`,`decision`.`status`,`states`.`state_name`,`stu`.`gpa`,`stu`.`test`,`stu`.`test_score`,`stu`.`international`,`hs`.`school_name`,`decision`.`comment` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `all_decisions2`
--

/*!50001 DROP VIEW IF EXISTS `all_decisions2`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `all_decisions2` AS select `decision`.`decision_id` AS `decision_id`,concat(`stu`.`first_name`,' ',`stu`.`last_name`) AS `full_name`,`uni`.`school_name` AS `university_name`,`major`.`major_name` AS `major`,`decision`.`year` AS `year`,`decision`.`status` AS `status`,`states`.`state_name` AS `from_state`,`stu`.`gpa` AS `gpa`,`stu`.`test` AS `test`,`stu`.`test_score` AS `test_score`,(case `stu`.`international` when 1 then 'Yes' else 'No' end) AS `international`,`hs`.`school_name` AS `high_school_name`,group_concat(distinct `act`.`activity_name` order by `act`.`activity_name` ASC separator ', ') AS `activities`,`decision`.`comment` AS `decision_comments` from (((((((`students` `stu` join `decision_records` `decision` on((`stu`.`student_id` = `decision`.`student_id`))) join `majors` `major` on((`decision`.`major_id` = `major`.`major_id`))) join `schools` `uni` on((`decision`.`school_id` = `uni`.`school_id`))) join `states` on((`stu`.`state_id` = `states`.`state_id`))) left join `schools` `hs` on((`stu`.`high_school` = `hs`.`school_id`))) left join `activity_records` `actrec` on((`stu`.`student_id` = `actrec`.`student_id`))) left join `activities` `act` on((`actrec`.`activity_id` = `act`.`activity_id`))) group by `decision`.`decision_id`,`stu`.`first_name`,`stu`.`last_name`,`uni`.`school_name`,`major`.`major_name`,`decision`.`year`,`decision`.`status`,`states`.`state_name`,`stu`.`gpa`,`stu`.`test`,`stu`.`test_score`,`stu`.`international`,`hs`.`school_name`,`decision`.`comment` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-09 21:25:45
