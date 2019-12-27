from flask import Flask, render_template, request

app = Flask(__name__)

# 기본 페이지
@app.route("/")
def index():
    return "index page"

# /~~ => 특정 페이지
@app.route("/join")
def join():
    # return "joinsss page<hr/> <hr/>"
    return render_template('join.html')

if __name__ == '__main__':
    # app.run() # 껏다 켯다 해야함, 배포할 때는 이걸로
    app.run(debug=True) # 바뀌면 알아서 리부트, 개발할 때만 써라
                        # Detected change in '경로...~.py', reloading