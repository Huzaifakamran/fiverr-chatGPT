import openai
import gunicorn
from flask import Flask, request,jsonify

openai.api_key = "API-Key"
app = Flask(__name__)



@app.route('/webhook',methods = ['GET','POST'])
def webhook():

    data = request.get_json(silent=True)
    if data['queryResult']['intent']['displayName'] == 'Default Fallback Intent':
        question = data['queryResult']['queryText']
        print(question)
        res = chatGPT(question)
        print(res)
        reply = {
            "fulfillmentText": res,
        }
        return jsonify(reply)

def chatGPT(question):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=question,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    res = response['choices'][0]['text']
    # print(res)
    return res



if __name__ == '__main__':
    app.run(debug=True)