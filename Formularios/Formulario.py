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
        MainWindow.resize(796, 447)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 801, 401))
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
        self.label_56.setGeometry(QRect(30, 150, 271, 31))
        self.label_56.setFont(font)
        self.label_57 = QLabel(self.widget_2)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(30, 200, 291, 31))
        self.label_57.setFont(font)
        self.label_58 = QLabel(self.widget_2)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(30, 250, 251, 31))
        self.label_58.setFont(font)
        self.label_59 = QLabel(self.widget_2)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(30, 100, 281, 31))
        self.label_59.setFont(font)
        self.txtFuncion_6 = QLineEdit(self.widget_2)
        self.txtFuncion_6.setObjectName(u"txtFuncion_6")
        self.txtFuncion_6.setGeometry(QRect(190, 50, 221, 31))
        self.txtTolerancia_6 = QLineEdit(self.widget_2)
        self.txtTolerancia_6.setObjectName(u"txtTolerancia_6")
        self.txtTolerancia_6.setGeometry(QRect(330, 250, 81, 31))
        self.txtPrimerValor_6 = QLineEdit(self.widget_2)
        self.txtPrimerValor_6.setObjectName(u"txtPrimerValor_6")
        self.txtPrimerValor_6.setGeometry(QRect(330, 150, 81, 31))
        self.txtNmax_6 = QLineEdit(self.widget_2)
        self.txtNmax_6.setObjectName(u"txtNmax_6")
        self.txtNmax_6.setGeometry(QRect(330, 100, 81, 31))
        self.txtSegundoValor_6 = QLineEdit(self.widget_2)
        self.txtSegundoValor_6.setObjectName(u"txtSegundoValor_6")
        self.txtSegundoValor_6.setGeometry(QRect(330, 200, 81, 31))
        self.btnCalcular_6 = QPushButton(self.widget_2)
        self.btnCalcular_6.setObjectName(u"btnCalcular_6")
        self.btnCalcular_6.setGeometry(QRect(230, 300, 181, 41))
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
        self.txtPrimerValor_7.setGeometry(QRect(340, 150, 81, 31))
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
        self.txtFuncion_7 = QLineEdit(self.tab_7)
        self.txtFuncion_7.setObjectName(u"txtFuncion_7")
        self.txtFuncion_7.setGeometry(QRect(200, 50, 221, 31))
        self.label_68 = QLabel(self.tab_7)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(490, 100, 161, 31))
        self.label_68.setFont(font)
        self.txtNmax_7 = QLineEdit(self.tab_7)
        self.txtNmax_7.setObjectName(u"txtNmax_7")
        self.txtNmax_7.setGeometry(QRect(340, 100, 81, 31))
        self.label_69 = QLabel(self.tab_7)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(40, 50, 161, 31))
        self.label_69.setFont(font)
        self.txtSegundoValor_7 = QLineEdit(self.tab_7)
        self.txtSegundoValor_7.setObjectName(u"txtSegundoValor_7")
        self.txtSegundoValor_7.setGeometry(QRect(340, 200, 81, 31))
        self.label_70 = QLabel(self.tab_7)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(40, 200, 291, 31))
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
        self.txtTolerancia_7 = QLineEdit(self.tab_7)
        self.txtTolerancia_7.setObjectName(u"txtTolerancia_7")
        self.txtTolerancia_7.setGeometry(QRect(340, 250, 81, 31))
        self.label_73 = QLabel(self.tab_7)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(40, 250, 251, 31))
        self.label_73.setFont(font)
        self.label_74 = QLabel(self.tab_7)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(40, 150, 271, 31))
        self.label_74.setFont(font)
        self.label_75 = QLabel(self.tab_7)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(490, 150, 161, 31))
        self.label_75.setFont(font)
        self.label_76 = QLabel(self.tab_7)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(40, 100, 281, 31))
        self.label_76.setFont(font)
        self.tabWidget_3.addTab(self.tab_7, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_2 = QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 801, 381))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_45 = QLabel(self.tab_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(20, 145, 301, 31))
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
        self.txtPrimerValor_5.setGeometry(QRect(320, 145, 81, 31))
        self.label_48 = QLabel(self.tab_3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(20, 95, 281, 31))
        self.label_48.setFont(font)
        self.label_49 = QLabel(self.tab_3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(20, 190, 251, 31))
        self.label_49.setFont(font)
        self.txtNmax_5 = QLineEdit(self.tab_3)
        self.txtNmax_5.setObjectName(u"txtNmax_5")
        self.txtNmax_5.setGeometry(QRect(320, 95, 81, 31))
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
        self.txtTolerancia_5.setGeometry(QRect(320, 190, 81, 31))
        self.btnCalcular_5 = QPushButton(self.tab_3)
        self.btnCalcular_5.setObjectName(u"btnCalcular_5")
        self.btnCalcular_5.setGeometry(QRect(220, 240, 181, 41))
        self.label_53 = QLabel(self.tab_3)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(470, 245, 161, 31))
        self.label_53.setFont(font)
        self.btnLimpiar_5 = QPushButton(self.tab_3)
        self.btnLimpiar_5.setObjectName(u"btnLimpiar_5")
        self.btnLimpiar_5.setGeometry(QRect(20, 240, 181, 41))
        self.txtRaizRespuesta_5 = QLabel(self.tab_3)
        self.txtRaizRespuesta_5.setObjectName(u"txtRaizRespuesta_5")
        self.txtRaizRespuesta_5.setGeometry(QRect(640, 100, 141, 31))
        self.txtRaizRespuesta_5.setFont(font)
        self.label_55 = QLabel(self.tab_3)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(560, 65, 111, 21))
        self.label_55.setFont(font1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 796, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        
        #Eventos de botones de biseccion
        self.btnCalcular_6.clicked.connect(self.calcularBiseccion)
        self.btnLimpiar_6.clicked.connect(self.limpiarBisseccion)
        
        #Eventos de botones Falsa Posicion
        self.btnCalcular_7.clicked.connect(self.calcularFalsaPosicion)
        self.btnLimpiar_7.clicked.connect(self.limpiarFalsaPosicion)
        
        #Eventos de botones Punto Fijo
        self.btnCalcular_5.clicked.connect(self.calcularPuntoFijo)
        self.btnLimpiar_5.clicked.connect(self.LimpiarPuntoFijo)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Ingrese la funcion: ", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Ingrese el primer valor inicial (a):", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Ingrese el segundo valor inicial (b):", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Ingrese la tolerancia deseada:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Numero maximo de interaciones:", None))
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
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.widget_2), QCoreApplication.translate("MainWindow", u"Biseccion", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Valor final de \"b\":", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Estimacion de Raiz: ", None))
        self.txtBfinal_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txtRaizRespuesta_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnCalcular_7.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Tolerancia Final:", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Ingrese la funcion: ", None))
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
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Numero maximo de interaciones:", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Regula Falsi", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Metodos Abiertos", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Ingrese el valor de la aproximacion:", None))
        self.txtToleranciaRespuesta_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Tolerancia Final:", None))
        self.txtAfinal_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Ingrese la funcion: ", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Numero maximo de interaciones:", None))
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
        

        