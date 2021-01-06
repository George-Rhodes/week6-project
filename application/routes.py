from flask import Flask, render_template, redirect, url_for, request
from application import app, db
from application.models import Routine, Excer
from application.forms import routeForm, updateForm, orderedForm, excerForm




@app.route('/', methods = ['GET', 'POST'])
def index():
	form = orderedForm()
	if form.orderedWith.data == "id":
		routeList = Routine.query.order_by(Routine.id.desc()).all()	
	else:
		routeList = Routine.query.all()
	return render_template('index.html', routeList = routeList, form=form)




@app.route('/add', methods=['GET', 'POST'])
def add():
	form = routeForm()
	if form.validate_on_submit():
		new_routine= Routine(rTitle=form.rTitle.data, author=form.author.data, description=form.description.data)
		db.session.add(new_routine)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template ('add.html', form=form)



@app.route('/update/<idNum>', methods=['POST', 'GET'])
def update(idNum):
	form = updateForm()
	route= Routine.query.get(idNum)Amanda Kekitinisa
	if form.validate_on_submit():
		route.rTitle=form.rTitle.data
		route.author=form.author.data
		route.description=form.description.data
		db.session.commit()
		return redirect(url_for('index'))
	elif request.method == 'GET':
		form.rTitle.data = route.rTitle
		form.author.data = route.author
		form.description.data = route.description
	
	return render_template('update.html', title='Update your routine', form=form)

@app.route('/delete/<idNum>')
def delete(idNum):
	route= Routine.query.get(idNum)
	db.session.delete(route)
	db.session.commit()
	return redirect(url_for('index'))



@app.route('/routine/<idNum>', methods=['POST', 'GET'])
def routine(idNum):

	return render_template('routine.html', excerList = Excer.query.filter_by(routine_id=idNum).all(), routine = Routine.query.get(idNum))



@app.route('/addexcer/<idNum>', methods=['GET', 'POST'])
def addexcer(idNum):
	form = excerForm()
	if form.validate_on_submit():
		new_excer= Excer(routine_id=idNum, set_name=form.set_name.data, level_num=form.level_num.data,
		 level_type=form.level_type.data, set_length=form.set_length.data, set_type= form.set_type.data)
		db.session.add(new_excer)
		db.session.commit()
		return redirect(url_for('routine', idNum=idNum))
	return render_template ('addexcer.html', form=form, routine = Routine.query.get(idNum))


@app.route('/updateEx/<idNum>', methods=['POST', 'GET'])
def updateEx(idNum):
	form = excerForm()
	ex= Excer.query.get(idNum)
	re_id = ex.routine_id
	if form.validate_on_submit():
		ex.set_name=form.set_name.data
		ex.level_num=form.level_num.data
		ex.level_type=form.level_type.data
		ex.set_length=form.set_length.data
		ex.set_type=form.set_type.data
		db.session.commit()
		return redirect(url_for('routine', idNum=re_id))
	elif request.method == 'GET':
		form.set_name.data = ex.set_name
		form.level_num.data = ex.level_num
		form.level_type.dat = ex.level_type
		form.set_length.data = ex.set_length
		form.set_type.data = ex.set_type
	
	return render_template('updateEx.html', title='Update your excersise', form=form , routine = Routine.query.get(re_id))	

@app.route('/deleteEx/<idNum>')
def deleteEx(idNum):

	ex = Excer.query.get(idNum)
	re_id = ex.routine_id
	db.session.delete(ex)
	db.session.commit()
	return redirect(url_for('routine', idNum=re_id))
