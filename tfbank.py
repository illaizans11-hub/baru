# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os, shutil
import connection  # pastikan ini modul koneksi ke MySQL-mu
import user        # modul session: user.is_logged_in, user.current_user

class Ui_MainWindow(object):

    def setupUi(self, MainWindow, id_penghuni, id_booking):
        self.id_booking = id_booking
        self.id_penghuni = id_penghuni
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(354, 668)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Background putih
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 351, 611))
        self.label.setStyleSheet("""
            background-color: #ffffff;
            border-radius: 10px;
            border: 1px solid #E0E0E0;
        """)

        # Card biru
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 321, 161))
        self.label_3.setStyleSheet("""
            background-color: qlineargradient(
                spread:pad, x1:0, y1:0.5,
                x2:1, y2:0.5,
                stop:0 rgba(90,150,255,255),
                stop:1 rgba(40,100,210,255)
            );
            border-radius: 15px;
        """)

        # Judul
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 40, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.label_2.setFont(font)

        # Transfer ke bank
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(40, 100, 141, 16))
        font2 = QtGui.QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet("color:white;")

        # Card biru bank
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 301, 121))
        self.label_4.setStyleSheet("""
            background-color: qlineargradient(
                spread:pad, x1:0, y1:0.5,
                x2:1, y2:0.5,
                stop:0 rgba(110,170,255,255),
                stop:1 rgba(60,120,220,255)
            );
            border-radius: 15px;
        """)

        # Label bank
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(50, 140, 111, 71))
        self.label_13.setText("Bank\n\nNo.Rekening\n\nAtas Nama")

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(220, 140, 111, 81))
        font3 = QtGui.QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet("color:white;")
        self.label_14.setText("BCA\n\n1234567890\n\nKos Mewah")

        # Card putih upload
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 260, 311, 271))
        self.label_11.setStyleSheet("""
            background:white;
            border-radius:10px;
            border: 1px solid #E0E0E0;
        """)

        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(110, 370, 151, 16))
        self.label_18.setText("Upload Bukti Transfer")

        # PREVIEW FOTO
        self.preview = QtWidgets.QLabel(self.centralwidget)
        self.preview.setGeometry(QtCore.QRect(95, 285, 170, 80))
        self.preview.setStyleSheet("border:1px solid #BDBDBD; border-radius:8px;")
        self.preview.setScaledContents(True)
        self.preview.setText("")

        self.selected_file = None

        # Tombol tambah foto
        self.btnTambah = QtWidgets.QPushButton(self.centralwidget)
        self.btnTambah.setGeometry(QtCore.QRect(120, 400, 131, 41))
        self.btnTambah.setStyleSheet(self.buttonBlue())
        self.btnTambah.setText("Tambah Foto")
        self.btnTambah.clicked.connect(self.selectImage)

        # Tombol kirim foto
        self.btnKirim = QtWidgets.QPushButton(self.centralwidget)
        self.btnKirim.setGeometry(QtCore.QRect(30, 560, 311, 41))
        self.btnKirim.setStyleSheet(self.buttonBlue())
        self.btnKirim.setText("Kirim Bukti Transfer")
        self.btnKirim.clicked.connect(lambda: self.kirimGambar(MainWindow))

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Style tombol biru
    def buttonBlue(self):
        return """
        QPushButton {
            background-color: qlineargradient(
                spread:pad, x1:0, y1:0.5,
                x2:1, y2:0.5,
                stop:0 rgba(90,150,255,255),
                stop:1 rgba(40,100,210,255)
            );
            color:white;
            font-weight:bold;
            border-radius:15px;
        }
        """

    # Kirim gambar ke folder & database
    def kirimGambar(self, MainWindow):
        if not self.selected_file:
            QMessageBox.warning(None, "Gagal", "Silakan tambah foto dulu sebelum mengirim.")
            return
        try:
            save_dir = "bukti"
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            ext = os.path.splitext(self.selected_file)[1]
            new_filename = f"TF_{int(QtCore.QDateTime.currentSecsSinceEpoch())}{ext}"
            save_path = os.path.join(save_dir, new_filename)
            shutil.copy(self.selected_file, save_path)

            conn = connection.get_connection()
            cursor = conn.cursor()

            sql = """
            INSERT INTO pembayaran
            (id_penghuni, id_booking, jumlah, tipe_pembayaran, bulan_ke, metode_pembayaran, bukti_transfer)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                self.id_penghuni,
                self.id_booking,
                500000,      # contoh harga
                "Pertama",
                1,
                "Transfer",
                save_path
            ))
            conn.commit()

            QMessageBox.information(None, "Sukses", "Bukti transfer berhasil dikirim!")
            MainWindow.close()
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Terjadi kesalahan:\n{e}")

    # Pilih file gambar
    def selectImage(self):
        filePath, _ = QFileDialog.getOpenFileName(None, "Pilih Bukti Transfer", "", "Image Files (*.png *.jpg *.jpeg)")
        if filePath:
            self.selected_file = filePath
            pixmap = QtGui.QPixmap(filePath)
            self.preview.setPixmap(pixmap)
            QMessageBox.information(None, "Berhasil", "Foto berhasil ditambahkan!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Transfer Bank")
        self.label_2.setText("Transfer Bank")
        self.label_17.setText("Transfer ke bank")

# ────────────── MAIN ──────────────
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Cek login
    if not user.is_logged_in or not user.current_user:
        QMessageBox.warning(None, "Login Dulu", "Silakan login terlebih dahulu!")
        sys.exit()

    # ambil id_penghuni otomatis
    id_penghuni = user.current_user["id"]

    # ambil id_booking terakhir yang belum dibayar
    conn = connection.get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM booking WHERE id_penghuni=%s AND status='Belum Bayar' ORDER BY id DESC LIMIT 1",
        (id_penghuni,)
    )
    result = cursor.fetchone()
    if not result:
        QMessageBox.warning(None, "Info", "Tidak ada booking yang harus dibayar!")
        sys.exit()
    id_booking = result[0]

    # Buka window transfer
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, id_penghuni=id_penghuni, id_booking=id_booking)
    MainWindow.show()
    sys.exit(app.exec_())
