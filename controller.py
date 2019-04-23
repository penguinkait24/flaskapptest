from model import SimpleForm
from flask import Flask, render_template, request
from compute import plot

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm(request.form)
    if request.method == 'POST':
        result = plot(form.gender.data, form.ethnicity.data)
    else:
        result = None
    print (form, dir(form))
    for f in form:
        print (f.id)
        print (f.name)
        print (f.label)
    return render_template("view.html", form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)

