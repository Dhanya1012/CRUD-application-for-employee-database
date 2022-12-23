from flask import Flask,render_template,request,redirect,session
from Model import db,EmployeeModel
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
Migrate(app, db)

@app.before_first_request
def create_table():
    db.create_all()
@app.route("/home", methods = ["GET","POST"])
def home():
    return render_template("home.html")
@app.route("/create", methods = ["GET","POST"])
def create():
    if request.method =='GET':
        return render_template("create.html")
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        gender = request.form['gender']
        salary = request.form['salary']

        employees = EmployeeModel(
            first_name = first_name,
            last_name = last_name,
            email = email,
            gender = gender,
            salary = salary
        )
        db.session.add(employees)
        db.session.commit()
        return redirect('/')

@app.route('/', methods=['GET'])
def RetriveList():
    employees = EmployeeModel.query.all()
    return render_template('index.html',employees = employees)

@app.route('/<int:id>/edit', methods=['GET','POST'])

def update(id):
    employee = EmployeeModel.query.filter_by(id=id).first()

    if request.method == 'POST':
            if employee:
                db.session.delete(employee)
                db.session.commit()

                first_name = request.form['first_name']
                last_name = request.form['last_name']
                email = request.form['email']
                gender = request.form['gender']
                salary =request.form['salary']

                employee = EmployeeModel(
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    gender = gender,
                    salary = salary
                )
                db.session.add(employee)
                db.session.commit()
                return redirect('/')
            return f"employee with id ={id} Does not exist"


    return render_template('update.html',employee = employee)



@app.route('/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    employees = EmployeeModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if employees:
            db.session.delete(employees)
            db.session.commit()
            return redirect('/')
        abort(404)
    #return redirect('/')
    return render_template('delete.html')

app.run(debug=True)
