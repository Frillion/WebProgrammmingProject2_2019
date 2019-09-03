from flask import Flask,render_template,redirect
from sys import argv

app = Flask(__name__)

hrefs = {
            "href main":"/",
            "href page2":"/pages/2",
            "href page3":"/pages/3"
        }

linktext = {
                "Link1":"Home",
                "Link2":"Page2",
                "Link3":"Page3"
            }

contents = {
                "content":"Hello World",
			    "Link1":linktext["Link1"],
                "Link2":linktext["Link2"],
                "Link3":linktext["Link3"],
			    "href1":hrefs["href main"],
                "href2":hrefs["href page2"],
                "href3":hrefs["href page3"]
			}

pg2contents = {
                "content":"This is page2",
                "Link1":linktext["Link1"],
                "Link2":linktext["Link2"],
                "Link3":linktext["Link3"],
                "href1":hrefs["href main"],
                "href2":hrefs["href page2"],
                "href3":hrefs["href page3"]
               }

pg3contents = {
                "content":"This is page3",
                "Link1":linktext["Link1"],
                "Link2":linktext["Link2"],
                "Link3":linktext["Link3"],
                "href1":hrefs["href main"],
                "href2":hrefs["href page2"],
                "href3":hrefs["href page3"]
               }

@app.route("/")
def index():
    return render_template('head.html', cnt=contents)


@app.route("/pages/<int:pgnumber>", methods=['Get'])
def page(pgnumber):
    if pgnumber == 1:
        return redirect("/")
    elif pgnumber == 2:
        return render_template('head.html', cnt=pg2contents)
    elif pgnumber == 3:
        return render_template('head.html', cnt=pg3contents)

if (__name__) == '__main__':
    app.run(host='0.0.0.0',debug=True, port=argv[1])