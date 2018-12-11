#! /usr/bin/python3
# -*- coding: UTF-8 -*-

import time, random, sqlite3

def sqliteDBAPI (db_file, sqlite_cmdline, args = None):

    flag = True;
    while flag == True:
        flag = False;
        if args == None:
            db_connection = sqlite3.connect (db_file);
            try:
                ret_list = [];
                #wair for unlock
                for item in db_connection.execute (sqlite_cmdline):
                    ret_list.append (item);
                db_connection.commit ();
            except BaseException as e:
                db_connection.rollback ();
                ret_list = None;
                if 'database is locked' in str (e):
                    flag = True;
                    time.sleep (random.randint (3, 5));
                else:
                    print ('Error Commend Line Is :');
                    print (sqlite_cmdline);
                    print ('Error Resean Is :');
                    print (e);
            finally:
                db_connection.close ();
                return ret_list;
        else:
            db_connection = sqlite3.connect (db_file);
            try:
                #wair for unlock
                db_connection.execute (sqlite_cmdline, args);
                db_connection.commit ();
            except BaseException as e:
                db_connection.rollback ();
                if 'database is locked' in str (e):
                    flag = True;
                    time.sleep (random.randint (3, 5));
                else:
                    print ('Error Resean Is :');
                    print (e);
                    if 'probably unsupported type' in str (e):                        
                        print ('args item is :');
                        number = 0;
                        for item in args:
                            print (number, ':', type (item), ':', item);
                            number += 1;
                        print ('args item over')
            finally:
                db_connection.close ();

def sqliteDBMANYAPI (db_file, sqlite_cmdline, args):

    flag = True;
    #wair for unlock
    while flag == True:
        flag = False;
        db_connection = sqlite3.connect (db_file);
        try:
            db_connection.executemany (sqlite_cmdline, args);
            db_connection.commit ();
        except BaseException as e:
            db_connection.rollback ();
            if 'database is locked' in str (e):
                flag = True;
                time.sleep (random.randint (3, 5));
            else:
                print ('Error Resean Is :');
                print (e);
        finally:
            db_connection.close ();

def main ():

    db_file = 'application.db';
    sqlite_cmdline = \
        '''CREATE TABLE IF NOT EXISTS Database
        (Id integer PRIMARY KEY autoincrement, 
        Date TEXT,
        Time TEXT,
        Location TEXT,
        Operator TEXT,
        FlightNo TEXT,
        Route TEXT,
        ACType TEXT,
        Registration TEXT,
        Aboard TEXT,
        Fatalities TEXT,
        Ground TEXT,
        Summary TEXT,
        FatalitiesInt TEXT,
        AboardInt TEXT,
        GroundInt TEXT,
        Month TEXT,
        Year TEXT,
        DeathRate TEXT,
        Jan TEXT,
        Feb TEXT,
        Mar TEXT,
        Apr TEXT,
        May TEXT,
        June TEXT,
        July TEXT,
        Aug TEXT,
        Sep TEXT,
        Oct TEXT,
        Nov TEXT,
        Dec TEXT,
        Weather TEXT
        );''';

    sqliteDBAPI (db_file, sqlite_cmdline);

    return;

if __name__ == '__main__':

    main ();
