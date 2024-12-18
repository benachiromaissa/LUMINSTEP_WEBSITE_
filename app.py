from flask import Flask, render_template , request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLAlchemy to use SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a contact
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.Text)


# Create database tables if they don't exist
with app.app_context():
    db.create_all()

#index page
@app.route('/')
def index():
    return render_template('index.html')

#about us page
@app.route('/about')
def about():
    return render_template('about.html')

#contact page
@app.route('/contact' ,methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        message = None
        # Add a new contact to the database
        contact = Contact()
        contact.name = request.form['name']
        contact.email = request.form['email']
        contact.subject = request.form['subject']
        contact.message = request.form['message']
        
        try:

            db.session.add(contact)
            db.session.commit()
            message = 'Your email has been sent successfully , you should wait for our reply soon!'
            
        except Exception as ex:

            print(ex)

            message = 'Something went wrong , try again later !'

        return render_template('contact.html' , message = message)
        
    return render_template('contact.html')


#team page
@app.route('/team')
def team():
    return render_template('team.html')


#service page
@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')



if __name__ == '__main__':
    app.run(debug=True)
