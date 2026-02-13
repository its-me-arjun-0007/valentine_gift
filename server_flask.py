from flask import Flask, render_template

# Point Flask to current folder for templates and static
app = Flask(__name__, template_folder='.', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    print("❤️  Starting Flask Application...")
    # Host='0.0.0.0' allows viewing from other devices on the same WiFi
    app.run(host='0.0.0.0', port=5000, debug=True)

