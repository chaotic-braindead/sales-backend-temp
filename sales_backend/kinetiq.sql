-- MySQL dump 10.13  Distrib 8.2.0, for Win64 (x86_64)
--
-- Host: localhost    Database: kinetiq
-- ------------------------------------------------------
-- Server version	11.4.3-MariaDB

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add customer',7,'add_customer'),(26,'Can change customer',7,'change_customer'),(27,'Can delete customer',7,'delete_customer'),(28,'Can view customer',7,'view_customer'),(29,'Can add quotation',8,'add_quotation'),(30,'Can change quotation',8,'change_quotation'),(31,'Can delete quotation',8,'delete_quotation'),(32,'Can view quotation',8,'view_quotation'),(33,'Can add quotation items',9,'add_quotationitems'),(34,'Can change quotation items',9,'change_quotationitems'),(35,'Can delete quotation items',9,'delete_quotationitems'),(36,'Can view quotation items',9,'view_quotationitems'),(37,'Can add chart of accounts',10,'add_chartofaccounts'),(38,'Can change chart of accounts',10,'change_chartofaccounts'),(39,'Can delete chart of accounts',10,'delete_chartofaccounts'),(40,'Can view chart of accounts',10,'view_chartofaccounts'),(41,'Can add employee',11,'add_employee'),(42,'Can change employee',11,'change_employee'),(43,'Can delete employee',11,'delete_employee'),(44,'Can view employee',11,'view_employee'),(45,'Can add policies',12,'add_policies'),(46,'Can change policies',12,'change_policies'),(47,'Can delete policies',12,'delete_policies'),(48,'Can view policies',12,'view_policies'),(49,'Can add general ledger accounts',13,'add_generalledgeraccounts'),(50,'Can change general ledger accounts',13,'change_generalledgeraccounts'),(51,'Can delete general ledger accounts',13,'delete_generalledgeraccounts'),(52,'Can view general ledger accounts',13,'view_generalledgeraccounts'),(53,'Can add product',14,'add_product'),(54,'Can change product',14,'change_product'),(55,'Can delete product',14,'delete_product'),(56,'Can view product',14,'view_product');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_customer`
--

DROP TABLE IF EXISTS `customer_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_customer` (
  `customer_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `email_address` varchar(255) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `address_line1` longtext NOT NULL,
  `address_line2` longtext DEFAULT NULL,
  `city` varchar(100) NOT NULL,
  `postal_code` varchar(20) NOT NULL,
  `country` varchar(100) NOT NULL,
  `customer_type` longtext NOT NULL,
  `status` longtext NOT NULL,
  `debt` decimal(10,2) NOT NULL,
  `gl_account_id_id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `email_address` (`email_address`),
  KEY `customer_customer_gl_account_id_id_3b46063e_fk_misc_gene` (`gl_account_id_id`),
  CONSTRAINT `customer_customer_gl_account_id_id_3b46063e_fk_misc_gene` FOREIGN KEY (`gl_account_id_id`) REFERENCES `misc_generalledgeraccounts` (`gl_account_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_customer`
--

LOCK TABLES `customer_customer` WRITE;
/*!40000 ALTER TABLE `customer_customer` DISABLE KEYS */;
INSERT INTO `customer_customer` VALUES (1,'contact@meditechph.com','+63-2-555-1001','123 Health Avenue','Suite 500','Manila','1000','Philippines','Client','Active',1500.00,1,'MediTech Solutions Inc.'),(2,'info@philcaremed.com','+63-2-555-1002','456 Wellness St.','','Quezon City','1101','Philippines','Prospect','Active',500.00,2,'PhilCare Medical Supplies'),(3,'support@lifelinediag.com','+63-2-555-1003','789 Diagnostic Road','Floor 2','Cebu City','6000','Philippines','Lead','Active',0.00,3,'LifeLine Diagnostics'),(4,'sales@biopharmph.com','+63-2-555-1004','101 Pharma Park','','Makati','1200','Philippines','Client','Active',2000.00,4,'BioPharm Innovations'),(5,'contact@wellnesspharma.com','+63-2-555-1005','202 Medical Blvd','','Davao City','8000','Philippines','Prospect','Inactive',300.00,5,'Wellness Pharma Corp.');
/*!40000 ALTER TABLE `customer_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'customer','customer'),(10,'misc','chartofaccounts'),(11,'misc','employee'),(13,'misc','generalledgeraccounts'),(12,'misc','policies'),(14,'misc','product'),(8,'quotation','quotation'),(9,'quotation','quotationitems'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-03-17 08:53:19.962975'),(2,'auth','0001_initial','2025-03-17 08:53:20.285925'),(3,'admin','0001_initial','2025-03-17 08:53:20.358000'),(4,'admin','0002_logentry_remove_auto_add','2025-03-17 08:53:20.366196'),(5,'admin','0003_logentry_add_action_flag_choices','2025-03-17 08:53:20.372091'),(6,'contenttypes','0002_remove_content_type_name','2025-03-17 08:53:20.417662'),(7,'auth','0002_alter_permission_name_max_length','2025-03-17 08:53:20.446902'),(8,'auth','0003_alter_user_email_max_length','2025-03-17 08:53:20.465326'),(9,'auth','0004_alter_user_username_opts','2025-03-17 08:53:20.470326'),(10,'auth','0005_alter_user_last_login_null','2025-03-17 08:53:20.496997'),(11,'auth','0006_require_contenttypes_0002','2025-03-17 08:53:20.498503'),(12,'auth','0007_alter_validators_add_error_messages','2025-03-17 08:53:20.504022'),(13,'auth','0008_alter_user_username_max_length','2025-03-17 08:53:20.538029'),(14,'auth','0009_alter_user_last_name_max_length','2025-03-17 08:53:20.562793'),(15,'auth','0010_alter_group_name_max_length','2025-03-17 08:53:20.579429'),(16,'auth','0011_update_proxy_permissions','2025-03-17 08:53:20.584978'),(17,'auth','0012_alter_user_first_name_max_length','2025-03-17 08:53:20.602334'),(18,'misc','0001_initial','2025-03-17 08:53:20.691956'),(19,'customer','0001_initial','2025-03-17 08:53:20.727342'),(20,'quotation','0001_initial','2025-03-17 08:53:20.826417'),(21,'sessions','0001_initial','2025-03-17 08:53:20.856989'),(22,'customer','0002_customer_name','2025-03-17 09:08:11.213743'),(23,'customer','0003_alter_customer_address_line2','2025-03-17 09:09:02.032903'),(24,'quotation','0002_rename_salesresp_id_quotation_salesrep_id','2025-03-17 09:22:01.565196'),(25,'customer','0004_alter_customer_city_alter_customer_country_and_more','2025-03-17 09:57:58.254694'),(26,'quotation','0003_alter_quotationitems_table','2025-03-17 09:57:58.259219'),(27,'quotation','0004_alter_quotation_type_and_more','2025-03-17 10:22:03.397972');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `misc_chartofaccounts`
--

DROP TABLE IF EXISTS `misc_chartofaccounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `misc_chartofaccounts` (
  `account_code` bigint(20) NOT NULL AUTO_INCREMENT,
  `account_name` longtext NOT NULL,
  PRIMARY KEY (`account_code`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `misc_chartofaccounts`
--

LOCK TABLES `misc_chartofaccounts` WRITE;
/*!40000 ALTER TABLE `misc_chartofaccounts` DISABLE KEYS */;
INSERT INTO `misc_chartofaccounts` VALUES (1,'Medical Equipment Inc.'),(2,'The Best Medical Corporation.'),(3,'Talipapa Hospital.'),(4,'Philippine General Hospital'),(5,'Manila Hospital');
/*!40000 ALTER TABLE `misc_chartofaccounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `misc_employee`
--

DROP TABLE IF EXISTS `misc_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `misc_employee` (
  `employee_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `first_name` longtext NOT NULL,
  `last_name` longtext NOT NULL,
  `email` longtext NOT NULL,
  `phone` longtext NOT NULL,
  `job_title` longtext NOT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `misc_employee`
--

LOCK TABLES `misc_employee` WRITE;
/*!40000 ALTER TABLE `misc_employee` DISABLE KEYS */;
INSERT INTO `misc_employee` VALUES (1,'Rafael Sebastian','Torres','rafael@kinetiq.ph','09123456789','Sales Representative'),(2,'Juan Paolo','Dionisio','paolo@kinetiq.ph','09123456789','Sales Representative'),(3,'Princess Nicole','Gregorio','princess@kinetiq.ph','09123456789','Sales Representative');
/*!40000 ALTER TABLE `misc_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `misc_generalledgeraccounts`
--

DROP TABLE IF EXISTS `misc_generalledgeraccounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `misc_generalledgeraccounts` (
  `gl_account_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `account_name` longtext NOT NULL,
  `account_code_id` bigint(20) NOT NULL,
  PRIMARY KEY (`gl_account_id`),
  KEY `misc_generalledgerac_account_code_id_3a80a8a6_fk_misc_char` (`account_code_id`),
  CONSTRAINT `misc_generalledgerac_account_code_id_3a80a8a6_fk_misc_char` FOREIGN KEY (`account_code_id`) REFERENCES `misc_chartofaccounts` (`account_code`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `misc_generalledgeraccounts`
--

LOCK TABLES `misc_generalledgeraccounts` WRITE;
/*!40000 ALTER TABLE `misc_generalledgeraccounts` DISABLE KEYS */;
INSERT INTO `misc_generalledgeraccounts` VALUES (1,'Medical Equipment Inc.',1),(2,'The Best Medical Corporation..',2),(3,'Talipapa Hospital',3),(4,'Philippine General Hospital',4),(5,'Manila Hospital',5);
/*!40000 ALTER TABLE `misc_generalledgeraccounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `misc_policies`
--

DROP TABLE IF EXISTS `misc_policies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `misc_policies` (
  `policy_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `policy_name` longtext NOT NULL,
  `description` longtext NOT NULL,
  `effective_date` date NOT NULL,
  PRIMARY KEY (`policy_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `misc_policies`
--

LOCK TABLES `misc_policies` WRITE;
/*!40000 ALTER TABLE `misc_policies` DISABLE KEYS */;
INSERT INTO `misc_policies` VALUES (1,'Policy 1','First Policy','0000-00-00'),(2,'Policy 2','Second Policy','0000-00-00'),(3,'Policy 3','Third Policy','0000-00-00');
/*!40000 ALTER TABLE `misc_policies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `misc_product`
--

DROP TABLE IF EXISTS `misc_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `misc_product` (
  `product_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `product_name` longtext NOT NULL,
  `description` longtext NOT NULL,
  `unit_of_measure` longtext NOT NULL,
  `policy_id_id` bigint(20) NOT NULL,
  PRIMARY KEY (`product_id`),
  KEY `misc_product_policy_id_id_99bca2b4_fk_misc_policies_policy_id` (`policy_id_id`),
  CONSTRAINT `misc_product_policy_id_id_99bca2b4_fk_misc_policies_policy_id` FOREIGN KEY (`policy_id_id`) REFERENCES `misc_policies` (`policy_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `misc_product`
--

LOCK TABLES `misc_product` WRITE;
/*!40000 ALTER TABLE `misc_product` DISABLE KEYS */;
INSERT INTO `misc_product` VALUES (1,'Surgical Scalpel','Precision Cutting Tool','pcs',1),(2,'A9','Used for critical patient or longer surgery, close-loop anesthesia.','kg',1),(3,'BeneVision N1','Portable patient monitor for continuous vital signs monitoring.','kg',2),(4,'HyLED 200 M','Surgical light for operating room illumination.','kg	',3),(5,'Lumis 150 VPAP','Ventilator providing variable positive airway pressure for respiratory support.','kg',3);
/*!40000 ALTER TABLE `misc_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quotation_quotation`
--

DROP TABLE IF EXISTS `quotation_quotation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quotation_quotation` (
  `quotation_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date_issued` datetime(6) NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `type` longtext NOT NULL,
  `status` longtext NOT NULL,
  `customer_id_id` bigint(20) NOT NULL,
  `salesrep_id_id` bigint(20) NOT NULL,
  PRIMARY KEY (`quotation_id`),
  KEY `quotation_quotation_customer_id_id_4b97d73c_fk_customer_` (`customer_id_id`),
  KEY `quotation_quotation_salesrep_id_id_39a429a6_fk_misc_empl` (`salesrep_id_id`),
  CONSTRAINT `quotation_quotation_customer_id_id_4b97d73c_fk_customer_` FOREIGN KEY (`customer_id_id`) REFERENCES `customer_customer` (`customer_id`),
  CONSTRAINT `quotation_quotation_salesrep_id_id_39a429a6_fk_misc_empl` FOREIGN KEY (`salesrep_id_id`) REFERENCES `misc_employee` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quotation_quotation`
--

LOCK TABLES `quotation_quotation` WRITE;
/*!40000 ALTER TABLE `quotation_quotation` DISABLE KEYS */;
INSERT INTO `quotation_quotation` VALUES (31,'0000-00-00 00:00:00.000000',250000.00,'Project Based','Pending',1,1),(32,'0000-00-00 00:00:00.000000',180000.00,'Non-Project Based','Approved',2,2),(33,'0000-00-00 00:00:00.000000',12000.00,'Service','Rejected',3,3),(34,'0000-00-00 00:00:00.000000',300000.00,'Project Based','Approved',4,1),(35,'0000-00-00 00:00:00.000000',15000.00,'Non-Project Based','Pending',5,2),(36,'0000-00-00 00:00:00.000000',22000.00,'Service','Approved',1,3),(37,'0000-00-00 00:00:00.000000',350000.00,'Project Based','Rejected',2,1),(38,'0000-00-00 00:00:00.000000',290000.00,'Non-Project Based','Approved',3,2),(39,'0000-00-00 00:00:00.000000',31000.00,'Service','Pending',4,3),(40,'0000-00-00 00:00:00.000000',400000.00,'Project Based','Approved',5,1),(41,'2025-03-17 10:39:09.005233',0.00,'Non-Project Based','Approved',1,1),(42,'2025-03-17 10:42:01.116782',0.00,'Project Based','Pending',2,1),(43,'2025-03-17 10:43:07.490057',0.00,'Project Based','Pending',2,1),(44,'2025-03-17 10:43:58.996227',0.00,'Project Based','Pending',2,1),(45,'2025-03-17 10:45:09.044208',0.00,'Project Based','Pending',2,1),(46,'2025-03-17 10:45:24.910757',194900.00,'Project Based','Pending',2,1),(47,'2025-03-17 10:46:11.904837',194900.00,'Project Based','Pending',2,1),(48,'2025-03-17 10:50:26.732051',194900.00,'Project Based','Pending',2,1);
/*!40000 ALTER TABLE `quotation_quotation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quotation_quotationitems`
--

DROP TABLE IF EXISTS `quotation_quotationitems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quotation_quotationitems` (
  `qitems_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `quantity` int(11) NOT NULL,
  `unit_price` decimal(10,2) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `product_id_id` bigint(20) NOT NULL,
  `quotation_id_id` bigint(20) NOT NULL,
  PRIMARY KEY (`qitems_id`),
  KEY `quotation_quotationi_product_id_id_fbfb2aae_fk_misc_prod` (`product_id_id`),
  KEY `quotation_quotationi_quotation_id_id_b0a13528_fk_quotation` (`quotation_id_id`),
  CONSTRAINT `quotation_quotationi_product_id_id_fbfb2aae_fk_misc_prod` FOREIGN KEY (`product_id_id`) REFERENCES `misc_product` (`product_id`),
  CONSTRAINT `quotation_quotationi_quotation_id_id_b0a13528_fk_quotation` FOREIGN KEY (`quotation_id_id`) REFERENCES `quotation_quotation` (`quotation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quotation_quotationitems`
--

LOCK TABLES `quotation_quotationitems` WRITE;
/*!40000 ALTER TABLE `quotation_quotationitems` DISABLE KEYS */;
INSERT INTO `quotation_quotationitems` VALUES (21,5,1200.00,6000.00,1,31),(22,10,500.00,5000.00,1,32),(23,50,150.00,7500.00,2,33),(24,2,3000.00,6000.00,3,34),(25,20,100.00,2000.00,4,35),(26,200,50.00,10000.00,5,36),(27,3,400.00,1200.00,1,37),(28,5,700.00,3500.00,2,38),(29,2,900.00,1800.00,3,39),(30,100,30.00,3000.00,4,40),(31,5,1200.00,6000.00,1,31),(32,10,500.00,5000.00,2,31),(33,50,150.00,7500.00,3,31),(34,2,3000.00,6000.00,3,32),(35,20,100.00,2000.00,4,33),(36,200,50.00,10000.00,5,33),(37,3,400.00,1200.00,1,34),(38,5,700.00,3500.00,2,34),(39,2,900.00,1800.00,3,34),(40,100,30.00,3000.00,4,35),(41,3,45000.00,0.00,2,46),(42,1,59900.00,0.00,3,46),(43,3,45000.00,0.00,2,47),(44,1,59900.00,0.00,3,47),(45,3,45000.00,0.00,2,48),(46,1,59900.00,0.00,3,48);
/*!40000 ALTER TABLE `quotation_quotationitems` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-17 18:58:25
