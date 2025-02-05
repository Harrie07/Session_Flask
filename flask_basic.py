from flask import Flask, render_template

app = Flask(__name__)

# Homepage Route
@app.route('/')
def home():
    return render_template('newindex.html')

# Add Note Page Route
@app.route('/add')
def add_note():
    return render_template('add_note.html')

if __name__ == "__main__":
    app.run(debug=True)
