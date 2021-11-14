from application import db
#Using the command "py create.py" in the terminal, the tables
# in the database will upload automatically using SQLAlchemy.
db.drop_all()
db.create_all()
