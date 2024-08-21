from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resume')
def resume():
    return send_file('uploads/Rupesh_Panwar.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
