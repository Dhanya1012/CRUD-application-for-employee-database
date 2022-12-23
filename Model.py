from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class EmployeeModel(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    gender = db.Column(db.String())
    salary = db.Column(db.String())

    def __init__(self,first_name,last_name,email,gender,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.salary = salary

        def __repr__(self):
            return f"{self.first_name}:{self.last_name}"
