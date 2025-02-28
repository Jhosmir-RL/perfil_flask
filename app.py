from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', title='Equisd')

# Servir archivos estáticos desde la carpeta 'static'
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.root_path, filename)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
