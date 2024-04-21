from flask import Flask, render_template, request, jsonify


app = Flask(__name__, static_folder='static')

def cautare_cuvant(fisier, cuvant):
    try:
        with open(fisier,  'r' ,  encoding='utf-8') as f:
            for linie in f:
                if cuvant.lower() in linie.rstrip().lower():
                    return True  
            return False  
    except FileNotFoundError:
        print("Fișierul nu a fost găsit.")
        return 'error'

@app.route('/search/<string:s>', methods=['GET'])
def find_domain_info(s):
    try:
        found = False
        s = s.lower()
        rezultat = cautare_cuvant('database.txt', s)
        if rezultat == 'error':
            return jsonify({'error': 'ERROR 4523'})
        elif rezultat:
            found = True
        return jsonify({'success': found})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/add/<string:s>', methods=['GET'])
def add(s):
    try:
        rezultat = cautare_cuvant('database.txt', s)
        if rezultat == 'error':
            return jsonify({'error': 'ERROR 4523'})
        elif rezultat:
            return jsonify({'success': False, 'message':'Alerday exist'})
        else:
            with open('database.txt', 'a', encoding='utf-8') as f:
                f.write(f'{s.lower()}\n')
            return jsonify({'succes': True, 'message':'successfully added'})
    except Exception as e:
        return jsonify({'error': str(e)})
 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1111)
