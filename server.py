from flask import Flask,render_template,request,url_for,redirect
import csv
app = Flask(__name__)

@app.route('/<string:username>')
def index(username):
    return render_template(username)

# def write_to_file(data):
#     with open('database.txt' ,mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n{email},{subject},{message}')
def write_to_csvfile(data):
    with open('database.csv',mode='a',newline="")as csvfile:
        email=data['email']
        subject=data["subject"]
        message=data["message"]
        ffile= csv.writer(csvfile,delimiter=",",quotechar="|",quoting=csv.QUOTE_MINIMAL)
        ffile.writerow([email,subject,message])   


@app.route('/submit', methods=['POST', 'GET'])
def submit1():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csvfile(data)
        return redirect("./thankyou.html")
    else:
        return "You have done something wrong TRY AGAIN"


# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')