# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormBiseccioniyQQQH.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)
import sympy as sp 
import tkinter
import tkinter.messagebox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(796, 603)
        MainWindow.setIconSize(QSize(100, 100))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 20, 801, 451))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(73, 147, 220, 179))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(160, 208, 255, 179))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(116, 177, 237, 179))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(37, 73, 110, 179))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(49, 98, 147, 179))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush7 = QBrush(QColor(164, 201, 237, 217))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush10 = QBrush(QColor(37, 73, 110, 89))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        brush11 = QBrush(QColor(116, 186, 255, 179))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush11)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setIconSize(QSize(100, 100))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget_3 = QTabWidget(self.tab)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(0, 0, 801, 381))
        self.widget_2 = QWidget()
        self.widget_2.setObjectName(u"widget_2")
        self.label_54 = QLabel(self.widget_2)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(30, 50, 161, 31))
        font = QFont()
        font.setPointSize(14)
        self.label_54.setFont(font)
        self.label_56 = QLabel(self.widget_2)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(30, 100, 271, 31))
        self.label_56.setFont(font)
        self.label_57 = QLabel(self.widget_2)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(30, 150, 291, 31))
        self.label_57.setFont(font)
        self.label_58 = QLabel(self.widget_2)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(30, 200, 251, 31))
        self.label_58.setFont(font)
        self.label_59 = QLabel(self.widget_2)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(30, 250, 281, 31))
        self.label_59.setFont(font)
        self.txtFuncion_6 = QLineEdit(self.widget_2)
        self.txtFuncion_6.setObjectName(u"txtFuncion_6")
        self.txtFuncion_6.setGeometry(QRect(190, 50, 221, 31))
        self.txtTolerancia_6 = QLineEdit(self.widget_2)
        self.txtTolerancia_6.setObjectName(u"txtTolerancia_6")
        self.txtTolerancia_6.setGeometry(QRect(330, 200, 81, 31))
        self.txtPrimerValor_6 = QLineEdit(self.widget_2)
        self.txtPrimerValor_6.setObjectName(u"txtPrimerValor_6")
        self.txtPrimerValor_6.setGeometry(QRect(330, 100, 81, 31))
        self.txtNmax_6 = QLineEdit(self.widget_2)
        self.txtNmax_6.setObjectName(u"txtNmax_6")
        self.txtNmax_6.setGeometry(QRect(330, 250, 81, 31))
        self.txtSegundoValor_6 = QLineEdit(self.widget_2)
        self.txtSegundoValor_6.setObjectName(u"txtSegundoValor_6")
        self.txtSegundoValor_6.setGeometry(QRect(330, 150, 81, 31))
        self.btnCalcular_6 = QPushButton(self.widget_2)
        self.btnCalcular_6.setObjectName(u"btnCalcular_6")
        self.btnCalcular_6.setGeometry(QRect(230, 300, 181, 41))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush12 = QBrush(QColor(255, 255, 127, 179))
        brush12.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush12)
        brush13 = QBrush(QColor(255, 255, 254, 179))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush13)
        brush14 = QBrush(QColor(255, 255, 190, 179))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        brush15 = QBrush(QColor(127, 127, 63, 179))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush15)
        brush16 = QBrush(QColor(170, 170, 85, 179))
        brush16.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush17 = QBrush(QColor(255, 255, 191, 217))
        brush17.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush17)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette1.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush13)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush17)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush18 = QBrush(QColor(127, 127, 63, 89))
        brush18.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        brush19 = QBrush(QColor(255, 255, 203, 179))
        brush19.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Accent, brush19)
        self.btnCalcular_6.setPalette(palette1)
        self.label_60 = QLabel(self.widget_2)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(570, 15, 111, 21))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_60.setFont(font1)
        self.label_61 = QLabel(self.widget_2)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(480, 50, 161, 31))
        self.label_61.setFont(font)
        self.txtRaizRespuesta_6 = QLabel(self.widget_2)
        self.txtRaizRespuesta_6.setObjectName(u"txtRaizRespuesta_6")
        self.txtRaizRespuesta_6.setGeometry(QRect(650, 50, 141, 31))
        self.txtRaizRespuesta_6.setFont(font)
        self.label_62 = QLabel(self.widget_2)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(480, 100, 161, 31))
        self.label_62.setFont(font)
        self.txtToleranciaRespuesta_6 = QLabel(self.widget_2)
        self.txtToleranciaRespuesta_6.setObjectName(u"txtToleranciaRespuesta_6")
        self.txtToleranciaRespuesta_6.setGeometry(QRect(630, 100, 151, 31))
        self.txtToleranciaRespuesta_6.setFont(font)
        self.label_63 = QLabel(self.widget_2)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(480, 150, 161, 31))
        self.label_63.setFont(font)
        self.txtAfinal_6 = QLabel(self.widget_2)
        self.txtAfinal_6.setObjectName(u"txtAfinal_6")
        self.txtAfinal_6.setGeometry(QRect(630, 150, 151, 31))
        self.txtAfinal_6.setFont(font)
        self.label_64 = QLabel(self.widget_2)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(480, 200, 161, 31))
        self.label_64.setFont(font)
        self.txtBfinal_5 = QLabel(self.widget_2)
        self.txtBfinal_5.setObjectName(u"txtBfinal_5")
        self.txtBfinal_5.setGeometry(QRect(630, 200, 151, 31))
        self.txtBfinal_5.setFont(font)
        self.btnLimpiar_6 = QPushButton(self.widget_2)
        self.btnLimpiar_6.setObjectName(u"btnLimpiar_6")
        self.btnLimpiar_6.setGeometry(QRect(30, 300, 181, 41))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush13)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush17)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush17)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.Accent, brush19)
        self.btnLimpiar_6.setPalette(palette2)
        self.label_65 = QLabel(self.widget_2)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(480, 250, 161, 31))
        self.label_65.setFont(font)
        self.txtIteracionFinal_6 = QLabel(self.widget_2)
        self.txtIteracionFinal_6.setObjectName(u"txtIteracionFinal_6")
        self.txtIteracionFinal_6.setGeometry(QRect(630, 250, 151, 31))
        self.txtIteracionFinal_6.setFont(font)
        self.tabWidget_3.addTab(self.widget_2, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.label_66 = QLabel(self.tab_7)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(490, 200, 161, 31))
        self.label_66.setFont(font)
        self.txtPrimerValor_7 = QLineEdit(self.tab_7)
        self.txtPrimerValor_7.setObjectName(u"txtPrimerValor_7")
        self.txtPrimerValor_7.setGeometry(QRect(340, 100, 81, 31))
        self.label_67 = QLabel(self.tab_7)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(490, 50, 161, 31))
        self.label_67.setFont(font)
        self.txtBfinal_6 = QLabel(self.tab_7)
        self.txtBfinal_6.setObjectName(u"txtBfinal_6")
        self.txtBfinal_6.setGeometry(QRect(640, 200, 151, 31))
        self.txtBfinal_6.setFont(font)
        self.txtRaizRespuesta_7 = QLabel(self.tab_7)
        self.txtRaizRespuesta_7.setObjectName(u"txtRaizRespuesta_7")
        self.txtRaizRespuesta_7.setGeometry(QRect(660, 50, 141, 31))
        self.txtRaizRespuesta_7.setFont(font)
        self.btnCalcular_7 = QPushButton(self.tab_7)
        self.btnCalcular_7.setObjectName(u"btnCalcular_7")
        self.btnCalcular_7.setGeometry(QRect(240, 300, 181, 41))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush17)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette3.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush17)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.Accent, brush19)
        self.btnCalcular_7.setPalette(palette3)
        self.txtFuncion_7 = QLineEdit(self.tab_7)
        self.txtFuncion_7.setObjectName(u"txtFuncion_7")
        self.txtFuncion_7.setGeometry(QRect(200, 50, 221, 31))
        self.label_68 = QLabel(self.tab_7)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(490, 100, 161, 31))
        self.label_68.setFont(font)
        self.txtNmax_7 = QLineEdit(self.tab_7)
        self.txtNmax_7.setObjectName(u"txtNmax_7")
        self.txtNmax_7.setGeometry(QRect(340, 250, 81, 31))
        self.label_69 = QLabel(self.tab_7)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(40, 50, 161, 31))
        self.label_69.setFont(font)
        self.txtSegundoValor_7 = QLineEdit(self.tab_7)
        self.txtSegundoValor_7.setObjectName(u"txtSegundoValor_7")
        self.txtSegundoValor_7.setGeometry(QRect(340, 150, 81, 31))
        self.label_70 = QLabel(self.tab_7)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(40, 150, 291, 31))
        self.label_70.setFont(font)
        self.label_71 = QLabel(self.tab_7)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(580, 15, 111, 21))
        self.label_71.setFont(font1)
        self.txtToleranciaRespuesta_7 = QLabel(self.tab_7)
        self.txtToleranciaRespuesta_7.setObjectName(u"txtToleranciaRespuesta_7")
        self.txtToleranciaRespuesta_7.setGeometry(QRect(640, 100, 151, 31))
        self.txtToleranciaRespuesta_7.setFont(font)
        self.txtAfinal_7 = QLabel(self.tab_7)
        self.txtAfinal_7.setObjectName(u"txtAfinal_7")
        self.txtAfinal_7.setGeometry(QRect(640, 150, 151, 31))
        self.txtAfinal_7.setFont(font)
        self.txtIteracionFinal_7 = QLabel(self.tab_7)
        self.txtIteracionFinal_7.setObjectName(u"txtIteracionFinal_7")
        self.txtIteracionFinal_7.setGeometry(QRect(640, 250, 151, 31))
        self.txtIteracionFinal_7.setFont(font)
        self.label_72 = QLabel(self.tab_7)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(490, 250, 161, 31))
        self.label_72.setFont(font)
        self.btnLimpiar_7 = QPushButton(self.tab_7)
        self.btnLimpiar_7.setObjectName(u"btnLimpiar_7")
        self.btnLimpiar_7.setGeometry(QRect(40, 300, 181, 41))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush17)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette4.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush17)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.Accent, brush19)
        self.btnLimpiar_7.setPalette(palette4)
        self.txtTolerancia_7 = QLineEdit(self.tab_7)
        self.txtTolerancia_7.setObjectName(u"txtTolerancia_7")
        self.txtTolerancia_7.setGeometry(QRect(340, 200, 81, 31))
        self.label_73 = QLabel(self.tab_7)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(40, 200, 251, 31))
        self.label_73.setFont(font)
        self.label_74 = QLabel(self.tab_7)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(40, 100, 271, 31))
        self.label_74.setFont(font)
        self.label_75 = QLabel(self.tab_7)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(490, 150, 161, 31))
        self.label_75.setFont(font)
        self.label_76 = QLabel(self.tab_7)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(40, 250, 281, 31))
        self.label_76.setFont(font)
        self.tabWidget_3.addTab(self.tab_7, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_2 = QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 801, 381))
        self.tabWidget_2.setStyleSheet(u"alternate-background-color: rgb(0, 144, 106);")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_45 = QLabel(self.tab_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(20, 100, 301, 31))
        self.label_45.setFont(font)
        self.txtToleranciaRespuesta_5 = QLabel(self.tab_3)
        self.txtToleranciaRespuesta_5.setObjectName(u"txtToleranciaRespuesta_5")
        self.txtToleranciaRespuesta_5.setGeometry(QRect(620, 150, 151, 31))
        self.txtToleranciaRespuesta_5.setFont(font)
        self.label_46 = QLabel(self.tab_3)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(470, 150, 161, 31))
        self.label_46.setFont(font)
        self.txtAfinal_5 = QLabel(self.tab_3)
        self.txtAfinal_5.setObjectName(u"txtAfinal_5")
        self.txtAfinal_5.setGeometry(QRect(640, 200, 151, 31))
        self.txtAfinal_5.setFont(font)
        self.txtFuncion_5 = QLineEdit(self.tab_3)
        self.txtFuncion_5.setObjectName(u"txtFuncion_5")
        self.txtFuncion_5.setGeometry(QRect(180, 45, 221, 31))
        self.label_47 = QLabel(self.tab_3)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(20, 45, 161, 31))
        self.label_47.setFont(font)
        self.txtPrimerValor_5 = QLineEdit(self.tab_3)
        self.txtPrimerValor_5.setObjectName(u"txtPrimerValor_5")
        self.txtPrimerValor_5.setGeometry(QRect(320, 100, 81, 31))
        self.label_48 = QLabel(self.tab_3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(20, 200, 281, 31))
        self.label_48.setFont(font)
        self.label_49 = QLabel(self.tab_3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(20, 150, 251, 31))
        self.label_49.setFont(font)
        self.txtNmax_5 = QLineEdit(self.tab_3)
        self.txtNmax_5.setObjectName(u"txtNmax_5")
        self.txtNmax_5.setGeometry(QRect(320, 200, 81, 31))
        self.label_50 = QLabel(self.tab_3)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(470, 100, 161, 31))
        self.label_50.setFont(font)
        self.txtIteracionFinal_5 = QLabel(self.tab_3)
        self.txtIteracionFinal_5.setObjectName(u"txtIteracionFinal_5")
        self.txtIteracionFinal_5.setGeometry(QRect(620, 245, 151, 31))
        self.txtIteracionFinal_5.setFont(font)
        self.label_52 = QLabel(self.tab_3)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(470, 200, 161, 31))
        self.label_52.setFont(font)
        self.txtTolerancia_5 = QLineEdit(self.tab_3)
        self.txtTolerancia_5.setObjectName(u"txtTolerancia_5")
        self.txtTolerancia_5.setGeometry(QRect(320, 150, 81, 31))
        self.btnCalcular_5 = QPushButton(self.tab_3)
        self.btnCalcular_5.setObjectName(u"btnCalcular_5")
        self.btnCalcular_5.setGeometry(QRect(220, 250, 181, 41))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush20 = QBrush(QColor(255, 255, 127, 255))
        brush20.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush21 = QBrush(QColor(0, 144, 106, 255))
        brush21.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush21)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette5.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush20)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush21)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush21)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.Accent, brush19)
        self.btnCalcular_5.setPalette(palette5)
        self.btnCalcular_5.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.label_53 = QLabel(self.tab_3)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(470, 245, 161, 31))
        self.label_53.setFont(font)
        self.btnLimpiar_5 = QPushButton(self.tab_3)
        self.btnLimpiar_5.setObjectName(u"btnLimpiar_5")
        self.btnLimpiar_5.setGeometry(QRect(20, 250, 181, 41))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush13)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush21)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette6.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush20)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush21)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush13)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush21)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.Accent, brush19)
        self.btnLimpiar_5.setPalette(palette6)
        self.btnLimpiar_5.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.txtRaizRespuesta_5 = QLabel(self.tab_3)
        self.txtRaizRespuesta_5.setObjectName(u"txtRaizRespuesta_5")
        self.txtRaizRespuesta_5.setGeometry(QRect(640, 100, 141, 31))
        self.txtRaizRespuesta_5.setFont(font)
        self.label_55 = QLabel(self.tab_3)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(560, 65, 111, 21))
        self.label_55.setFont(font1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.label_99 = QLabel(self.tab_6)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(30, 50, 161, 31))
        self.label_99.setFont(font)
        self.txtFuncion_10 = QLineEdit(self.tab_6)
        self.txtFuncion_10.setObjectName(u"txtFuncion_10")
        self.txtFuncion_10.setGeometry(QRect(190, 50, 221, 31))
        self.label_100 = QLabel(self.tab_6)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setGeometry(QRect(30, 100, 181, 31))
        self.label_100.setFont(font)
        self.txtPrimerValor_12 = QLineEdit(self.tab_6)
        self.txtPrimerValor_12.setObjectName(u"txtPrimerValor_12")
        self.txtPrimerValor_12.setGeometry(QRect(330, 100, 81, 31))
        self.label_101 = QLabel(self.tab_6)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(30, 150, 181, 31))
        self.label_101.setFont(font)
        self.txtPrimerValor_13 = QLineEdit(self.tab_6)
        self.txtPrimerValor_13.setObjectName(u"txtPrimerValor_13")
        self.txtPrimerValor_13.setGeometry(QRect(330, 150, 81, 31))
        self.label_102 = QLabel(self.tab_6)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setGeometry(QRect(30, 200, 251, 31))
        self.label_102.setFont(font)
        self.txtTolerancia_10 = QLineEdit(self.tab_6)
        self.txtTolerancia_10.setObjectName(u"txtTolerancia_10")
        self.txtTolerancia_10.setGeometry(QRect(330, 200, 81, 31))
        self.label_103 = QLabel(self.tab_6)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setGeometry(QRect(30, 250, 281, 31))
        self.label_103.setFont(font)
        self.txtNmax_10 = QLineEdit(self.tab_6)
        self.txtNmax_10.setObjectName(u"txtNmax_10")
        self.txtNmax_10.setGeometry(QRect(330, 250, 81, 31))
        self.btnLimpiar_15 = QPushButton(self.tab_6)
        self.btnLimpiar_15.setObjectName(u"btnLimpiar_15")
        self.btnLimpiar_15.setGeometry(QRect(40, 300, 181, 41))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush13)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush21)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette7.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush21)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush13)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush21)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.Accent, brush19)
        self.btnLimpiar_15.setPalette(palette7)
        self.btnCalcular_15 = QPushButton(self.tab_6)
        self.btnCalcular_15.setObjectName(u"btnCalcular_15")
        self.btnCalcular_15.setGeometry(QRect(240, 300, 181, 41))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush13)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette8.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush21)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette8.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush13)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush21)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush13)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette8.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush21)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.Accent, brush19)
        self.btnCalcular_15.setPalette(palette8)
        self.label_161 = QLabel(self.tab_6)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setGeometry(QRect(580, 20, 111, 21))
        self.label_161.setFont(font1)
        self.label_162 = QLabel(self.tab_6)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setGeometry(QRect(490, 50, 161, 31))
        self.label_162.setFont(font)
        self.label_163 = QLabel(self.tab_6)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setGeometry(QRect(490, 100, 161, 31))
        self.label_163.setFont(font)
        self.label_164 = QLabel(self.tab_6)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setGeometry(QRect(490, 150, 161, 31))
        self.label_164.setFont(font)
        self.label_165 = QLabel(self.tab_6)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setGeometry(QRect(490, 200, 161, 31))
        self.label_165.setFont(font)
        self.label_166 = QLabel(self.tab_6)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setGeometry(QRect(490, 250, 161, 31))
        self.label_166.setFont(font)
        self.txtRaizRespuesta_25 = QLabel(self.tab_6)
        self.txtRaizRespuesta_25.setObjectName(u"txtRaizRespuesta_25")
        self.txtRaizRespuesta_25.setGeometry(QRect(660, 50, 141, 31))
        self.txtRaizRespuesta_25.setFont(font)
        self.txtRaizRespuesta_26 = QLabel(self.tab_6)
        self.txtRaizRespuesta_26.setObjectName(u"txtRaizRespuesta_26")
        self.txtRaizRespuesta_26.setGeometry(QRect(660, 100, 141, 31))
        self.txtRaizRespuesta_26.setFont(font)
        self.txtRaizRespuesta_27 = QLabel(self.tab_6)
        self.txtRaizRespuesta_27.setObjectName(u"txtRaizRespuesta_27")
        self.txtRaizRespuesta_27.setGeometry(QRect(660, 150, 141, 31))
        self.txtRaizRespuesta_27.setFont(font)
        self.txtRaizRespuesta_28 = QLabel(self.tab_6)
        self.txtRaizRespuesta_28.setObjectName(u"txtRaizRespuesta_28")
        self.txtRaizRespuesta_28.setGeometry(QRect(660, 200, 141, 31))
        self.txtRaizRespuesta_28.setFont(font)
        self.txtRaizRespuesta_29 = QLabel(self.tab_6)
        self.txtRaizRespuesta_29.setObjectName(u"txtRaizRespuesta_29")
        self.txtRaizRespuesta_29.setGeometry(QRect(660, 250, 141, 31))
        self.txtRaizRespuesta_29.setFont(font)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.label_167 = QLabel(self.tab_15)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setGeometry(QRect(40, 50, 161, 31))
        self.label_167.setFont(font)
        self.txtFuncion_17 = QLineEdit(self.tab_15)
        self.txtFuncion_17.setObjectName(u"txtFuncion_17")
        self.txtFuncion_17.setGeometry(QRect(200, 50, 221, 31))
        self.label_169 = QLabel(self.tab_15)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setGeometry(QRect(40, 150, 181, 31))
        self.label_169.setFont(font)
        self.label_170 = QLabel(self.tab_15)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setGeometry(QRect(40, 200, 251, 31))
        self.label_170.setFont(font)
        self.txtPrimerValor_23 = QLineEdit(self.tab_15)
        self.txtPrimerValor_23.setObjectName(u"txtPrimerValor_23")
        self.txtPrimerValor_23.setGeometry(QRect(340, 100, 81, 31))
        self.txtPrimerValor_24 = QLineEdit(self.tab_15)
        self.txtPrimerValor_24.setObjectName(u"txtPrimerValor_24")
        self.txtPrimerValor_24.setGeometry(QRect(340, 150, 81, 31))
        self.btnLimpiar_16 = QPushButton(self.tab_15)
        self.btnLimpiar_16.setObjectName(u"btnLimpiar_16")
        self.btnLimpiar_16.setGeometry(QRect(40, 300, 181, 41))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush13)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette9.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush21)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette9.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush13)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette9.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush21)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush13)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette9.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette9.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush21)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.Accent, brush19)
        self.btnLimpiar_16.setPalette(palette9)
        self.btnCalcular_20 = QPushButton(self.tab_15)
        self.btnCalcular_20.setObjectName(u"btnCalcular_20")
        self.btnCalcular_20.setGeometry(QRect(240, 300, 181, 41))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush13)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette10.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush21)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette10.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush13)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette10.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush21)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush13)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette10.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette10.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush21)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.Accent, brush19)
        self.btnCalcular_20.setPalette(palette10)
        self.label_219 = QLabel(self.tab_15)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setGeometry(QRect(580, 20, 111, 21))
        self.label_219.setFont(font1)
        self.label_220 = QLabel(self.tab_15)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setGeometry(QRect(490, 50, 161, 31))
        self.label_220.setFont(font)
        self.label_221 = QLabel(self.tab_15)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setGeometry(QRect(490, 100, 161, 31))
        self.label_221.setFont(font)
        self.label_222 = QLabel(self.tab_15)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setGeometry(QRect(490, 150, 161, 31))
        self.label_222.setFont(font)
        self.label_223 = QLabel(self.tab_15)
        self.label_223.setObjectName(u"label_223")
        self.label_223.setGeometry(QRect(490, 250, 161, 31))
        self.label_223.setFont(font)
        self.txtRaizRespuesta_41 = QLabel(self.tab_15)
        self.txtRaizRespuesta_41.setObjectName(u"txtRaizRespuesta_41")
        self.txtRaizRespuesta_41.setGeometry(QRect(660, 50, 141, 31))
        self.txtRaizRespuesta_41.setFont(font)
        self.txtRaizRespuesta_42 = QLabel(self.tab_15)
        self.txtRaizRespuesta_42.setObjectName(u"txtRaizRespuesta_42")
        self.txtRaizRespuesta_42.setGeometry(QRect(660, 100, 141, 31))
        self.txtRaizRespuesta_42.setFont(font)
        self.txtRaizRespuesta_43 = QLabel(self.tab_15)
        self.txtRaizRespuesta_43.setObjectName(u"txtRaizRespuesta_43")
        self.txtRaizRespuesta_43.setGeometry(QRect(660, 150, 141, 31))
        self.txtRaizRespuesta_43.setFont(font)
        self.txtRaizRespuesta_44 = QLabel(self.tab_15)
        self.txtRaizRespuesta_44.setObjectName(u"txtRaizRespuesta_44")
        self.txtRaizRespuesta_44.setGeometry(QRect(660, 210, 141, 31))
        self.txtRaizRespuesta_44.setFont(font)
        self.txtRaizRespuesta_45 = QLabel(self.tab_15)
        self.txtRaizRespuesta_45.setObjectName(u"txtRaizRespuesta_45")
        self.txtRaizRespuesta_45.setGeometry(QRect(660, 250, 141, 31))
        self.txtRaizRespuesta_45.setFont(font)
        self.txtTolerancia_11 = QLineEdit(self.tab_15)
        self.txtTolerancia_11.setObjectName(u"txtTolerancia_11")
        self.txtTolerancia_11.setGeometry(QRect(340, 200, 81, 31))
        self.label_104 = QLabel(self.tab_15)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setGeometry(QRect(40, 100, 181, 31))
        self.label_104.setFont(font)
        self.label_105 = QLabel(self.tab_15)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setGeometry(QRect(40, 250, 281, 31))
        self.label_105.setFont(font)
        self.txtNmax_11 = QLineEdit(self.tab_15)
        self.txtNmax_11.setObjectName(u"txtNmax_11")
        self.txtNmax_11.setGeometry(QRect(340, 250, 81, 31))
        self.label_168 = QLabel(self.tab_15)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setGeometry(QRect(490, 210, 161, 31))
        self.label_168.setFont(font)
        self.tabWidget_2.addTab(self.tab_15, "")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 796, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(2)
        
        self.btnCalcular_6.clicked.connect(self.calcularBiseccion)
        self.btnLimpiar_6.clicked.connect(self.limpiarBisseccion)
        
        #Eventos de botones Falsa Posicion
        self.btnCalcular_7.clicked.connect(self.calcularFalsaPosicion)
        self.btnLimpiar_7.clicked.connect(self.limpiarFalsaPosicion)
        
        #Eventos de botones Punto Fijo
        self.btnCalcular_5.clicked.connect(self.calcularPuntoFijo)
        self.btnLimpiar_5.clicked.connect(self.LimpiarPuntoFijo)
        
        #Eventos de botones de Newton
        self.btnCalcular_15.clicked.connect(self.calcularNewtonRaphson)
        
        #Eventos de botones de Secante
        self.btnCalcular_20.clicked.connect(self.calcularSecante)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Ingrese la funci\u00f3n: ", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Ingrese el primer valor inicial (a):", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Ingrese el segundo valor inicial (b):", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Ingrese la tolerancia deseada:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"N\u00famero m\u00e1ximo de interaciones:", None))
        self.btnCalcular_6.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Estimacion de Raiz: ", None))
        self.txtRaizRespuesta_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Tolerancia Final:", None))
        self.txtToleranciaRespuesta_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Valor final de \"a\":", None))
        self.txtAfinal_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Valor final de \"b\":", None))
        self.txtBfinal_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnLimpiar_6.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Iteracion final:", None))
        self.txtIteracionFinal_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.widget_2), QCoreApplication.translate("MainWindow", u"Bisecci\u00f3n", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Valor final de \"b\":", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Estimacion de Raiz: ", None))
        self.txtBfinal_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txtRaizRespuesta_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnCalcular_7.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Tolerancia Final:", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Ingrese la funci\u00f3n: ", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Ingrese el segundo valor inicial (b):", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.txtToleranciaRespuesta_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txtAfinal_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txtIteracionFinal_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Iteracion final:", None))
        self.btnLimpiar_7.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Ingrese la tolerancia deseada:", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Ingrese el primer valor inicial (a):", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Valor final de \"a\":", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"N\u00famero m\u00e1ximo de interaciones:", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Falsa Posici\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Metodos Abiertos", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Ingrese el valor de la aproximacion:", None))
        self.txtToleranciaRespuesta_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Tolerancia Final:", None))
        self.txtAfinal_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Ingrese la funci\u00f3n: ", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"N\u00famero m\u00e1ximo de interaciones:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Ingrese la tolerancia deseada:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Estimacion de Raiz: ", None))
        self.txtIteracionFinal_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Aproximacion Final:", None))
        self.btnCalcular_5.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Iteracion final:", None))
        self.btnLimpiar_5.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.txtRaizRespuesta_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Punto Fijo", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Ingrese la funci\u00f3n: ", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Ingrese el valor (Xo):", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Ingrese el valor (X1):", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Ingrese la tolerancia deseada:", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"N\u00famero m\u00e1ximo de interaciones:", None))
        self.btnLimpiar_15.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.btnCalcular_15.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"Estimacion de Raiz: ", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"Tolerancia Final:", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"Valor final de \"Xo\":", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"Valor final de \"X1\":", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"Iteracion final:", None))
        self.txtRaizRespuesta_25.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txtRaizRespuesta_26.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txtRaizRespuesta_27.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txtRaizRespuesta_28.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txtRaizRespuesta_29.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Newton-Raphson", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"Ingrese la funci\u00f3n: ", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"Ingrese el valor (X1):", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"Ingrese la tolerancia deseada:", None))
        self.btnLimpiar_16.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.btnCalcular_20.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label_219.setText(QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"Estimaci\u00f3n de Raiz: ", None))
        self.label_221.setText(QCoreApplication.translate("MainWindow", u"Tolerancia Final:", None))
        self.label_222.setText(QCoreApplication.translate("MainWindow", u"Valor final de \"Xo\":", None))
        self.label_223.setText(QCoreApplication.translate("MainWindow", u"Iteracion final:", None))
        self.txtRaizRespuesta_41.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txtRaizRespuesta_42.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txtRaizRespuesta_43.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txtRaizRespuesta_44.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txtRaizRespuesta_45.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Ingrese el valor (Xo):", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"N\u00famero m\u00e1ximo de interaciones:", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"Valor final de \"X1\":", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"Secante", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Metodos Cerrados", None))
    # retranslateUi



    
    
    def eval_func(self, expr, val):
            x = sp.symbols('x')
            return expr.subs(x, val)

    def biseccion(self, fx, a, b, e, nmax):
        expr = sp.sympify(fx)
        fa = self.eval_func(expr, a)
        fb = self.eval_func(expr, b)
        
        iteraciones = 0
        last_valid_iteration = None

        # Variables para guardar los valores de la ultima iteracion valida
        a_final = None
        b_final = None
        m_final = None
        fm_final = None
        tolerancia_final = None

        while iteraciones < nmax:
            m = (a + b) / 2
            fm = self.eval_func(expr, m)
            tolerancia_calculada = abs((b - a) / 2) * 100
            
            if tolerancia_calculada <= e:
                last_valid_iteration = iteraciones
                a_final = a
                b_final = b
                m_final = m
                fm_final = fm
                tolerancia_final = tolerancia_calculada
                break
            
            if fa * fm < 0:
                b = m
                fb = fm
            else:
                a = m
                fa = fm
            
            iteraciones += 1

        # Si no se alcanzo la tolerancia, guarda los ultimos valores calculados
        if a_final is None:
            a_final = a
            b_final = b
            m_final = m
            fm_final = fm
            tolerancia_final = tolerancia_calculada

        self.txtRaizRespuesta_6.setText(f"{m_final:.8f}")
        self.txtToleranciaRespuesta_6.setText(f"{tolerancia_final:.8f}")
        self.txtAfinal_6.setText(f"{a_final:.8f}")
        self.txtBfinal_5.setText(f"{b_final:.8f}")
        self.txtIteracionFinal_6.setText(f"{last_valid_iteration:.0f}")

    def calcularBiseccion(self):
        funcion = self.txtFuncion_6.text().strip()
        a_text = self.txtPrimerValor_6.text().strip()
        b_text = self.txtSegundoValor_6.text().strip()
        tol_text = self.txtTolerancia_6.text().strip()
        nmax_text = self.txtNmax_6.text().strip()

        # Validar si la función está vacía
        if not funcion:
            tkinter.messagebox.showinfo( "Entrada inválida", "Por favor, ingresa una función f(x).")
            return

        # Validar si el valor 'a' es un número
        try:
            a = float(a_text)
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "El valor 'a' debe ser un número.")
            return

        # Validar si el valor 'b' es un número
        try:
            b = float(b_text)
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "El valor 'b' debe ser un número.")
            return

        # Validar si la tolerancia es un número y positiva
        try:
            tol = float(tol_text)
            if tol <= 0:
                raise ValueError
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "La tolerancia debe ser un número positivo.")
            return

        # Validar si nmax es un entero y positivo
        try:
            nmax = int(nmax_text)
            if nmax <= 0:
                raise ValueError
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "El número máximo de iteraciones debe ser un entero positivo.")
            return

        # Si todas las validaciones pasan, ejecutar el método
        self.biseccion(funcion, a, b, tol, nmax)


    def limpiarBisseccion(self):
        self.txtFuncion_6.clear()
        self.txtTolerancia_6.clear()
        self.txtPrimerValor_6.clear()
        self.txtSegundoValor_6.clear()
        self.txtNmax_6.clear()
        
        self.txtRaizRespuesta_6.clear()
        self.txtAfinal_6.clear()
        self.txtBfinal_5.clear()
        self.txtToleranciaRespuesta_6.clear()
        self.txtIteracionFinal_6.clear()

    #Metodos Falsa Posicion
    def falsaPosicion(self, fx, a, b, e, nmax):
        expr = sp.sympify(fx)
        fa = self.eval_func(expr, a)
        fb = self.eval_func(expr, b)  # Inicializa fb aquí

        iteraciones = 0
        xrAnterior = None
        last_valid_iteration = None

        # Variables para guardar los valores de la última iteración válida
        a_final = None
        b_final = None
        xr_final = None
        fxr_final = None
        tolerancia_final = None

        while iteraciones < nmax:
            # Calcular xrActual
            xrActual = b - ((fb * (b - a)) / (fb - fa))
            fxr = self.eval_func(expr, xrActual)
            
            if xrAnterior is None:
                tolerancia_calculada = 100  # Inicialmente alta porque no hay valor anterior
            else:
                tolerancia_calculada = abs((xrActual - xrAnterior) / xrActual) * 100
            
            # Guardar valores de la última iteración válida
            if tolerancia_calculada <= e:
                last_valid_iteration = iteraciones + 1
                a_final = a
                b_final = b
                xr_final = xrActual
                fxr_final = fxr
                tolerancia_final = tolerancia_calculada
                break
            
            if fa * fxr < 0:
                b = xrActual
                fb = fxr  # Actualiza fb aquí
            else:
                a = xrActual
                fa = fxr  # Actualiza fa aquí
            
            xrAnterior = xrActual
            iteraciones += 1

        # Si no se alcanzó la tolerancia, guarda los últimos valores calculados
        if a_final is None:
            a_final = a
            b_final = b
            xr_final = xrActual
            fxr_final = fxr
            tolerancia_final = tolerancia_calculada

        # Retornar los valores finales para mostrarlos después
        self.txtIteracionFinal_7.setText(f"{iteraciones:.8f}")
        self.txtAfinal_7.setText(f"{a_final:.8f}")
        self.txtBfinal_6.setText(f"{b_final:.8f}")
        self.txtRaizRespuesta_7.setText(f"{xr_final:.8f}")
        self.txtToleranciaRespuesta_7.setText(f"{tolerancia_final:.8f}")
        self.txtIteracionFinal_7.setText(f"{last_valid_iteration:.0f}")
    
    def calcularFalsaPosicion(self):
        # Validar si la función está vacía
        if not self.txtFuncion_7.text().strip():
            tkinter.messagebox.showinfo("Entrada inválida", "Por favor, ingresa una función f(x).")
            return

        # Validar si el valor 'a' es un número
        try:
            a = float(self.txtPrimerValor_7.text())
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "El valor 'a' debe ser un número.")
            return

        # Validar si el valor 'b' es un número
        try:
            b = float(self.txtSegundoValor_7.text())
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "El valor 'b' debe ser un número.")
            return

        # Validar si la tolerancia es un número y positiva
        try:
            e = float(self.txtTolerancia_7.text())
            if e <= 0:
                raise ValueError
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "La tolerancia debe ser un número positivo.")
            return

        # Validar si nmax es un entero y positivo
        try:
            nmax = int(self.txtNmax_7.text())
            if nmax <= 0:
                raise ValueError
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "El número máximo de iteraciones debe ser un entero positivo.")
            return

        fx = self.txtFuncion_7.text().strip()
        
        # Si todas las validaciones pasan, ejecutar el método
        self.falsaPosicion(fx, a, b, e, nmax)
    
    def limpiarFalsaPosicion(self):
        self.txtFuncion_7.clear()
        self.txtTolerancia_7.clear()
        self.txtPrimerValor_7.clear()
        self.txtSegundoValor_7.clear()
        self.txtNmax_7.clear()
        
        self.txtRaizRespuesta_7.clear()
        self.txtAfinal_7.clear()
        self.txtBfinal_6.clear()
        self.txtToleranciaRespuesta_7.clear()
        self.txtIteracionFinal_7.clear()
    
    #Metodo de Punto Fijo
    def puntoFijo(self, gx, x0, e, nmax):
        expr = sp.sympify(gx)
        iteraciones = 0
        xrAnterior = None
        last_valid_iteration = None

        # Variables para guardar los valores de la ultima iteración valida
        x_final = None
        gx_final = None
        tolerancia_final = None

        while iteraciones < nmax:
            xrActual = self.eval_func(expr, x0)

            if xrAnterior is None:
                tolerancia_calculada = 100  # Inicialmente alta porque no hay valor anterior
            else:
                tolerancia_calculada = abs((xrActual - xrAnterior) / xrActual) * 100
            
            # Guardar valores de la ultima iteracion valida
            if tolerancia_calculada <= e:
                last_valid_iteration = iteraciones + 1
                x_final = xrActual
                gx_final = self.eval_func(expr, x_final)
                tolerancia_final = tolerancia_calculada
                break

            xrAnterior = xrActual
            x0 = xrActual  # Actualizar x0 para la proxima iteracion
            iteraciones += 1

        # Si no se alcanzo la tolerancia, guarda los ultimos valores calculados
        if x_final is None:
            x_final = xrActual
            gx_final = self.eval_func(expr, x_final)
            tolerancia_final = tolerancia_calculada

        # Retornar los valores finales para mostrarlos despues
        self.txtIteracionFinal_5.setText(f"{iteraciones:.0f}")
        self.txtRaizRespuesta_5.setText(f"{x_final:.8f}")
        self.txtAfinal_5.setText(f"{gx_final:.8f}")
        self.txtToleranciaRespuesta_5.setText(f"{tolerancia_final:.8f}")
    
    def calcularPuntoFijo(self):
        gx = self.txtFuncion_5.text().strip()
        x0_text = self.txtPrimerValor_5.text().strip()
        e_text = self.txtTolerancia_5.text().strip()
        nmax_text = self.txtNmax_5.text().strip()

        # Validar si la función está vacía
        if not gx:
            tkinter.messagebox.showinfo("Entrada inválida", "Por favor, ingresa una función g(x).")
            return

        # Validar si el valor inicial es un número
        try:
            x0 = float(x0_text)
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "El valor inicial debe ser un número.")
            return

        # Validar si la tolerancia es un número y positiva
        try:
            e = float(e_text)
            if e <= 0:
                raise ValueError
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "La tolerancia debe ser un número positivo.")
            return

        # Validar si nmax es un entero y positivo
        try:
            nmax = int(nmax_text)
            if nmax <= 0:
                raise ValueError
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "El número máximo de iteraciones debe ser un entero positivo.")
            return

        # Si todas las validaciones pasan, ejecutar el método
        self.puntoFijo(gx, x0, e, nmax)
    
    def LimpiarPuntoFijo(self):
        self.txtFuncion_5.clear()
        self.txtPrimerValor_5.clear()
        self.txtTolerancia_5.clear()
        self.txtNmax_5.clear()
        self.txtIteracionFinal_5.clear()
        self.txtRaizRespuesta_5.clear()
        self.txtAfinal_5.clear()
        self.txtToleranciaRespuesta_5.clear()
        
    #Metodos para  el metodo de Newton-Raphson
    def newtonRaphson(self, fx, x0, e, nmax):
        expr = sp.sympify(fx)
        deriv = sp.diff(expr, sp.Symbol('x'))
        iteraciones = 0
        xrAnterior = None
        last_valid_iteration = None

        # Variables para guardar los valores de la última iteración válida
        x0_final = x0  # Guardar el valor inicial
        x1_final = None
        fx_final = None
        tolerancia_final = None

        while iteraciones < nmax:
            fx_value = self.eval_func(expr, x0)
            fpx_value = self.eval_func(deriv, x0)
            if fpx_value == 0:
                tkinter.messagebox.showinfo("Error", "La derivada es cero. El método no puede continuar.")
                return

            xrActual = x0 - fx_value / fpx_value

            if xrAnterior is None:
                tolerancia_calculada = 100  # Inicialmente alta porque no hay valor anterior
            else:
                tolerancia_calculada = abs((xrActual - xrAnterior) / xrActual) * 100

            # Guardar valores de la última iteración válida
            if tolerancia_calculada <= e:
                last_valid_iteration = iteraciones + 1
                x0_final = x0  # Guardar el valor de x0 en esta iteración
                x1_final = xrActual  # Guardar el valor de x1 en esta iteración
                fx_final = self.eval_func(expr, x1_final)
                tolerancia_final = tolerancia_calculada
                break

            xrAnterior = xrActual
            x0 = xrActual  # Actualizar x0 para la próxima iteración
            iteraciones += 1

        # Si no se alcanzó la tolerancia, guarda los últimos valores calculados
        if x1_final is None:
            x0_final = x0  # Último valor de x0
            x1_final = xrActual  # Último valor de x1
            fx_final = self.eval_func(expr, x1_final)
            tolerancia_final = tolerancia_calculada

        # Retornar los valores finales para mostrarlos después
        self.txtRaizRespuesta_29.setText(f"{last_valid_iteration:.0f}")
        self.txtRaizRespuesta_25.setText(f"{x1_final:.8f}")
        self.txtRaizRespuesta_27.setText(f"{x0_final:.8f}")
        self.txtRaizRespuesta_26.setText(f"{tolerancia_final:.8f}")

        
    def calcularNewtonRaphson(self):
        fx = self.txtFuncion_10.text().strip()
        x0_text = self.txtPrimerValor_12.text().strip()
        e_text = self.txtTolerancia_10.text().strip()
        nmax_text = self.txtNmax_10.text().strip()

        # Validar si la función está vacía
        if not fx:
            tkinter.messagebox.showinfo("Entrada inválida", "Por favor, ingresa una función f(x).")
            return

        # Validar si el valor inicial es un número
        try:
            x0 = float(x0_text)
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "El valor inicial debe ser un número.")
            return

        # Validar si la tolerancia es un número y positiva
        try:
            e = float(e_text)
            if e <= 0:
                raise ValueError
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "La tolerancia debe ser un número positivo.")
            return

        # Validar si nmax es un entero y positivo
        try:
            nmax = int(nmax_text)
            if nmax <= 0:
                raise ValueError
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "El número máximo de iteraciones debe ser un entero positivo.")
            return

        # Si todas las validaciones pasan, ejecutar el método
        self.newtonRaphson(fx, x0, e, nmax)

    #Aca iria  el metodo limpiar newton raphson

    #Metodos de la secante
    def secante(self, fx, x0, e, nmax):
        expr = sp.sympify(fx)
        iteraciones = 0
        xrAnterior = None
        last_valid_iteration = None

        # Generar el segundo punto inicial como una pequeña perturbación de x0
        perturbacion = 0.1  # Pequeña perturbación para el punto x1
        x1 = x0 + perturbacion

        # Variables para guardar los valores de la última iteración válida
        x_final = None
        fx_final = None
        tolerancia_final = None

        while iteraciones < nmax:
            fx0 = self.eval_func(expr, x0)
            fx1 = self.eval_func(expr, x1)

            if fx1 - fx0 == 0:
                tkinter.messagebox.showinfo("Error", "División por cero en la secante. El método no puede continuar.")
                return

            xrActual = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

            if xrAnterior is None:
                tolerancia_calculada = 100  # Inicialmente alta porque no hay valor anterior
            else:
                tolerancia_calculada = abs((xrActual - xrAnterior) / xrActual) * 100

            # Guardar valores de la última iteración válida
            if tolerancia_calculada <= e:
                last_valid_iteration = iteraciones + 1
                x_final = xrActual
                fx_final = self.eval_func(expr, x_final)
                tolerancia_final = tolerancia_calculada
                break

            xrAnterior = xrActual
            x0 = x1  # Actualizar x0 para la próxima iteración
            x1 = xrActual  # Actualizar x1 para la próxima iteración
            iteraciones += 1

        # Si no se alcanzó la tolerancia, guarda los últimos valores calculados
        if x_final is None:
            x_final = xrActual
            fx_final = self.eval_func(expr, x_final)
            tolerancia_final = tolerancia_calculada

        # Retornar los valores finales para mostrarlos después
        self.txtRaizRespuesta_45.setText(f"{last_valid_iteration if last_valid_iteration is not None else iteraciones:.0f}")
        self.txtRaizRespuesta_41.setText(f"{x_final:.8f}")
        self.txtRaizRespuesta_43.setText(f"{fx_final:.8f}")
        self.txtRaizRespuesta_42.setText(f"{tolerancia_final:.8f}")

    
    def calcularSecante(self):
        fx = self.txtFuncion_17.text().strip()
        x0_text = self.txtPrimerValor_23.text().strip()
        e_text = self.txtTolerancia_11.text().strip()
        nmax_text = self.txtNmax_11.text().strip()

        # Validar si la función está vacía
        if not fx:
            tkinter.messagebox.showinfo("Entrada inválida", "Por favor, ingresa una función f(x).")
            return

        # Validar si el valor inicial x0 es un número
        try:
            x0 = float(x0_text)
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "El valor inicial x0 debe ser un número.")
            return


        # Validar si la tolerancia es un número y positiva
        try:
            e = float(e_text)
            if e <= 0:
                raise ValueError
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "La tolerancia debe ser un número positivo.")
            return

        # Validar si nmax es un entero y positivo
        try:
            nmax = int(nmax_text)
            if nmax <= 0:
                raise ValueError
        except ValueError:
            tkinter.messagebox.showinfo("Entrada inválida", "El número máximo de iteraciones debe ser un entero positivo.")
            return

        # Si todas las validaciones pasan, ejecutar el método
        self.secante(fx, x0, e, nmax)



        

        