from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Tebrikler! Vercel Üzerinde Python Sitem Çalışıyor!</h1>"

if __name__ == '__main__':
    app.run()
  
