from flask import Flask, render_template, request
from projem.crew import crew

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_crew():
    topic = request.form['topic']
    result = crew.kickoff(inputs={'topic': topic})
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
