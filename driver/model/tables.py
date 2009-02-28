# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       driver/model/tables.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------


from lib.model.dbconnect import THE_CURSOR


#-----------------------------------------------------------------Create Tables

def create_tables():

    sql = """
        CREATE TABLE sects (
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

    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE gender (
            uuid TEXT PRIMARY KEY,
            handle TEXT,
            script);
        """

    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE skill (
            uuid TEXT PRIMARY KEY,
            handle TEXT,
            script);
        """

    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE effect (
            uuid TEXT PRIMARY KEY,
            handle TEXT,
            script TEXT,
            module TEXT);
        """

    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE bot (
            uuid TEXT PRIMARY KEY,
            handle TEXT,
            script TEXT,
            module TEXT);
        """

    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE item (
            uuid TEXT PRIMARY KEY,
            handle TEXT,
            script TEXT,
            module TEXT);
        """

    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE room (
            uuid TEXT PRIMARY KEY,
            handle TEXT,
            script TEXT,
            module TEXT);
        """

    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE module (
            uuid TEXT PRIMARY KEY,
            handle TEXT,
            script);
        """

    THE_CURSOR.execute(sql)

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

    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE player_flag (
            player_uuid TEXT PRIMARY KEY,
            handle TEXT,
            value TEXT,
            created DATETIME);
        """

    THE_CURSOR.execute(sql)
        
    sql = """
        CREATE TABLE player_skill (
            player_uuid TEXT PRIMARY KEY,        
            skill_uuid TEXT,
            value TEXT,
            created DATETIME);
        """

    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE player_inventory (
            player_uuid TEXT PRIMARY KEY,
            slot TEXT,
            item_uuid);
        """
             
    THE_CURSOR.execute(sql)


    sql = """
        CREATE TABLE banned_ip (
            ip_address TEXT,
            note TEXT,
            created DATETIME);
        """

    THE_CURSOR.execute(sql)

