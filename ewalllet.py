# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class Ui_EwalletWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 670)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Background Card
        self.card = QtWidgets.QLabel(self.centralwidget)
        self.card.setGeometry(QtCore.QRect(5, 10, 350, 610))
        self.card.setStyleSheet("""
            background-color: white;
            border-radius: 10px;
            border:1px solid #E0E0E0;
        """)

        # Judul
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(90, 30, 200, 40))
        self.label_title.setFont(self.boldFont(17))
        self.label_title.setText("E - Wallet")

        # Section Top (background gradien)
        self.section_bg = QtWidgets.QLabel(self.centralwidget)
        self.section_bg.setGeometry(QtCore.QRect(20, 90, 320, 160))
        self.section_bg.setStyleSheet("""
            background-color: qlineargradient(
                spread:pad,
                x1:0, y1:0.5,
                x2:1, y2:0.5,
                stop:0 rgba(90,150,255,255),
                stop:1 rgba(40,100,210,255)
            );
            border-radius: 15px;
        """)

        # Label: Nama E-wallet
        self.label_walet_title = QtWidgets.QLabel(self.centralwidget)
        self.label_walet_title.setGeometry(QtCore.QRect(40, 100, 200, 20))
        self.label_walet_title.setFont(self.boldFont(10))
        self.label_walet_title.setStyleSheet("color:white;")
        self.label_walet_title.setText("Pembayaran ke E-Wallet")

        # Deskripsi kiri
        self.label_left = QtWidgets.QLabel(self.centralwidget)
        self.label_left.setGeometry(QtCore.QRect(40, 140, 120, 70))
        self.label_left.setText("E-Wallet\n\nNo. Telepon\n\nAtas Nama")

        # Detail kanan
        self.label_right = QtWidgets.QLabel(self.centralwidget)
        self.label_right.setGeometry(QtCore.QRect(210, 140, 150, 80))
        self.label_right.setFont(self.boldFont(10))
        self.label_right.setStyleSheet("color:white;")
        self.label_right.setText("GOPAY\n\n081234567890\n\nKos Mewah")

        # Card Upload bukti
        self.card_upload = QtWidgets.QLabel(self.centralwidget)
        self.card_upload.setGeometry(QtCore.QRect(30, 270, 310, 260))
        self.card_upload.setStyleSheet("""
            background:white;
            border-radius:10px;
            border:1px solid #E0E0E0;
        """)

        # Label upload
        self.label_upload = QtWidgets.QLabel(self.centralwidget)
        self.label_upload.setGeometry(QtCore.QRect(110, 360, 200, 20))
        self.label_upload.setFont(self.normalFont(10))
        self.label_upload.setText("Upload Bukti Pembayaran")

        # Tombol pilih foto
        self.btn_tambah_foto = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tambah_foto.setGeometry(QtCore.QRect(120, 390, 130, 40))
        self.btn_tambah_foto.setStyleSheet(self.btnStyle())
        self.btn_tambah_foto.setText("Tambah Foto")
        self.btn_tambah_foto.clicked.connect(self.uploadFoto)

        # Tombol Bayar
        self.btn_bayar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bayar.setGeometry(QtCore.QRect(30, 550, 310, 45))
        self.btn_bayar.setFont(self.boldFont(10))
        self.btn_bayar.setStyleSheet(self.btnStyle())
        self.btn_bayar.setText("Bayar Sekarang")
        self.btn_bayar.clicked.connect(self.konfirmasiPembayaran)

        # Menampilkan gambar upload (jika dipilih)
        self.preview = QtWidgets.QLabel(self.centralwidget)
        self.preview.setGeometry(QtCore.QRect(60, 290, 250, 130))
        self.preview.setStyleSheet("border:1px dashed #999; border-radius:10px;")
        self.preview.setScaledContents(True)
        self.preview.setText("")
        self.preview.hide()

        MainWindow.setCentralWidget(self.centralwidget)

    # ========== STYLE & FONT ==========
    def boldFont(self, size):
        f = QtGui.QFont()
        f.setPointSize(size)
        f.setBold(True)
        return f

    def normalFont(self, size):
        f = QtGui.QFont()
        f.setPointSize(size)
        return f

    def btnStyle(self):
        return """
            QPushButton {
                background-color: qlineargradient(
                    spread:pad,
                    x1:0, y1:0.5,
                    x2:1, y2:0.5,
                    stop:0 rgba(90,150,255,255),
                    stop:1 rgba(40,100,210,255)
                );
                color:white;
                border-radius:10px;
                font-weight:bold;
            }
        """

    # ========== UPLOAD FOTO ==========
    def uploadFoto(self):
        path, _ = QFileDialog.getOpenFileName(None, "Pilih Bukti Pembayaran", "", "Image Files (*.png *.jpg *.jpeg)")
        if path:
            self.preview.show()
            self.preview.setPixmap(QtGui.QPixmap(path))
            self.foto_path = path

    # ========== KONFIRMASI ==========
    def konfirmasiPembayaran(self):
        if not hasattr(self, "foto_path"):
            self.pesan("Silakan upload bukti pembayaran terlebih dahulu.")
            return

        self.pesan("Pembayaran berhasil dikirim!\nTunggu konfirmasi admin.")

    def pesan(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Informasi")
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()


# MAIN RUN
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_EwalletWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
