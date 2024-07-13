from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap5

from converter.converter import Converter


app = Flask(__name__)
Bootstrap5(app)

@app.route('/', methods=['GET','POST'])
def home():
    converter.history = ""
    return f"<a href={url_for('demo')}>play<a/>"

@app.route('/demo', methods=['GET','POST'])
def demo():
    if request.method == "POST":
        enter = request.form.get('user_input')
        converter.history += enter + "\n" # type: ignore
        converter.history += converter.convert(user_input=enter) + "\n" # type: ignore
    return render_template(
        'demo.html',
        terminal_lines=converter.history,
        )

@app.route('/input-recieve')
def input_receive():
    return render_template(
        'cz_terminal.html',
        terminal_lines=converter.history,
        ) # cz stands for customized

@app.route('/demo/reset-terminal-history')
def reset_terminal_history():
    converter.history = ""
    return redirect(url_for('demo'))


if __name__ == "__main__":
    converter = Converter()
    app.run(debug=True, port=5000)
    