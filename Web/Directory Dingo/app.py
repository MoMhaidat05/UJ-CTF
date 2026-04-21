from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1/dig')
def dig():
    file = request.args.get('file')
    if not file:
        return "Missing 'file' parameter", 400

    file_path = os.path.join("public_bones", file)
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return "Bone not found!", 404
    except Exception:
        return "An error occurred excavating the bone.", 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', '5000'))
    app.run(host='0.0.0.0', port=port, debug=False)