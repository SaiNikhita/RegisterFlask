import mysql.connector
from flask import Flask,render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("register.html")

def getDb():
   mydb = mysql.connector.connect(
       host="192.168.169.16",
       user="sapplica",
       passwd="s@pplic@2008#",
       database="parsing")
   return mydb

@app.route('/signup',methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    pno = request.form['pno']
    sex = request.form['sex']
    dob = request.form['dob']
    edu = request.form['edu']
    con=getDb()
    cursor = con.cursor(buffered=True)
    cursor.execute("insert into parsing(name,email,phonenumber,sex,dob,education) values('" + name + "','" + email + "','" + pno + "','" + sex + "','" + dob + "','" + edu+ "')")
    cursor.execute("select * from parsing")
    data = cursor.fetchall()
    cursor.close()
    con.commit()
    con.close()
    if data is not None:
        return render_template("table.html", value=data)
    else:
        return "Error"

@app.route('/editform',methods=['POST','GET'])
def editform():
    name = request.form['name']
    email = request.form['email']
    pno = request.form['pno']
    sex = request.form['sex']
    dob = request.form['dob']
    edu = request.form['edu']
    data=[name,email,pno,sex,dob,edu]
    return render_template("edit.html",value=data)

@app.route('/edit', methods=['POST', 'GET'])
def edit():
    name=request.form['name']
    email = request.form['email']
    pno = request.form['pno']
    dob = request.form['dob']
    edu = request.form['edu']
    con = getDb()
    cursor = con.cursor(buffered=True)
    cursor.execute("update parsing set email='" + email + "',phonenumber='" + pno + "',dob='" + dob + "',education='" + edu + "' where name='"+name+"'")
    cursor.execute("select * from parsing")
    data = cursor.fetchall()
    cursor.close()
    con.commit()
    con.close()
    if data is not None:
        return render_template("table.html", value=data)
    else:
        return "Error"

@app.route('/delete',methods=['POST','GET'])
def delete():
    name=request.form['name']
    print(name)
    con = getDb()
    cursor = con.cursor(buffered=True)
    cursor.execute("delete from parsing where name='"+name+"'")
    cursor.execute("select * from parsing")
    data = cursor.fetchall()
    cursor.close()
    con.commit()
    con.close()
    if data is not None:
        return render_template("table.html", value=data)
    else:
        return "Error"

@app.route('/view',methods=['POST','GET'])
def view():
    name = request.form['name']
    con = getDb()
    cursor = con.cursor(buffered=True)
    cursor.execute("select * from parsing where name='" + name + "'")
    data = cursor.fetchall()
    cursor.close()
    con.commit()
    con.close()
    if data is not None:
        return render_template("view.html", value=data)
    else:
        return "Error"

if __name__ == '__main__':
   app.run(debug=True)
