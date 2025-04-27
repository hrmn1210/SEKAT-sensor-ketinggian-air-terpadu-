from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

# Simulasi pembacaan sensor
def read_sensor():
    # Untuk simulasi, kita generate angka tinggi air random (cm)
    tinggi_air = random.uniform(10.0, 200.0)  # tinggi antara 10cm sampai 200cm
    status = "Normal"
    if tinggi_air > 150:
        status = "Bahaya"
    elif tinggi_air > 100:
        status = "Waspada"
    return {
        "tinggi_air": round(tinggi_air, 2),
        "status": status,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/sensor')
def api_sensor():
    data = read_sensor()
    return jsonify(data)

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')

@app.route('/cctv')
def cctv():
    return render_template('cctv.html')

@app.route('/cctv1')
def cctv1():
    return render_template('cctv_sungaikapuas.html')

@app.route('/cctv2')
def cctv2():
    return render_template('cctv2.html')

@app.route('/status_banjir')
def statusbanjir():
    return render_template('status_banjir.html')


if __name__ == '__main__':
    app.run(debug=True)
