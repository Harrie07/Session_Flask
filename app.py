from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session handling

# Homepage Route
@app.route('/')
def home():
    notes = session.get('notes', [])  # Get notes from session
    return render_template('index.html', notes=notes)

# Add Note Page Route
@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        note = request.form['note']
        notes = session.get('notes', [])
        notes.append(note)
        session['notes'] = notes  # Save to session
        return redirect('/')
    return render_template('add_note.html')

@app.route('/save', methods=['POST'])
def save_note():
    note = request.form['note']
    notes = session.get('notes', [])
    notes.append(note)
    session['notes'] = notes
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

