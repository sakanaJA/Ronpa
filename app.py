from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reply", methods=["POST"])
def reply():
    user_message = request.form["message"]
    bot_message = refute(user_message)
    return bot_message

def refute(message):
    # ここで論破のロジックを実装します。
    # 今回はシンプルな例として、反対の意見を返すようにします。
    if "好き" in message:
        return "なぜ好きだと思うの？"
    elif "嫌い" in message:
        return "なぜ嫌いだと思うの？"
    else:
        return "それにはどのような根拠がありますか？"

if __name__ == "__main__":
    app.run()
