import io
import sys

import qrcode
from PIL import Image

import os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox, QSpinBox, QFileDialog, QDialog
from PyQt5 import QtCore

# 是否添加logo
H_logo = 1

class qrcodeGUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        # self.setFixedSize(600, 500)
        self.setWindowTitle('二维码生成器-BlueBox')
        logo_path = os.getcwd() + '\\' + 'image' + '\\' + 'logo' + '.ico'
        # print(logo_path)
        self.setWindowIcon(QIcon(logo_path))
        self.grid = QGridLayout()

        # 定义组件
        # --label
        self.content_label = QLabel('内容：')
        self.size_label = QLabel('尺寸：')
        self.version_label = QLabel('版本：')
        self.margin_label = QLabel('边距：')
        self.rendering_label = QLabel('二维码预览')
        self.show_label = QLabel()


        # 使得图片可缩放
        self.show_label.setScaledContents(True)
        # 显示时的最大尺寸
        self.show_label.setMaximumSize(500, 500)
        # -- 输入框
        self.content_edit = QLineEdit()
        self.content_edit.setText('请填入文本')
        self.content_edit.setAlignment(QtCore.Qt.AlignCenter)
        # -- 按钮
        self.generate_button = QPushButton('生成二维码')
        self.save_button = QPushButton('保存二维码')
        # -- 下拉框
        self.version_combobox = QComboBox()
        for i in range(1, 41):
            self.version_combobox.addItem('%s' % str(i))
        self.size_combobox = QComboBox()
        for i in range(8, 40, 2):
            self.size_combobox.addItem('%s * %s' %(str(i * 29), str(i * 29)))
        # --微调框
        self.margin_spinbox = QSpinBox()

        # 文字居中
        self.content_label.setAlignment(QtCore.Qt.AlignCenter)
        self.size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.version_label.setAlignment(QtCore.Qt.AlignCenter)
        self.margin_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rendering_label.setAlignment(QtCore.Qt.AlignCenter)

        # 设置字体
        font = QtGui.QFont()
        font.setFamily("等线")
        # font.setBold(True)
        font.setPointSize(12)

        self.rendering_label.setFont(font)
        self.margin_label.setFont(font)
        self.content_label.setFont(font)
        self.version_label.setFont(font)
        self.size_label.setFont(font)

        self.content_edit.setFont(font)
        self.version_combobox.setFont(font)
        self.size_combobox.setFont(font)
        self.margin_spinbox.setFont(font)
        self.generate_button.setFont(font)
        self.save_button.setFont(font)

        # 布局
        # 数字一次对应行 列 行数 列数
        self.grid.addWidget(self.rendering_label, 0, 0, 1, 1)
        self.grid.addWidget(self.show_label, 1, 0, 5, 5)
        self.grid.addWidget(self.content_label, 0, 5, 1, 1)
        self.grid.addWidget(self.content_edit, 0, 6, 1, 3)
        self.grid.addWidget(self.version_label, 1, 5, 1, 1)
        self.grid.addWidget(self.version_combobox, 1, 6, 1, 3)
        self.grid.addWidget(self.size_label, 2, 5, 1, 1)
        self.grid.addWidget(self.size_combobox, 2, 6, 1, 3)
        self.grid.addWidget(self.margin_label, 3, 5, 1, 1)
        self.grid.addWidget(self.margin_spinbox, 3, 6, 1, 3)
        self.grid.addWidget(self.generate_button, 4, 5, 1, 4)
        self.grid.addWidget(self.save_button, 5, 5, 1, 4)
        self.setLayout(self.grid)
        self.generate_button.clicked.connect(self.genQrcode)
        self.save_button.clicked.connect(self.saveQrcode)
        self.margin_spinbox.valueChanged.connect(self.genQrcode)
        self.genQrcode()

    '''生成二维码'''
    def genQrcode(self):
        content = self.content_edit.text()
        try:
            margin = int(self.margin_spinbox.text())
        except:
            margin = 0
        size = int(self.size_combobox.currentText().split('*')[0])

        qr = qrcode.QRCode(version=1,
                           error_correction=qrcode.constants.ERROR_CORRECT_L,
                           box_size=size//29,
                           border=margin)

        qr.add_data(content)
        self.qr_img = qr.make_image()

        if H_logo != 0:
            # 添加logo
            self.qr_img = self.qr_img.convert("RGBA")
            imgW, imgH = self.qr_img.size
            w1, h1 = map(lambda x: x // 4, self.qr_img.size)
            # 要粘贴的自定义图片，生成缩略图
            # im = Image.open('./image/logo.jpg')
            im = Image.open('E:/BlueBox/BlueBox_file/Pycharm_Project/MakeQrcode20220105/image/logo.jpg')
            imW, imH = im.size
            w1 = w1 if w1 < imW else imW
            h1 = h1 if h1 < imH else imH
            im = im.resize((w1, h1))
            # 在二维码上中间位置粘贴自定义图片
            self.qr_img.paste(im, ((imgW - w1) // 2, (imgH - h1) // 2))

        fp = io.BytesIO()
        self.qr_img.save(fp, 'BMP')
        qimg = QtGui.QImage()
        qimg.loadFromData(fp.getvalue(), 'BMP')
        qimg_pixmap = QtGui.QPixmap.fromImage(qimg)
        self.show_label.setPixmap(qimg_pixmap)

    '''保存二维码'''
    def saveQrcode(self):
        filename = QFileDialog.getSaveFileName(self, '保存', './qrcode.png', '所有文件(*)')
        if filename[0] != '':
            self.qr_img.save(filename[0])
            QDialog().show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = qrcodeGUI()
    gui.show()
    sys.exit(app.exec_())
