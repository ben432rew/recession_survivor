--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: bears; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO bears;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: bears
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO bears;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bears
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: bears; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO bears;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: bears
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO bears;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bears
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: bears; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO bears;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: bears
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO bears;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bears
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: bears; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO bears;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: bears; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO bears;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: bears
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO bears;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bears
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: bears
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO bears;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bears
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: bears; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO bears;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: bears
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO bears;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bears
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: bears; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO bears;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: bears
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO bears;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bears
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: bears; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO bears;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: bears
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO bears;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bears
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: bears; Tablespace: 
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO bears;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: bears
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO bears;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bears
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: bears; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO bears;

--
-- Name: game_stock; Type: TABLE; Schema: public; Owner: bears; Tablespace: 
--

CREATE TABLE game_stock (
    id integer NOT NULL,
    price integer NOT NULL,
    date date NOT NULL,
    ticker character varying(50) NOT NULL
);


ALTER TABLE public.game_stock OWNER TO bears;

--
-- Name: game_stock_id_seq; Type: SEQUENCE; Schema: public; Owner: bears
--

CREATE SEQUENCE game_stock_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_stock_id_seq OWNER TO bears;

--
-- Name: game_stock_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bears
--

ALTER SEQUENCE game_stock_id_seq OWNED BY game_stock.id;


--
-- Name: portfolio_portfolio; Type: TABLE; Schema: public; Owner: bears; Tablespace: 
--

CREATE TABLE portfolio_portfolio (
    id integer NOT NULL,
    final_score double precision NOT NULL,
    date_played timestamp with time zone NOT NULL,
    balance double precision NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.portfolio_portfolio OWNER TO bears;

--
-- Name: portfolio_portfolio_id_seq; Type: SEQUENCE; Schema: public; Owner: bears
--

CREATE SEQUENCE portfolio_portfolio_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.portfolio_portfolio_id_seq OWNER TO bears;

--
-- Name: portfolio_portfolio_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bears
--

ALTER SEQUENCE portfolio_portfolio_id_seq OWNED BY portfolio_portfolio.id;


--
-- Name: portfolio_snippet; Type: TABLE; Schema: public; Owner: bears; Tablespace: 
--

CREATE TABLE portfolio_snippet (
    id integer NOT NULL,
    snippet text NOT NULL,
    stock_id integer NOT NULL
);


ALTER TABLE public.portfolio_snippet OWNER TO bears;

--
-- Name: portfolio_snippet_id_seq; Type: SEQUENCE; Schema: public; Owner: bears
--

CREATE SEQUENCE portfolio_snippet_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.portfolio_snippet_id_seq OWNER TO bears;

--
-- Name: portfolio_snippet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bears
--

ALTER SEQUENCE portfolio_snippet_id_seq OWNED BY portfolio_snippet.id;


--
-- Name: portfolio_stock; Type: TABLE; Schema: public; Owner: bears; Tablespace: 
--

CREATE TABLE portfolio_stock (
    id integer NOT NULL,
    symbol character varying(50) NOT NULL,
    price double precision NOT NULL,
    date date NOT NULL,
    name character varying(50) NOT NULL,
    volume double precision NOT NULL
);


ALTER TABLE public.portfolio_stock OWNER TO bears;

--
-- Name: portfolio_stock_id_seq; Type: SEQUENCE; Schema: public; Owner: bears
--

CREATE SEQUENCE portfolio_stock_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.portfolio_stock_id_seq OWNER TO bears;

--
-- Name: portfolio_stock_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bears
--

ALTER SEQUENCE portfolio_stock_id_seq OWNED BY portfolio_stock.id;


--
-- Name: portfolio_stock_owned; Type: TABLE; Schema: public; Owner: bears; Tablespace: 
--

CREATE TABLE portfolio_stock_owned (
    id integer NOT NULL,
    symbol character varying(50) NOT NULL,
    amount integer NOT NULL,
    price_bought double precision NOT NULL,
    date_bought date NOT NULL,
    name character varying(50) NOT NULL,
    portfolio_id integer NOT NULL
);


ALTER TABLE public.portfolio_stock_owned OWNER TO bears;

--
-- Name: portfolio_stock_owned_id_seq; Type: SEQUENCE; Schema: public; Owner: bears
--

CREATE SEQUENCE portfolio_stock_owned_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.portfolio_stock_owned_id_seq OWNER TO bears;

--
-- Name: portfolio_stock_owned_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bears
--

ALTER SEQUENCE portfolio_stock_owned_id_seq OWNED BY portfolio_stock_owned.id;


--
-- Name: portfolio_transcation; Type: TABLE; Schema: public; Owner: bears; Tablespace: 
--

CREATE TABLE portfolio_transcation (
    id integer NOT NULL,
    symbol character varying(50) NOT NULL,
    number_of_shares integer NOT NULL,
    date_created timestamp with time zone NOT NULL,
    account_change double precision NOT NULL,
    portfolio_id integer NOT NULL
);


ALTER TABLE public.portfolio_transcation OWNER TO bears;

--
-- Name: portfolio_transcation_id_seq; Type: SEQUENCE; Schema: public; Owner: bears
--

CREATE SEQUENCE portfolio_transcation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.portfolio_transcation_id_seq OWNER TO bears;

--
-- Name: portfolio_transcation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bears
--

ALTER SEQUENCE portfolio_transcation_id_seq OWNED BY portfolio_transcation.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: bears
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: bears
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: bears
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: bears
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: bears
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: bears
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: bears
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: bears
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: bears
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: bears
--

ALTER TABLE ONLY game_stock ALTER COLUMN id SET DEFAULT nextval('game_stock_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: bears
--

ALTER TABLE ONLY portfolio_portfolio ALTER COLUMN id SET DEFAULT nextval('portfolio_portfolio_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: bears
--

ALTER TABLE ONLY portfolio_snippet ALTER COLUMN id SET DEFAULT nextval('portfolio_snippet_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: bears
--

ALTER TABLE ONLY portfolio_stock ALTER COLUMN id SET DEFAULT nextval('portfolio_stock_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: bears
--

ALTER TABLE ONLY portfolio_stock_owned ALTER COLUMN id SET DEFAULT nextval('portfolio_stock_owned_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: bears
--

ALTER TABLE ONLY portfolio_transcation ALTER COLUMN id SET DEFAULT nextval('portfolio_transcation_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: bears
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bears
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: bears
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bears
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: bears
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add stock	7	add_stock
20	Can change stock	7	change_stock
21	Can delete stock	7	delete_stock
22	Can add portfolio	8	add_portfolio
23	Can change portfolio	8	change_portfolio
24	Can delete portfolio	8	delete_portfolio
25	Can add transcation	9	add_transcation
26	Can change transcation	9	change_transcation
27	Can delete transcation	9	delete_transcation
28	Can add stock_owned	10	add_stock_owned
29	Can change stock_owned	10	change_stock_owned
30	Can delete stock_owned	10	delete_stock_owned
31	Can add stock	11	add_stock
32	Can change stock	11	change_stock
33	Can delete stock	11	delete_stock
34	Can add snippet	12	add_snippet
35	Can change snippet	12	change_snippet
36	Can delete snippet	12	delete_snippet
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bears
--

SELECT pg_catalog.setval('auth_permission_id_seq', 36, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: bears
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	bcrypt_sha256$$2a$12$C9/wrFliXISlJ0szTG36H.R7QEG9xgo9NIAhz1EPezKe/r3rsN3p.	2014-12-14 18:33:43.528839-05	f	b				f	t	2014-12-14 18:33:43.528839-05
2	bcrypt_sha256$$2a$12$tDpsyNW6d5G6o8kbBUrQpOjhf0rHMus69IK321tHr30CgG9xZSvTC	2014-12-14 18:35:18.456793-05	f	benny				f	t	2014-12-14 18:35:18.456793-05
3	bcrypt_sha256$$2a$12$nszrWq8EGvcHQMZm9tV/UeTewwK5N52yYaQODtwAVPDDglkJIkHUi	2014-12-14 18:39:59.43619-05	f	benny3				f	t	2014-12-14 18:39:59.43619-05
4	bcrypt_sha256$$2a$12$Bao7bQHbz4LwJ66BWzQ6GuEUpMqBnUDF9VPdk5Eci.RuFYStpRIwS	2014-12-14 18:41:59.067866-05	f	benny4				f	t	2014-12-14 18:41:59.067866-05
5	bcrypt_sha256$$2a$12$rOsVrzBoTPsKLzxdysxFRuKguBwl.2dgRQfJ./6kJ2lm44JbkBegi	2014-12-14 18:42:25.68804-05	f	benny5				f	t	2014-12-14 18:42:25.68804-05
6	bcrypt_sha256$$2a$12$LAJZE9QutF7KDrzD/4Bq5ujdRh9zM3fdSWBNYIeAlO4kcjXEOXPwG	2014-12-14 18:43:32.452265-05	f	benny6				f	t	2014-12-14 18:43:32.452265-05
7	bcrypt_sha256$$2a$12$zbHhLKmtXOTiuAkeJYDN5ezEPKsva0Q2xvcy9oL7Lw3TtV0IgcSLG	2014-12-14 18:44:06.190474-05	f	benny7				f	t	2014-12-14 18:44:06.190474-05
8	bcrypt_sha256$$2a$12$ndTwCaQ/KJB.kWAAvsrEM.OY7hGbPAmIs4UWAhxqsXucuS85Yhyo6	2014-12-14 18:45:55.29183-05	f	benny11				f	t	2014-12-14 18:45:55.29183-05
9	bcrypt_sha256$$2a$12$LMgc84nX5sySJ6hAew1RL.jmZttuIuZ8xZ2ACrKzh7.QpQ26Opj5O	2014-12-14 18:48:10.650043-05	f	benny12				f	t	2014-12-14 18:48:10.650043-05
10	bcrypt_sha256$$2a$12$zefJy9hXEPESoA6GRGuwZePmY.mMxL28gumWvACxuWeNzHwUWCyzi	2014-12-14 18:55:05.216646-05	f	benny13				f	t	2014-12-14 18:55:05.216646-05
11	bcrypt_sha256$$2a$12$X1OgItISzLge0aVQ/6HBRunL2223Ch6.VR8HxXlEZlZ7NJke78NwK	2014-12-14 18:55:23.301597-05	f	benny14				f	t	2014-12-14 18:55:23.301597-05
12	bcrypt_sha256$$2a$12$P7MrB0w/4i5UgeJWK/ZO..hfJFvCKDjfSOyj3XORnqK93ity6.Lvu	2014-12-14 20:41:06.047645-05	f	benny15				f	t	2014-12-14 20:41:06.047645-05
13	bcrypt_sha256$$2a$12$a2aI36zX/w7Y28Az2i5x/ez4RKcA3Vyxbi74DeiI9U3ZT1htQXqGa	2014-12-14 21:14:09.023226-05	f	benny16				f	t	2014-12-14 21:13:58.579556-05
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: bears
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bears
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bears
--

SELECT pg_catalog.setval('auth_user_id_seq', 13, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: bears
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bears
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: bears
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bears
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: bears
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	log entry	admin	logentry
2	permission	auth	permission
3	group	auth	group
4	user	auth	user
5	content type	contenttypes	contenttype
6	session	sessions	session
7	stock	game	stock
8	portfolio	portfolio	portfolio
9	transcation	portfolio	transcation
10	stock_owned	portfolio	stock_owned
11	stock	portfolio	stock
12	snippet	portfolio	snippet
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bears
--

SELECT pg_catalog.setval('django_content_type_id_seq', 12, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: bears
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2014-12-14 12:19:09.627239-05
2	auth	0001_initial	2014-12-14 12:19:10.416438-05
3	admin	0001_initial	2014-12-14 12:19:10.616414-05
4	portfolio	0001_initial	2014-12-14 12:19:11.104839-05
5	sessions	0001_initial	2014-12-14 12:19:11.294829-05
6	portfolio	0002_auto_20141215_0147	2014-12-14 20:47:09.758668-05
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bears
--

SELECT pg_catalog.setval('django_migrations_id_seq', 6, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: bears
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
w5rvqynxl2ry93xj7dah7a95d500oaeb	OTNmMGYyMjFjOGY2YzZmOWZiNDE1OGMxMDBiNDIxMWY2N2NmN2NmMTp7Il9hdXRoX3VzZXJfaWQiOjEzLCJfYXV0aF91c2VyX2hhc2giOiJmZmZjYzM1ZDAzNDAyZTNkOGQzM2JhMDAxZDZkNDEyMTUyZWY5YjI5IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==	2014-12-28 21:14:09.034513-05
\.


--
-- Data for Name: game_stock; Type: TABLE DATA; Schema: public; Owner: bears
--

COPY game_stock (id, price, date, ticker) FROM stdin;
1	421	2009-06-30	GOOGL
2	417	2009-05-31	GOOGL
3	395	2009-04-30	GOOGL
4	348	2009-03-31	GOOGL
5	337	2009-02-28	GOOGL
6	338	2009-01-31	GOOGL
7	307	2008-12-31	GOOGL
8	292	2008-11-30	GOOGL
9	359	2008-10-31	GOOGL
10	400	2008-09-30	GOOGL
11	463	2008-08-31	GOOGL
12	473	2008-07-31	GOOGL
13	526	2008-06-30	GOOGL
14	23	2009-06-30	MSFT
15	20	2009-05-31	MSFT
16	20	2009-04-30	MSFT
17	18	2009-03-31	MSFT
18	16	2009-02-28	MSFT
19	17	2009-01-31	MSFT
20	19	2008-12-31	MSFT
21	20	2008-11-30	MSFT
22	22	2008-10-31	MSFT
23	26	2008-09-30	MSFT
24	27	2008-08-31	MSFT
25	25	2008-07-31	MSFT
26	27	2008-06-30	MSFT
27	15	2009-06-30	YHOO
28	15	2009-05-31	YHOO
29	14	2009-04-30	YHOO
30	12	2009-03-31	YHOO
31	13	2009-02-28	YHOO
32	11	2009-01-31	YHOO
33	12	2008-12-31	YHOO
34	11	2008-11-30	YHOO
35	12	2008-10-31	YHOO
36	17	2008-09-30	YHOO
37	19	2008-08-31	YHOO
38	19	2008-07-31	YHOO
39	20	2008-06-30	YHOO
40	21	2009-06-30	ORCL
41	19	2009-05-31	ORCL
42	19	2009-04-30	ORCL
43	18	2009-03-31	ORCL
44	15	2009-02-28	ORCL
45	16	2009-01-31	ORCL
46	17	2008-12-31	ORCL
47	16	2008-11-30	ORCL
48	18	2008-10-31	ORCL
49	20	2008-09-30	ORCL
50	21	2008-08-31	ORCL
51	21	2008-07-31	ORCL
52	21	2008-06-30	ORCL
53	104	2009-06-30	IBM
54	106	2009-05-31	IBM
55	103	2009-04-30	IBM
56	96	2009-03-31	IBM
57	92	2009-02-28	IBM
58	91	2009-01-31	IBM
59	84	2008-12-31	IBM
60	81	2008-11-30	IBM
61	92	2008-10-31	IBM
62	116	2008-09-30	IBM
63	121	2008-08-31	IBM
64	127	2008-07-31	IBM
65	118	2008-06-30	IBM
66	142	2009-06-30	AAPL
67	135	2009-05-31	AAPL
68	125	2009-04-30	AAPL
69	105	2009-03-31	AAPL
70	89	2009-02-28	AAPL
71	90	2009-01-31	AAPL
72	85	2008-12-31	AAPL
73	92	2008-11-30	AAPL
74	107	2008-10-31	AAPL
75	113	2008-09-30	AAPL
76	169	2008-08-31	AAPL
77	158	2008-07-31	AAPL
78	167	2008-06-30	AAPL
79	33	2009-06-30	BBY
80	35	2009-05-31	BBY
81	38	2009-04-30	BBY
82	37	2009-03-31	BBY
83	28	2009-02-28	BBY
84	28	2009-01-31	BBY
85	28	2008-12-31	BBY
86	20	2008-11-30	BBY
87	26	2008-10-31	BBY
88	37	2008-09-30	BBY
89	44	2008-08-31	BBY
90	39	2008-07-31	BBY
91	39	2008-06-30	BBY
92	38	2009-06-30	HPQ
93	34	2009-05-31	HPQ
94	35	2009-04-30	HPQ
95	32	2009-03-31	HPQ
96	29	2009-02-28	HPQ
97	34	2009-01-31	HPQ
98	36	2008-12-31	HPQ
99	35	2008-11-30	HPQ
100	38	2008-10-31	HPQ
101	46	2008-09-30	HPQ
102	46	2008-08-31	HPQ
103	44	2008-07-31	HPQ
104	44	2008-06-30	HPQ
105	83	2009-06-30	AMZN
106	77	2009-05-31	AMZN
107	80	2009-04-30	AMZN
108	73	2009-03-31	AMZN
109	64	2009-02-28	AMZN
110	58	2009-01-31	AMZN
111	51	2008-12-31	AMZN
112	42	2008-11-30	AMZN
113	57	2008-10-31	AMZN
114	72	2008-09-30	AMZN
115	80	2008-08-31	AMZN
116	76	2008-07-31	AMZN
117	73	2008-06-30	AMZN
118	11	2009-06-30	GE
119	13	2009-05-31	GE
120	12	2009-04-30	GE
121	10	2009-03-31	GE
122	8	2009-02-28	GE
123	12	2009-01-31	GE
124	16	2008-12-31	GE
125	17	2008-11-30	GE
126	19	2008-10-31	GE
127	25	2008-09-30	GE
128	28	2008-08-31	GE
129	28	2008-07-31	GE
130	26	2008-06-30	GE
131	69	2009-06-30	XOM
132	69	2009-05-31	XOM
133	66	2009-04-30	XOM
134	68	2009-03-31	XOM
135	67	2009-02-28	XOM
136	76	2009-01-31	XOM
137	79	2008-12-31	XOM
138	80	2008-11-30	XOM
139	74	2008-10-31	XOM
140	77	2008-09-30	XOM
141	80	2008-08-31	XOM
142	80	2008-07-31	XOM
143	88	2008-06-30	XOM
144	66	2009-06-30	CVX
145	66	2009-05-31	CVX
146	66	2009-04-30	CVX
147	67	2009-03-31	CVX
148	60	2009-02-28	CVX
149	70	2009-01-31	CVX
150	73	2008-12-31	CVX
151	79	2008-11-30	CVX
152	74	2008-10-31	CVX
153	82	2008-09-30	CVX
154	86	2008-08-31	CVX
155	84	2008-07-31	CVX
156	99	2008-06-30	CVX
157	2	2009-06-30	C
158	3	2009-05-31	C
159	3	2009-04-30	C
160	2	2009-03-31	C
161	1	2009-02-28	C
162	3	2009-01-31	C
163	6	2008-12-31	C
164	8	2008-11-30	C
165	13	2008-10-31	C
166	20	2008-09-30	C
167	18	2008-08-31	C
168	18	2008-07-31	C
169	16	2008-06-30	C
170	37	2009-06-30	ED
171	35	2009-05-31	ED
172	37	2009-04-30	ED
173	39	2009-03-31	ED
174	36	2009-02-28	ED
175	40	2009-01-31	ED
176	38	2008-12-31	ED
177	40	2008-11-30	ED
178	43	2008-10-31	ED
179	42	2008-09-30	ED
180	40	2008-08-31	ED
181	39	2008-07-31	ED
182	39	2008-06-30	ED
183	70	2009-06-30	CL
184	65	2009-05-31	CL
185	59	2009-04-30	CL
186	58	2009-03-31	CL
187	60	2009-02-28	CL
188	65	2009-01-31	CL
189	68	2008-12-31	CL
190	65	2008-11-30	CL
191	62	2008-10-31	CL
192	75	2008-09-30	CL
193	76	2008-08-31	CL
194	74	2008-07-31	CL
195	69	2008-06-30	CL
196	11	2009-06-30	WSM
197	12	2009-05-31	WSM
198	14	2009-04-30	WSM
199	10	2009-03-31	WSM
200	8	2009-02-28	WSM
201	7	2009-01-31	WSM
202	7	2008-12-31	WSM
203	7	2008-11-30	WSM
204	8	2008-10-31	WSM
205	16	2008-09-30	WSM
206	17	2008-08-31	WSM
207	17	2008-07-31	WSM
208	19	2008-06-30	WSM
209	51	2009-06-30	PG
210	51	2009-05-31	PG
211	49	2009-04-30	PG
212	47	2009-03-31	PG
213	48	2009-02-28	PG
214	54	2009-01-31	PG
215	61	2008-12-31	PG
216	64	2008-11-30	PG
217	64	2008-10-31	PG
218	69	2008-09-30	PG
219	69	2008-08-31	PG
220	65	2008-07-31	PG
221	60	2008-06-30	PG
222	46	2009-06-30	K
223	43	2009-05-31	K
224	42	2009-04-30	K
225	36	2009-03-31	K
226	38	2009-02-28	K
227	43	2009-01-31	K
228	43	2008-12-31	K
229	43	2008-11-30	K
230	50	2008-10-31	K
231	56	2008-09-30	K
232	54	2008-08-31	K
233	53	2008-07-31	K
234	48	2008-06-30	K
235	36	2009-06-30	HSY
236	35	2009-05-31	HSY
237	36	2009-04-30	HSY
238	34	2009-03-31	HSY
239	33	2009-02-28	HSY
240	37	2009-01-31	HSY
241	34	2008-12-31	HSY
242	36	2008-11-30	HSY
243	37	2008-10-31	HSY
244	39	2008-09-30	HSY
245	36	2008-08-31	HSY
246	36	2008-07-31	HSY
247	32	2008-06-30	HSY
248	23	2009-06-30	DIS
249	24	2009-05-31	DIS
250	21	2009-04-30	DIS
251	18	2009-03-31	DIS
252	16	2009-02-28	DIS
253	20	2009-01-31	DIS
254	22	2008-12-31	DIS
255	22	2008-11-30	DIS
256	25	2008-10-31	DIS
257	30	2008-09-30	DIS
258	32	2008-08-31	DIS
259	30	2008-07-31	DIS
260	31	2008-06-30	DIS
261	26	2009-06-30	COH
262	26	2009-05-31	COH
263	24	2009-04-30	COH
264	16	2009-03-31	COH
265	13	2009-02-28	COH
266	14	2009-01-31	COH
267	20	2008-12-31	COH
268	17	2008-11-30	COH
269	20	2008-10-31	COH
270	25	2008-09-30	COH
271	28	2008-08-31	COH
272	25	2008-07-31	COH
273	28	2008-06-30	COH
274	24	2009-06-30	ALL
275	25	2009-05-31	ALL
276	23	2009-04-30	ALL
277	19	2009-03-31	ALL
278	16	2009-02-28	ALL
279	21	2009-01-31	ALL
280	32	2008-12-31	ALL
281	25	2008-11-30	ALL
282	26	2008-10-31	ALL
283	46	2008-09-30	ALL
284	45	2008-08-31	ALL
285	46	2008-07-31	ALL
286	45	2008-06-30	ALL
287	56	2009-06-30	GIS
288	51	2009-05-31	GIS
289	50	2009-04-30	GIS
290	49	2009-03-31	GIS
291	52	2009-02-28	GIS
292	59	2009-01-31	GIS
293	60	2008-12-31	GIS
294	63	2008-11-30	GIS
295	67	2008-10-31	GIS
296	68	2008-09-30	GIS
297	66	2008-08-31	GIS
298	64	2008-07-31	GIS
299	60	2008-06-30	GIS
300	13	2009-06-30	KWR
301	13	2009-05-31	KWR
302	11	2009-04-30	KWR
303	7	2009-03-31	KWR
304	5	2009-02-28	KWR
305	11	2009-01-31	KWR
306	16	2008-12-31	KWR
307	12	2008-11-30	KWR
308	19	2008-10-31	KWR
309	28	2008-09-30	KWR
310	29	2008-08-31	KWR
311	29	2008-07-31	KWR
312	26	2008-06-30	KWR
313	19	2009-06-30	CAG
314	18	2009-05-31	CAG
315	17	2009-04-30	CAG
316	16	2009-03-31	CAG
317	15	2009-02-28	CAG
318	17	2009-01-31	CAG
319	16	2008-12-31	CAG
320	14	2008-11-30	CAG
321	17	2008-10-31	CAG
322	19	2008-09-30	CAG
323	21	2008-08-31	CAG
324	21	2008-07-31	CAG
325	19	2008-06-30	CAG
326	47	2009-06-30	KO
327	49	2009-05-31	KO
328	43	2009-04-30	KO
329	43	2009-03-31	KO
330	40	2009-02-28	KO
331	42	2009-01-31	KO
332	45	2008-12-31	KO
333	46	2008-11-30	KO
334	44	2008-10-31	KO
335	52	2008-09-30	KO
336	52	2008-08-31	KO
337	51	2008-07-31	KO
338	51	2008-06-30	KO
339	54	2009-06-30	PEP
340	52	2009-05-31	PEP
341	49	2009-04-30	PEP
342	51	2009-03-31	PEP
343	48	2009-02-28	PEP
344	50	2009-01-31	PEP
345	54	2008-12-31	PEP
346	56	2008-11-30	PEP
347	57	2008-10-31	PEP
348	71	2008-09-30	PEP
349	68	2008-08-31	PEP
350	66	2008-07-31	PEP
351	63	2008-06-30	PEP
352	11	2009-06-30	M
353	11	2009-05-31	M
354	13	2009-04-30	M
355	8	2009-03-31	M
356	7	2009-02-28	M
357	8	2009-01-31	M
358	10	2008-12-31	M
359	7	2008-11-30	M
360	12	2008-10-31	M
361	17	2008-09-30	M
362	20	2008-08-31	M
363	18	2008-07-31	M
364	19	2008-06-30	M
365	42	2009-06-30	WHR
366	42	2009-05-31	WHR
367	45	2009-04-30	WHR
368	29	2009-03-31	WHR
369	22	2009-02-28	WHR
370	33	2009-01-31	WHR
371	41	2008-12-31	WHR
372	39	2008-11-30	WHR
373	46	2008-10-31	WHR
374	79	2008-09-30	WHR
375	81	2008-08-31	WHR
376	75	2008-07-31	WHR
377	61	2008-06-30	WHR
378	32	2009-06-30	MKC
379	30	2009-05-31	MKC
380	29	2009-04-30	MKC
381	29	2009-03-31	MKC
382	31	2009-02-28	MKC
383	32	2009-01-31	MKC
384	31	2008-12-31	MKC
385	29	2008-11-30	MKC
386	33	2008-10-31	MKC
387	38	2008-09-30	MKC
388	40	2008-08-31	MKC
389	40	2008-07-31	MKC
390	35	2008-06-30	MKC
391	51	2009-06-30	NKE
392	57	2009-05-31	NKE
393	52	2009-04-30	NKE
394	46	2009-03-31	NKE
395	41	2009-02-28	NKE
396	45	2009-01-31	NKE
397	51	2008-12-31	NKE
398	53	2008-11-30	NKE
399	57	2008-10-31	NKE
400	66	2008-09-30	NKE
401	60	2008-08-31	NKE
402	58	2008-07-31	NKE
403	59	2008-06-30	NKE
404	48	2009-06-30	SJM
405	40	2009-05-31	SJM
406	39	2009-04-30	SJM
407	37	2009-03-31	SJM
408	37	2009-02-28	SJM
409	45	2009-01-31	SJM
410	43	2008-12-31	SJM
411	45	2008-11-30	SJM
412	44	2008-10-31	SJM
413	50	2008-09-30	SJM
414	54	2008-08-31	SJM
415	48	2008-07-31	SJM
416	40	2008-06-30	SJM
417	18	2009-06-30	WFM
418	18	2009-05-31	WFM
419	20	2009-04-30	WFM
420	16	2009-03-31	WFM
421	12	2009-02-28	WFM
422	10	2009-01-31	WFM
423	9	2008-12-31	WFM
424	10	2008-11-30	WFM
425	10	2008-10-31	WFM
426	20	2008-09-30	WFM
427	18	2008-08-31	WFM
428	22	2008-07-31	WFM
429	23	2008-06-30	WFM
430	14	2009-06-30	AEO
431	14	2009-05-31	AEO
432	14	2009-04-30	AEO
433	12	2009-03-31	AEO
434	9	2009-02-28	AEO
435	9	2009-01-31	AEO
436	9	2008-12-31	AEO
437	9	2008-11-30	AEO
438	11	2008-10-31	AEO
439	15	2008-09-30	AEO
440	15	2008-08-31	AEO
441	14	2008-07-31	AEO
442	13	2008-06-30	AEO
443	53	2009-06-30	RL
444	53	2009-05-31	RL
445	53	2009-04-30	RL
446	42	2009-03-31	RL
447	34	2009-02-28	RL
448	41	2009-01-31	RL
449	45	2008-12-31	RL
450	43	2008-11-30	RL
451	47	2008-10-31	RL
452	66	2008-09-30	RL
453	75	2008-08-31	RL
454	59	2008-07-31	RL
455	62	2008-06-30	RL
456	23	2009-06-30	HD
457	23	2009-05-31	HD
458	26	2009-04-30	HD
459	23	2009-03-31	HD
460	20	2009-02-28	HD
461	21	2009-01-31	HD
462	23	2008-12-31	HD
463	23	2008-11-30	HD
464	23	2008-10-31	HD
465	25	2008-09-30	HD
466	27	2008-08-31	HD
467	23	2008-07-31	HD
468	23	2008-06-30	HD
469	16	2009-06-30	GPS
470	17	2009-05-31	GPS
471	15	2009-04-30	GPS
472	12	2009-03-31	GPS
473	10	2009-02-28	GPS
474	11	2009-01-31	GPS
475	13	2008-12-31	GPS
476	13	2008-11-30	GPS
477	12	2008-10-31	GPS
478	17	2008-09-30	GPS
479	19	2008-08-31	GPS
480	16	2008-07-31	GPS
481	16	2008-06-30	GPS
482	22	2009-06-30	UA
483	24	2009-05-31	UA
484	23	2009-04-30	UA
485	16	2009-03-31	UA
486	14	2009-02-28	UA
487	18	2009-01-31	UA
488	23	2008-12-31	UA
489	22	2008-11-30	UA
490	26	2008-10-31	UA
491	31	2008-09-30	UA
492	33	2008-08-31	UA
493	29	2008-07-31	UA
494	25	2008-06-30	UA
495	18	2009-06-30	CSCO
496	18	2009-05-31	CSCO
497	19	2009-04-30	CSCO
498	16	2009-03-31	CSCO
499	14	2009-02-28	CSCO
500	14	2009-01-31	CSCO
501	16	2008-12-31	CSCO
502	16	2008-11-30	CSCO
503	17	2008-10-31	CSCO
504	22	2008-09-30	CSCO
505	24	2008-08-31	CSCO
506	21	2008-07-31	CSCO
507	23	2008-06-30	CSCO
508	30	2009-06-30	BBBY
509	28	2009-05-31	BBBY
510	30	2009-04-30	BBBY
511	24	2009-03-31	BBBY
512	21	2009-02-28	BBBY
513	23	2009-01-31	BBBY
514	25	2008-12-31	BBBY
515	20	2008-11-30	BBBY
516	25	2008-10-31	BBBY
517	31	2008-09-30	BBBY
518	30	2008-08-31	BBBY
519	27	2008-07-31	BBBY
520	28	2008-06-30	BBBY
521	6	2009-06-30	F
522	5	2009-05-31	F
523	5	2009-04-30	F
524	2	2009-03-31	F
525	2	2009-02-28	F
526	1	2009-01-31	F
527	2	2008-12-31	F
528	2	2008-11-30	F
529	2	2008-10-31	F
530	5	2008-09-30	F
531	4	2008-08-31	F
532	4	2008-07-31	F
533	4	2008-06-30	F
534	13	2009-06-30	BAC
535	11	2009-05-31	BAC
536	8	2009-04-30	BAC
537	6	2009-03-31	BAC
538	3	2009-02-28	BAC
539	6	2009-01-31	BAC
540	14	2008-12-31	BAC
541	16	2008-11-30	BAC
542	24	2008-10-31	BAC
543	35	2008-09-30	BAC
544	31	2008-08-31	BAC
545	32	2008-07-31	BAC
546	23	2008-06-30	BAC
547	48	2009-06-30	WMT
548	49	2009-05-31	WMT
549	50	2009-04-30	WMT
550	52	2009-03-31	WMT
551	49	2009-02-28	WMT
552	47	2009-01-31	WMT
553	56	2008-12-31	WMT
554	55	2008-11-30	WMT
555	55	2008-10-31	WMT
556	59	2008-09-30	WMT
557	59	2008-08-31	WMT
558	58	2008-07-31	WMT
559	56	2008-06-30	WMT
560	45	2009-06-30	COST
561	48	2009-05-31	COST
562	48	2009-04-30	COST
563	46	2009-03-31	COST
564	42	2009-02-28	COST
565	45	2009-01-31	COST
566	52	2008-12-31	COST
567	51	2008-11-30	COST
568	57	2008-10-31	COST
569	64	2008-09-30	COST
570	67	2008-08-31	COST
571	62	2008-07-31	COST
572	70	2008-06-30	COST
573	56	2009-06-30	JNJ
574	55	2009-05-31	JNJ
575	52	2009-04-30	JNJ
576	52	2009-03-31	JNJ
577	50	2009-02-28	JNJ
578	57	2009-01-31	JNJ
579	59	2008-12-31	JNJ
580	58	2008-11-30	JNJ
581	61	2008-10-31	JNJ
582	69	2008-09-30	JNJ
583	70	2008-08-31	JNJ
584	68	2008-07-31	JNJ
585	64	2008-06-30	JNJ
586	30	2009-06-30	MET
587	31	2009-05-31	MET
588	29	2009-04-30	MET
589	22	2009-03-31	MET
590	18	2009-02-28	MET
591	28	2009-01-31	MET
592	34	2008-12-31	MET
593	28	2008-11-30	MET
594	33	2008-10-31	MET
595	56	2008-09-30	MET
596	54	2008-08-31	MET
597	50	2008-07-31	MET
598	52	2008-06-30	MET
599	30	2009-06-30	VZ
600	29	2009-05-31	VZ
601	30	2009-04-30	VZ
602	30	2009-03-31	VZ
603	28	2009-02-28	VZ
604	29	2009-01-31	VZ
605	33	2008-12-31	VZ
606	32	2008-11-30	VZ
607	29	2008-10-31	VZ
608	32	2008-09-30	VZ
609	35	2008-08-31	VZ
610	34	2008-07-31	VZ
611	35	2008-06-30	VZ
612	24	2009-06-30	T
613	24	2009-05-31	T
614	25	2009-04-30	T
615	25	2009-03-31	T
616	23	2009-02-28	T
617	24	2009-01-31	T
618	28	2008-12-31	T
619	28	2008-11-30	T
620	26	2008-10-31	T
621	27	2008-09-30	T
622	31	2008-08-31	T
623	30	2008-07-31	T
624	33	2008-06-30	T
\.


--
-- Name: game_stock_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bears
--

SELECT pg_catalog.setval('game_stock_id_seq', 624, true);


--
-- Data for Name: portfolio_portfolio; Type: TABLE DATA; Schema: public; Owner: bears
--

COPY portfolio_portfolio (id, final_score, date_played, balance, user_id) FROM stdin;
\.


--
-- Name: portfolio_portfolio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bears
--

SELECT pg_catalog.setval('portfolio_portfolio_id_seq', 1, false);


--
-- Data for Name: portfolio_snippet; Type: TABLE DATA; Schema: public; Owner: bears
--

COPY portfolio_snippet (id, snippet, stock_id) FROM stdin;
\.


--
-- Name: portfolio_snippet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bears
--

SELECT pg_catalog.setval('portfolio_snippet_id_seq', 1, false);


--
-- Data for Name: portfolio_stock; Type: TABLE DATA; Schema: public; Owner: bears
--

COPY portfolio_stock (id, symbol, price, date, name, volume) FROM stdin;
\.


--
-- Name: portfolio_stock_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bears
--

SELECT pg_catalog.setval('portfolio_stock_id_seq', 1, false);


--
-- Data for Name: portfolio_stock_owned; Type: TABLE DATA; Schema: public; Owner: bears
--

COPY portfolio_stock_owned (id, symbol, amount, price_bought, date_bought, name, portfolio_id) FROM stdin;
\.


--
-- Name: portfolio_stock_owned_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bears
--

SELECT pg_catalog.setval('portfolio_stock_owned_id_seq', 1, false);


--
-- Data for Name: portfolio_transcation; Type: TABLE DATA; Schema: public; Owner: bears
--

COPY portfolio_transcation (id, symbol, number_of_shares, date_created, account_change, portfolio_id) FROM stdin;
\.


--
-- Name: portfolio_transcation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bears
--

SELECT pg_catalog.setval('portfolio_transcation_id_seq', 1, false);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_4d4adc6a80714f_uniq; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_4d4adc6a80714f_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: game_stock_pkey; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY game_stock
    ADD CONSTRAINT game_stock_pkey PRIMARY KEY (id);


--
-- Name: portfolio_portfolio_pkey; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY portfolio_portfolio
    ADD CONSTRAINT portfolio_portfolio_pkey PRIMARY KEY (id);


--
-- Name: portfolio_snippet_pkey; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY portfolio_snippet
    ADD CONSTRAINT portfolio_snippet_pkey PRIMARY KEY (id);


--
-- Name: portfolio_stock_owned_pkey; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY portfolio_stock_owned
    ADD CONSTRAINT portfolio_stock_owned_pkey PRIMARY KEY (id);


--
-- Name: portfolio_stock_pkey; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY portfolio_stock
    ADD CONSTRAINT portfolio_stock_pkey PRIMARY KEY (id);


--
-- Name: portfolio_transcation_pkey; Type: CONSTRAINT; Schema: public; Owner: bears; Tablespace: 
--

ALTER TABLE ONLY portfolio_transcation
    ADD CONSTRAINT portfolio_transcation_pkey PRIMARY KEY (id);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: bears; Tablespace: 
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: bears; Tablespace: 
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: bears; Tablespace: 
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: bears; Tablespace: 
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: bears; Tablespace: 
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: bears; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: bears; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: bears; Tablespace: 
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: bears; Tablespace: 
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: bears; Tablespace: 
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- Name: portfolio_portfolio_e8701ad4; Type: INDEX; Schema: public; Owner: bears; Tablespace: 
--

CREATE INDEX portfolio_portfolio_e8701ad4 ON portfolio_portfolio USING btree (user_id);


--
-- Name: portfolio_snippet_aff86b81; Type: INDEX; Schema: public; Owner: bears; Tablespace: 
--

CREATE INDEX portfolio_snippet_aff86b81 ON portfolio_snippet USING btree (stock_id);


--
-- Name: portfolio_stock_owned_fcd19535; Type: INDEX; Schema: public; Owner: bears; Tablespace: 
--

CREATE INDEX portfolio_stock_owned_fcd19535 ON portfolio_stock_owned USING btree (portfolio_id);


--
-- Name: portfolio_transcation_fcd19535; Type: INDEX; Schema: public; Owner: bears; Tablespace: 
--

CREATE INDEX portfolio_transcation_fcd19535 ON portfolio_transcation USING btree (portfolio_id);


--
-- Name: auth_content_type_id_633b0c8ef1636548_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: bears
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_content_type_id_633b0c8ef1636548_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissio_group_id_611836ee460d1368_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: bears
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_611836ee460d1368_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permission_id_74f5c3468608f4ee_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: bears
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_74f5c3468608f4ee_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user__permission_id_2127980c67c124dd_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: bears
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user__permission_id_2127980c67c124dd_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_6ae84f87aadd954d_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: bears
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_6ae84f87aadd954d_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_6d9672edea5e39fa_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: bears
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6d9672edea5e39fa_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permiss_user_id_4c5170608b59e8da_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: bears
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permiss_user_id_4c5170608b59e8da_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: djan_content_type_id_4cba72c8f8be0692_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: bears
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT djan_content_type_id_4cba72c8f8be0692_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_67559c5f981eec2e_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: bears
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_67559c5f981eec2e_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: portfol_portfolio_id_3e1d2a27f66287c5_fk_portfolio_portfolio_id; Type: FK CONSTRAINT; Schema: public; Owner: bears
--

ALTER TABLE ONLY portfolio_stock_owned
    ADD CONSTRAINT portfol_portfolio_id_3e1d2a27f66287c5_fk_portfolio_portfolio_id FOREIGN KEY (portfolio_id) REFERENCES portfolio_portfolio(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: portfol_portfolio_id_4a48d6ba1f1f0c2e_fk_portfolio_portfolio_id; Type: FK CONSTRAINT; Schema: public; Owner: bears
--

ALTER TABLE ONLY portfolio_transcation
    ADD CONSTRAINT portfol_portfolio_id_4a48d6ba1f1f0c2e_fk_portfolio_portfolio_id FOREIGN KEY (portfolio_id) REFERENCES portfolio_portfolio(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: portfolio_portfolio_user_id_6088ae2fd94f975e_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: bears
--

ALTER TABLE ONLY portfolio_portfolio
    ADD CONSTRAINT portfolio_portfolio_user_id_6088ae2fd94f975e_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: portfolio_snipp_stock_id_443b3651eafa89af_fk_portfolio_stock_id; Type: FK CONSTRAINT; Schema: public; Owner: bears
--

ALTER TABLE ONLY portfolio_snippet
    ADD CONSTRAINT portfolio_snipp_stock_id_443b3651eafa89af_fk_portfolio_stock_id FOREIGN KEY (stock_id) REFERENCES portfolio_stock(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

