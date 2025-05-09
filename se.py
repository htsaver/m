from flask import Flask
import pyngrok
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Welcome to My Web Server</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <h1>Hello from my Python Web Server!</h1>
        <p>This server is accessible from the internet via ngrok.</p>
    </body>
    </html>
    '''

def start_ngrok():
    ngrok = pyngrok.ngrok
    tunnel = ngrok.connect(80, bind_tls=True)  # Changed to port 80
    print(f'Public URL: {tunnel.public_url}')

if __name__ == '__main__':
    # Start ngrok in a separate thread
    threading.Thread(target=start_ngrok, daemon=True).start()
    # Run Flask server on port 80
    app.run(host='0.0.0.0', port=80)