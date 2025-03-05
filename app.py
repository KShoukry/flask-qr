from flask import Flask, request, send_file, render_template_string
import qrcode
import io

app = Flask(__name__)

# Simple HTML template with a form to input data
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
</body>
</html>
'''


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['data']
        # Generate the QR code image
        img = qrcode.make(data)
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        # Automatically download the image by sending it as an attachment
        return send_file(buf, mimetype='image/png', as_attachment=True, download_name='qrcode.png')
    return render_template_string(html)


if __name__ == '__main__':
    # Use the dynamic port provided by deployment services like Render
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)