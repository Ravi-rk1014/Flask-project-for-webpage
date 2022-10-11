from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/data')
def homepage():
    return render_template('data.html')

@app.route("/success", methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        n = request.form.get('name')
        p = request.form.get('phone')
        e = request.form.get('email')
        
        return  render_template('success.html',name=n,phone=p,email=e)

if __name__ == "__main__":
    app.run(debug=True)