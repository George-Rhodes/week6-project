from flask import Flask, render_template, redirect, url_for, request
from application import app, db
from application.models import Routine
from application.forms import routeForm, updateForm, orderedForm




@app.route('/', methods = ['GET', 'POST'])
def index():
	form = orderedForm()
	totals = {"total": Routine.query.count(), "totalCompleted" : ToDoList.query.filter_by(status=True).count()}
	if form.orderedWith.data == "id":
		routeList = Routine.query.order_by(Routine.id.desc()).all()	
	else:
		routeList = Routine.query.all()
	return render_template('index.html', routeList = routeList, form=form)




@app.route('/add', methods=['GET', 'POST'])
def add():
	form = routeForm()
	if form.validate_on_submit():
		new_routine= Routine(task=form.task.data)
		db.session.add(new_routine)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template ('add.html', form=form)



@app.route('/update/<idNum>', methods=['POST', 'GET'])
def update(idNum):
	form = updateForm()
	route= Routine.query.get(idNum)
	if form.validate_on_submit():
		route.rTitle=form.rTitle.data
		route.author=form.author.data
		route.description=form.description.data
		db.session.commit()
		return redirect(url_for('index'))
	elif request.method == 'GET':
		form.rTitle.data = route.rTitle
	
	return render_template('update.html', title='Update your routine', form=form)

@app.route('/delete/<idNum>')
def delete(idNum):
	route= Routine.query.get(idNum)
	db.session.delete(route)
	db.session.commit()
	return redirect(url_for('index'))