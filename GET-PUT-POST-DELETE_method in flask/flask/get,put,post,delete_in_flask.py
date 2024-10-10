from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Sample data for notes
notes = [
    {"id": 1, "title": "Meeting notes", "content": "Discuss project timelines."},
    {"id": 2, "title": "Grocery list", "content": "Milk, eggs, bread."},
]

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    new_note = {
        "id": len(notes) + 1,
        "title": request.form['title'],
        "content": request.form['content']
    }
    notes.append(new_note)
    return redirect(url_for('index'))

@app.route('/edit_note/<int:note_id>')
def edit_note(note_id):
    note = next((n for n in notes if n["id"] == note_id), None)
    if note:
        return render_template('edit.html', note=note)
    else:
        return "Note not found"

@app.route('/update_note/<int:note_id>', methods=['POST'])
def update_note(note_id):
    note = next((n for n in notes if n["id"] == note_id), None)
    if note:
        note["title"] = request.form['title']
        note["content"] = request.form['content']
        return redirect(url_for('index'))
    else:
        return "Note not found"

@app.route('/delete_note/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    global notes
    notes = [n for n in notes if n["id"] != note_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)