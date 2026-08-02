-- MySQL dump 10.13  Distrib 9.7.0, for macos15 (x86_64)
--
-- Host: localhost    Database: moviebooking
-- ------------------------------------------------------
-- Server version	9.7.0

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '55d39e70-49db-11f1-9d2f-a1950558ad5b:1-62';

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `admin_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES (1,'admin_aarav','AdminPass@1','aarav.admin@cinema.com'),(2,'admin_ananya','AdminPass@2','ananya.admin@cinema.com'),(3,'admin_vihaan','AdminPass@3','vihaan.admin@cinema.com'),(4,'admin_diya','AdminPass@4','diya.admin@cinema.com'),(5,'admin_arjun','AdminPass@5','arjun.admin@cinema.com'),(6,'admin_isha','AdminPass@6','isha.admin@cinema.com'),(7,'admin_rohan','AdminPass@7','rohan.admin@cinema.com'),(8,'admin_kavya','AdminPass@8','kavya.admin@cinema.com'),(9,'admin_sai','AdminPass@9','sai.admin@cinema.com'),(10,'admin_meera','AdminPass@10','meera.admin@cinema.com'),(11,'admin_rahul','AdminPass@11','rahul.admin@cinema.com'),(12,'admin_sanya','AdminPass@12','sanya.admin@cinema.com'),(13,'admin_varun','AdminPass@13','varun.admin@cinema.com'),(14,'admin_kriti','AdminPass@14','kriti.admin@cinema.com'),(15,'admin_yash','AdminPass@15','yash.admin@cinema.com'),(16,'admin_simran','AdminPass@16','simran.admin@cinema.com'),(17,'admin_gaurav','AdminPass@17','gaurav.admin@cinema.com'),(18,'admin_nisha','AdminPass@18','nisha.admin@cinema.com'),(19,'admin_tarun','AdminPass@19','tarun.admin@cinema.com'),(20,'admin_shreya','AdminPass@20','shreya.admin@cinema.com');
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Booking`
--

DROP TABLE IF EXISTS `Booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Booking` (
  `booking_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `show_id` int DEFAULT NULL,
  `seat_numbers` varchar(255) DEFAULT NULL,
  `booking_date` datetime DEFAULT NULL,
  `payment_status` varchar(50) DEFAULT NULL,
  `total_amount` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`booking_id`),
  KEY `user_id` (`user_id`),
  KEY `show_id` (`show_id`),
  CONSTRAINT `Booking_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`),
  CONSTRAINT `Booking_ibfk_2` FOREIGN KEY (`show_id`) REFERENCES `Shows` (`show_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Booking`
--

LOCK TABLES `Booking` WRITE;
/*!40000 ALTER TABLE `Booking` DISABLE KEYS */;
INSERT INTO `Booking` VALUES (1,1,1,'A1, A2, A3, A4, A5','2026-02-25 10:15:00','COMPLETED',1750.00),(2,2,2,'B10, B11','2026-02-25 11:20:00','COMPLETED',560.00),(3,3,3,'C4, C5, C6, C7, C8','2026-02-25 12:45:00','COMPLETED',1600.00),(4,4,4,'D1, D2, D3, D4, D5','2026-02-25 14:10:00','COMPLETED',2000.00),(5,5,5,'E12, E13, E14, E15, E16','2026-02-26 09:30:00','COMPLETED',1500.00),(6,6,6,'F8, F9, F10, F11, F12','2026-02-26 10:50:00','COMPLETED',1250.00),(7,7,7,'G1, G2, G3, G4, G5','2026-02-26 13:15:00','COMPLETED',1450.00),(8,8,8,'H5, H6, H7, H8, H9, H10','2026-02-26 15:40:00','COMPLETED',2700.00),(9,9,9,'I1, I2, I3, I4, I5','2026-02-27 11:00:00','COMPLETED',1100.00),(10,10,10,'J10, J11, J12, J13, J14','2026-02-27 12:30:00','COMPLETED',1750.00),(11,11,11,'K2, K3, K4, K5, K6, K7, K8, K9, K10','2026-02-27 14:00:00','COMPLETED',2340.00),(12,12,12,'L1, L2, L3, L4, L5, L6, L7, L8, L9, L10','2026-02-27 16:20:00','COMPLETED',3100.00),(13,13,13,'M5, M6, M7, M8, M9, M10','2026-02-28 09:15:00','COMPLETED',1080.00),(14,14,14,'N1, N2, N3, N4, N5, N6, N7, N8','2026-02-28 10:45:00','COMPLETED',2160.00),(15,15,15,'O10, O11, O12, O13, O14, O15, O16, O17, O18, O19','2026-02-28 13:00:00','COMPLETED',2300.00),(16,16,16,'P1, P2, P3, P4, P5','2026-02-28 15:30:00','COMPLETED',1450.00),(17,17,17,'Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17','2026-03-01 10:00:00','COMPLETED',2400.00),(18,18,18,'R1, R2, R3, R4, R5, R6, R7, R8','2026-03-01 11:30:00','COMPLETED',1680.00),(19,19,19,'S5, S6, S7, S8, S9, S10, S11, S12, S13, S14','2026-03-01 14:15:00','COMPLETED',2600.00),(20,20,20,'T1, T2, T3, T4, T5, T6, T7, T8','2026-03-01 16:50:00','COMPLETED',3040.00);
/*!40000 ALTER TABLE `Booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Halls`
--

DROP TABLE IF EXISTS `Halls`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Halls` (
  `hall_id` int NOT NULL AUTO_INCREMENT,
  `hall_name` varchar(100) DEFAULT NULL,
  `total_seats` int DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`hall_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Halls`
--

LOCK TABLES `Halls` WRITE;
/*!40000 ALTER TABLE `Halls` DISABLE KEYS */;
INSERT INTO `Halls` VALUES (1,'PVR Director’s Cut',120,'Vasant Kunj, New Delhi'),(2,'INOX Megaplex',250,'Inorbit Mall, Mumbai'),(3,'Cinepolis VIP',150,'Forum Mall, Bengaluru'),(4,'PVR ICON Gold Screen 1',180,'Oberoi Mall, Mumbai'),(5,'Miraj Cinemas Screen A',200,'Kalyan, Thane'),(6,'Mukta A2 Multiplex',160,'Central Mall, Ahmedabad'),(7,'Carnival Cinemas Screen 2',220,'Andheri West, Mumbai'),(8,'Waves Cinema Auditorium 1',190,'Noida Sector 18'),(9,'Delite Diamond Screen',300,'Daryaganj, New Delhi'),(10,'Regal Cinema Heritage',350,'Connaught Place, New Delhi'),(11,'Liberty Cinema Screen 1',280,'Marine Lines, Mumbai'),(12,'Eros Cinema IMAX',210,'Churchgate, Mumbai'),(13,'Maratha Mandir Screen 1',400,'Mumbai Central, Mumbai'),(14,'MovieMax Screen 3',170,'Sion, Mumbai'),(15,'Rajmandir Cinema Grand',320,'Panch Batti, Jaipur'),(16,'Movietime Cinema Hall B',140,'Pitampura, New Delhi'),(17,'NY Cinemas Screen 1',160,'Ghatkopar, Mumbai'),(18,'SRS Cinemas Screen 2',180,'Faridabad, Haryana'),(19,'Pacific Mall Multiplex',230,'Subhash Nagar, New Delhi'),(20,'PVR Superplex Screen 5',260,'Logix City Center, Noida');
/*!40000 ALTER TABLE `Halls` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Movies`
--

DROP TABLE IF EXISTS `Movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Movies` (
  `movie_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `genre` varchar(100) DEFAULT NULL,
  `language` varchar(100) DEFAULT NULL,
  `duration` int DEFAULT NULL,
  `rating` decimal(3,1) DEFAULT NULL,
  `release_date` date DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`movie_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Movies`
--

LOCK TABLES `Movies` WRITE;
/*!40000 ALTER TABLE `Movies` DISABLE KEYS */;
INSERT INTO `Movies` VALUES (1,'Saiyaara','Romantic Drama','Hindi',145,8.5,'2025-02-14','An emotional love story testing relationships across boundaries.'),(2,'Chennai Express','Action Comedy','Hindi',141,7.4,'2013-08-08','A man journeying to Rameshwaram inadvertently gets involved with a local don\'s daughter.'),(3,'Yeh Jawaani Hai Deewani','Romantic Comedy','Hindi',160,8.2,'2013-05-31','Two people discover love and self-growth during a trek and subsequent reunion.'),(4,'The Amazing Spider-Man','Superhero Action','English',136,7.6,'2012-07-03','Peter Parker gains spider-like powers and battles the monstrous Lizard in NYC.'),(5,'Interstellar','Sci-Fi Drama','English',169,9.3,'2014-11-07','A team of explorers travel through a wormhole in space to ensure humanity\'s survival.'),(6,'Inception','Sci-Fi Action','English',148,9.0,'2010-07-16','A thief who steals corporate secrets through dream-sharing technology.'),(7,'The Dark Knight','Action Crime','English',152,9.2,'2008-07-18','Batman faces his ultimate test against the sadistic mastermind known as the Joker.'),(8,'Avengers: Endgame','Superhero Action','English',181,8.9,'2019-04-26','The Avengers assemble once more to reverse Thanos\'s actions and restore balance.'),(9,'Titanic','Romantic Drama','English',195,8.8,'1997-12-19','A seventeen-year-old aristocrat falls in love with a kind-hearted artist aboard the RMS Titanic.'),(10,'Oppenheimer','Biographical Drama','English',180,8.7,'2023-07-21','The story of American scientist J. Robert Oppenheimer and his role in the Manhattan Project.'),(11,'3 Idiots','Comedy Drama','Hindi',170,8.9,'2009-12-25','Two friends search for their long-lost college companion while recalling their engineering days.'),(12,'Dangal','Biographical Sports','Hindi',161,8.8,'2016-12-23','A former wrestler trains his daughters to become world-class wrestlers.'),(13,'Zindagi Na Milegi Dobara','Comedy Drama','Hindi',155,8.2,'2011-07-15','Three friends go on a road trip in Spain that turns into an opportunity to face their fears.'),(14,'Pathaan','Action Thriller','Hindi',146,7.8,'2023-01-25','An exiled RAW field operative takes on a mercenary leader targeting India.'),(15,'Jawan','Action Thriller','Hindi',169,8.2,'2023-09-07','A personal vendetta drives a man to rectify social wrongs while honoring a promise.'),(16,'Brahmastra: Part One - Shiva','Fantasy Action','Hindi',167,7.1,'2022-09-09','A young man learns about his secret connection to a legendary magical weapon.'),(17,'Stree','Horror Comedy','Hindi',128,8.2,'2018-08-31','In a small town, men disappear mysteriously during a festive period.'),(18,'Chhichhore','Comedy Drama','Hindi',143,8.3,'2019-09-06','A tragic incident causes a middle-aged man to reunite with his college friends.'),(19,'Sholay','Action Adventure','Hindi',204,9.0,'1975-08-15','Two ex-convicts are hired to capture a ruthless bandit terrorizing a village.'),(20,'Dilwale Dulhania Le Jayenge','Romance','Hindi',189,8.9,'1995-10-20','A young man tries to win over the conservative father of the girl he loves.');
/*!40000 ALTER TABLE `Movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Payments`
--

DROP TABLE IF EXISTS `Payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Payments` (
  `payment_id` int NOT NULL AUTO_INCREMENT,
  `booking_id` int DEFAULT NULL,
  `payment_mode` varchar(50) DEFAULT NULL,
  `transaction_id` varchar(255) DEFAULT NULL,
  `payment_date` datetime DEFAULT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `booking_id` (`booking_id`),
  CONSTRAINT `Payments_ibfk_1` FOREIGN KEY (`booking_id`) REFERENCES `Booking` (`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Payments`
--

LOCK TABLES `Payments` WRITE;
/*!40000 ALTER TABLE `Payments` DISABLE KEYS */;
INSERT INTO `Payments` VALUES (1,1,'UPI','TXN_UPI_10001','2026-02-25 10:16:05'),(2,2,'Credit Card','TXN_CC_10002','2026-02-25 11:21:10'),(3,3,'Debit Card','TXN_DC_10003','2026-02-25 12:46:22'),(4,4,'Net Banking','TXN_NB_10004','2026-02-25 14:11:45'),(5,5,'UPI','TXN_UPI_10005','2026-02-26 09:31:12'),(6,6,'Wallet','TXN_WAL_10006','2026-02-26 10:51:30'),(7,7,'UPI','TXN_UPI_10007','2026-02-26 13:16:02'),(8,8,'Credit Card','TXN_CC_10008','2026-02-26 15:41:18'),(9,9,'Debit Card','TXN_DC_10009','2026-02-27 11:01:05'),(10,10,'UPI','TXN_UPI_10010','2026-02-27 12:31:50'),(11,11,'Net Banking','TXN_NB_10011','2026-02-27 14:01:12'),(12,12,'Credit Card','TXN_CC_10012','2026-02-27 16:21:30'),(13,13,'UPI','TXN_UPI_10013','2026-02-28 09:16:00'),(14,14,'Debit Card','TXN_DC_10014','2026-02-28 10:46:15'),(15,15,'UPI','TXN_UPI_10015','2026-02-28 13:01:40'),(16,16,'Wallet','TXN_WAL_10016','2026-02-28 15:31:25'),(17,17,'Credit Card','TXN_CC_10017','2026-03-01 10:01:10'),(18,18,'UPI','TXN_UPI_10018','2026-03-01 11:31:55'),(19,19,'Net Banking','TXN_NB_10019','2026-03-01 14:16:20'),(20,20,'UPI','TXN_UPI_10020','2026-03-01 16:51:05');
/*!40000 ALTER TABLE `Payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Shows`
--

DROP TABLE IF EXISTS `Shows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Shows` (
  `show_id` int NOT NULL AUTO_INCREMENT,
  `movie_id` int DEFAULT NULL,
  `hall_id` int DEFAULT NULL,
  `show_date` date DEFAULT NULL,
  `show_time` time DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `available_seats` int DEFAULT NULL,
  PRIMARY KEY (`show_id`),
  KEY `movie_id` (`movie_id`),
  KEY `hall_id` (`hall_id`),
  CONSTRAINT `Shows_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `Movies` (`movie_id`),
  CONSTRAINT `Shows_ibfk_2` FOREIGN KEY (`hall_id`) REFERENCES `Halls` (`hall_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Shows`
--

LOCK TABLES `Shows` WRITE;
/*!40000 ALTER TABLE `Shows` DISABLE KEYS */;
INSERT INTO `Shows` VALUES (1,1,1,'2026-03-01','10:00:00',350.00,115),(2,2,2,'2026-03-01','13:30:00',280.00,240),(3,3,3,'2026-03-01','17:00:00',320.00,142),(4,4,4,'2026-03-01','20:30:00',400.00,175),(5,5,5,'2026-03-02','11:00:00',300.00,195),(6,6,6,'2026-03-02','14:30:00',250.00,155),(7,7,7,'2026-03-02','18:00:00',290.00,210),(8,8,8,'2026-03-02','21:15:00',450.00,180),(9,9,9,'2026-03-03','10:30:00',220.00,290),(10,10,10,'2026-03-03','14:00:00',350.00,340),(11,11,11,'2026-03-03','17:30:00',260.00,270),(12,12,12,'2026-03-03','21:00:00',310.00,200),(13,13,13,'2026-03-04','11:30:00',180.00,390),(14,14,14,'2026-03-04','15:00:00',270.00,162),(15,15,15,'2026-03-04','18:30:00',230.00,310),(16,16,16,'2026-03-04','22:00:00',290.00,135),(17,17,17,'2026-03-05','12:00:00',240.00,150),(18,18,18,'2026-03-05','15:30:00',210.00,172),(19,19,19,'2026-03-05','19:00:00',260.00,220),(20,20,20,'2026-03-05','22:30:00',380.00,252);
/*!40000 ALTER TABLE `Shows` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `join_date` date DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'Aarav Sharma','aarav.sharma@example.com','9876543210','Pass@123','2026-01-05'),(2,'Sneha Reddy','sneha.reddy@example.com','9876543211','Pass@123','2026-01-08'),(3,'Amit Verma','amit.verma@example.com','9876543212','Pass@123','2026-01-10'),(4,'Priya Nair','priya.nair@example.com','9876543213','Pass@123','2026-01-12'),(5,'Karan Mehta','karan.mehta@example.com','9876543214','Pass@123','2026-01-15'),(6,'Neha Kapoor','neha.kapoor@example.com','9876543215','Pass@123','2026-01-18'),(7,'Vikram Singh','vikram.singh@example.com','9876543216','Pass@123','2026-01-20'),(8,'Anjali Rao','anjali.rao@example.com','9876543217','Pass@123','2026-01-22'),(9,'Rohit Das','rohit.das@example.com','9876543218','Pass@123','2026-01-25'),(10,'Pooja Iyer','pooja.iyer@example.com','9876543219','Pass@123','2026-01-28'),(11,'Rohan Gupta','rohan.gupta@example.com','9876543220','Pass@123','2026-02-01'),(12,'Tanvi Saxena','tanvi.saxena@example.com','9876543221','Pass@123','2026-02-03'),(13,'Siddharth Joshi','siddharth.j@example.com','9876543222','Pass@123','2026-02-05'),(14,'Riya Sen','riya.sen@example.com','9876543223','Pass@123','2026-02-07'),(15,'Kabir Malhotra','kabir.m@example.com','9876543224','Pass@123','2026-02-10'),(16,'Ishita Roy','ishita.roy@example.com','9876543225','Pass@123','2026-02-12'),(17,'Aditya Chawla','aditya.c@example.com','9876543226','Pass@123','2026-02-14'),(18,'Kavya Bansal','kavya.b@example.com','9876543227','Pass@123','2026-02-16'),(19,'Devansh Agarwal','devansh.a@example.com','9876543228','Pass@123','2026-02-18'),(20,'Meera Bhatia','meera.b@example.com','9876543229','Pass@123','2026-02-20');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-08-02 10:58:17
