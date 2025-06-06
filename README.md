# ⚔️ Async HTTP Flood Tool (Educational Purposes Only)

Sebuah script Python berbasis `async/await` untuk melakukan *stress test* atau *load testing* pada server HTTP menggunakan modul `aiohttp`.

---

## 🚀 Fitur

- ⚡ Asynchronous HTTP flooding dengan `aiohttp`
- 🎭 Random User-Agent untuk setiap request (simulasi trafik nyata)
- 🔁 Loop terus-menerus untuk beban berkelanjutan
- 🎯 Jumlah request & koneksi bersamaan dapat diatur

---

## ⚙️ Instalasi & Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/pangeran-droid/HTTP-Flood-Attack.git
cd HTTP-Flood-Attack
```

> ❗ Pastikan direktori tertulis dengan benar: `HTTP-Flood-Attack` (bukan `Atack`).

---

### 🐧 Linux (Ubuntu/Debian/Arch/Fedora, dll.)

```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install aiohttp
```

---

### 🪟 Windows

1. Unduh Python dari: https://www.python.org/downloads/
2. Centang opsi **"Add Python to PATH"** saat instalasi.
3. Buka Command Prompt (CMD) lalu jalankan:

```bash
pip install aiohttp
```

---

### 🍎 macOS

```bash
brew install python
pip3 install aiohttp
```

---

### 2. Jalankan Script

- Simpan script sebagai `tester.py` (jika belum).
- Jalankan via terminal:

```bash
chmod +x tester.py
./tester.py
```

> ✅ Di Windows, gunakan `python tester.py` saja (tanpa angka 3) jika `python3` tidak dikenali.

---

## ⚠️ DISCLAIMER

**Alat ini dibuat hanya untuk tujuan pembelajaran dan riset.**

### ✅ Diperbolehkan untuk:

- Menguji ketahanan server milik sendiri
- Simulasi beban sebelum server dipublikasikan
- Belajar konsep asynchronous di Python

### ❌ Dilarang keras digunakan untuk:

- Menyerang atau membuat sistem orang lain menjadi down
- Aktivitas ilegal atau yang melanggar hukum

> ⚖️ **Segala bentuk penyalahgunaan alat ini adalah tanggung jawab pengguna sepenuhnya. Developer tidak bertanggung jawab atas tindakan ilegal yang dilakukan dengan script ini.**
