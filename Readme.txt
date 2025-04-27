============================================================
🌊 SEKAT (Sensor Ketinggian Air Terpadu)
============================================================

📜 Deskripsi
-------------
Proyek ini adalah sistem dashboard monitoring banjir berbasis web untuk wilayah Pontianak.
Sistem menampilkan:
- Realtime status tinggi air dari beberapa titik sensor.
- Grafik perubahan tinggi air (dengan simulasi data random).
- Tampilan live feed CCTV di beberapa lokasi strategis.
- Notifikasi otomatis saat status banjir mencapai level "Bahaya".
- Countdown waktu update data berikutnya.

📍 Titik Pemantauan
-------------------
1. Sungai Kapuas
2. Parit Mayor
3. Jalan Ahmad Yani
4. Taman Alun Kapuas

📷 Fitur Live CCTV
-------------------
- Menampilkan snapshot atau stream dari masing-masing lokasi.
- Ukuran CCTV disamakan untuk tampilan yang rapi.
- Responsif di semua perangkat (mobile & desktop).

🚀 Fitur Tambahan
------------------
- Warna grafik berubah otomatis sesuai status air: Normal (Biru), Waspada (Kuning), Bahaya (Merah).
- Garis batas indikator Waspada (100 cm) dan Bahaya (150 cm) di grafik.
- Animasi toast dan sirine bunyi otomatis jika terjadi status "Bahaya".
- Countdown real-time untuk update data.
- Badges status dengan warna otomatis.

🛠 Teknologi yang Digunakan
----------------------------
- HTML5, CSS3, JavaScript (vanilla)
- Bootstrap 5
- Chart.js (untuk grafik)
- Leaflet.js (untuk peta, opsional)
- Bootstrap Icons
- Animations (basic CSS keyframes)

📦 Cara Menjalankan
--------------------
1. Clone repository ini ke lokal:
   > git clone [https://github.com/hrmn1210/SEKAT-sensor-ketinggian-air-terpadu-.git]

2. Buka file `index.html` menggunakan browser modern (Chrome, Edge, Firefox).

3. Semua simulasi sudah berjalan otomatis (simulasi sensor, update grafik, notifikasi).

📋 Catatan
-----------
- CCTV yang tampil di sistem ini adalah contoh link/snapshot dari server.
- Untuk penggunaan production, pastikan link CCTV sudah stabil dan aman.
- Jika ingin integrasi data sensor real-time dari IoT/Database, sesuaikan pada bagian `readSensor()`.

🙌 Kontribusi
--------------
Pull request sangat diterima! 
Jika ada ide, fitur baru, atau perbaikan bug, jangan ragu untuk kirimkan.

📬 Kontak
----------
Developer: [Herman Firmansyah]
Email    : [15220648@bsi.ac.id]
GitHub   : [hrmn1210]

============================================================
Dibuat dengan ❤️ untuk masyarakat Pontianak dan Indonesia.
============================================================
