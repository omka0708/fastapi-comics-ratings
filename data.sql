--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1 (Debian 16.1-1.pgdg120+1)
-- Dumped by pg_dump version 16.1 (Debian 16.1-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: root
--

INSERT INTO public.alembic_version (version_num) VALUES ('c58271f2c0ec');


--
-- Data for Name: comic; Type: TABLE DATA; Schema: public; Owner: root
--

INSERT INTO public.comic (id, title, author, rating) VALUES (2, 'title_2', 'author_2', 0);
INSERT INTO public.comic (id, title, author, rating) VALUES (1, 'title_1', 'author_1', 0);
INSERT INTO public.comic (id, title, author, rating) VALUES (100, 'ONLY_FOR_TEST', 'ONLY_FOR_TEST', 3.5);


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: root
--

INSERT INTO public."user" (id, email, hashed_password, is_active, is_superuser, is_verified) VALUES (1, 'user1@example.com', '$2b$12$nFtXr5Lc2c6j/j/4d/yQuucDDwlmtwYUwaUNe5qNFQkUStQctFf3S', true, false, false);
INSERT INTO public."user" (id, email, hashed_password, is_active, is_superuser, is_verified) VALUES (2, 'user2@example.com', '$2b$12$wcr/Rx8MdFXPx.cG7Wc6..wvT006pJB5aNbVx2dvQGL5LVeolQssy', true, false, false);
INSERT INTO public."user" (id, email, hashed_password, is_active, is_superuser, is_verified) VALUES (3, 'user3@example.com', '$2b$12$E0tn0m9F2Xmlovv6HXDY/eGmDTnPjcpglX5ay/iMCgXKBTZAns5DC', true, false, false);
INSERT INTO public."user" (id, email, hashed_password, is_active, is_superuser, is_verified) VALUES (4, 'user4@example.com', '$2b$12$GZOku0xLP5a6qcVWTTaOh.J..BCr2xegYu7ZHAYTUH6TIyKiZM/RO', true, false, false);


--
-- Data for Name: rating; Type: TABLE DATA; Schema: public; Owner: root
--

INSERT INTO public.rating (id, comic_id, user_id, "VALUE") VALUES (6, 100, 1, 2);
INSERT INTO public.rating (id, comic_id, user_id, "VALUE") VALUES (7, 100, 2, 3);
INSERT INTO public.rating (id, comic_id, user_id, "VALUE") VALUES (8, 100, 3, 4);
INSERT INTO public.rating (id, comic_id, user_id, "VALUE") VALUES (9, 100, 4, 5);


--
-- Name: comic_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.comic_id_seq', 1, false);


--
-- Name: rating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.rating_id_seq', 10, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.user_id_seq', 4, true);


--
-- PostgreSQL database dump complete
--

