from flask import Flask, request, redirect, url_for, render_template
import sqlite3

app = Flask(__name__)
app.secret_key = 'bzzcnxfhdghmkxhgfjsfjzdfh'


@app.route('/')
@app.route('/<int:page>', methods=['GET'])
def index(page=0):
	
	per = 20
	start, end = page*per, (page+1)*per

	conn = sqlite3.connect('database.db')
	WRITINGS_TOTAL, = conn.execute('SELECT COUNT(*) FROM writings').fetchone()
	writings = conn.execute('SELECT * FROM writings LIMIT ? OFFSET ?', (per, start))
	
	keys, writings = ('writng_id', 'author', 'writing'), (dict(zip(keys, writing)) for writing in writings)

	parameters = {
            'page': page,
            'writings': writings,
            'has_next': end < WRITINGS_TOTAL,
            }

	return render_template('index.html', **parameters)


@app.route('/del',  methods=['POST'])
def delete_writing():

	conn = sqlite3.connect('database.db')
	conn.execute('DELETE FROM writings WHERE writing_id = ?', [request.form['writing_id']])
	conn.commit()

	return redirect(url_for('index'))


@app.route('/edit_page',  methods=['POST'])
def edit_page():

	conn = sqlite3.connect('database.db')
	values = conn.execute('SELECT * FROM writings WHERE writing_id = ?', [request.form['writing_id']])
	keys = ('writing_id', 'author', 'writing')
	writing = dict(zip(keys,values.fetchone()))

	return render_template('edit.html', **writing)


@app.route('/edit_action',  methods=['POST'])
def edit_action():
 
	conn = sqlite3.connect('database.db')
	conn.execute('UPDATE writings SET  author = ?, writing = ? WHERE writing_id = ?',\
		(request.form['author'], request.form['writing'], request.form['writing_id']))
	conn.commit()

	return redirect(url_for('index'))


@app.route('/add',  methods=['GET','POST'])
def add():

	if request.method == 'GET':
		return render_template('add.html')
	elif request.method == 'POST':
		conn = sqlite3.connect('database.db')
		conn.execute('INSERT INTO  writings (author, writing) VALUES (?,?)', \
			(request.form['author'], request.form['writing']))
		conn.commit()

		return redirect(url_for('index'))

@app.route('/search',  methods=['GET','POST'])
def search():
	if request.method == 'POST':

		writing = request.form['writing'] 
		writing_cap = writing.capitalize()

		conn = sqlite3.connect('database.db')
		cur = conn.cursor()
		writings = cur.execute('SELECT * FROM writings WHERE writing LIKE ? OR writing LIKE ? OR author LIKE ? OR author LIKE ?  ',\
		 ('%' + writing + '%', '%' + writing_cap + '%', '%' + writing + '%', '%' + writing_cap + '%', ))

		keys = ('writng_id', 'author', 'writing')
		
		writings_list = []
		for item in writings:
			writings_list.append(dict(zip(keys, item)))
		
		return render_template('search.html', writings_list  = writings_list)

	elif request.method == 'GET':

		return render_template('search.html')


if __name__ == '__main__':
	app.run()
	