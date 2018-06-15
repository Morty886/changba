from flask import Flask,render_template,request
from modu import get_mp3
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('tijiao.html')

@app.route('/changba',methods=['POST','GET'])
def changba():
    get_url = request.form.get('name')
    print('前台传入参数：',get_url)
    a = get_mp3.new_url(get_url)
    return render_template('a.html',url = a,name = 'test1')



if __name__ == '__main__':
    app.run()
