from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap5

from converter.converter import Converter




app = Flask(__name__)
Bootstrap5(app)


@app.route('/', methods=['GET','POST'])
def home():
    print("in home")
    converter.history = ""
    return f"<a href={url_for('demo')}>play<a/>"

@app.route('/demo', methods=['GET','POST'])
def demo():
    # TODO: add function text:
    # "enter text to convert into morse code:\n"
    # f"converted morse code:\n{output}"
    
    print("in demo")
    if request.method == "POST":
        print("post")
        enter = request.form.get('user_input')
        converter.history += enter + "\n" # type: ignore
        converter.history += converter.convert(user_input=enter) + "\n" # type: ignore
        # dk_showmaker.player_input(user_input=enter) # type: ignore
    # result = dk_showmaker.output
    # pwd = dk_showmaker.pwd
    # history = dk_showmaker.history
    # is_winner = str(dk_showmaker._iswinner)
    # player = int(dk_showmaker._current_player) + 1
    return render_template(
        'demo.html',
        # history='history',
        terminal_lines=converter.history,
        
        # terminal_lines=result,
        # pwd=pwd,
        # history=history,
        # is_winner=is_winner,
        # player=player
        )

@app.route('/input-recieve')
def input_receive():
    print("in inputreceive")
    # result = dk_showmaker.output
    # pwd = dk_showmaker.pwd
    # history = dk_showmaker.history
    # is_winner = str(dk_showmaker._iswinner)
    # player = int(dk_showmaker._current_player) + 1
    return render_template(
        'cz_terminal.html',
        # history='history',
        terminal_lines=converter.history,
        
        # terminal_lines=result,
        # pwd=pwd, history=history,
        # is_winner=is_winner,
        # player=player
        ) # cz stands for customized

# def og():
#     while organizer.operate:
#         print('========================================================')
#         user_input = input("enter text to convert into morse code or command below: (!commands for all commands)\n")
#         print("\n")
#         converter.update_configs(configs=organizer.commands(user_input=user_input))
#         if organizer.user_command:
#             continue
#         output = converter.convert(user_input)
#         print(f"converted morse code:\n{output}")
#     print('program ended.')

if __name__ == "__main__":
    converter = Converter()
    
    app.run(debug=True, port=5000)
    