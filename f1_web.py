from flask import Flask, render_template, request, redirect

import cx_Oracle as oci

#                   아이디/암호@서버주소:포트번호/SID
conn = oci.connect("admin/1234@192.168.99.100:32764/xe", encoding="utf-8")
cursor = conn.cursor()
print(conn)


app = Flask(__name__)

# 기본 페이지
@app.route("/", methods = ['GET'])
def index():
    sql = "SELECT * FROM MEMBER"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(type(data))
    print(data)

    sum = 0
    for tmp in data:
        print(tmp[3])
        sum += tmp[3]
    print(sum)
    
    return render_template('list.html', list = data)
    # return render_template('index.html')

@app.route("/", methods = ['POST'])
def index_post():
    return redirect('/join')

# /~~ => 특정 페이지
@app.route("/join", methods = ['GET'])
def join():
    # return "joinsss page<hr/> <hr/>"
    return render_template('join.html')

# POST에서는 render 하지마라!!
# 페이지 넘어가는 사이에 잠깐 시간버는 것이라 생각.
@app.route("/join", methods = ['POST'])
def join_post():
    a = request.form['id']
    b = request.form['pw']
    c = request.form['name']
    d = request.form['age']

    # print("{}:{}:{}:{}".format(a,b,c,d))

    # 오라클 DB접속
    # 추가하는 SQL문 작성 => INSERT, SELECT, UPDATE, DELETE
    # SQL문 수행
    sql = "INSERT INTO MEMBER VALUES(:id, :pw, :na, :ag, SYSDATE)"
    cursor.execute(sql, id=a, pw=b, na=c, ag=d)
    conn.commit()

    # 크롬에서 입력한 것처럼 동작 => 000.0.0.0/
    return redirect('/')

@app.route("/login", methods = ['GET'])
def login():
    return render_template('login.html')

@app.route("/login", methods = ['POST'])
def login_post():
    return redirect('/')

if __name__ == '__main__':
    # app.run() # 껏다 켯다 해야함, 배포할 때는 이걸로
    app.run(debug=True) # 바뀌면 알아서 리부트, 개발할 때만 써라
                        # Detected change in '경로...~.py', reloading