from flask import *
import sqlite3 as sql
app=Flask(__name__)
app.secret_key="qwertyuiop"

@app.route('/')
def login():
    return render_template("Login.html")

@app.route('/homepage')
def homepage():
    return render_template("Homepage.html")

@app.route('/logout')
def logout():
    session.pop('email' and 'passw',None)
    return render_template("Login.html")

@app.route('/registration')
def registration():
    return render_template("Registration.html")


@app.route('/realme')
def realme():
    return render_template("Realme Avail.html")

@app.route('/nothing')
def nothing():
    return render_template("Nothing Avail.html")

@app.route('/motorola')
def motorola():
    return render_template("Motorola Avail.html")



@app.route('/userdash')
def userdash():
    if "Email" in session:
        con = sql.connect("storage.db")
        c = con.cursor()
        c.execute("SELECT name, device,date FROM user WHERE Email=?", (session["Email"],))
        data = c.fetchone()
        con.close()
        if data:
            name, device, date = data
            return render_template("User Panel.html", email=session["Email"], name=name, device=device, date=date)
    return redirect(url_for("login"))

@app.route('/admindash')
def admindash():
    return render_template("Admin Panel.html")

@app.route('/devices')
def devices():
    return render_template("Devices.html")

@app.route('/support')
def support():
    return render_template("Support.html")

@app.route('/supportform',methods=["POST"])
def supportform():
    if request.method=="POST":
        fname=request.form["Name1"]
        email=request.form["Email1"]
        issue=request.form["Issue1"]
        desc=request.form["Description1"]
        con=sql.connect("Storage.db")
        c=con.cursor()
        c.execute("Insert into support (Name,Email,Issue,Description) values (?,?,?,?)",(fname,email,issue,desc))
        con.commit()
        con.close()
        return "Done"
    else:
        return "failed"

@app.route('/saveform',methods=["POST"])
def saveform():
    if request.method=="POST":
        nam=request.form["Name1"]
        em=request.form["Email1"]
        dev=request.form["Device1"]
        dat=request.form["Date1"]
        passw=request.form["Password1"]
        return render_template("index.html")
    
        con=sql.connect("Storage.db")
        c=con.cursor()
        c.execute("insert into user(Name,Email,Device,Date,Password) values(?,?,?,?,?)",(nam,em,dev,dat,passw))
        con.commit()
        con.close()
        return redirect(url_for("login"))
    else:
        return "Failed"
    
@app.route('/loginform', methods=["POST"])
def loginform():
    if request.method=="POST":
        em=request.form["Email1"]
        passw=request.form["Password1"]
        con=sql.connect("Storage.db")
        c=con.cursor()
        c.execute("Select * from user where Email=? and Password=?",(em,passw))
        data=c.fetchall()
        con.close()
        if data:
            session["Email"]=em
            session["Password"]=passw
            return render_template("Homepage.html")
        else:
            return redirect(url_for("login"))
        
@app.route('/upassword', methods=["POST"])
def upassword():
    if request.method=="POST":
        em=request.form["Email1"]
        passw1=request.form["Passw1"]
        passw2=request.form["Passw2"]
        con=sql.connect("Storage.db")
        c=con.cursor()
        if passw1==passw2:
            c.execute("update user set Password=(?) where Email=(?)",(passw2,em))
            con.commit()
            con.close()
            return "Success"
        else:
            return "Failed"

if __name__=='__main__':
    app.run(debug=True)