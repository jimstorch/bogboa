#------------------------------------------------------------------------------
#   File:       tables.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------


from lib.model.dbconnect import THE_CURSOR


def create_tables():

    sql = """
        CREATE TABLE archetype (
            uuid TEXT PRIMARY KEY.
            handle TEXT,
            script);
        """     

    THE_CURSOR.execute(sql)


    sql = """
        CREATE TABLE race (
            uuid TEXT PRIMARY KEY,
            handle TEXT,
            script);
        """

    THE_CURSOR.execute(sql

    sql = """
        CREATE TABLE gender (
            uuid TEXT PRIMARY KEY,
            handle TEXT,
            script);
        """

    THE_CURSOR.execute(sql

    sql = """
        CREATE TABLE skill (
            uuid TEXT PRIMARY KEY,
            handle TEXT,
            script);
        """

    THE_CURSOR.execute(sql

    sql = """
        CREATE TABLE effect (
            uuid TEXT PRIMARY KEY,
            handle TEXT,
            script TEXT,
            module TEXT);
        """

    THE_CURSOR.execute(sql

    sql = """
        CREATE TABLE mob (
            uuid TEXT PRIMARY KEY,
            handle TEXT,
            script TEXT,
            module TEXT);
        """

    THE_CURSOR.execute(sql

    sql = """
        CREATE TABLE item (
            uuid TEXT PRIMARY KEY,
            handle TEXT,
            script TEXT,
            module TEXT);
        """

    THE_CURSOR.execute(sql

    sql = """
        CREATE TABLE room (
            uuid TEXT PRIMARY KEY,
            handle TEXT,
            script TEXT,
            module TEXT);
        """

    THE_CURSOR.execute(sql

    sql = """
        CREATE TABLE module (
            uuid TEXT PRIMARY KEY,
            handle TEXT,
            script);
        """

    THE_CURSOR.execute(sql

    sql = """
        CREATE TABLE player (
            uuid TEXT PRIMARY KEY,
            handle TEXT,
            password TEXT,
            archetype_uuid TEXT,
            level INT,
            race_uuid TEXT,
            gender_uuid TEXT,
            money INT,
            created DATETIME);
        """

    THE_CURSOR.execute(sql

    sql = """
        CREATE TABLE player_flag (
            player_uuid TEXT PRIMARY KEY,
            handle TEXT,
            value TEXT,
            created DATETIME);
        """

    THE_CURSOR.execute(sql
        
    sql = """
        CREATE TABLE player_skill (
            player_uuid TEXT PRIMARY KEY,        
            skill_uuid TEXT,
            value TEXT,
            created DATETIME);
        """

    THE_CURSOR.execute(sql

    sql = """
        CREATE TABLE inventory (
            player_uuid TEXT PRIMARY KEY,
            slot TEXT,
            item_uuid);
        """
             
    THE_CURSOR.execute(sql

