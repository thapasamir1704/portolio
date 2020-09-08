
from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt',mode='a') as dbase:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		file=dbase.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv', mode='a') as dbase2:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		csv_written=csv.writer(dbase2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_written.writerow([email,subject,message])

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
	 if request.method=='POST':
	 	try:
	 		data=request.form_to_dict()
	 		write_to_csv(data)
	 		return redirect('/thankyou.html')
	 	except:
	 		return 'did not save to database'
	 else:
	 	return 'something went wrong'
	 	