from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
from flask import Flask, jsonify, request, abort
from get_relevant_chunk import get_relevant_chunk

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("savasy/bert-base-turkish-squad")
model = AutoModelForQuestionAnswering.from_pretrained("savasy/bert-base-turkish-squad")
nlp=pipeline("question-answering", model=model, tokenizer=tokenizer)


@app.route('/question', methods=['POST'])
def question():
    data = request.get_json()
    if 'question' in data : 
        ctx = get_relevant_chunk(data['question'])
        print("ctx=>\n", ctx, "\n")
        if ctx :
            res = nlp(data['question'], ctx)
        else :
            res = {"answer": "Doküman bu bilgiyi içermiyor.", "end": 0, "score": 0, "end": 0}
        return jsonify(res)
    else :
        return abort(400)
    
@app.route('/questionWithContext', methods=['POST'])
def questionWithContext() :
    data = request.get_json()
    if 'question' in data and 'context' in data: 
            res = nlp(data['question'], data['context'])
            return jsonify(res)
    else :
        return abort(400)
    
if __name__ == '__main__' : 
    app.run(host='0.0.0.0', port='5002')
