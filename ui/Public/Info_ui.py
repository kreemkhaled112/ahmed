# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p:\API\ahmed\ui\Public\Info.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(722, 347)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_1 = QtWidgets.QWidget(Form)
        self.widget_1.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_1.setObjectName("widget_1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_1)
        self.gridLayout_4.setContentsMargins(5, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.widget_1)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.widget_Info = QtWidgets.QWidget(self.widget_2)
        self.widget_Info.setObjectName("widget_Info")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.widget_Info)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.successful1 = QtWidgets.QLabel(self.widget_Info)
        self.successful1.setObjectName("successful1")
        self.horizontalLayout_31.addWidget(self.successful1)
        self.successful = QtWidgets.QLabel(self.widget_Info)
        self.successful.setStyleSheet(" QLabel {\n"
"    color: rgb(0, 170, 127);\n"
"    }")
        self.successful.setObjectName("successful")
        self.horizontalLayout_31.addWidget(self.successful)
        self.label_28 = QtWidgets.QLabel(self.widget_Info)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_31.addWidget(self.label_28)
        self.faild = QtWidgets.QLabel(self.widget_Info)
        self.faild.setStyleSheet(" QLabel {\n"
"color: rgb(255, 0, 0);\n"
"    }")
        self.faild.setObjectName("faild")
        self.horizontalLayout_31.addWidget(self.faild)
        self.label_29 = QtWidgets.QLabel(self.widget_Info)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_31.addWidget(self.label_29)
        self.total = QtWidgets.QLabel(self.widget_Info)
        self.total.setStyleSheet(" QLabel {\n"
"color: rgb(0, 170, 127);\n"
"    }\n"
"")
        self.total.setObjectName("total")
        self.horizontalLayout_31.addWidget(self.total)
        self.label_34 = QtWidgets.QLabel(self.widget_Info)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_31.addWidget(self.label_34)
        self.order = QtWidgets.QLabel(self.widget_Info)
        self.order.setStyleSheet("color: rgb(51, 255, 163);")
        self.order.setObjectName("order")
        self.horizontalLayout_31.addWidget(self.order)
        self.horizontalLayout.addWidget(self.widget_Info)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.gridLayout_4.addWidget(self.widget_2, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.table = QtWidgets.QTableWidget(self.widget_1)
        self.table.setObjectName("table")
        self.table.setColumnCount(6)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        self.gridLayout_4.addWidget(self.table, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_1, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.pushButton_4.toggled['bool'].connect(self.table.setVisible) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.successful1.setText(_translate("Form", "Succeful :"))
        self.successful.setText(_translate("Form", "0"))
        self.label_28.setText(_translate("Form", "Failed :"))
        self.faild.setText(_translate("Form", "0"))
        self.label_29.setText(_translate("Form", "Total :"))
        self.total.setText(_translate("Form", "0"))
        self.label_34.setText(_translate("Form", "Order:"))
        self.order.setText(_translate("Form", "0"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Id"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Date"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Name"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Acction"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Message"))
import resource_rc
