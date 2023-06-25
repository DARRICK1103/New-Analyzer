-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 25, 2023 at 09:57 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `newspaper_analyzer`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `ADMIN_ID` varchar(10) NOT NULL,
  `NAME` varchar(50) NOT NULL,
  `GENDER` varchar(6) NOT NULL,
  `AGE` int(3) NOT NULL,
  `IC_NUMBER` varchar(12) NOT NULL,
  `CONTACT_NUMBER` varchar(11) NOT NULL,
  `EMAIL` varchar(250) NOT NULL,
  `STATUS` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`ADMIN_ID`, `NAME`, `GENDER`, `AGE`, `IC_NUMBER`, `CONTACT_NUMBER`, `EMAIL`, `STATUS`) VALUES
('A000000001', 'Zi Bin', 'Male', 22, '010501040369', '0166513198', 'zbtan51@gmail.com', 1),
('A000000002', 'May', 'Female', 21, '010821040329', '0196621531', 'may@gmail.com', 1);

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `CATEGORY_ID` varchar(10) NOT NULL,
  `NAME` varchar(50) NOT NULL,
  `DESCRIPTION` varchar(500) NOT NULL,
  `STATUS` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `COMMENT_ID` varchar(10) NOT NULL,
  `CONTENT` varchar(500) NOT NULL,
  `USER_ID` varchar(10) NOT NULL,
  `NEWS_ID` varchar(10) NOT NULL,
  `STATUS` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `news`
--

CREATE TABLE `news` (
  `NEWS_ID` varchar(10) NOT NULL,
  `TITLE` varchar(250) NOT NULL,
  `URL` varchar(500) NOT NULL,
  `SOURCE_ID` varchar(10) NOT NULL,
  `CATEGORY_ID` varchar(10) NOT NULL,
  `STATUS` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `read_history`
--

CREATE TABLE `read_history` (
  `HISTORY_ID` varchar(10) NOT NULL,
  `USER_ID` varchar(10) NOT NULL,
  `NEWS_ID` varchar(10) NOT NULL,
  `DATE_TIME` datetime NOT NULL,
  `STATUS` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `source`
--

CREATE TABLE `source` (
  `SOURCE_ID` varchar(10) NOT NULL,
  `NAME` varchar(50) NOT NULL,
  `URL` varchar(500) NOT NULL,
  `STATUS` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `USER_ID` varchar(10) NOT NULL,
  `NAME` varchar(50) NOT NULL,
  `GENDER` varchar(6) NOT NULL,
  `AGE` int(3) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `STATUS` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_admin`
--

CREATE TABLE `user_admin` (
  `UA_ID` varchar(10) NOT NULL,
  `ADMIN_ID` varchar(10) NOT NULL,
  `USER_ID` varchar(10) NOT NULL,
  `STATUS` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`ADMIN_ID`),
  ADD UNIQUE KEY `ADMIN_ID` (`ADMIN_ID`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`CATEGORY_ID`),
  ADD UNIQUE KEY `CATEGORY_ID` (`CATEGORY_ID`);

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`COMMENT_ID`),
  ADD KEY `USER_ID` (`USER_ID`),
  ADD KEY `NEWS_ID` (`NEWS_ID`);

--
-- Indexes for table `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`NEWS_ID`),
  ADD KEY `SOURCE_ID` (`SOURCE_ID`),
  ADD KEY `CATEGORY_ID` (`CATEGORY_ID`);

--
-- Indexes for table `read_history`
--
ALTER TABLE `read_history`
  ADD PRIMARY KEY (`HISTORY_ID`),
  ADD KEY `USER_ID` (`USER_ID`),
  ADD KEY `NEWS_ID` (`NEWS_ID`);

--
-- Indexes for table `source`
--
ALTER TABLE `source`
  ADD PRIMARY KEY (`SOURCE_ID`),
  ADD UNIQUE KEY `SOURCE_ID` (`SOURCE_ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`USER_ID`),
  ADD UNIQUE KEY `USER_ID` (`USER_ID`);

--
-- Indexes for table `user_admin`
--
ALTER TABLE `user_admin`
  ADD PRIMARY KEY (`UA_ID`),
  ADD UNIQUE KEY `UA_ID` (`UA_ID`),
  ADD KEY `ADMIN_ID` (`ADMIN_ID`),
  ADD KEY `USER_ID` (`USER_ID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`USER_ID`) REFERENCES `users` (`USER_ID`),
  ADD CONSTRAINT `comments_ibfk_2` FOREIGN KEY (`NEWS_ID`) REFERENCES `news` (`NEWS_ID`);

--
-- Constraints for table `news`
--
ALTER TABLE `news`
  ADD CONSTRAINT `news_ibfk_1` FOREIGN KEY (`SOURCE_ID`) REFERENCES `source` (`SOURCE_ID`),
  ADD CONSTRAINT `news_ibfk_2` FOREIGN KEY (`CATEGORY_ID`) REFERENCES `category` (`CATEGORY_ID`);

--
-- Constraints for table `read_history`
--
ALTER TABLE `read_history`
  ADD CONSTRAINT `read_history_ibfk_1` FOREIGN KEY (`USER_ID`) REFERENCES `users` (`USER_ID`),
  ADD CONSTRAINT `read_history_ibfk_2` FOREIGN KEY (`NEWS_ID`) REFERENCES `news` (`NEWS_ID`);

--
-- Constraints for table `user_admin`
--
ALTER TABLE `user_admin`
  ADD CONSTRAINT `user_admin_ibfk_1` FOREIGN KEY (`ADMIN_ID`) REFERENCES `admin` (`ADMIN_ID`),
  ADD CONSTRAINT `user_admin_ibfk_2` FOREIGN KEY (`USER_ID`) REFERENCES `users` (`USER_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
