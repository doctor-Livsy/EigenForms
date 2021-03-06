import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from PyQt5.QtCore import pyqtSignal
import bdf_reading
from multiprocessing import freeze_support


class UiMainWindow(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(333, 355)
        main_window.setMinimumSize(QtCore.QSize(333, 355))
        main_window.setMaximumSize(QtCore.QSize(333, 355))
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setMinimumSize(QtCore.QSize(300, 355))
        self.centralwidget.setMaximumSize(QtCore.QSize(340, 355))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 198, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 226, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 99, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 132, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 198, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 226, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 198, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 226, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 99, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 132, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 198, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 226, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 99, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 198, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 226, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 99, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 132, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 99, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 99, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 198, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 198, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 198, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(5, 10, 322, 334))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.selectfiles = QtWidgets.QGroupBox(self.layoutWidget)
        self.selectfiles.setMinimumSize(QtCore.QSize(320, 85))
        self.selectfiles.setMaximumSize(QtCore.QSize(280, 85))
        self.selectfiles.setObjectName("selectfiles")
        self.gridLayout = QtWidgets.QGridLayout(self.selectfiles)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.op2 = QtWidgets.QLabel(self.selectfiles)
        self.op2.setObjectName("op2")
        self.horizontalLayout_6.addWidget(self.op2)
        self.lineEdit_op2 = QtWidgets.QLineEdit(self.selectfiles)
        self.lineEdit_op2.setObjectName("lineEdit_op2")
        self.horizontalLayout_6.addWidget(self.lineEdit_op2)
        self.op2_tb = QtWidgets.QToolButton(self.selectfiles)
        self.op2_tb.setObjectName("op2_tb")
        self.horizontalLayout_6.addWidget(self.op2_tb)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bdf = QtWidgets.QLabel(self.selectfiles)
        self.bdf.setObjectName("bdf")
        self.horizontalLayout_5.addWidget(self.bdf)
        self.lineEdit_bdf = QtWidgets.QLineEdit(self.selectfiles)
        self.lineEdit_bdf.setObjectName("lineEdit_bdf")
        self.horizontalLayout_5.addWidget(self.lineEdit_bdf)
        self.bdf_tb = QtWidgets.QToolButton(self.selectfiles)
        self.bdf_tb.setObjectName("bdf_tb")
        self.horizontalLayout_5.addWidget(self.bdf_tb)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.selectfiles, 0, 0, 1, 1)
        self.CancelOk = QtWidgets.QHBoxLayout()
        self.CancelOk.setObjectName("CancelOk")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.CancelOk.addItem(spacerItem)
        self.Cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.Cancel.setObjectName("Cancel")
        self.CancelOk.addWidget(self.Cancel)
        self.OK = QtWidgets.QPushButton(self.layoutWidget)
        self.OK.setObjectName("OK")
        self.CancelOk.addWidget(self.OK)
        self.gridLayout_5.addLayout(self.CancelOk, 3, 0, 1, 1)
        self.status_box = QtWidgets.QGroupBox(self.layoutWidget)
        self.status_box.setMinimumSize(QtCore.QSize(320, 80))
        self.status_box.setMaximumSize(QtCore.QSize(280, 100))
        self.status_box.setObjectName("status_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.status_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.status_label = QtWidgets.QLabel(self.status_box)
        self.status_label.setMinimumSize(QtCore.QSize(300, 20))
        self.status_label.setMaximumSize(QtCore.QSize(260, 20))
        self.status_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.status_label.setText("")
        self.status_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.status_label.setObjectName("status_label")
        self.gridLayout_2.addWidget(self.status_label, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.status_box)
        self.progressBar.setMinimumSize(QtCore.QSize(300, 25))
        self.progressBar.setMaximumSize(QtCore.QSize(260, 25))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.status_box, 2, 0, 1, 1)
        self.param = QtWidgets.QGroupBox(self.layoutWidget)
        self.param.setMinimumSize(QtCore.QSize(320, 120))
        self.param.setMaximumSize(QtCore.QSize(280, 120))
        self.param.setObjectName("param")
        self.widget = QtWidgets.QWidget(self.param)
        self.widget.setGeometry(QtCore.QRect(5, 25, 313, 82))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.XYswap = QtWidgets.QRadioButton(self.widget)
        self.XYswap.setObjectName("XYswap")
        self.verticalLayout.addWidget(self.XYswap)
        self.XZswap = QtWidgets.QRadioButton(self.widget)
        self.XZswap.setObjectName("XZswap")
        self.verticalLayout.addWidget(self.XZswap)
        self.YZswap = QtWidgets.QRadioButton(self.widget)
        self.YZswap.setObjectName("YZswap")
        self.YZswap.setChecked(True)
        self.verticalLayout.addWidget(self.YZswap)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 68, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deformmultipler = QtWidgets.QLabel(self.widget)
        self.deformmultipler.setMaximumSize(QtCore.QSize(120, 100))
        self.deformmultipler.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.deformmultipler.setObjectName("deformmultipler")
        self.horizontalLayout.addWidget(self.deformmultipler)
        self.def_spinbox = QtWidgets.QSpinBox(self.widget)
        self.def_spinbox.setMinimumSize(QtCore.QSize(70, 20))
        self.def_spinbox.setMaximumSize(QtCore.QSize(70, 20))
        self.def_spinbox.setMaximum(100000)
        self.def_spinbox.setSingleStep(10)
        self.def_spinbox.setProperty("value", 2000)
        self.def_spinbox.setObjectName("def_spinbox")
        self.horizontalLayout.addWidget(self.def_spinbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.scale = QtWidgets.QHBoxLayout()
        self.scale.setObjectName("scale")
        self.newscale = QtWidgets.QLabel(self.widget)
        self.newscale.setMaximumSize(QtCore.QSize(100, 100))
        self.newscale.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.newscale.setObjectName("newscale")
        self.scale.addWidget(self.newscale)
        self.scale_spinbox = QtWidgets.QDoubleSpinBox(self.widget)
        self.scale_spinbox.setMinimumSize(QtCore.QSize(70, 20))
        self.scale_spinbox.setMaximumSize(QtCore.QSize(70, 20))
        self.scale_spinbox.setDecimals(1)
        self.scale_spinbox.setMaximum(10.0)
        self.scale_spinbox.setSingleStep(0.1)
        self.scale_spinbox.setProperty("value", 0.9)
        self.scale_spinbox.setObjectName("scale_spinbox")
        self.scale.addWidget(self.scale_spinbox)
        self.verticalLayout_2.addLayout(self.scale)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dpi = QtWidgets.QLabel(self.widget)
        self.dpi.setMaximumSize(QtCore.QSize(100, 100))
        self.dpi.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dpi.setObjectName("dpi")
        self.horizontalLayout_2.addWidget(self.dpi)
        self.dpi_spinBox = QtWidgets.QSpinBox(self.widget)
        self.dpi_spinBox.setMinimumSize(QtCore.QSize(70, 20))
        self.dpi_spinBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.dpi_spinBox.setMaximum(1000)
        self.dpi_spinBox.setSingleStep(100)
        self.dpi_spinBox.setProperty("value", 300)
        self.dpi_spinBox.setObjectName("dpi_spinBox")
        self.horizontalLayout_2.addWidget(self.dpi_spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_5.addWidget(self.param, 1, 0, 1, 1)
        self.canceled = 0
        main_window.setCentralWidget(self.centralwidget)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EigenForms"))
        self.selectfiles.setTitle(_translate("MainWindow", "Select files"))
        self.op2.setText(_translate("MainWindow", "OP2"))
        self.op2_tb.setText(_translate("MainWindow", "..."))
        self.bdf.setText(_translate("MainWindow", "BDF"))
        self.bdf_tb.setText(_translate("MainWindow", "..."))
        self.Cancel.setText(_translate("MainWindow", "Cancel"))
        self.OK.setText(_translate("MainWindow", "OK"))
        self.status_box.setTitle(_translate("MainWindow", "Status"))
        self.param.setTitle(_translate("MainWindow", "Parameters"))
        self.XYswap.setText(_translate("MainWindow", "XY replace"))
        self.XZswap.setText(_translate("MainWindow", "XZ replace"))
        self.YZswap.setText(_translate("MainWindow", "YZ replace"))
        self.deformmultipler.setText(_translate("MainWindow", "Deformation multiplier"))
        self.newscale.setText(_translate("MainWindow", "View scale"))
        self.dpi.setText(_translate("MainWindow", "Picture DPI"))

    def status_update(self, number, percent):
        self.progressBar.setValue(percent)
        self.status_label.setText(f' mode ??? {number} created.')

    def status_start(self):
        self.selectfiles.setEnabled(False)
        self.param.setEnabled(False)
        self.OK.setEnabled(False)
        self.progressBar.setValue(0)
        self.status_label.setText('Start of creating images...')

    def status_end(self):
        if self.canceled != 1:
            self.status_label.setText('Images created. Check directory.')
        if self.canceled == 1:
            self.status_label.setText('Cancel clicked. Try again.')
        self.progressBar.setValue(0)
        self.OK.setEnabled(True)
        self.param.setEnabled(True)
        self.selectfiles.setEnabled(True)

    def set_canceled(self, a):
        self.canceled = a


class MySignals(QtCore.QObject):
    signal_update = pyqtSignal(int, int)
    signal_start = pyqtSignal()
    signal_end = pyqtSignal()

    def emit_update(self, number, percent):
        self.signal_update.emit(number, percent)

    def emit_start(self):
        self.signal_start.emit()

    def emit_end(self):
        self.signal_end.emit()


def thread(my_func):
    """
    ?????????????????? ?????????????? ?? ?????????????????? ????????????
    """

    def wrapper():
        my_thread = threading.Thread(target=my_func, name='bdf_reading')
        my_thread.setDaemon(True)
        my_thread.start()

    return wrapper


def get_file(object_to_paste, file_mask='*.*'):
    def wrapper():
        file_name = QtWidgets.QFileDialog.getOpenFileName(filter=file_mask)
        object_to_paste.setText(str(file_name[0]))

    return wrapper


@thread
def go_to_main():
    op2_name = ui.lineEdit_op2.text()
    bdf_name = ui.lineEdit_bdf.text()
    deform_multipler = ui.def_spinbox.value()
    coef_scale = ui.scale_spinbox.value()
    dpi = ui.dpi_spinBox.value()

    swap = 1
    if ui.XYswap.isChecked():
        swap = 1
    elif ui.XZswap.isChecked():
        swap = 2
    elif ui.YZswap.isChecked():
        swap = 3

    ui.set_canceled(0)
    MySignals.emit_start()
    bdf_reading.main(op2_name, bdf_name, deform_multipler, coef_scale, dpi, swap, MySignals, exit_thread)
    MySignals.emit_end()
    exit_thread.clear()


def prog_exit():
    ui.set_canceled(1)
    for thread in threading.enumerate():
        if thread.name == 'bdf_reading':
            print('Cancel clicked')
            exit_thread.set()


if __name__ == "__main__":
    # On Windows calling this function is necessary.
    freeze_support()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(MainWindow)
    my_signals = MySignals()
    my_signals.signal_update.connect(ui.status_update)
    my_signals.signal_start.connect(ui.status_start)
    my_signals.signal_end.connect(ui.status_end)
    MainWindow.show()
    MainWindow.setFocus()
    exit_thread = threading.Event()

    ui.op2_tb.clicked.connect(get_file(ui.lineEdit_op2, file_mask='*.op2'))
    ui.bdf_tb.clicked.connect(get_file(ui.lineEdit_bdf, file_mask='*.bdf'))
    ui.OK.clicked.connect(go_to_main)
    ui.Cancel.clicked.connect(prog_exit)
    sys.exit(app.exec_())
