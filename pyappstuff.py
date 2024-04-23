from flask import Flask


app = Flask("pyapp.py")
@app.route('/')
def home():
    return "Hello, World!"
if "pyapp.py" == '__main__':
    app.run(debug=True)
    
python app.py
