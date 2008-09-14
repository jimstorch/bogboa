#------------------------------------------------------------------------------
#   File:       tables.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

sql = """
    CREATE TABLE archetypes (
        uuid TEXT PRIMARY KEY.
        alias TEXT,
        script);
    """     

sql = """
    CREATE TABLE races (
        uuid TEXT PRIMARY KEY,
        alias TEXT,
        script);
    """

sql = """
    CREATE TABLE skills (
        uuid TEXT PRIMARY KEY,
        alias TEXT,
        script);
    """

sql = """
    CREATE TABLE effects (
        uuid TEXT PRIMARY KEY,
        alias TEXT,
        script TEXT,
        module TEXT);
    """

sql = """
    CREATE TABLE mobs (
        uuid TEXT PRIMARY KEY,
        alias TEXT,
        script TEXT,
        module TEXT);
    """

sql = """
    CREATE TABLE items (
        uuid TEXT PRIMARY KEY,
        alias TEXT,
        script TEXT,
        module TEXT);
    """

sql = """
    CREATE TABLE rooms (
        uuid TEXT PRIMARY KEY,
        alias TEXT,
        script TEXT,
        module TEXT);
    """

sql = """
    CREATE TABLE modules (
        uuid TEXT PRIMARY KEY,
        alias TEXT,
        script);
    """

sql = """
    CREATE TABLE flags (
        player TEXT,
        flag TEXT,
        created DATETIME);
    """
    

