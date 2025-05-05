from tkinter import *
from tkinter import messagebox
from pyswip import Prolog

# Pertanyaan sesuai ID Prolog
pertanyaan_dict = {
    "nyaman_keramaian": "Apakah kamu merasa nyaman di keramaian atau bertemu orang baru?",
    "suka_merencanakan": "Apakah kamu suka merencanakan sesuatu jauh-jauh hari?",
    "cemas": "Apakah kamu cenderung merasa cemas atau khawatir tanpa ada alasan yang jelas?",
    "hal_baru": "Apakah kamu senang mencoba hal-hal baru yang belum pernah kamu lakukan sebelumnya?",
    "paham_perasaan": "Apakah kamu mudah memahami perasaan orang lain tanpa harus dijelaskan?",
    "sendiri": "Apakah kamu lebih suka bekerja sendiri daripada dalam kelompok?",
    "tak_sesuai_rencana": "Apakah kamu merasa sangat terganggu jika sesuatu berjalan tidak sesuai dengan rencana?",
    "bosan": "Apakah kamu sering merasa bosan jika rutinitas tidak berubah?",
    "hindari_konflik": "Apakah kamu sering menghindari konflik atau konfrontasi langsung?",
    "sulit_percaya_orang": "Apakah kamu merasa sulit mempercayai orang lain pada awal perkenalan?"
}

#Deskripsi Tipe Kepribadian
deskripsi_kepribadian = {
    "Singa": """🦁 Sang Pemimpin (Singa)
Dominan, percaya diri, fokus pada tujuan. 
Kekuatan: Tegas, ambisius. 
Tantangan: Keras kepala, otoriter.""",

    "Lumba-lumba": """🐬 Sang Penjelajah (Lumba-lumba)
Kreatif, ekspresif, penuh empati. 
Kekuatan: Fleksibel, menyenangkan. 
Tantangan: Mudah terdistraksi, moody.""",

    "Burung Hantu": """🦉 Sang Pengamat (Burung Hantu)
Bijaksana, analitis, reflektif. 
Kekuatan: Mendalam, cermat. 
Tantangan: Cemas, terlalu banyak berpikir.""",

    "Semut": """🐜 Sang Pekerja Keras (Semut)
Tekun, fokus, efisien. 
Kekuatan: Mandiri, disiplin. 
Tantangan: Kurang fleksibel, kaku.""",

    "Kura-kura": """🐢 Sang Penjaga Kedamaian (Kura-kura)
Pendiam, penyabar, pengamat. 
Kekuatan: Penuh empati, setia. 
Tantangan: Menutup diri, menghindar dari tantangan."""
}

# Inisialisasi Prolog
prolog = Prolog()
prolog.consult("embeti.pl")

class KepribadianApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tes Kepribadian Hewan")
        self.index = 0
        self.sifat_ids = list(pertanyaan_dict.keys())
        self.jawaban_user = {}

        self.label = Label(master, text="", wraplength=400, font=("Helvetica", 12))
        self.label.pack(pady=20)

        self.btn_frame = Frame(master)
        self.btn_frame.pack(pady=10)

        self.yes_btn = Button(self.btn_frame, text="Ya", width=10, command=lambda: self.jawab("y"))
        self.yes_btn.grid(row=0, column=0, padx=10)

        self.no_btn = Button(self.btn_frame, text="Tidak", width=10, command=lambda: self.jawab("n"))
        self.no_btn.grid(row=0, column=1, padx=10)

        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index < len(self.sifat_ids):
            sifat_id = self.sifat_ids[self.index]
            pertanyaan = pertanyaan_dict[sifat_id]
            self.label.config(text=pertanyaan)
        else:
            self.selesaikan_tes()

    def jawab(self, pilihan):
        sifat_id = self.sifat_ids[self.index]
        self.jawaban_user[sifat_id] = pilihan
        self.index += 1
        self.tampilkan_pertanyaan()

    def selesaikan_tes(self):
        prolog.query("reset_jawaban")
        for sifat, jawaban in self.jawaban_user.items():
            if jawaban == "y":
                prolog.assertz(f"sifat_pos({sifat})")
            else:
                prolog.assertz(f"sifat_neg({sifat})")

        hasil = list(prolog.query("evaluasi_kepribadian(X)"))
        if hasil:
            tipe = hasil[0]["X"].decode() if isinstance(hasil[0]["X"], bytes) else hasil[0]["X"]
            deskripsi = deskripsi_kepribadian.get(tipe, "Deskripsi Tidak Tersedia.")
            messagebox.showinfo("Hasil Kepribadian", f"Kepribadian kamu adalah: {tipe}\n\n{deskripsi}")
        else:
            messagebox.showinfo("Hasil", "Tidak dapat menentukan kepribadian.")

        self.master.destroy()

# Jalankan Aplikasi
if __name__ == "__main__":
    root = Tk()
    root.geometry("500x250")
    app = KepribadianApp(root)
    root.mainloop()
