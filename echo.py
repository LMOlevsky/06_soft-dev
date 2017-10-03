from flask import Flask, render_template, request

form_site = Flask(__name__)

@form_site.route("/", methods=['POST', 'GET'])
def root():
    userInp = "Stranger"
    if request.method == "POST":
        userInp = request.form['data']
    return render_template("temp.html", user=userInp, form_type=request.method)

@form_site.route("/test", methods=['POST', 'GET'])
def tester():
    ret_str = ""
    ret_str +=  str(request.method) + '\n'
    ret_str += str(request.form)
    return ret_str + '\n' + render_template("temp.html")

    
if __name__ == '__main__':
    form_site.debug = True
    form_site.run()
