-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 14, 2024 at 12:03 PM
-- Server version: 8.0.37
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `acu`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET= utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add doctor', 1, 'add_doctor'),
(2, 'Can change doctor', 1, 'change_doctor'),
(3, 'Can delete doctor', 1, 'delete_doctor'),
(4, 'Can view doctor', 1, 'view_doctor'),
(5, 'Can add user', 2, 'add_user'),
(6, 'Can change user', 2, 'change_user'),
(7, 'Can delete user', 2, 'delete_user'),
(8, 'Can view user', 2, 'view_user'),
(9, 'Can add patient', 3, 'add_patient'),
(10, 'Can change patient', 3, 'change_patient'),
(11, 'Can delete patient', 3, 'delete_patient'),
(12, 'Can view patient', 3, 'view_patient'),
(13, 'Can add medical result', 4, 'add_medicalresult'),
(14, 'Can change medical result', 4, 'change_medicalresult'),
(15, 'Can delete medical result', 4, 'delete_medicalresult'),
(16, 'Can view medical result', 4, 'view_medicalresult'),
(17, 'Can add appointment', 5, 'add_appointment'),
(18, 'Can change appointment', 5, 'change_appointment'),
(19, 'Can delete appointment', 5, 'delete_appointment'),
(20, 'Can view appointment', 5, 'view_appointment'),
(21, 'Can add log entry', 6, 'add_logentry'),
(22, 'Can change log entry', 6, 'change_logentry'),
(23, 'Can delete log entry', 6, 'delete_logentry'),
(24, 'Can view log entry', 6, 'view_logentry'),
(25, 'Can add permission', 7, 'add_permission'),
(26, 'Can change permission', 7, 'change_permission'),
(27, 'Can delete permission', 7, 'delete_permission'),
(28, 'Can view permission', 7, 'view_permission'),
(29, 'Can add group', 8, 'add_group'),
(30, 'Can change group', 8, 'change_group'),
(31, 'Can delete group', 8, 'delete_group'),
(32, 'Can view group', 8, 'view_group'),
(33, 'Can add user', 9, 'add_user'),
(34, 'Can change user', 9, 'change_user'),
(35, 'Can delete user', 9, 'delete_user'),
(36, 'Can view user', 9, 'view_user'),
(37, 'Can add content type', 10, 'add_contenttype'),
(38, 'Can change content type', 10, 'change_contenttype'),
(39, 'Can delete content type', 10, 'delete_contenttype'),
(40, 'Can view content type', 10, 'view_contenttype'),
(41, 'Can add session', 11, 'add_session'),
(42, 'Can change session', 11, 'change_session'),
(43, 'Can delete session', 11, 'delete_session'),
(44, 'Can view session', 11, 'view_session'),
(45, 'Can add blackbox medical measurement', 12, 'add_blackboxmedicalmeasurement'),
(46, 'Can change blackbox medical measurement', 12, 'change_blackboxmedicalmeasurement'),
(47, 'Can delete blackbox medical measurement', 12, 'delete_blackboxmedicalmeasurement'),
(48, 'Can view blackbox medical measurement', 12, 'view_blackboxmedicalmeasurement'),
(49, 'Can add emg measurement', 13, 'add_emgmeasurement'),
(50, 'Can change emg measurement', 13, 'change_emgmeasurement'),
(51, 'Can delete emg measurement', 13, 'delete_emgmeasurement'),
(52, 'Can view emg measurement', 13, 'view_emgmeasurement'),
(53, 'Can add gaitband measurement', 14, 'add_gaitbandmeasurement'),
(54, 'Can change gaitband measurement', 14, 'change_gaitbandmeasurement'),
(55, 'Can delete gaitband measurement', 14, 'delete_gaitbandmeasurement'),
(56, 'Can view gaitband measurement', 14, 'view_gaitbandmeasurement'),
(57, 'Can add measurement', 15, 'add_measurement'),
(58, 'Can change measurement', 15, 'change_measurement'),
(59, 'Can delete measurement', 15, 'delete_measurement'),
(60, 'Can view measurement', 15, 'view_measurement'),
(61, 'Can add prescription', 16, 'add_prescription'),
(62, 'Can change prescription', 16, 'change_prescription'),
(63, 'Can delete prescription', 16, 'delete_prescription'),
(64, 'Can view prescription', 16, 'view_prescription'),
(65, 'Can add uric acid measurement', 17, 'add_uricacidmeasurement'),
(66, 'Can change uric acid measurement', 17, 'change_uricacidmeasurement'),
(67, 'Can delete uric acid measurement', 17, 'delete_uricacidmeasurement'),
(68, 'Can view uric acid measurement', 17, 'view_uricacidmeasurement'),
(69, 'Can add profile', 18, 'add_profile'),
(70, 'Can change profile', 18, 'change_profile'),
(71, 'Can delete profile', 18, 'delete_profile'),
(72, 'Can view profile', 18, 'view_profile');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(67, 'pbkdf2_sha256$870000$xntDZxmBPaXZrZ5MnOhq2E$drxiyJNjSNXpRM7nr/MFihk6nXkIKbKOu+7aQ1Cc+qw=', '2024-08-14 09:58:14.357526', 1, 'vcons', '', '', 'victor@gmail.com', 1, 1, '2024-08-14 07:46:08.631016'),
(68, 'pbkdf2_sha256$870000$kXRtCHEmAZUXrFRXol6s9l$AgkVfZ6aDdfgf5Vzl+BUYPtvfxJprT66y6jKnjaZyIQ=', '2024-08-14 09:57:43.033694', 0, 'pac', '', '', '', 0, 1, '2024-08-14 07:54:19.544391');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-08-14 07:52:35.241184', '127', 'vcons', 2, '[{\"changed\": {\"fields\": [\"Nume\", \"Prenume\", \"Cnp\", \"Adresa\", \"Varsta\", \"Telefon\", \"Email\", \"Role\"]}}]', 18, 67),
(2, '2024-08-14 07:54:20.163104', '68', 'pac', 1, '[{\"added\": {}}]', 9, 67),
(3, '2024-08-14 07:55:22.103135', '128', 'pac', 2, '[{\"changed\": {\"fields\": [\"Nume\", \"Prenume\", \"Cnp\", \"Adresa\", \"Varsta\", \"Telefon\", \"Email\", \"Role\", \"Id doctor\"]}}]', 18, 67),
(4, '2024-08-14 09:34:46.207364', '1', 'Ionescu Pop', 1, '[{\"added\": {}}]', 3, 67),
(5, '2024-08-14 09:55:04.390108', '1', 'Ionescu Pop - 2024-08-16 18:00:00+00:00', 1, '[{\"added\": {}}]', 5, 67);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(6, 'admin', 'logentry'),
(8, 'auth', 'group'),
(7, 'auth', 'permission'),
(9, 'auth', 'user'),
(10, 'contenttypes', 'contenttype'),
(5, 'm4h', 'appointment'),
(12, 'm4h', 'blackboxmedicalmeasurement'),
(1, 'm4h', 'doctor'),
(13, 'm4h', 'emgmeasurement'),
(14, 'm4h', 'gaitbandmeasurement'),
(15, 'm4h', 'measurement'),
(4, 'm4h', 'medicalresult'),
(3, 'm4h', 'patient'),
(16, 'm4h', 'prescription'),
(18, 'm4h', 'profile'),
(17, 'm4h', 'uricacidmeasurement'),
(2, 'm4h', 'user'),
(11, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-08-08 09:44:12.054050'),
(2, 'auth', '0001_initial', '2024-08-08 09:44:13.090866'),
(3, 'admin', '0001_initial', '2024-08-08 09:44:13.275986'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-08-08 09:44:13.283985'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-08-08 09:44:13.295989'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-08-08 09:44:13.407029'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-08-08 09:44:13.484950'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-08-08 09:44:13.566490'),
(9, 'auth', '0004_alter_user_username_opts', '2024-08-08 09:44:13.574490'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-08-08 09:44:13.642128'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-08-08 09:44:13.646132'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-08-08 09:44:13.652640'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-08-08 09:44:13.731665'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-08-08 09:44:13.831718'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-08-08 09:44:13.934259'),
(16, 'auth', '0011_update_proxy_permissions', '2024-08-08 09:44:13.952183'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-08-08 09:44:14.048712'),
(18, 'm4h', '0001_initial', '2024-08-08 09:44:14.770458'),
(19, 'sessions', '0001_initial', '2024-08-08 09:44:14.818751'),
(20, 'm4h', '0002_remove_medicalresult_doctor_alter_patient_doctor_and_more', '2024-08-08 13:06:04.168737'),
(21, 'm4h', '0003_profile', '2024-08-08 13:58:27.345522'),
(22, 'm4h', '0004_remove_profile_nume_remove_profile_prenume_and_more', '2024-08-09 08:04:06.474313'),
(23, 'm4h', '0002_profile_email_profile_id_doctor_profile_last_active_and_more', '2024-08-09 08:10:32.055254'),
(24, 'm4h', '0003_alter_profile_role', '2024-08-12 11:12:39.758686'),
(25, 'm4h', '0004_remove_profile_id_doctor_remove_profile_last_active_and_more', '2024-08-14 07:04:46.182411'),
(26, 'm4h', '0005_alter_profile_varsta', '2024-08-14 07:12:13.509312'),
(27, 'm4h', '0006_profile_id_doctor_profile_last_active_and_more', '2024-08-14 07:17:56.527678');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('a2h6tn24nj20wkb7amdma1apxaiuap3g', 'e30:1sdU9A:uTgCJmCUctHWdnur_4iukgZiFqgQ0zpDslKKpjkwJ7o', '2024-08-26 12:27:36.020350'),
('t3i2zfmysys1ucrwkn2snpp0vl0at2nz', '.eJxVjMsOwiAQRf-FtSEw8nTp3m8gAwNSNZCUdmX8d9ukC93ec859s4DrUsM68hwmYhdmLDv9jhHTM7ed0APbvfPU2zJPke8KP-jgt075dT3cv4OKo251QU8aJERdoDiLkuCMFrMzjkAYJZRVtBGw3hpMEbxWKIWWxrsCUbLPFwJxN1A:1seAli:Rill5Va3LFg2qvILkuzSmlC1F2anuv5HC3O9gFdP2dY', '2024-08-28 09:58:14.362291');

-- --------------------------------------------------------

--
-- Table structure for table `m4h_appointment`
--

CREATE TABLE `m4h_appointment` (
  `id` bigint NOT NULL,
  `appointment_date` datetime(6) NOT NULL,
  `doctor_id` int NOT NULL,
  `patient_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `m4h_appointment`
--

INSERT INTO `m4h_appointment` (`id`, `appointment_date`, `doctor_id`, `patient_id`) VALUES
(1, '2024-08-16 18:00:00.000000', 67, 1);

-- --------------------------------------------------------

--
-- Table structure for table `m4h_blackboxmedicalmeasurement`
--

CREATE TABLE `m4h_blackboxmedicalmeasurement` (
  `id` bigint NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `ekg` double NOT NULL,
  `pulse` double NOT NULL,
  `spo2` double NOT NULL,
  `temperature` double NOT NULL,
  `co2` double NOT NULL,
  `alcoolemia` double NOT NULL,
  `patient_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `m4h_emgmeasurement`
--

CREATE TABLE `m4h_emgmeasurement` (
  `id` bigint NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `muscle_activity` double NOT NULL,
  `patient_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `m4h_gaitbandmeasurement`
--

CREATE TABLE `m4h_gaitbandmeasurement` (
  `id` bigint NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `fall_detected` tinyint(1) NOT NULL,
  `patient_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `m4h_measurement`
--

CREATE TABLE `m4h_measurement` (
  `id` bigint NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `uric_acid_level` double NOT NULL,
  `absorbance` double NOT NULL,
  `patient_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `m4h_patient`
--

CREATE TABLE `m4h_patient` (
  `id` bigint NOT NULL,
  `nume` varchar(100) NOT NULL,
  `prenume` varchar(100) NOT NULL,
  `varsta` int DEFAULT NULL,
  `doctor_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  `email` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `m4h_patient`
--

INSERT INTO `m4h_patient` (`id`, `nume`, `prenume`, `varsta`, `doctor_id`, `user_id`, `email`) VALUES
(1, 'Ionescu', 'Pop', 34, 67, 68, 'i.pop@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `m4h_prescription`
--

CREATE TABLE `m4h_prescription` (
  `id` bigint NOT NULL,
  `date_issued` datetime(6) NOT NULL,
  `medication_name` varchar(100) NOT NULL,
  `dosage` varchar(100) NOT NULL,
  `duration` varchar(100) NOT NULL,
  `quantity` int NOT NULL,
  `additional_info` longtext,
  `doctor_id` int NOT NULL,
  `patient_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `m4h_profile`
--

CREATE TABLE `m4h_profile` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `adresa` varchar(255) DEFAULT NULL,
  `cnp` varchar(13) NOT NULL,
  `varsta` int DEFAULT NULL,
  `telefon` varchar(15) DEFAULT NULL,
  `nume` varchar(100) NOT NULL,
  `prenume` varchar(100) NOT NULL,
  `role` enum('doctor','pacient') NOT NULL,
  `email` varchar(254) NOT NULL,
  `id_doctor_id` bigint DEFAULT NULL,
  `last_active` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `doctor_profiles` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `adresa` varchar(255) DEFAULT NULL,
  `cnp` varchar(13) NOT NULL,
  `varsta` int DEFAULT NULL,
  `telefon` varchar(15) DEFAULT NULL,
  `nume` varchar(100) NOT NULL,
  `prenume` varchar(100) NOT NULL,
  `cod_parafa` varchar(6) NOT NULL,
  `email` varchar(254) NOT NULL,
  `last_active` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `pacient_profiles` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `adresa` varchar(255) DEFAULT NULL,
  `cnp` varchar(13) NOT NULL,
  `varsta` int DEFAULT NULL,
  `telefon` varchar(15) DEFAULT NULL,
  `nume` varchar(100) NOT NULL,
  `prenume` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `id_doctor_id` bigint DEFAULT NULL,
  `last_active` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

ALTER TABLE `doctor_profiles`
    ADD PRIMARY KEY (`id`),
    ADD UNIQUE KEY `user_id` (`user_id`),
    ADD UNIQUE KEY `cnp` (`cnp`),
    ADD UNIQUE KEY `email` (`email`),
    ADD UNIQUE KEY `cod_parafa` (`cod_parafa`),
    ADD FOREIGN KEY (`user_id`) REFERENCES `m4h_profile` (`user_id`);

ALTER TABLE `pacient_profiles`
    ADD PRIMARY KEY (`id`),
    ADD UNIQUE KEY `user_id` (`user_id`),
    ADD UNIQUE KEY `cnp` (`cnp`),
    ADD UNIQUE KEY `email` (`email`),
    ADD FOREIGN KEY (`user_id`) REFERENCES `m4h_profile` (`user_id`),
    ADD FOREIGN KEY (`id_doctor_id`) REFERENCES `doctor_profiles` (`id`);


--
-- Dumping data for table `m4h_profile`
--

INSERT INTO `m4h_profile` (`id`, `user_id`, `adresa`, `cnp`, `varsta`, `telefon`, `nume`, `prenume`, `role`, `email`, `id_doctor_id`, `last_active`) VALUES
(127, 67, 'Str. Grigore Mora 42', '5011001450022', 23, '0786044271', 'Constantin', 'Victor', 'doctor', 'vconstantin261@gmail.com', NULL, NULL),
(128, 68, 'str marului', '1234567890786', 34, '0786055162', 'Ionescu', 'Pop', 'pacient', 'i.pop@gmail.com', 127, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `m4h_uricacidmeasurement`
--

CREATE TABLE `m4h_uricacidmeasurement` (
  `id` bigint NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `uric_acid_level` double NOT NULL,
  `absorbance` double NOT NULL,
  `patient_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `m4h_appointment`
--
ALTER TABLE `m4h_appointment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `m4h_appointment_patient_id_53eea92e_fk_m4h_patient_id` (`patient_id`),
  ADD KEY `m4h_appointment_doctor_id_f5a7aec9_fk_auth_user_id` (`doctor_id`);

--
-- Indexes for table `m4h_blackboxmedicalmeasurement`
--
ALTER TABLE `m4h_blackboxmedicalmeasurement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `m4h_blackboxmedicalm_patient_id_eb53e318_fk_m4h_patie` (`patient_id`);

--
-- Indexes for table `m4h_emgmeasurement`
--
ALTER TABLE `m4h_emgmeasurement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `m4h_emgmeasurement_patient_id_96827b2e_fk_m4h_patient_id` (`patient_id`);

--
-- Indexes for table `m4h_gaitbandmeasurement`
--
ALTER TABLE `m4h_gaitbandmeasurement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `m4h_gaitbandmeasurement_patient_id_b80d99f6_fk_m4h_patient_id` (`patient_id`);

--
-- Indexes for table `m4h_measurement`
--
ALTER TABLE `m4h_measurement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `m4h_measurement_patient_id_90b1e9dc_fk_m4h_patient_id` (`patient_id`);

--
-- Indexes for table `m4h_patient`
--
ALTER TABLE `m4h_patient`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD KEY `m4h_patient_doctor_id_3c9b1060_fk_auth_user_id` (`doctor_id`);

--
-- Indexes for table `m4h_prescription`
--
ALTER TABLE `m4h_prescription`
  ADD PRIMARY KEY (`id`),
  ADD KEY `m4h_prescription_doctor_id_378b8a85_fk_auth_user_id` (`doctor_id`),
  ADD KEY `m4h_prescription_patient_id_bc240d33_fk_m4h_patient_id` (`patient_id`);

--
-- Indexes for table `m4h_profile`
--
ALTER TABLE `m4h_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD UNIQUE KEY `cnp` (`cnp`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `m4h_profile_id_doctor_id_571e4019_fk_m4h_profile_id` (`id_doctor_id`);

--
-- Indexes for table `m4h_uricacidmeasurement`
--
ALTER TABLE `m4h_uricacidmeasurement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `m4h_uricacidmeasurement_patient_id_450f5996_fk_m4h_patient_id` (`patient_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `m4h_appointment`
--
ALTER TABLE `m4h_appointment`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `m4h_blackboxmedicalmeasurement`
--
ALTER TABLE `m4h_blackboxmedicalmeasurement`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `m4h_emgmeasurement`
--
ALTER TABLE `m4h_emgmeasurement`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `m4h_gaitbandmeasurement`
--
ALTER TABLE `m4h_gaitbandmeasurement`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `m4h_measurement`
--
ALTER TABLE `m4h_measurement`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `m4h_patient`
--
ALTER TABLE `m4h_patient`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `m4h_prescription`
--
ALTER TABLE `m4h_prescription`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `m4h_profile`
--
ALTER TABLE `m4h_profile`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=129;

--
-- AUTO_INCREMENT for table `m4h_uricacidmeasurement`
--
ALTER TABLE `m4h_uricacidmeasurement`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `m4h_appointment`
--
ALTER TABLE `m4h_appointment`
  ADD CONSTRAINT `m4h_appointment_doctor_id_f5a7aec9_fk_auth_user_id` FOREIGN KEY (`doctor_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `m4h_appointment_patient_id_53eea92e_fk_m4h_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `m4h_patient` (`id`);

--
-- Constraints for table `m4h_blackboxmedicalmeasurement`
--
ALTER TABLE `m4h_blackboxmedicalmeasurement`
  ADD CONSTRAINT `m4h_blackboxmedicalm_patient_id_eb53e318_fk_m4h_patie` FOREIGN KEY (`patient_id`) REFERENCES `m4h_patient` (`id`);

--
-- Constraints for table `m4h_emgmeasurement`
--
ALTER TABLE `m4h_emgmeasurement`
  ADD CONSTRAINT `m4h_emgmeasurement_patient_id_96827b2e_fk_m4h_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `m4h_patient` (`id`);

--
-- Constraints for table `m4h_gaitbandmeasurement`
--
ALTER TABLE `m4h_gaitbandmeasurement`
  ADD CONSTRAINT `m4h_gaitbandmeasurement_patient_id_b80d99f6_fk_m4h_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `m4h_patient` (`id`);

--
-- Constraints for table `m4h_measurement`
--
ALTER TABLE `m4h_measurement`
  ADD CONSTRAINT `m4h_measurement_patient_id_90b1e9dc_fk_m4h_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `m4h_patient` (`id`);

--
-- Constraints for table `m4h_patient`
--
ALTER TABLE `m4h_patient`
  ADD CONSTRAINT `m4h_patient_doctor_id_3c9b1060_fk_auth_user_id` FOREIGN KEY (`doctor_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `m4h_patient_user_id_39e857f4_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `m4h_prescription`
--
ALTER TABLE `m4h_prescription`
  ADD CONSTRAINT `m4h_prescription_doctor_id_378b8a85_fk_auth_user_id` FOREIGN KEY (`doctor_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `m4h_prescription_patient_id_bc240d33_fk_m4h_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `m4h_patient` (`id`);

--
-- Constraints for table `m4h_profile`
--
ALTER TABLE `m4h_profile`
  ADD CONSTRAINT `m4h_profile_id_doctor_id_571e4019_fk_m4h_profile_id` FOREIGN KEY (`id_doctor_id`) REFERENCES `m4h_profile` (`id`),
  ADD CONSTRAINT `m4h_profile_user_id_9602d0aa_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `m4h_uricacidmeasurement`
--
ALTER TABLE `m4h_uricacidmeasurement`
  ADD CONSTRAINT `m4h_uricacidmeasurement_patient_id_450f5996_fk_m4h_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `m4h_patient` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
