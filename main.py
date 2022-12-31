from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017')
db = client.mydatabase

@app.route('/edit/<document_id>')
def edit_document(document_id):
    collection = db.mycollection
    document = collection.find_one({'_id': document_id})
    return render_template('edit_document.html', document=document)

@app.route('/update', methods=['POST'])
def update_document():
    collection = db.mycollection
    document_id = request.form['document_id']
    updated_document = {
        'field1': request.form['field1'],
        'field2': request.form['field2'],
        'field3': request.form['field3']
    }
    collection.update_one({'_id': document_id}, {'$set': updated_document})
    return redirect('/')

if __name__ == '__main__':
    app.run()
