import datetime
import importlib
import os
import sqlite3
import sys

def get_latest_migration(cursor):
    sql_create_command = """
    CREATE TABLE IF NOT EXISTS applied_migrations (
    name TEXT PRIMARY KEY,
    applied_at DATETIME NOT NULL
    );"""

    cursor.execute(sql_create_command)

    sql_select_command = "SELECT name FROM applied_migrations ORDER BY name DESC LIMIT 1;"

    cursor.execute(sql_select_command)

    return cursor.fetchone()

def add_latest_migration(latest_migration, cursor):
    sql_create_command = """
    CREATE TABLE IF NOT EXISTS applied_migrations (
    name TEXT PRIMARY KEY,
    applied_at DATETIME NOT NULL
    );"""

    cursor.execute(sql_create_command)

    sql_insert_command = """
    INSERT INTO applied_migrations (name, applied_at)
    VALUES (?, ?)
    ON CONFLICT(name) DO UPDATE SET applied_at = excluded.applied_at;"""

    cursor.execute(sql_insert_command, (latest_migration, datetime.datetime.now()))


def do_migrations():
    print("Inside do migrations")
    with sqlite3.connect("logger.db") as connection:
        print("do_migrate()")
        #check if migration_table exists and get latest migration
        latest_migration = get_latest_migration(connection.cursor())
        #get migrations and apply those that follow the latest migration
        folder_path ='logger/migrations'
        file_list = os.listdir(folder_path)
        print(file_list)
        migration_list = [filename[:-3] for filename in file_list if filename.endswith(".py")]
        migration_list.sort()
        if latest_migration and latest_migration in migration_list:
            lm_index = migration_list.index(latest_migration)
            migration_list = migration_list[(lm_index +1):]
        for modulename in migration_list:
            print(modulename)
            filepath = os.path.join(folder_path, modulename + ".py")

            spec = importlib.util.spec_from_file_location(modulename, filepath)
            module = importlib.util.module_from_spec(spec)
            sys.modules[modulename] = module
            spec.loader.exec_module(module)

            if hasattr(module, "migrate"):
                func = getattr(module, "migrate")
                func()
        if len(migration_list) > 0:
            add_latest_migration(migration_list[-1], connection.cursor())
            connection.commit()