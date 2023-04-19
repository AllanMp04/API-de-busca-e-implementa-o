from flask import Flask, jsonify, request

app = Flask(__name__)

Musicas = [
    {
      'id':1,
      'títulos': 'Outra vida - Armandinho Acústico',
      'Cantor': 'Armandinho'
    },
    {
      'id':2,
      'títulos': 'Seja Para MiM - Ao vivo em Sp',
      'Cantor': 'Maneva'
    },
    {
      'id':3,
      'títulos': 'Anjo do céu - Transe Acústico',
      'Cantor': 'Maskavo'
    },
]

#consultar(todos)
@app.route ('/Musicas',methods=['GET'])
def obter_Musicas():
    return jsonify(Musicas)
#consultar(id)
@app.route('/Musicas/<int:id>',methods=['Get'])
def obter_Musicas_por_id(id):
    for Musicas in Musicas:
       if Musicas.get('id') == id:
          return jsonify(Musicas)
#Editar
@app.route('/Musicas/<int:id>',methods=['PUTS'])
def editar_Musicas_por_id(id):
    Musicas_alterado = request.get_jason()
    for indice,Musicas in enumerate(Musicas):
        if Musicas.get('id') == id:
            Musicas[indice].update(Musicas_alterado)
            return jsonify(Musicas[indice])
#criar
@app.route('/Musicas',methods=['POST'])
def incluir_novo_Musicas():
    novo_Musicas = request.get_json()
    Musicas.append(novo_Musicas) 

    return jsonify(novo_Musicas)    
#Excluir
@app.route('/Musicas/<int:id>',methods=['DELETE'])
def excluir_Musicas(id):
    for indice, Musicas in enumerate(Musicas):
        if Musicas.get('id') == id:
            del Musicas[indice]
                       
    return jsonify(Musicas)
                                           
app.run(port=500,host='localhost',debug=True)