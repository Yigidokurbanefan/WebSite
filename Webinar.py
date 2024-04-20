from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p><a href = '/abc'>DomDomKursunuDedi</a>"

@app.route("/abc")
def abc():
    return "<h1>Abc</h1> "

bosliste = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
            "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
            "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
            "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır."]

@app.route("/facts")
def liste():
    if len(bosliste) == 0:
        return "<p>Daha Fazla Gerçek Kalmadı.</p>"
    x = random.choice(bosliste)
    bosliste.remove(x)
    return f"<p>{x}</p><a href = '/def'>Gercekler</a>"


@app.route("/def")
def ghi():
    return 0

@app.route("/<yazitura>")
def merhaba():
    a =('yazı',
       'tura')
    b = random.choice(a)
    if set == b:
        return'Doğru Cevap'
    else:
        return 
    return f'<h1{b}</h1>'


if __name__ == "__main__":
    app.run(debug=True)
