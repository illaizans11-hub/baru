# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_TunaiWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 650)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Background Card
        self.card = QtWidgets.QLabel(self.centralwidget)
        self.card.setGeometry(QtCore.QRect(5, 10, 350, 620))
        self.card.setStyleSheet("""
            background-color: white;
            border-radius: 10px;
            border:1px solid #E0E0E0;
        """)

        # Title
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(80, 20, 250, 40))
        self.label_title.setFont(self.boldFont(18))
        self.label_title.setText("Pembayaran Tunai")

        # Orange Gradient Header
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(20, 80, 320, 160))
        self.header.setStyleSheet("""
            background-color: qlineargradient(
                spread:pad,
                x1:0, y1:0.5,
                x2:1, y2:0.5,
                stop:0 rgba(255,170,60,255),
                stop:1 rgba(230,120,20,255)
            );
            border-radius: 15px;
        """)

        # Header Description
        self.header_text = QtWidgets.QLabel(self.centralwidget)
        self.header_text.setGeometry(QtCore.QRect(40, 90, 260, 140))
        self.header_text.setFont(self.boldFont(10))
        self.header_text.setStyleSheet("color:white;")
        self.header_text.setText(
            "Metode Pembayaran : TUNAI\n\n"
            "Anda dapat melakukan pembayaran secara langsung\n"
            "kepada pengelola kos.\n\n"
            "Detail Pembayaran:\n"
            "- Bayar Kepada : Pengelola Kos\n"
            "- Alamat       : Jl. Mawar No. 23\n"
            "- Atas Nama    : Kos Mewah"
        )

        # Informasi tambahan
        self.info_card = QtWidgets.QLabel(self.centralwidget)
        self.info_card.setGeometry(QtCore.QRect(25, 260, 320, 240))
        self.info_card.setStyleSheet("""
            background:white;
            border-radius:10px;
            border:1px solid #E0E0E0;
        """)

        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(40, 275, 290, 210))
        self.label_info.setFont(self.normalFont(10))
        self.label_info.setWordWrap(True)
        self.label_info.setText(
            "Cara melakukan pembayaran tunai:\n\n"
            "1. Datang langsung ke pengelola kos.\n"
            "2. Bawa uang sesuai total pembayaran.\n"
            "3. Berikan uang kepada pengelola.\n"
            "4. Minta bukti pembayaran (nota).\n"
            "5. Admin akan memverifikasi pembayaran Anda dalam sistem.\n\n"
            "Jam Operasional Pembayaran:\n"
            "Senin – Minggu : 09.00 – 20.00\n\n"
            "Jika ada kendala, hubungi Admin:\n"
            "WhatsApp : 0812-3456-7890"
        )

        # Button Tunai
        self.btn_tunai = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tunai.setGeometry(QtCore.QRect(30, 520, 310, 50))
        self.btn_tunai.setFont(self.boldFont(11))
        self.btn_tunai.setStyleSheet(self.buttonStyle())
        self.btn_tunai.setText("Saya Mengerti, Akan Bayar Tunai")
        self.btn_tunai.clicked.connect(self.konfirmasiTunai)

    # Font
    def boldFont(self, size):
        f = QtGui.QFont()
        f.setPointSize(size)
        f.setBold(True)
        return f

    def normalFont(self, size):
        f = QtGui.QFont()
        f.setPointSize(size)
        return f

    # Button Style
    def buttonStyle(self):
        return """
            QPushButton {
                background-color: qlineargradient(
                    spread:pad,
                    x1:0, y1:0.5,
                    x2:1, y2:0.5,
                    stop:0 rgba(255,170,60,255),
                    stop:1 rgba(230,120,20,255)
                );
                color:white;
                border-radius:12px;
                font-weight:bold;
            }
        """

    # Konfirmasi
    def konfirmasiTunai(self):
        msg = QMessageBox()
        msg.setWindowTitle("Informasi")
        msg.setText(
            "Baik! Silakan lakukan pembayaran tunai ke pengelola kos.\n"
            "Setelah Anda membayar, admin akan memverifikasi status pembayaran Anda."
        )
        msg.setIcon(QMessageBox.Information)
        msg.exec_()


# MAIN
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    ui = Ui_TunaiWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())
