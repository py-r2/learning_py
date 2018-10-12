--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.8
-- Dumped by pg_dump version 9.6.8

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.data (
    id integer NOT NULL,
    user_name character varying(20),
    title character varying(200),
    article character varying(1000),
    date_posted date
);


ALTER TABLE public.data OWNER TO postgres;

--
-- Name: data_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.data_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_id_seq OWNER TO postgres;

--
-- Name: data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.data_id_seq OWNED BY public.data.id;


--
-- Name: userdata; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.userdata (
    id integer NOT NULL,
    username character varying(15),
    password character varying(20),
    email character varying(50)
);


ALTER TABLE public.userdata OWNER TO postgres;

--
-- Name: userdata_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.userdata_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.userdata_id_seq OWNER TO postgres;

--
-- Name: userdata_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.userdata_id_seq OWNED BY public.userdata.id;


--
-- Name: data id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data ALTER COLUMN id SET DEFAULT nextval('public.data_id_seq'::regclass);


--
-- Name: userdata id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata ALTER COLUMN id SET DEFAULT nextval('public.userdata_id_seq'::regclass);


--
-- Data for Name: data; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.data (id, user_name, title, article, date_posted) FROM stdin;
1	Romeo Rauta	How I become a software developer	Hi, I'm Romeo Rauta – a Python-Flask software engineer from Calgary, Canada\r\n\r\nMy journey as a developer started back in 1993 in the University. Then life drove me to SysAdmin rather until...  when I had a challenge to accomplish a free Python online course on CodeAcademy. Was enough for me to dive in to this wonderful world and continued with few other Python, Flask, SQL, Linux etc. courses on Udemy.\r\n\r\nThe next step was to find guidance on to what skills to acquire and to create a portfolio.\r\n\r\nFor guidance I asked everyone I found online or around me and had anything to do with programming. As for the portfolio I found lots of online resources built one Python-Flask-PostgreSQL login app with sign-up option and this portfolio website.	2018-04-17
2	Romeo Rauta	Build your own portfolio website	This article is about how I built my portfolio website and what web features does it have that might be beneficial for you. The code is for free on my GitHub portfolio and you can feel free to use it.	2018-04-17
\.


--
-- Name: data_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.data_id_seq', 2, true);


--
-- Data for Name: userdata; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.userdata (id, username, password, email) FROM stdin;
\.


--
-- Name: userdata_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.userdata_id_seq', 1, false);


--
-- Name: data data_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data
    ADD CONSTRAINT data_pkey PRIMARY KEY (id);


--
-- Name: data data_title_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data
    ADD CONSTRAINT data_title_key UNIQUE (title);


--
-- Name: userdata userdata_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata
    ADD CONSTRAINT userdata_email_key UNIQUE (email);


--
-- Name: userdata userdata_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata
    ADD CONSTRAINT userdata_pkey PRIMARY KEY (id);


--
-- Name: userdata userdata_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata
    ADD CONSTRAINT userdata_username_key UNIQUE (username);


--
-- PostgreSQL database dump complete
--

