
from flask import Flask, render_template, request, session, Request, flash, redirect, url_for
from baldes import Balde3, Balde4

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='dev',
)


@app.route('/', methods=['POST', 'GET'])
def index():
    
    b1 = Balde4()
    b2 = Balde3()      

    if request.method == 'POST':
        estados = []
        estados += session.pop('estados', [])
        
        operacao = request.form.get('operacao')

        b1_quantidade = request.form.get('b1_quantidade')
        b2_quantidade = request.form.get('b2_quantidade')
        
        b1.quantidade = float(b1_quantidade)
        b2.quantidade = float(b2_quantidade)

        if operacao is not None:
            if 'encher_b1' == operacao:                
                b1.encher()
                estados.append('Encheu Balde 1')
            elif 'encher_b2' == operacao:
                b2.encher()
                estados.append('Encheu Balde 2')
            elif 'esvaziar_b1' == operacao:
                b1.esvaziar()
                estados.append('Esvaziou Balde 1')
            elif 'esvaziar_b2' == operacao:
                b2.esvaziar()
                estados.append('Esvaziou Balde 2')
            elif 'b1_to_b2' == operacao:
                try:
                    b2.receber_conteudo(b1)
                    estados.append('Passou o conteúdo do balde 1 para o balde 2')
                except Exception as e:
                    flash(str(e))
            elif 'b2_to_b1' == operacao:
                try:
                    b1.receber_conteudo(b2)
                    estados.append('Passou o conteúdo do balde 2 para o balde 1')
                except Exception as e:
                    flash(str(e))
            elif 'reset' == operacao:
                session.pop('estados', None)
                return redirect(url_for('index'))
        
        session['estados'] = estados

    baldes = {
        'b1': b1,
        'b2': b2,
    }  
        
    return render_template('index.html', baldes=baldes)


if __name__ == "__main__":
    app.run( debug=True, port='5000')