from flask import Flask, request, render_template
import os
app = Flask(__name__)  
 
@app.route('/', methods =["GET", "POST"])


def nslookup():
    special = "!@#$%^;:|&*()-+?_=,<>/"
    if request.method == "POST":
       website = request.form.get("website")
       if any(c in special for c in website):
            return "Yabta Ya gholi"
       else:     
            cmd = "nslookup "+ website
            result = os.popen(cmd).read()
            result = result.replace('\n', '<br />')
            return result
    return render_template("form.html")
 
if __name__=='__main__':
   app.run()
