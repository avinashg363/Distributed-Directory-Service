-- MySQL dump 10.13  Distrib 5.7.22, for osx10.13 (x86_64)
--
-- Host: localhost    Database: DS
-- ------------------------------------------------------
-- Server version	5.7.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `DIT`
--

DROP TABLE IF EXISTS `DIT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DIT` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `tablename` varchar(100) DEFAULT NULL,
  `parent` int(11) DEFAULT NULL,
  `classname` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DIT`
--

LOCK TABLES `DIT` WRITE;
/*!40000 ALTER TABLE `DIT` DISABLE KEYS */;
INSERT INTO `DIT` VALUES (1,'IITKGP',NULL,NULL,'campus'),(2,'KGPCAMPUS',NULL,1,'campus'),(3,'KOLKATAGUESTHOUSE',NULL,1,'campus'),(4,'HALLS',NULL,2,'InstitutionalBody'),(5,'PROFS','prof',2,'person'),(6,'HMC',NULL,2,'InstitutionalBody'),(7,'worker','kolworker',3,'person'),(8,'RK',NULL,4,'InstitutionalBody'),(9,'RP',NULL,4,'InstitutionalBody'),(10,'MS',NULL,4,'InstitutionalBody'),(11,'EMPLOYEE','hmcemployee',6,'person'),(12,'worker','hmcworker',6,'person'),(13,'student','RKstudent',8,'person'),(14,'worker','RKworker',8,'person'),(15,'student','RPstudent',9,'person'),(16,'worker','RPworker',9,'person'),(17,'student','MSstudent',10,'person'),(18,'worker','MSworker',10,'person');
/*!40000 ALTER TABLE `DIT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MSstudent`
--

DROP TABLE IF EXISTS `MSstudent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MSstudent` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MSstudent`
--

LOCK TABLES `MSstudent` WRITE;
/*!40000 ALTER TABLE `MSstudent` DISABLE KEYS */;
/*!40000 ALTER TABLE `MSstudent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MSworker`
--

DROP TABLE IF EXISTS `MSworker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MSworker` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MSworker`
--

LOCK TABLES `MSworker` WRITE;
/*!40000 ALTER TABLE `MSworker` DISABLE KEYS */;
/*!40000 ALTER TABLE `MSworker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RKstudent`
--

DROP TABLE IF EXISTS `RKstudent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RKstudent` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RKstudent`
--

LOCK TABLES `RKstudent` WRITE;
/*!40000 ALTER TABLE `RKstudent` DISABLE KEYS */;
/*!40000 ALTER TABLE `RKstudent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RKworker`
--

DROP TABLE IF EXISTS `RKworker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RKworker` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RKworker`
--

LOCK TABLES `RKworker` WRITE;
/*!40000 ALTER TABLE `RKworker` DISABLE KEYS */;
/*!40000 ALTER TABLE `RKworker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RPstudent`
--

DROP TABLE IF EXISTS `RPstudent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RPstudent` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RPstudent`
--

LOCK TABLES `RPstudent` WRITE;
/*!40000 ALTER TABLE `RPstudent` DISABLE KEYS */;
/*!40000 ALTER TABLE `RPstudent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RPworker`
--

DROP TABLE IF EXISTS `RPworker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RPworker` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RPworker`
--

LOCK TABLES `RPworker` WRITE;
/*!40000 ALTER TABLE `RPworker` DISABLE KEYS */;
/*!40000 ALTER TABLE `RPworker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hmcemployee`
--

DROP TABLE IF EXISTS `hmcemployee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hmcemployee` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hmcemployee`
--

LOCK TABLES `hmcemployee` WRITE;
/*!40000 ALTER TABLE `hmcemployee` DISABLE KEYS */;
/*!40000 ALTER TABLE `hmcemployee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hmcemployee_initial`
--

DROP TABLE IF EXISTS `hmcemployee_initial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hmcemployee_initial` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hmcemployee_initial`
--

LOCK TABLES `hmcemployee_initial` WRITE;
/*!40000 ALTER TABLE `hmcemployee_initial` DISABLE KEYS */;
/*!40000 ALTER TABLE `hmcemployee_initial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hmcworker`
--

DROP TABLE IF EXISTS `hmcworker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hmcworker` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hmcworker`
--

LOCK TABLES `hmcworker` WRITE;
/*!40000 ALTER TABLE `hmcworker` DISABLE KEYS */;
/*!40000 ALTER TABLE `hmcworker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hmcworker_inital`
--

DROP TABLE IF EXISTS `hmcworker_inital`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hmcworker_inital` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hmcworker_inital`
--

LOCK TABLES `hmcworker_inital` WRITE;
/*!40000 ALTER TABLE `hmcworker_inital` DISABLE KEYS */;
/*!40000 ALTER TABLE `hmcworker_inital` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kolworker`
--

DROP TABLE IF EXISTS `kolworker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kolworker` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kolworker`
--

LOCK TABLES `kolworker` WRITE;
/*!40000 ALTER TABLE `kolworker` DISABLE KEYS */;
/*!40000 ALTER TABLE `kolworker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `msstudent_inital`
--

DROP TABLE IF EXISTS `msstudent_inital`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `msstudent_inital` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `msstudent_inital`
--

LOCK TABLES `msstudent_inital` WRITE;
/*!40000 ALTER TABLE `msstudent_inital` DISABLE KEYS */;
/*!40000 ALTER TABLE `msstudent_inital` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `msworker_inital`
--

DROP TABLE IF EXISTS `msworker_inital`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `msworker_inital` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `msworker_inital`
--

LOCK TABLES `msworker_inital` WRITE;
/*!40000 ALTER TABLE `msworker_inital` DISABLE KEYS */;
/*!40000 ALTER TABLE `msworker_inital` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prof`
--

DROP TABLE IF EXISTS `prof`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prof` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prof`
--

LOCK TABLES `prof` WRITE;
/*!40000 ALTER TABLE `prof` DISABLE KEYS */;
/*!40000 ALTER TABLE `prof` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prof_initial`
--

DROP TABLE IF EXISTS `prof_initial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prof_initial` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prof_initial`
--

LOCK TABLES `prof_initial` WRITE;
/*!40000 ALTER TABLE `prof_initial` DISABLE KEYS */;
/*!40000 ALTER TABLE `prof_initial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rkstudent_initial`
--

DROP TABLE IF EXISTS `rkstudent_initial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rkstudent_initial` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rkstudent_initial`
--

LOCK TABLES `rkstudent_initial` WRITE;
/*!40000 ALTER TABLE `rkstudent_initial` DISABLE KEYS */;
/*!40000 ALTER TABLE `rkstudent_initial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rkworker_initial`
--

DROP TABLE IF EXISTS `rkworker_initial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rkworker_initial` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rkworker_initial`
--

LOCK TABLES `rkworker_initial` WRITE;
/*!40000 ALTER TABLE `rkworker_initial` DISABLE KEYS */;
/*!40000 ALTER TABLE `rkworker_initial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rpstudent_inital`
--

DROP TABLE IF EXISTS `rpstudent_inital`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rpstudent_inital` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rpstudent_inital`
--

LOCK TABLES `rpstudent_inital` WRITE;
/*!40000 ALTER TABLE `rpstudent_inital` DISABLE KEYS */;
/*!40000 ALTER TABLE `rpstudent_inital` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rpworker_initial`
--

DROP TABLE IF EXISTS `rpworker_initial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rpworker_initial` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
  `Hall` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rpworker_initial`
--

LOCK TABLES `rpworker_initial` WRITE;
/*!40000 ALTER TABLE `rpworker_initial` DISABLE KEYS */;
/*!40000 ALTER TABLE `rpworker_initial` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-28 23:30:32
