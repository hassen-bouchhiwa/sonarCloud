from flask import Flask, request, render_template
import os
app = Flask(__name__)  
 
@app.route('/', methods =["GET", "POST"])

def nslookup():
    if request.method == "POST":
       website = request.form.get("website")
       cmd = "nslookup "+ website
       result = os.popen(cmd).read()
       result = result.replace('\n', '<br />')
       return result
    return render_template("form.html")
 
if __name__=='__main__':
   app.run(host='0.0.0.0', port=5001)
