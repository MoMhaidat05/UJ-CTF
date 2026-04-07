import base64
import json
import os
from flask import Flask, render_template, request

app = Flask(__name__)

def b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')

def b64url_decode(data: str) -> bytes:
    padding = '=' * (4 - (len(data) % 4))
    return base64.urlsafe_b64decode(data + padding)

@app.route('/')
def index():
    header = {"alg": "HS256", "typ": "JWT"}
    payload = {"user": "raccoon_fan", "role": "guest"}
    
    h_b64 = b64url_encode(json.dumps(header).encode('utf-8'))
    p_b64 = b64url_encode(json.dumps(payload).encode('utf-8'))
    s_b64 = b64url_encode(b"fake_signature_bytes_for_guest_pass")
    
    token = f"{h_b64}.{p_b64}.{s_b64}"
    return render_template('index.html', token=token)

@app.route('/verify', methods=['POST'])
def verify():
    token = request.form.get('token', '').strip()
    parts = token.split('.')
    
    if len(parts) < 2 or len(parts) > 3:
        return "<h3 style='color:red;'>Invalid token format. A JWT must have at least a Header and a Payload separated by a dot.</h3>"
        
    try:
        header_json = b64url_decode(parts[0]).decode('utf-8')
        payload_json = b64url_decode(parts[1]).decode('utf-8')
        header = json.loads(header_json)
        payload = json.loads(payload_json)
    except Exception as e:
        return f"<h3 style='color:red;'>Could not decode base64url or parse JSON: {str(e)}</h3>"

    role = payload.get("role", "")
    alg = header.get("alg", "").lower()
    signature = parts[2] if len(parts) == 3 else ""

    if role == "vip":
        if alg == "none" and signature == "":
            try:
                flag_path = os.path.join(os.path.dirname(__file__), 'flag.txt')
                with open(flag_path, 'r') as f:
                    flag = f.read().strip()
                return f"""
                <body style="background-color:#111; color:#39ff14; font-family:monospace; text-align:center; padding-top: 50px;">
                    <h1 style='color:#b026ff; text-shadow:0 0 10px #b026ff;'>🦝 Welcome to the VIP Lounge! 🦝</h1>
                    <h2>Access Granted. Here is your flag:</h2>
                    <h3 style="background:#222; padding:20px; border:2px solid #39ff14; display:inline-block;">{flag}</h3>
                </body>
                """
            except Exception as e:
                return "<h3 style='color:red;'>Flag file missing on server! Contact admin.</h3>"
        else:
            return """
            <body style="background-color:#111; font-family:monospace; text-align:center; padding-top: 50px;">
                <h3 style="color:red; text-shadow:0 0 5px red;">Invalid Signature! The Raccoon King's secret key is required... unless there's a way to tell the server to SKIP the algorithm check entirely? 🦝🔍</h3>
            </body>
            """
    
    return """
    <body style="background-color:#111; color:#fff; font-family:monospace; text-align:center; padding-top: 50px;">
        <h3 style="color:#b026ff;">Access Denied. Guests are not allowed in the VIP Lounge.</h3>
    </body>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)