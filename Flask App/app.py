from flask import Flask, render_template, request, session, sessions
import mysql.connector

app = Flask(__name__)

# DB Creds
dbuser = 'Admin'
dbpassword = 'admin@123'
dbhost = 'localhost'  # IP of where MYSQL is installed
db = ' BreakFixSearch'
dbport = '4928'

# Connection to DB

cnx = mysql.connector.MySQLConnection(user=dbuser, password=dbpassword,
                                      host=dbhost,
                                      database=db, port=dbport)
dbcursor = cnx.cursor()


@app.route("/")
def AddPage():
    return render_template('app.html')


@app.route('/insert', methods=['POST', 'GET'])
def InsertData():
    if request.method == 'POST':
        IssueTitle = request.form.get('IssueTitle')
        IssueDescription = request.form.get('IssueDescription')

        # Query Execution
        sql = "INSERT INTO Issues (Title,Description) VALUES (%s,%s)"
        val = (IssueTitle, IssueDescription)
        dbcursor.execute(sql, val)
        cnx.commit()

        return render_template('app.html')


@app.route("/get.html")
def GetPage():
    return render_template('get.html')


@app.route('/find', methods=['POST', 'GET'])
def FindIssue():
    if request.method == 'POST':
        Keywords = request.form.get('Keyword')
        # Query Execution
        sql = "select Title,Description from Issues where Title like '%%s%'"
        val = (Keywords)
        dbcursor.execute(sql, val)
        result = dbcursor.fetchall()
        print(result)
        # cnx.commit()

        return render_template('get.html', resultset=result)


if __name__ == '__main__':
    app.run(debug=True)
