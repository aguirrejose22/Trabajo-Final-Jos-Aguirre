PGDMP  &    4                }            paletizador_db    16.8 (Debian 16.8-1.pgdg120+1)    17.4                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false                       1262    16389    paletizador_db    DATABASE     y   CREATE DATABASE paletizador_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.UTF8';
    DROP DATABASE paletizador_db;
                     paletizador_db_user    false                       0    0    paletizador_db    DATABASE PROPERTIES     7   ALTER DATABASE paletizador_db SET "TimeZone" TO 'utc';
                          paletizador_db_user    false                        2615    2200    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                     paletizador_db_user    false            �            1259    16413    palletizer_info    TABLE     �   CREATE TABLE public.palletizer_info (
    machine_id character varying(10) NOT NULL,
    model character varying(50),
    location character varying(100),
    install_date date,
    last_maintenance date,
    certified_operator character varying(100)
);
 #   DROP TABLE public.palletizer_info;
       public         heap r       paletizador_db_user    false    5                      0    16413    palletizer_info 
   TABLE DATA           z   COPY public.palletizer_info (machine_id, model, location, install_date, last_maintenance, certified_operator) FROM stdin;
    public               paletizador_db_user    false    215   �       �           2606    16417 $   palletizer_info palletizer_info_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.palletizer_info
    ADD CONSTRAINT palletizer_info_pkey PRIMARY KEY (machine_id);
 N   ALTER TABLE ONLY public.palletizer_info DROP CONSTRAINT palletizer_info_pkey;
       public                 paletizador_db_user    false    215            �           826    16391     DEFAULT PRIVILEGES FOR SEQUENCES    DEFAULT ACL     Z   ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON SEQUENCES TO paletizador_db_user;
                        postgres    false            �           826    16393    DEFAULT PRIVILEGES FOR TYPES    DEFAULT ACL     V   ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON TYPES TO paletizador_db_user;
                        postgres    false            �           826    16392     DEFAULT PRIVILEGES FOR FUNCTIONS    DEFAULT ACL     Z   ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON FUNCTIONS TO paletizador_db_user;
                        postgres    false            �           826    16390    DEFAULT PRIVILEGES FOR TABLES    DEFAULT ACL     �   ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT SELECT,INSERT,REFERENCES,DELETE,TRIGGER,TRUNCATE,UPDATE ON TABLES TO paletizador_db_user;
                        postgres    false               �   x�E�1n�@E��S�͌�%82J�V�u����H�#�bxQ�)����ʟ\��6��� $��Ȕ�)CΡ�P�֮�Gp7#4�E�o�ƪNiB���(�c���Q��~/=�`Et�QST���Տ簌�؝��f�6�]:(�+��YPJ�A�G�v3�[���i��HS���Sİv�����7�s/�c�ɽI�     