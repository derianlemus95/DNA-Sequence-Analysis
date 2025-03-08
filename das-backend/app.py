from flask import Flask, request, jsonify, Response
from flask_cors import CORS
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return 'Hello World!'

#return status 200 if ok and returning data to client
#return status 400 if error with data recived
#return status 500 if error on server side
@app.route('/calculation/dna-seq', methods=['POST'])
def dna_seq():
    dna_seq = request.json.get('dna_seq')
    data = "e"
    #if error with dna sequence return 400
    if  (dna_seq.isalpha() == False) or len(dna_seq)==0:
        return Response('Invalid DNA Sequence', status=400)
    #if no error, calc gc content as percent
    gc_calc = gc_content(dna_seq)
    return jsonify(gc_calc), 200


def gc_content(dna_seq):
    #GC Content = 100% * COUNT(G+C) / COUNT(A+T+G+C)
    gc_count = dna_seq.count("G") + dna_seq.count("C")
    atgc_count = dna_seq.count("A") + dna_seq.count("T") + gc_count
    gc_percent = 100 * gc_count / atgc_count
    return gc_percent

@app.route('/calculation/motif', methods=['POST'])
def motif():
    motif = request.json.get('motif')
    dna_seq = request.json.get('dna_seq')
    if (motif.isalpha() == False) or len(motif)==0 :
        return Response('Invalid motif', status=400)

    print(motif)
    #return true if substring found else false
    if motif not in dna_seq:
        return Response("DNA sequence not found", status=404)
    return Response("DNA sequence found", status=200)


if __name__ == '__main__':
    app.run(debug=True)

