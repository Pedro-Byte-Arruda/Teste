from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#Questions HTML

@app.route('/QuestHTML1')
def home():
    return render_template('QuestHTML1.html')

@app.route('/QuestHTML2')
def home():
    return render_template('QuestHTML2.html')

@app.route('/QuestHTML3')
def home():
    return render_template('QuestHTML3.html')

@app.route('/QuestHTML4')
def home():
    return render_template('QuestHTML4.html')

@app.route('/QuestHTML5')
def home():
    return render_template('QuestHTML5.html')

@app.route('/QuestHTML6')
def home():
    return render_template('QuestHTML6.html')

@app.route('/QuestHTML7')
def home():
    return render_template('QuestHTML7.html')

@app.route('/QuestHTML8')
def home():
    return render_template('QuestHTML8.html')

@app.route('/QuestHTML9')
def home():
    return render_template('QuestHTML9.html')

@app.route('/Quest1')
def home():
    return render_template('Quest1.html')

@app.route('/Quest1')
def home():
    return render_template('Quest1.html')

@app.route('/Quest1')
def home():
    return render_template('Quest1.html')

@app.route('/Quest1')
def home():
    return render_template('Quest1.html')

@app.route('/Quest1')
def home():
    return render_template('Quest1.html')

if __name__ == '__main__':
    app.run(debug = True)