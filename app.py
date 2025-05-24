# app.py
from flask import Flask, render_template, request, redirect, url_for
import data_store

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_number', methods=['GET', 'POST'])
def add_number():
    if request.method == 'POST':
        num = request.form.get('number')
        if num:
            data_store.add_number_to_list(int(num))
        return redirect(url_for('view_data'))
    return render_template('add_number.html')

@app.route('/add_hash', methods=['GET', 'POST'])
def add_hash():
    if request.method == 'POST':
        key = request.form.get('key')
        value = request.form.get('value')
        if key and value:
            data_store.add_to_hash_table(key, value)
        return redirect(url_for('view_data'))
    return render_template('add_hash.html')

@app.route('/search_number', methods=['GET', 'POST'])
def search_number():
    result = None
    sorted_list = []
    if request.method == 'POST':
        num = request.form.get('number')
        if num:
            result, sorted_list = data_store.search_in_list(int(num))
    return render_template('search_number.html', result=result, sorted_list=sorted_list)

@app.route('/edit_hash', methods=['GET', 'POST'])
def edit_hash():
    message = None
    if request.method == 'POST':
        key = request.form.get('key')
        value = request.form.get('new_value')
        if key and value:
            success = data_store.edit_hash_table(key, value)
            message = "Updated" if success else "Key not found"
    return render_template('edit_hash.html', message=message)

@app.route('/delete_number', methods=['GET', 'POST'])
def delete_number():
    if request.method == 'POST':
        num = request.form.get('number')
        if num:
            data_store.delete_from_list(int(num))
        return redirect(url_for('view_data'))
    return render_template('delete_number.html')

@app.route('/delete_hash', methods=['GET', 'POST'])
def delete_hash():
    if request.method == 'POST':
        key = request.form.get('key')
        if key:
            data_store.delete_from_hash_table(key)
        return redirect(url_for('view_data'))
    return render_template('delete_hash.html')

@app.route('/view_data')
def view_data():
    return render_template('view_data.html', numbers=data_store.numbers_list, hash_table=data_store.hash_table)

@app.route('/sort_merge')
def sort_merge():
    sorted_data = data_store.merge_sort(data_store.numbers_list.copy())
    return render_template('sort_result.html', method="Merge Sort", sorted_data=sorted_data)

@app.route('/sort_quick')
def sort_quick():
    sorted_data = data_store.quick_sort(data_store.numbers_list.copy())
    return render_template('sort_result.html', method="Quick Sort", sorted_data=sorted_data)

if __name__ == '__main__':
    app.run(debug=True)
