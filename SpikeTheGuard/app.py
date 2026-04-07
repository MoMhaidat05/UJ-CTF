from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    if request.method == 'POST':
        ip = request.form.get('ip', '')
        
        # The Filter
        if 'cat' in ip.lower():
            output = '<h3 class="error-bark">BARK! BARK! Spike caught Tom! 😾🐶<br>No cats allowed in this yard!</h3>'
        else:
            # The Exploit (Vulnerable to OS Command Injection)
            command = f"ping {ip}"
            try:
                result = subprocess.getoutput(command)
                output = f"<pre><code>{result}</code></pre>"
            except Exception as e:
                output = f"<pre><code>Error executing command.</code></pre>"
                
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
