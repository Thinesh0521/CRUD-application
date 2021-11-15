from flask import request, redirect, render_template, url_for
from application import app, db
from application.forms import StudentForm, PostForm
from application.models import Students, Posts

#This is the index route where we are going to query on all 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/student/add', methods= ['GET', 'POST'])
def add_student():
    name =None
    form = StudentForm()
    if form.validate_on_submit():
        student= Students.query.filter_by(email=form.email.data).first()
        if student is None:
            student = Students(name=form.name.data, email=form.email.data)
            db.session.add(student)
            db.session.commit()
          name = form.name.data = ''
          form.name.data = ''
          form.email.data = ''
        our_students = Students.query.order_by(Students)
        return render_template("add_students.html", form=form )
            form=form,
            name=name,
            our_students=our_students)
# Add Post Page
@app.route('/add_post', methods= ['GET', 'POST'])
def add_post():
    form = PostForm()

    if form.validate_on_submit():
        post= Posts(course=form.course.data, content= form.content.data)
        # Clear The Form
        form.course.data =''
        form.content.data = ''
    return render_template("add_post.html", form=form )

        
@app.route('/posts')
def posts():
    #Showing all the posts from the database
    posts= Posts.query.order_by(Posts)

    return render_template("posts.html", posts=posts)

@app.route('/posts/<int:id>')
def post(id):
    post = Posts.query_or_404(id)
    return render_template('post.html',post=post)


@app.route('/posts/edit/<int:id>', method=['GET', 'POST'])
def edit_post(id):
    post = Posts.query.get_or_404(id)
    form = PostForm()
    if form.validate_on_submit():
        post.course = form.course.data
        post.content= form.content.data
        return redirect (url_for('post', id=post.id))
    form.course.data = post.course 
    form.content.data = post.content
    return render_template('edit_post.html', form=form)

@app.route('/posts/delete/<int:id>')
def delete_post(id):
    post_to_delete = Posts.query.get_or_404(id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect("/")
