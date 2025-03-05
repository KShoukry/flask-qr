from flask import Flask, request, send_file, render_template_string
import qrcode
import io

app = Flask(__name__)

# A simple HTML template with a form
html = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>QR Code Generator</title>
</head>
<body>
    <h1>Generate a QR Code</h1>
    <form method="post">
        <input type="text" name="data" placeholder="Enter text or URL" required>
        <input type="submit" value="Generate">
    </form>
    {% if qr_code %}
    <h2>Your QR Code:</h2>
    <img src="{{ qr_code }}" alt="QR Code">
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_img = None
    if request.method == 'POST':
        data = request.form['data']
        # Generate QR code
        img = qrcode.make(data)
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        # Convert to base64 for displaying in HTML
        import base64
        img_b64 = base64.b64encode(buf.getvalue()).decode('ascii')
        qr_code_img = f"data:image/png;base64,{img_b64}"
    return render_template_string(html, qr_code=qr_code_img)


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)