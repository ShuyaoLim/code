from  flask import Flask
import time
app=Flask(__name__)

@app.route('/yuyuan')
def index_yuyuan():
    time.sleep(2)
    return 'hello yuyuan'
@app.route('/bobo')
def index_bobo():
    time.sleep(2)
    return 'hello bobo'
@app.route('/yao')
def index_yao():
    time.sleep(2)
    return 'hello yao'

if __name__ == '__main__':
    app.run(threaded=True)

