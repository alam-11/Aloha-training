from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/')
def upload_file():
    return render_template('file_upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
    return redirect(url_for('success'))


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
