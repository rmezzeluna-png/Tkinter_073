import tkinter as tk

def prediksi_prodi():
    hasil_label.config(text="prediksi prodi = Teknologi Informasi")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
root.configure(bg="#f0f4f8")

# Judul aplikasi
judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Helvetica", 18, "bold"), bg="#f0f4f8", fg="#333333")
judul.pack(pady=20)

# Frame untuk input
input_frame = tk.Frame(root, bg="#f0f4f8")
input_frame.pack(pady=10)

# Label dan entry untuk 10 nilai pelajaran
entries = []