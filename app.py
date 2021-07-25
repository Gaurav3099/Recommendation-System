from flask import *
import numpy as np
import recsys

app = Flask(__name__)

@app.route('/')  
def customer():  
   return render_template('home.html')  
  
@app.route('/success',methods = ['POST', 'GET'])  
def print_data():
	if request.method == 'POST':

		result = request.form['search']
		m,y=recsys.rec_movie(result)
		if m == "Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies":
			m="e"
			y="e"
			return render_template('page2.html', movie=m, year=y)
		else:

			# m.insert(0, "MOVIES")
			# y.insert(0, "YEAR")
			# return m
			res = "Movies similar to "+result
			return render_template('page2.html', movie=m, year=y, input=res)
		

if __name__ == '__main__':  
   app.run(debug = True)