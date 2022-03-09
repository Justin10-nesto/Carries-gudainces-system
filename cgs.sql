CREATE DATABASE CGD;
USE CGD;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `auth_group` (`id`, `name`) VALUES
(3, 'Adminr'),
(9, 'studemt');
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(106,1, 1),
(107,1, 2),
(108,1, 3),
(109,1, 4),
(110,1, 5),
(111,1, 6),
(112,1, 7),
(113,1, 8),
(114,1, 9),
(115,1, 10),
(116,1, 11),
(117,1, 12),
(118,1, 13),
(119,1, 14),
(120,1, 15),
(121,1, 16),
(122,1, 17),
(123,1, 18),
(124,1, 19),
(125,1, 20),
(126,1, 21),
(127,1, 22),
(128,1, 23),
(129,1, 24),
(130,1, 25),
(131,1, 26),
(132,1, 27),
(133,1, 28),
(134,1, 29),
(135,1, 30),
(136,1, 31),
(137,1, 32),
(138,1, 33),
(139,1, 34),
(140,1, 35),
(141,1, 36),
(142,1, 37),
(143,1, 38),
(144,1, 39),
(145,1, 40),
(146,1, 41),
(147,1, 42),
(148,1, 43),
(149,1, 44),
(150,1, 45),
(151,1, 46),
(152,1, 47),
(153,1, 48),
(154,1, 49),
(155,1, 50),
(156,1, 51),
(157,1, 52),
(158,1, 53),
(159,1, 54),
(160,1, 55),
(161,1, 56),
(162,1, 57),
(163,1, 58),
(164,1, 59),
(165,1, 60),
(166,1, 61),
(167,1, 62),
(168,1, 63),
(169,1, 64),
(170,1, 65),
(171,1, 66),
(172,1, 67),
(173,1, 68),
(174,1, 69),
(175,1, 70),
(176,1, 71),
(177,1, 72),
(178,1, 73),
(179,1, 74),
(180,1, 75),
(181,1, 76),
(182,1, 77),
(183,1, 78),
(184,1, 79),
(185,1, 80),
(186,1, 81),
(187,1, 82)
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group',1, 'add_group'),
(10, 'Can change group',1, 'change_group'),
(11, 'Can delete group',1, 'delete_group'),
(12, 'Can view group',1, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add admission', 7, 'add_admission'),
(26, 'Can change admission', 7, 'change_admission'),
(27, 'Can delete admission', 7, 'delete_admission'),
(28, 'Can view admission', 7, 'view_admission'),
(29, 'Can add catgory', 8, 'add_catgory'),
(30, 'Can change catgory', 8, 'change_catgory'),
(31, 'Can delete catgory', 8, 'delete_catgory'),
(32, 'Can view catgory', 8, 'view_catgory'),
(33, 'Can add course', 9, 'add_course'),
(34, 'Can change course', 9, 'change_course'),
(35, 'Can delete course', 9, 'delete_course'),
(36, 'Can view course', 9, 'view_course'),
(37, 'Can add field', 10, 'add_field'),
(38, 'Can change field', 10, 'change_field'),
(39, 'Can delete field', 10, 'delete_field'),
(40, 'Can view field', 10, 'view_field'),
(41, 'Can add learning', 11, 'add_learning'),
(42, 'Can change learning', 11, 'change_learning'),
(43, 'Can delete learning', 11, 'delete_learning'),
(44, 'Can view learning', 11, 'view_learning'),
(45, 'Can add level', 12, 'add_level'),
(46, 'Can change level', 12, 'change_level'),
(47, 'Can delete level', 12, 'delete_level'),
(48, 'Can view level', 12, 'view_level'),
(49, 'Can add material', 13, 'add_material'),
(50, 'Can change material', 13, 'change_material'),
(51, 'Can delete material', 13, 'delete_material'),
(52, 'Can view material', 13, 'view_material'),
(53, 'Can add u group', 14, 'add_ugroup'),
(54, 'Can change u group', 14, 'change_ugroup'),
(55, 'Can delete u group', 14, 'delete_ugroup'),
(56, 'Can view u group', 14, 'view_ugroup'),
(57, 'Can add ugroup_learder', 15, 'add_ugroup_learder'),
(58, 'Can change ugroup_learder', 15, 'change_ugroup_learder'),
(59, 'Can delete ugroup_learder', 15, 'delete_ugroup_learder'),
(60, 'Can view ugroup_learder', 15, 'view_ugroup_learder'),
(61, 'Can add univerisity', 16, 'add_univerisity'),
(62, 'Can change univerisity', 16, 'change_univerisity'),
(63, 'Can delete univerisity', 16, 'delete_univerisity'),
(64, 'Can view univerisity', 16, 'view_univerisity'),
(65, 'Can add user group', 17, 'add_usergroup'),
(66, 'Can change user group', 17, 'change_usergroup'),
(67, 'Can delete user group', 17, 'delete_usergroup'),
(68, 'Can view user group', 17, 'view_usergroup'),
(69, 'Can add univ_cours', 18, 'add_univ_cours'),
(70, 'Can change univ_cours', 18, 'change_univ_cours'),
(71, 'Can delete univ_cours', 18, 'delete_univ_cours'),
(72, 'Can view univ_cours', 18, 'view_univ_cours'),
(73, 'Can add ugr_usr', 19, 'add_ugr_usr'),
(74, 'Can change ugr_usr', 19, 'change_ugr_usr'),
(75, 'Can delete ugr_usr', 19, 'delete_ugr_usr'),
(76, 'Can view ugr_usr', 19, 'view_ugr_usr'),
(77, 'Can add technology', 20, 'add_technology'),
(78, 'Can change technology', 20, 'change_technology'),
(79, 'Can delete technology', 20, 'delete_technology'),
(80, 'Can view technology', 20, 'view_technology'),
(81, 'Can add subject', 21, 'add_subject'),
(82, 'Can change subject', 21, 'change_subject'),
(83, 'Can delete subject', 21, 'delete_subject'),
(84, 'Can view subject', 21, 'view_subject'),
(85, 'Can add post_message', 22, 'add_post_message'),
(86, 'Can change post_message', 22, 'change_post_message'),
(87, 'Can delete post_message', 22, 'delete_post_message'),
(88, 'Can view post_message', 22, 'view_post_message'),
(89, 'Can add other_info', 23, 'add_other_info'),
(90, 'Can change other_info', 23, 'change_other_info'),
(91, 'Can delete other_info', 23, 'delete_other_info'),
(92, 'Can view other_info', 23, 'view_other_info'),
(93, 'Can add image', 24, 'add_image'),
(94, 'Can change image', 24, 'change_image'),
(95, 'Can delete image', 24, 'delete_image'),
(96, 'Can view image', 24, 'view_image'),
(97, 'Can add field_technology', 25, 'add_field_technology'),
(98, 'Can change field_technology', 25, 'change_field_technology'),
(99, 'Can delete field_technology', 25, 'delete_field_technology'),
(100, 'Can view field_technology', 25, 'view_field_technology');
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(4, 'pbkdf2_sha256$320000$HBuWZatnGbFms8XSLdiylc$+zVoxbfsI1cuSqzOOjdqgUapEmuplR04zFyIKBT+wHM=', NULL, 0, 'ahmad', 'ahmad', 'abdu bakari', 'ahmad@gmail.com', 0, 1, '2022-01-01 13:42:16.552442'),
(7, 'pbkdf2_sha256$320000$4ssKFzXM83aNuUt36ZfP4M$YtBbRJ55FiW6hSpk77Hop4XomsZQbqV2fLj4sPBXr50=', '2022-01-10 04:07:39.591190', 0, '12345', '12345', 'john', '12345@gmail.com', 0, 1, '2022-01-07 13:21:19.475890'),
(8, 'pbkdf2_sha256$320000$fot7SKuq0ads1AV5xYNKtY$6K31LJ1Fy+KRsynKW9w6N3JjerttDg/nizFYY/DWpp8=', NULL, 0, 'john', 'john', 'silivan', 'john@gmail.com', 0, 1, '2022-01-08 20:45:24.202454'),
(10, 'pbkdf2_sha256$320000$HedTGQMGWVUIJsYbClKX9m$mww7bpHU4uBQHgwW8QLBsyrW+jx8MVbPSps0KnVNQQo=', '2022-01-10 06:52:34.350299', 0, 'justin', 'justin', 'lasway', 'jastin@gmail.com', 0, 1, '2022-01-09 14:31:57.931938'),
(11, 'pbkdf2_sha256$320000$kC5BCT65ZSAZV2tJlOGOPQ$U0CJZmG45XIigURSW6UwQrS6CLYcJJkmjvuw17fShuI=', NULL, 0, ' john', 'john', 'abu', 'john@gmail.com', 0, 1, '2022-01-10 04:06:40.733699');
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(3, 4, 3),
(5, 7, 3),
(8, 10, 3),
(9, 11, 3);
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'Student', 'admission'),
(8, 'Student', 'catgory'),
(9, 'Student', 'course'),
(10, 'Student', 'field'),
(25, 'Student', 'field_technology'),
(24, 'Student', 'image'),
(11, 'Student', 'learning'),
(12, 'Student', 'level'),
(13, 'Student', 'material'),
(23, 'Student', 'other_info'),
(22, 'Student', 'post_message'),
(21, 'Student', 'subject'),
(20, 'Student', 'technology'),
(14, 'Student', 'ugroup'),
(15, 'Student', 'ugroup_learder'),
(19, 'Student', 'ugr_usr'),
(16, 'Student', 'univerisity'),
(18, 'Student', 'univ_cours'),
(17, 'Student', 'usergroup');
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-01-03 07:08:29.540410'),
(2, 'contenttypes', '0002_remove_content_type_name', '2022-01-03 07:08:30.631656'),
(3, 'auth', '0001_initial', '2022-01-03 07:08:44.388317'),
(4, 'auth', '0002_alter_permission_name_max_length', '2022-01-03 07:08:45.412348'),
(5, 'auth', '0003_alter_user_email_max_length', '2022-01-03 07:08:45.677326'),
(6, 'auth', '0004_alter_user_username_opts', '2022-01-03 07:08:45.758696'),
(7, 'auth', '0005_alter_user_last_login_null', '2022-01-03 07:08:46.485479'),
(8, 'auth', '0006_require_contenttypes_0002', '2022-01-03 07:08:46.606662'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2022-01-03 07:08:46.835664'),
(10, 'auth', '0008_alter_user_username_max_length', '2022-01-03 07:08:46.996660'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2022-01-03 07:08:47.190660'),
(12, 'auth', '0010_alter_group_name_max_length', '2022-01-03 07:08:47.385663'),
(13, 'auth', '0011_update_proxy_permissions', '2022-01-03 07:08:47.477655'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2022-01-03 07:08:47.644665'),
(15, 'Student', '0001_initial', '2022-01-03 07:09:15.237972'),
(16, 'admin', '0001_initial', '2022-01-03 07:09:19.736234'),
(17, 'admin', '0002_logentry_remove_auto_add', '2022-01-03 07:09:19.984235'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2022-01-03 07:09:20.256229'),
(19, 'sessions', '0001_initial', '2022-01-03 07:09:22.685233');
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('6vthwmiev4133psc23mtca0c4qd84qxs', '.eJxVjEEOwiAQRe_C2hAGaAGX7j0DGWBGqoYmpV0Z765NutDtf-_9l4i4rTVunZY4FXEWIE6_W8L8oLaDcsd2m2We27pMSe6KPGiX17nQ83K4fwcVe_3WZgR0mYpmTAycDKFltM6jMsHrEBQCacJiGawdnFbk2IyZQwLn8yDeHwSuOGA:1n4zxl:L5yjhvKz_6KSSxGXTFIRHWZzJqTB4kx50a-yDSydjU0', '2022-01-19 06:39:57.854091'),
('uk5ij0j6ehkw1hwv50xee65ihiefp3fb', '.eJxVjEEOwiAQRe_C2hAYoYBL9z0DGZhBqoYmpV0Z765NutDtf-_9l4i4rTVunZc4kbgIrcTpd0yYH9x2Qndst1nmua3LlOSuyIN2Oc7Ez-vh_h1U7PVbg0OdOCgsgzeQjfdYmCyEoD0BofUFHKcCgzXkkjFK6TMqDYo9uezE-wMHszfQ:1n6oXi:wimuAtTzwAmKJviQwDk71wYr5CDyTAo3muhHAXJxH34', '2022-01-24 06:52:34.452343');
CREATE TABLE `student_admission` (
  `admission_id` int(11) NOT NULL,
  `marks` varchar(255) NOT NULL,
  `subject_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `student_admission` (`admission_id`, `marks`, `subject_id`) VALUES
(1, 'DD', 3),
(2, 'CCB', 1);
CREATE TABLE `student_catgory` (
  `catgory_id` int(11) NOT NULL,
  `category_nam` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `student_catgory` (`catgory_id`, `category_nam`) VALUES
(2, 'arts'),
(1, 'science');
CREATE TABLE `student_course` (
  `course_id` int(11) NOT NULL,
  `cours_name` varchar(255) NOT NULL,
  `year` int(11) NOT NULL,
  `admission_id` int(11) NOT NULL,
  `catgory_id` int(11) NOT NULL,
  `field_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `student_course` (`course_id`, `cours_name`, `year`, `admission_id`, `catgory_id`, `field_id`) VALUES
(1, 'medical doctor', 5, 2, 1, 4),
(2, 'medical doctor', 5, 2, 1, 5),
(3, 'law',1, 1, 2, 5);
CREATE TABLE `student_field` (
  `field_id` int(11) NOT NULL,
  `field_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `student_field` (`field_id`, `field_name`) VALUES
(3, 'medical doctor'),
(4, 'lawer'),
(5, 'pharmacy');
CREATE TABLE `student_field_technology` (
  `id` int(11) NOT NULL,
  `Field_id` int(11) NOT NULL,
  `Technology_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `student_image` (
  `id` int(11) NOT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `User_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `student_learning` (
  `id` int(11) NOT NULL,
  `topic` varchar(255) NOT NULL,
  `Material_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `student_level` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `student_level` (`id`, `name`) VALUES
(1, 'o-LEVEL'),
(2, 'A-LEVEL'),
(3, 'OD');
CREATE TABLE `student_material` (
  `id` int(11) NOT NULL,
  `book_tittle` varchar(255) NOT NULL,
  `book_author` varchar(255) NOT NULL,
  `book_edition` varchar(255) NOT NULL,
  `book_year` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `student_other_info` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `bod` varchar(255) NOT NULL,
  `gender` bigint(20) NOT NULL,
  `location` varchar(255) NOT NULL,
  `phon_no` bigint(20) NOT NULL,
  `User_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `student_post_message` (
  `post_id` int(11) NOT NULL,
  `tittle` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `category` varchar(255) NOT NULL,
  `time_post` datetime(6) NOT NULL,
  `User_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `student_subject` (
  `sub_id` int(11) NOT NULL,
  `subject_name` varchar(255) NOT NULL,
  `class_lvl_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `student_subject` (`sub_id`, `subject_name`, `class_lvl_id`) VALUES
(1, 'PCB', 2),
(2, 'PCM', 2),
(3, 'HKL', 2);
CREATE TABLE `student_technology` (
  `tchnology_id` int(11) NOT NULL,
  `tchnology_name` varchar(255) NOT NULL,
  `learning_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `student_ugroup` (
  `group_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `leader` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `student_ugroup_learder` (
  `id` int(11) NOT NULL,
  `position` varchar(255) NOT NULL,
  `priority` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `student_ugr_usr` (
  `id` int(11) NOT NULL,
  `User_id` int(11) NOT NULL,
  `leader_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `student_univerisity` (
  `university_id` int(11) NOT NULL,
  `university_name` varchar(255) NOT NULL,
  `total_coursers` bigint(20) NOT NULL,
  `no_lectures` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `student_univ_cours` (
  `univ_course_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `university_id` int(11) NOT NULL,
  `uni_cours_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `student_usergroup` (
  `us_group_id` int(11) NOT NULL,
  `User_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

LTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

LTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

LTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

LTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

LTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

LTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

LTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

LTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

LTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

LTER TABLE `student_admission`
  ADD PRIMARY KEY (`admission_id`),
  ADD KEY `Student_admission_subject_id_6be0665c_fk_Student_subject_sub_id` (`subject_id`);

LTER TABLE `student_catgory`
  ADD PRIMARY KEY (`catgory_id`),
  ADD UNIQUE KEY `category_nam` (`category_nam`);

LTER TABLE `student_course`
  ADD PRIMARY KEY (`course_id`),
  ADD KEY `Student_course_field_id_5222400d_fk_Student_field_field_id` (`field_id`),
  ADD KEY `Student_course_admission_id_3e5e6fec_fk_Student_a` (`admission_id`),
  ADD KEY `Student_course_catgory_id_a66caed1_fk_Student_catgory_catgory_id` (`catgory_id`);

LTER TABLE `student_field`
  ADD PRIMARY KEY (`field_id`);

LTER TABLE `student_field_technology`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Student_field_techno_Field_id_6c4cc947_fk_Student_f` (`Field_id`),
  ADD KEY `Student_field_techno_Technology_id_6a02b380_fk_Student_t` (`Technology_id`);

LTER TABLE `student_image`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `User_id` (`User_id`);

LTER TABLE `student_learning`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Student_learning_Material_id_ec080b70_fk_Student_material_id` (`Material_id`);

LTER TABLE `student_level`
  ADD PRIMARY KEY (`id`);

LTER TABLE `student_material`
  ADD PRIMARY KEY (`id`);

LTER TABLE `student_other_info`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `User_id` (`User_id`);

LTER TABLE `student_post_message`
  ADD PRIMARY KEY (`post_id`),
  ADD KEY `Student_post_message_User_id_88e4a366_fk_auth_user_id` (`User_id`);

LTER TABLE `student_subject`
  ADD PRIMARY KEY (`sub_id`),
  ADD KEY `Student_subject_class_lvl_id_754045ad_fk_Student_level_id` (`class_lvl_id`);

LTER TABLE `student_technology`
  ADD PRIMARY KEY (`tchnology_id`),
  ADD KEY `Student_technology_learning_id_c942bff3_fk_Student_learning_id` (`learning_id`);

LTER TABLE `student_ugroup`
  ADD PRIMARY KEY (`group_id`);

LTER TABLE `student_ugroup_learder`
  ADD PRIMARY KEY (`id`);

LTER TABLE `student_ugr_usr`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Student_ugr_usr_User_id_4817e683_fk_auth_user_id` (`User_id`),
  ADD KEY `Student_ugr_usr_leader_id_bab1fe44_fk_Student_ugroup_learder_id` (`leader_id`);

LTER TABLE `student_univerisity`
  ADD PRIMARY KEY (`university_id`);

LTER TABLE `student_univ_cours`
  ADD PRIMARY KEY (`univ_course_id`),
  ADD KEY `Student_univ_cours_uni_cours_id_3cb95c71_fk_Student_c` (`uni_cours_id`);

LTER TABLE `student_usergroup`
  ADD PRIMARY KEY (`us_group_id`),
  ADD KEY `Student_usergroup_User_id_10e75fa4_fk_auth_user_id` (`User_id`),
  ADD KEY `Student_usergroup_group_id_25c2a40a_fk_Student_ugroup_group_id` (`group_id`);

LTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

LTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=212;

LTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

LTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

LTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

LTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

LTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

LTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

LTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

LTER TABLE `student_admission`
  MODIFY `admission_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

LTER TABLE `student_catgory`
  MODIFY `catgory_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

LTER TABLE `student_course`
  MODIFY `course_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

LTER TABLE `student_field`
  MODIFY `field_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

LTER TABLE `student_field_technology`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

LTER TABLE `student_image`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

LTER TABLE `student_learning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

LTER TABLE `student_level`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

LTER TABLE `student_material`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

LTER TABLE `student_other_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

LTER TABLE `student_post_message`
  MODIFY `post_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

LTER TABLE `student_subject`
  MODIFY `sub_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

LTER TABLE `student_technology`
  MODIFY `tchnology_id` int(11) NOT NULL AUTO_INCREMENT;

LTER TABLE `student_ugroup`
  MODIFY `group_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

LTER TABLE `student_ugroup_learder`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

LTER TABLE `student_ugr_usr`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

LTER TABLE `student_univerisity`
  MODIFY `university_id` int(11) NOT NULL AUTO_INCREMENT;

LTER TABLE `student_univ_cours`
  MODIFY `univ_course_id` int(11) NOT NULL AUTO_INCREMENT;

LTER TABLE `student_usergroup`
  MODIFY `us_group_id` int(11) NOT NULL AUTO_INCREMENT;

LTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

LTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

LTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

LTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

LTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

LTER TABLE `student_admission`
  ADD CONSTRAINT `Student_admission_subject_id_6be0665c_fk_Student_subject_sub_id` FOREIGN KEY (`subject_id`) REFERENCES `student_subject` (`sub_id`);

LTER TABLE `student_course`
  ADD CONSTRAINT `Student_course_admission_id_3e5e6fec_fk_Student_a` FOREIGN KEY (`admission_id`) REFERENCES `student_admission` (`admission_id`),
  ADD CONSTRAINT `Student_course_catgory_id_a66caed1_fk_Student_catgory_catgory_id` FOREIGN KEY (`catgory_id`) REFERENCES `student_catgory` (`catgory_id`),
  ADD CONSTRAINT `Student_course_field_id_5222400d_fk_Student_field_field_id` FOREIGN KEY (`field_id`) REFERENCES `student_field` (`field_id`);

LTER TABLE `student_field_technology`
  ADD CONSTRAINT `Student_field_techno_Field_id_6c4cc947_fk_Student_f` FOREIGN KEY (`Field_id`) REFERENCES `student_field` (`field_id`),
  ADD CONSTRAINT `Student_field_techno_Technology_id_6a02b380_fk_Student_t` FOREIGN KEY (`Technology_id`) REFERENCES `student_technology` (`tchnology_id`);

LTER TABLE `student_image`
  ADD CONSTRAINT `Student_image_User_id_9824d4b8_fk_auth_user_id` FOREIGN KEY (`User_id`) REFERENCES `auth_user` (`id`);

LTER TABLE `student_learning`
  ADD CONSTRAINT `Student_learning_Material_id_ec080b70_fk_Student_material_id` FOREIGN KEY (`Material_id`) REFERENCES `student_material` (`id`);

LTER TABLE `student_other_info`
  ADD CONSTRAINT `Student_other_info_User_id_aa07d6b4_fk_auth_user_id` FOREIGN KEY (`User_id`) REFERENCES `auth_user` (`id`);

LTER TABLE `student_post_message`
  ADD CONSTRAINT `Student_post_message_User_id_88e4a366_fk_auth_user_id` FOREIGN KEY (`User_id`) REFERENCES `auth_user` (`id`);

LTER TABLE `student_subject`
  ADD CONSTRAINT `Student_subject_class_lvl_id_754045ad_fk_Student_level_id` FOREIGN KEY (`class_lvl_id`) REFERENCES `student_level` (`id`);

LTER TABLE `student_technology`
  ADD CONSTRAINT `Student_technology_learning_id_c942bff3_fk_Student_learning_id` FOREIGN KEY (`learning_id`) REFERENCES `student_learning` (`id`);

LTER TABLE `student_ugr_usr`
  ADD CONSTRAINT `Student_ugr_usr_User_id_4817e683_fk_auth_user_id` FOREIGN KEY (`User_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `Student_ugr_usr_leader_id_bab1fe44_fk_Student_ugroup_learder_id` FOREIGN KEY (`leader_id`) REFERENCES `student_ugroup_learder` (`id`);

LTER TABLE `student_univ_cours`
  ADD CONSTRAINT `Student_univ_cours_uni_cours_id_3cb95c71_fk_Student_c` FOREIGN KEY (`uni_cours_id`) REFERENCES `student_course` (`course_id`);

LTER TABLE `student_usergroup`
  ADD CONSTRAINT `Student_usergroup_User_id_10e75fa4_fk_auth_user_id` FOREIGN KEY (`User_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `Student_usergroup_group_id_25c2a40a_fk_Student_ugroup_group_id` FOREIGN KEY (`group_id`) REFERENCES `student_ugroup` (`group_id`);
COMMIT;

