from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#Questions HTML

@app.route('/QuestHTML1')
def QuestHTML1():
    return render_template('QuestHTML1.html')

@app.route('/QuestHTML2')
def QuestHTML2():
    return render_template('QuestHTML2.html')

@app.route('/QuestHTML3')
def QuestHTML3():
    return render_template('QuestHTML3.html')

@app.route('/QuestHTML4')
def QuestHTML4():
    return render_template('QuestHTML4.html')

@app.route('/QuestHTML5')
def QuestHTML5():
    return render_template('QuestHTML5.html')

@app.route('/QuestHTML6')
def QuestHTML6():
    return render_template('QuestHTML6.html')

@app.route('/QuestHTML7')
def QuestHTML7():
    return render_template('QuestHTML7.html')

@app.route('/QuestHTML8')
def QuestHTML8():
    return render_template('QuestHTML8.html')

@app.route('/QuestHTML9')
def QuestHTML9():
    return render_template('QuestHTML9.html')

@app.route('/QuestHTML10')
def QuestHTML10():
    return render_template('QuestHTML10.html')

@app.route('/QuestHTML11')
def QuestHTML11():
    return render_template('QuestHTML11.html')

@app.route('/QuestHTML12')
def QuestHTML12():
    return render_template('QuestHTML12.html')

@app.route('/QuestHTML13')
def QuestHTML13():
    return render_template('QuestHTML13.html')

@app.route('/QuestHTML14')
def QuestHTML14():
    return render_template('QuestHTML14.html')

@app.route('/QuestHTML15')
def QuestHTML15():
    return render_template('QuestHTML15.html')

#Questions CSS

@app.route('/QuestCSS1')
def QuestCSS1():
    return render_template('QuestCSS1.html')

@app.route('/QuestQuestCSS2')
def QuestCSS2():
    return render_template('QuestCSS2.html')

@app.route('/QuestCSS3')
def QuestCSS3():
    return render_template('QuestCSS3')

@app.route('/QuestCSS4')
def QuestCSS4():
    return render_template('QuestCSS4.html')

@app.route('/QuestCSS5')
def QuestCSS5():
    return render_template('QuestCSS5.html')

@app.route('/QuestCSS6')
def QuestCSS6():
    return render_template('QuestCSS6.html')

@app.route('/QuestCSS7')
def QuestCSS7():
    return render_template('QuestCSS7.html')

@app.route('/QuestCSS8')
def QuestCSS8():
    return render_template('QuestCSS8.html')

@app.route('/QuestCSS9')
def QuestCSS9():
    return render_template('QuestCSS9.html')

@app.route('/QuestCSS10')
def QuestCSS10():
    return render_template('QuestCSS10.html')

@app.route('/QuestCSS11')
def QuestCSS11():
    return render_template('QuestCSS11.html')

@app.route('/QuestCSS12')
def QuestCSS12():
    return render_template('QuestCSS12.html')

@app.route('/QuestCSS13')
def QuestCSS13():
    return render_template('QuestCSS13.html')

@app.route('/QuestCSS14')
def QuestCSS14():
    return render_template('QuestCSS14.html')

@app.route('/QuestCSS15')
def QuestCSS15():
    return render_template('QuestCSS15.html')

if __name__ == '__main__':
    app.run(debug = True)