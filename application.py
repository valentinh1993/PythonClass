#! /usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

from sqliteDB import sqliteDBAPI

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        db_file = 'application.db'
        sqlite_cmdline = 'SELECT * FROM Database WHERE '
        print(request.form)
        flag = True
        for item in request.form:
            if request.form[item] != '':
                if flag:
                    sqlite_cmdline += item + ' = "' + request.form[item] + '"'
                    flag = False
                else:
                    sqlite_cmdline += ' AND ' + item + ' = "' + request.form[item] + '"'
        sqlite_cmdline += ';'
        #print(sqlite_cmdline)
        result = sqliteDBAPI(db_file, sqlite_cmdline)
        #print(result)
        if result != []:
            column = ['Id', 'Date', 'Time', 'Location', 'Operator', 'FlightNo', 'Route', 'ACType', 'Registration', 'Aboard', 'Fatalities', 'Ground', 'Summary', 'FatalitiesInt', 'AboardInt', 'GroundInt', 'Month', 'Year', 'DeathRate', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Weather']
            Data = []
            for item in result:
                temp_dict = {}
                for index in range (1, len (item)):
                    temp_dict [column [index]] = item [index]
                Data.append (temp_dict)
            print (Data)
            return render_template('index.html', Data = Data)
        else:
            Result = 'No Result'
            return render_template('index.html', Result = Result)
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
