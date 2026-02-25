# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coordinator.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QSplitter, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2040, 1147)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionShow_IP_address = QAction(MainWindow)
        self.actionShow_IP_address.setObjectName(u"actionShow_IP_address")
        self.action_convert_h264_video_files = QAction(MainWindow)
        self.action_convert_h264_video_files.setObjectName(u"action_convert_h264_video_files")
        self.actionEdit_parameters = QAction(MainWindow)
        self.actionEdit_parameters.setObjectName(u"actionEdit_parameters")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_34 = QLabel(self.centralwidget)
        self.label_34.setObjectName(u"label_34")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_34.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_34)

        self.get_status_all_pb = QPushButton(self.centralwidget)
        self.get_status_all_pb.setObjectName(u"get_status_all_pb")

        self.horizontalLayout_12.addWidget(self.get_status_all_pb)

        self.time_synchro_all_pb = QPushButton(self.centralwidget)
        self.time_synchro_all_pb.setObjectName(u"time_synchro_all_pb")

        self.horizontalLayout_12.addWidget(self.time_synchro_all_pb)

        self.shutdown_all_pb = QPushButton(self.centralwidget)
        self.shutdown_all_pb.setObjectName(u"shutdown_all_pb")

        self.horizontalLayout_12.addWidget(self.shutdown_all_pb)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_16)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.main_tw = QTabWidget(self.centralwidget)
        self.main_tw.setObjectName(u"main_tw")
        self.rasp_list_tab = QWidget()
        self.rasp_list_tab.setObjectName(u"rasp_list_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.rasp_list_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.splitter = QSplitter(self.rasp_list_tab)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_scan_network = QPushButton(self.layoutWidget)
        self.pb_scan_network.setObjectName(u"pb_scan_network")

        self.horizontalLayout.addWidget(self.pb_scan_network)

        self.pb_up = QPushButton(self.layoutWidget)
        self.pb_up.setObjectName(u"pb_up")

        self.horizontalLayout.addWidget(self.pb_up)

        self.pb_down = QPushButton(self.layoutWidget)
        self.pb_down.setObjectName(u"pb_down")

        self.horizontalLayout.addWidget(self.pb_down)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.rpi_list = QListWidget(self.layoutWidget)
        self.rpi_list.setObjectName(u"rpi_list")

        self.verticalLayout.addWidget(self.rpi_list)

        self.message_box = QLineEdit(self.layoutWidget)
        self.message_box.setObjectName(u"message_box")

        self.verticalLayout.addWidget(self.message_box)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.raspberry_id_lb = QLabel(self.layoutWidget1)
        self.raspberry_id_lb.setObjectName(u"raspberry_id_lb")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.raspberry_id_lb.setFont(font1)

        self.verticalLayout_3.addWidget(self.raspberry_id_lb)

        self.rpi_tw = QTabWidget(self.layoutWidget1)
        self.rpi_tw.setObjectName(u"rpi_tw")
        self.rpi_tw.setEnabled(False)
        self.status_tab = QWidget()
        self.status_tab.setObjectName(u"status_tab")
        self.verticalLayout_5 = QVBoxLayout(self.status_tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_22 = QLabel(self.status_tab)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 11, 0, 1, 1)

        self.free_sd_space_lb = QLabel(self.status_tab)
        self.free_sd_space_lb.setObjectName(u"free_sd_space_lb")

        self.gridLayout.addWidget(self.free_sd_space_lb, 6, 1, 1, 1)

        self.wifi_essid_lb = QLabel(self.status_tab)
        self.wifi_essid_lb.setObjectName(u"wifi_essid_lb")

        self.gridLayout.addWidget(self.wifi_essid_lb, 4, 1, 1, 1)

        self.time_lapse_active_lb = QLabel(self.status_tab)
        self.time_lapse_active_lb.setObjectName(u"time_lapse_active_lb")

        self.gridLayout.addWidget(self.time_lapse_active_lb, 11, 1, 1, 1)

        self.label_2 = QLabel(self.status_tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.video_recording_active_lb = QLabel(self.status_tab)
        self.video_recording_active_lb.setObjectName(u"video_recording_active_lb")

        self.gridLayout.addWidget(self.video_recording_active_lb, 9, 1, 1, 1)

        self.datetime_lb = QLabel(self.status_tab)
        self.datetime_lb.setObjectName(u"datetime_lb")

        self.gridLayout.addWidget(self.datetime_lb, 2, 1, 1, 1)

        self.label = QLabel(self.status_tab)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.status_tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_8 = QLabel(self.status_tab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.camera_detected_lb = QLabel(self.status_tab)
        self.camera_detected_lb.setObjectName(u"camera_detected_lb")

        self.gridLayout.addWidget(self.camera_detected_lb, 7, 1, 1, 1)

        self.ip_address_lb = QLabel(self.status_tab)
        self.ip_address_lb.setObjectName(u"ip_address_lb")

        self.gridLayout.addWidget(self.ip_address_lb, 1, 1, 1, 1)

        self.cpu_temp_lb = QLabel(self.status_tab)
        self.cpu_temp_lb.setObjectName(u"cpu_temp_lb")

        self.gridLayout.addWidget(self.cpu_temp_lb, 3, 1, 1, 1)

        self.label_12 = QLabel(self.status_tab)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_10 = QLabel(self.status_tab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)

        self.label_14 = QLabel(self.status_tab)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 10, 0, 1, 1)

        self.label_9 = QLabel(self.status_tab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)

        self.label_13 = QLabel(self.status_tab)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 9, 0, 1, 1)

        self.label_11 = QLabel(self.status_tab)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 8, 0, 1, 1)

        self.uptime_lb = QLabel(self.status_tab)
        self.uptime_lb.setObjectName(u"uptime_lb")

        self.gridLayout.addWidget(self.uptime_lb, 8, 1, 1, 1)

        self.video_streaming_active_lb = QLabel(self.status_tab)
        self.video_streaming_active_lb.setObjectName(u"video_streaming_active_lb")

        self.gridLayout.addWidget(self.video_streaming_active_lb, 10, 1, 1, 1)

        self.status_lb = QLabel(self.status_tab)
        self.status_lb.setObjectName(u"status_lb")

        self.gridLayout.addWidget(self.status_lb, 0, 1, 1, 1)

        self.label_23 = QLabel(self.status_tab)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 5, 0, 1, 1)

        self.server_version_lb = QLabel(self.status_tab)
        self.server_version_lb.setObjectName(u"server_version_lb")

        self.gridLayout.addWidget(self.server_version_lb, 5, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.status_update_pb = QPushButton(self.status_tab)
        self.status_update_pb.setObjectName(u"status_update_pb")

        self.horizontalLayout_4.addWidget(self.status_update_pb)

        self.time_synchro_pb = QPushButton(self.status_tab)
        self.time_synchro_pb.setObjectName(u"time_synchro_pb")

        self.horizontalLayout_4.addWidget(self.time_synchro_pb)

        self.get_log_pb = QPushButton(self.status_tab)
        self.get_log_pb.setObjectName(u"get_log_pb")

        self.horizontalLayout_4.addWidget(self.get_log_pb)

        self.blink_pb = QPushButton(self.status_tab)
        self.blink_pb.setObjectName(u"blink_pb")

        self.horizontalLayout_4.addWidget(self.blink_pb)

        self.pb_send_command = QPushButton(self.status_tab)
        self.pb_send_command.setObjectName(u"pb_send_command")

        self.horizontalLayout_4.addWidget(self.pb_send_command)

        self.reboot_pb = QPushButton(self.status_tab)
        self.reboot_pb.setObjectName(u"reboot_pb")

        self.horizontalLayout_4.addWidget(self.reboot_pb)

        self.shutdown_pb = QPushButton(self.status_tab)
        self.shutdown_pb.setObjectName(u"shutdown_pb")

        self.horizontalLayout_4.addWidget(self.shutdown_pb)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.rpi_tw.addTab(self.status_tab, "")
        self.picture_tab = QWidget()
        self.picture_tab.setObjectName(u"picture_tab")
        self.verticalLayout_21 = QVBoxLayout(self.picture_tab)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.scrollArea_2 = QScrollArea(self.picture_tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1387, 485))
        self.verticalLayout_23 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.picture_resolution_cb = QComboBox(self.groupBox_5)
        self.picture_resolution_cb.setObjectName(u"picture_resolution_cb")
        self.picture_resolution_cb.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.picture_resolution_cb)

        self.label_19 = QLabel(self.groupBox_5)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_2.addWidget(self.label_19)

        self.picture_rotation_sb = QSpinBox(self.groupBox_5)
        self.picture_rotation_sb.setObjectName(u"picture_rotation_sb")
        self.picture_rotation_sb.setMaximum(180)
        self.picture_rotation_sb.setSingleStep(180)

        self.horizontalLayout_2.addWidget(self.picture_rotation_sb)

        self.picture_hflip_cb = QCheckBox(self.groupBox_5)
        self.picture_hflip_cb.setObjectName(u"picture_hflip_cb")

        self.horizontalLayout_2.addWidget(self.picture_hflip_cb)

        self.picture_vflip_cb = QCheckBox(self.groupBox_5)
        self.picture_vflip_cb.setObjectName(u"picture_vflip_cb")

        self.horizontalLayout_2.addWidget(self.picture_vflip_cb)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_20.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.cb_enable_picture_parameters = QCheckBox(self.groupBox_5)
        self.cb_enable_picture_parameters.setObjectName(u"cb_enable_picture_parameters")

        self.horizontalLayout_13.addWidget(self.cb_enable_picture_parameters)

        self.lb_brightness = QLabel(self.groupBox_5)
        self.lb_brightness.setObjectName(u"lb_brightness")
        self.lb_brightness.setEnabled(False)

        self.horizontalLayout_13.addWidget(self.lb_brightness)

        self.picture_brightness_sb = QDoubleSpinBox(self.groupBox_5)
        self.picture_brightness_sb.setObjectName(u"picture_brightness_sb")
        self.picture_brightness_sb.setEnabled(False)
        self.picture_brightness_sb.setMaximum(1.000000000000000)
        self.picture_brightness_sb.setSingleStep(0.100000000000000)

        self.horizontalLayout_13.addWidget(self.picture_brightness_sb)

        self.lb_contrast = QLabel(self.groupBox_5)
        self.lb_contrast.setObjectName(u"lb_contrast")
        self.lb_contrast.setEnabled(False)

        self.horizontalLayout_13.addWidget(self.lb_contrast)

        self.picture_contrast_sb = QSpinBox(self.groupBox_5)
        self.picture_contrast_sb.setObjectName(u"picture_contrast_sb")
        self.picture_contrast_sb.setEnabled(False)
        self.picture_contrast_sb.setMinimum(-100)
        self.picture_contrast_sb.setMaximum(100)
        self.picture_contrast_sb.setValue(1)

        self.horizontalLayout_13.addWidget(self.picture_contrast_sb)

        self.lb_sharpness = QLabel(self.groupBox_5)
        self.lb_sharpness.setObjectName(u"lb_sharpness")
        self.lb_sharpness.setEnabled(False)

        self.horizontalLayout_13.addWidget(self.lb_sharpness)

        self.picture_sharpness_sb = QSpinBox(self.groupBox_5)
        self.picture_sharpness_sb.setObjectName(u"picture_sharpness_sb")
        self.picture_sharpness_sb.setEnabled(False)
        self.picture_sharpness_sb.setMinimum(-100)
        self.picture_sharpness_sb.setMaximum(100)
        self.picture_sharpness_sb.setValue(1)

        self.horizontalLayout_13.addWidget(self.picture_sharpness_sb)

        self.lb_saturation = QLabel(self.groupBox_5)
        self.lb_saturation.setObjectName(u"lb_saturation")
        self.lb_saturation.setEnabled(False)

        self.horizontalLayout_13.addWidget(self.lb_saturation)

        self.picture_saturation_sb = QSpinBox(self.groupBox_5)
        self.picture_saturation_sb.setObjectName(u"picture_saturation_sb")
        self.picture_saturation_sb.setEnabled(False)
        self.picture_saturation_sb.setMinimum(0)
        self.picture_saturation_sb.setMaximum(100)
        self.picture_saturation_sb.setValue(1)

        self.horizontalLayout_13.addWidget(self.picture_saturation_sb)

        self.lb_gain = QLabel(self.groupBox_5)
        self.lb_gain.setObjectName(u"lb_gain")
        self.lb_gain.setEnabled(False)

        self.horizontalLayout_13.addWidget(self.lb_gain)

        self.picture_gain_sb = QSpinBox(self.groupBox_5)
        self.picture_gain_sb.setObjectName(u"picture_gain_sb")
        self.picture_gain_sb.setEnabled(False)
        self.picture_gain_sb.setMinimum(0)
        self.picture_gain_sb.setMaximum(100)
        self.picture_gain_sb.setSingleStep(1)
        self.picture_gain_sb.setValue(1)

        self.horizontalLayout_13.addWidget(self.picture_gain_sb)

        self.picture_annotation_cb = QCheckBox(self.groupBox_5)
        self.picture_annotation_cb.setObjectName(u"picture_annotation_cb")
        self.picture_annotation_cb.setEnabled(False)
        self.picture_annotation_cb.setCheckable(False)

        self.horizontalLayout_13.addWidget(self.picture_annotation_cb)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)


        self.verticalLayout_20.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_14.addLayout(self.verticalLayout_20)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.take_picture_pb = QPushButton(self.groupBox_5)
        self.take_picture_pb.setObjectName(u"take_picture_pb")

        self.verticalLayout_6.addWidget(self.take_picture_pb)

        self.download_live_pictures_pb = QPushButton(self.groupBox_5)
        self.download_live_pictures_pb.setObjectName(u"download_live_pictures_pb")

        self.verticalLayout_6.addWidget(self.download_live_pictures_pb)

        self.download_pictures_pb = QPushButton(self.groupBox_5)
        self.download_pictures_pb.setObjectName(u"download_pictures_pb")

        self.verticalLayout_6.addWidget(self.download_pictures_pb)

        self.pb_delete_live_pictures = QPushButton(self.groupBox_5)
        self.pb_delete_live_pictures.setObjectName(u"pb_delete_live_pictures")

        self.verticalLayout_6.addWidget(self.pb_delete_live_pictures)

        self.pb_delete_timelapse_pictures = QPushButton(self.groupBox_5)
        self.pb_delete_timelapse_pictures.setObjectName(u"pb_delete_timelapse_pictures")

        self.verticalLayout_6.addWidget(self.pb_delete_timelapse_pictures)


        self.horizontalLayout_14.addLayout(self.verticalLayout_6)


        self.verticalLayout_26.addLayout(self.horizontalLayout_14)

        self.tw_picture = QTabWidget(self.groupBox_5)
        self.tw_picture.setObjectName(u"tw_picture")
        self.tab_manual = QWidget()
        self.tab_manual.setObjectName(u"tab_manual")
        self.verticalLayout_16 = QVBoxLayout(self.tab_manual)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_20 = QLabel(self.tab_manual)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_15.addWidget(self.label_20)

        self.time_lapse_duration_sb = QSpinBox(self.tab_manual)
        self.time_lapse_duration_sb.setObjectName(u"time_lapse_duration_sb")
        self.time_lapse_duration_sb.setMaximum(31536000)
        self.time_lapse_duration_sb.setSingleStep(3600)
        self.time_lapse_duration_sb.setValue(3600)

        self.horizontalLayout_15.addWidget(self.time_lapse_duration_sb)

        self.label_21 = QLabel(self.tab_manual)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_15.addWidget(self.label_21)

        self.time_lapse_wait_sb = QSpinBox(self.tab_manual)
        self.time_lapse_wait_sb.setObjectName(u"time_lapse_wait_sb")
        self.time_lapse_wait_sb.setMinimum(10)
        self.time_lapse_wait_sb.setMaximum(86400)

        self.horizontalLayout_15.addWidget(self.time_lapse_wait_sb)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)


        self.verticalLayout_16.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.start_time_lapse_pb = QPushButton(self.tab_manual)
        self.start_time_lapse_pb.setObjectName(u"start_time_lapse_pb")

        self.horizontalLayout_31.addWidget(self.start_time_lapse_pb)

        self.stop_time_lapse_pb = QPushButton(self.tab_manual)
        self.stop_time_lapse_pb.setObjectName(u"stop_time_lapse_pb")

        self.horizontalLayout_31.addWidget(self.stop_time_lapse_pb)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_6)


        self.verticalLayout_16.addLayout(self.horizontalLayout_31)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_2)

        self.tw_picture.addTab(self.tab_manual, "")
        self.tab_schedula = QWidget()
        self.tab_schedula.setObjectName(u"tab_schedula")
        self.verticalLayout_25 = QVBoxLayout(self.tab_schedula)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.picture_schedule_tw = QTabWidget(self.tab_schedula)
        self.picture_schedule_tw.setObjectName(u"picture_schedule_tw")
        self.view_picture_schedule = QWidget()
        self.view_picture_schedule.setObjectName(u"view_picture_schedule")
        self.verticalLayout_18 = QVBoxLayout(self.view_picture_schedule)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.view_picture_schedule_pb = QPushButton(self.view_picture_schedule)
        self.view_picture_schedule_pb.setObjectName(u"view_picture_schedule_pb")

        self.horizontalLayout_28.addWidget(self.view_picture_schedule_pb)

        self.delete_picture_schedule_pb = QPushButton(self.view_picture_schedule)
        self.delete_picture_schedule_pb.setObjectName(u"delete_picture_schedule_pb")

        self.horizontalLayout_28.addWidget(self.delete_picture_schedule_pb)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_22)


        self.verticalLayout_19.addLayout(self.horizontalLayout_28)

        self.time_lapse_schedule_table = QTableWidget(self.view_picture_schedule)
        if (self.time_lapse_schedule_table.columnCount() < 6):
            self.time_lapse_schedule_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.time_lapse_schedule_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.time_lapse_schedule_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.time_lapse_schedule_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.time_lapse_schedule_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.time_lapse_schedule_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.time_lapse_schedule_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.time_lapse_schedule_table.setObjectName(u"time_lapse_schedule_table")
        self.time_lapse_schedule_table.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.time_lapse_schedule_table.sizePolicy().hasHeightForWidth())
        self.time_lapse_schedule_table.setSizePolicy(sizePolicy1)
        self.time_lapse_schedule_table.setMaximumSize(QSize(16777215, 16777215))
        self.time_lapse_schedule_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.time_lapse_schedule_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_19.addWidget(self.time_lapse_schedule_table)


        self.verticalLayout_18.addLayout(self.verticalLayout_19)

        self.picture_schedule_tw.addTab(self.view_picture_schedule, "")
        self.add_picture_schedule_tab = QWidget()
        self.add_picture_schedule_tab.setObjectName(u"add_picture_schedule_tab")
        self.verticalLayout_17 = QVBoxLayout(self.add_picture_schedule_tab)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_35 = QLabel(self.add_picture_schedule_tab)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_25.addWidget(self.label_35)

        self.picture_hours_le = QLineEdit(self.add_picture_schedule_tab)
        self.picture_hours_le.setObjectName(u"picture_hours_le")
        self.picture_hours_le.setFrame(True)
        self.picture_hours_le.setClearButtonEnabled(False)

        self.horizontalLayout_25.addWidget(self.picture_hours_le)

        self.label_36 = QLabel(self.add_picture_schedule_tab)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_25.addWidget(self.label_36)

        self.picture_minutes_le = QLineEdit(self.add_picture_schedule_tab)
        self.picture_minutes_le.setObjectName(u"picture_minutes_le")

        self.horizontalLayout_25.addWidget(self.picture_minutes_le)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_19)


        self.verticalLayout_17.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_37 = QLabel(self.add_picture_schedule_tab)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_26.addWidget(self.label_37)

        self.picture_days_of_week_le = QLineEdit(self.add_picture_schedule_tab)
        self.picture_days_of_week_le.setObjectName(u"picture_days_of_week_le")

        self.horizontalLayout_26.addWidget(self.picture_days_of_week_le)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_20)


        self.verticalLayout_17.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_38 = QLabel(self.add_picture_schedule_tab)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_27.addWidget(self.label_38)

        self.picture_days_of_month_le = QLineEdit(self.add_picture_schedule_tab)
        self.picture_days_of_month_le.setObjectName(u"picture_days_of_month_le")

        self.horizontalLayout_27.addWidget(self.picture_days_of_month_le)

        self.label_39 = QLabel(self.add_picture_schedule_tab)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_27.addWidget(self.label_39)

        self.picture_months_le = QLineEdit(self.add_picture_schedule_tab)
        self.picture_months_le.setObjectName(u"picture_months_le")

        self.horizontalLayout_27.addWidget(self.picture_months_le)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_21)


        self.verticalLayout_17.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.configure_picture_pb = QPushButton(self.add_picture_schedule_tab)
        self.configure_picture_pb.setObjectName(u"configure_picture_pb")

        self.horizontalLayout_30.addWidget(self.configure_picture_pb)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_24)


        self.verticalLayout_17.addLayout(self.horizontalLayout_30)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_3)

        self.picture_schedule_tw.addTab(self.add_picture_schedule_tab, "")

        self.verticalLayout_25.addWidget(self.picture_schedule_tw)

        self.tw_picture.addTab(self.tab_schedula, "")
        self.tab_view_picture = QWidget()
        self.tab_view_picture.setObjectName(u"tab_view_picture")
        self.verticalLayout_24 = QVBoxLayout(self.tab_view_picture)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.picture_lb = QLabel(self.tab_view_picture)
        self.picture_lb.setObjectName(u"picture_lb")
        sizePolicy1.setHeightForWidth(self.picture_lb.sizePolicy().hasHeightForWidth())
        self.picture_lb.setSizePolicy(sizePolicy1)

        self.verticalLayout_24.addWidget(self.picture_lb)

        self.tw_picture.addTab(self.tab_view_picture, "")

        self.verticalLayout_26.addWidget(self.tw_picture)


        self.verticalLayout_23.addWidget(self.groupBox_5)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_21.addWidget(self.scrollArea_2)

        self.rpi_tw.addTab(self.picture_tab, "")
        self.streaming_tab = QWidget()
        self.streaming_tab.setObjectName(u"streaming_tab")
        self.verticalLayout_9 = QVBoxLayout(self.streaming_tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pb_start_video_streaming = QPushButton(self.streaming_tab)
        self.pb_start_video_streaming.setObjectName(u"pb_start_video_streaming")

        self.horizontalLayout_5.addWidget(self.pb_start_video_streaming)

        self.pb_stop_video_streaming = QPushButton(self.streaming_tab)
        self.pb_stop_video_streaming.setObjectName(u"pb_stop_video_streaming")

        self.horizontalLayout_5.addWidget(self.pb_stop_video_streaming)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_18)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.streaming_wdg = QWidget(self.streaming_tab)
        self.streaming_wdg.setObjectName(u"streaming_wdg")

        self.verticalLayout_8.addWidget(self.streaming_wdg)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.rpi_tw.addTab(self.streaming_tab, "")
        self.video_tab = QWidget()
        self.video_tab.setObjectName(u"video_tab")
        self.verticalLayout_12 = QVBoxLayout(self.video_tab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea = QScrollArea(self.video_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 739, 871))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.video_mode_cb = QComboBox(self.groupBox_3)
        self.video_mode_cb.setObjectName(u"video_mode_cb")

        self.horizontalLayout_7.addWidget(self.video_mode_cb)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_durations = QLabel(self.groupBox_3)
        self.lb_durations.setObjectName(u"lb_durations")

        self.horizontalLayout_8.addWidget(self.lb_durations)

        self.video_duration_sb = QSpinBox(self.groupBox_3)
        self.video_duration_sb.setObjectName(u"video_duration_sb")
        self.video_duration_sb.setMinimum(60)
        self.video_duration_sb.setMaximum(86000)
        self.video_duration_sb.setSingleStep(60)
        self.video_duration_sb.setValue(2400)

        self.horizontalLayout_8.addWidget(self.video_duration_sb)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.video_quality_sb = QSpinBox(self.groupBox_3)
        self.video_quality_sb.setObjectName(u"video_quality_sb")
        self.video_quality_sb.setMinimum(1)
        self.video_quality_sb.setMaximum(10)

        self.horizontalLayout_10.addWidget(self.video_quality_sb)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.video_fps_sb = QSpinBox(self.groupBox_3)
        self.video_fps_sb.setObjectName(u"video_fps_sb")
        self.video_fps_sb.setMinimum(1)
        self.video_fps_sb.setMaximum(30)

        self.horizontalLayout_9.addWidget(self.video_fps_sb)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_9)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_29 = QLabel(self.groupBox_3)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_20.addWidget(self.label_29)

        self.video_rotation_sb = QSpinBox(self.groupBox_3)
        self.video_rotation_sb.setObjectName(u"video_rotation_sb")
        self.video_rotation_sb.setFrame(True)
        self.video_rotation_sb.setMaximum(270)
        self.video_rotation_sb.setSingleStep(90)

        self.horizontalLayout_20.addWidget(self.video_rotation_sb)

        self.video_hflip_cb = QCheckBox(self.groupBox_3)
        self.video_hflip_cb.setObjectName(u"video_hflip_cb")

        self.horizontalLayout_20.addWidget(self.video_hflip_cb)

        self.video_vflip_cb = QCheckBox(self.groupBox_3)
        self.video_vflip_cb.setObjectName(u"video_vflip_cb")

        self.horizontalLayout_20.addWidget(self.video_vflip_cb)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_12)


        self.verticalLayout_10.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_31 = QLabel(self.groupBox_3)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_22.addWidget(self.label_31)

        self.video_brightness_sb = QDoubleSpinBox(self.groupBox_3)
        self.video_brightness_sb.setObjectName(u"video_brightness_sb")
        self.video_brightness_sb.setMinimum(-1.000000000000000)
        self.video_brightness_sb.setMaximum(1.000000000000000)
        self.video_brightness_sb.setSingleStep(0.010000000000000)

        self.horizontalLayout_22.addWidget(self.video_brightness_sb)

        self.label_30 = QLabel(self.groupBox_3)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_22.addWidget(self.label_30)

        self.video_contrast_sb = QSpinBox(self.groupBox_3)
        self.video_contrast_sb.setObjectName(u"video_contrast_sb")
        self.video_contrast_sb.setMinimum(0)
        self.video_contrast_sb.setMaximum(100)
        self.video_contrast_sb.setValue(1)

        self.horizontalLayout_22.addWidget(self.video_contrast_sb)

        self.Sharpness_2 = QLabel(self.groupBox_3)
        self.Sharpness_2.setObjectName(u"Sharpness_2")

        self.horizontalLayout_22.addWidget(self.Sharpness_2)

        self.video_sharpness_sb = QSpinBox(self.groupBox_3)
        self.video_sharpness_sb.setObjectName(u"video_sharpness_sb")
        self.video_sharpness_sb.setMinimum(0)
        self.video_sharpness_sb.setMaximum(100)
        self.video_sharpness_sb.setValue(1)

        self.horizontalLayout_22.addWidget(self.video_sharpness_sb)

        self.label_32 = QLabel(self.groupBox_3)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_22.addWidget(self.label_32)

        self.video_saturation_sb = QSpinBox(self.groupBox_3)
        self.video_saturation_sb.setObjectName(u"video_saturation_sb")
        self.video_saturation_sb.setMinimum(0)
        self.video_saturation_sb.setMaximum(100)
        self.video_saturation_sb.setValue(1)

        self.horizontalLayout_22.addWidget(self.video_saturation_sb)

        self.label_33 = QLabel(self.groupBox_3)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_22.addWidget(self.label_33)

        self.video_gain_sb = QSpinBox(self.groupBox_3)
        self.video_gain_sb.setObjectName(u"video_gain_sb")
        self.video_gain_sb.setMinimum(0)
        self.video_gain_sb.setMaximum(100)
        self.video_gain_sb.setSingleStep(1)
        self.video_gain_sb.setValue(1)

        self.horizontalLayout_22.addWidget(self.video_gain_sb)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_14)


        self.verticalLayout_10.addLayout(self.horizontalLayout_22)


        self.verticalLayout_22.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.start_video_recording_pb = QPushButton(self.groupBox_2)
        self.start_video_recording_pb.setObjectName(u"start_video_recording_pb")

        self.horizontalLayout_6.addWidget(self.start_video_recording_pb)

        self.stop_video_recording_pb = QPushButton(self.groupBox_2)
        self.stop_video_recording_pb.setObjectName(u"stop_video_recording_pb")

        self.horizontalLayout_6.addWidget(self.stop_video_recording_pb)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)


        self.verticalLayout_22.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 300))
        self.verticalLayout_13 = QVBoxLayout(self.groupBox)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.video_rec_schedule_tw = QTabWidget(self.groupBox)
        self.video_rec_schedule_tw.setObjectName(u"video_rec_schedule_tw")
        self.view_video_rec_schedule = QWidget()
        self.view_video_rec_schedule.setObjectName(u"view_video_rec_schedule")
        self.verticalLayout_15 = QVBoxLayout(self.view_video_rec_schedule)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.view_video_recording_schedule_pb = QPushButton(self.view_video_rec_schedule)
        self.view_video_recording_schedule_pb.setObjectName(u"view_video_recording_schedule_pb")

        self.horizontalLayout_21.addWidget(self.view_video_recording_schedule_pb)

        self.delete_video_recording_schedule_pb = QPushButton(self.view_video_rec_schedule)
        self.delete_video_recording_schedule_pb.setObjectName(u"delete_video_recording_schedule_pb")

        self.horizontalLayout_21.addWidget(self.delete_video_recording_schedule_pb)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_13)


        self.verticalLayout_14.addLayout(self.horizontalLayout_21)

        self.video_rec_schedule_table = QTableWidget(self.view_video_rec_schedule)
        if (self.video_rec_schedule_table.columnCount() < 6):
            self.video_rec_schedule_table.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.video_rec_schedule_table.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.video_rec_schedule_table.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.video_rec_schedule_table.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.video_rec_schedule_table.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.video_rec_schedule_table.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.video_rec_schedule_table.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.video_rec_schedule_table.setObjectName(u"video_rec_schedule_table")
        self.video_rec_schedule_table.setMinimumSize(QSize(0, 150))
        self.video_rec_schedule_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.video_rec_schedule_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_14.addWidget(self.video_rec_schedule_table)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)

        self.video_rec_schedule_tw.addTab(self.view_video_rec_schedule, "")
        self.add_video_rec_schedule_tab = QWidget()
        self.add_video_rec_schedule_tab.setObjectName(u"add_video_rec_schedule_tab")
        self.verticalLayout_7 = QVBoxLayout(self.add_video_rec_schedule_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_24 = QLabel(self.add_video_rec_schedule_tab)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_18.addWidget(self.label_24)

        self.hours_le = QLineEdit(self.add_video_rec_schedule_tab)
        self.hours_le.setObjectName(u"hours_le")
        self.hours_le.setFrame(True)
        self.hours_le.setClearButtonEnabled(False)

        self.horizontalLayout_18.addWidget(self.hours_le)

        self.label_25 = QLabel(self.add_video_rec_schedule_tab)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_18.addWidget(self.label_25)

        self.minutes_le = QLineEdit(self.add_video_rec_schedule_tab)
        self.minutes_le.setObjectName(u"minutes_le")

        self.horizontalLayout_18.addWidget(self.minutes_le)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_9)


        self.verticalLayout_7.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_26 = QLabel(self.add_video_rec_schedule_tab)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_16.addWidget(self.label_26)

        self.days_of_week_le = QLineEdit(self.add_video_rec_schedule_tab)
        self.days_of_week_le.setObjectName(u"days_of_week_le")

        self.horizontalLayout_16.addWidget(self.days_of_week_le)

        self.label_27 = QLabel(self.add_video_rec_schedule_tab)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_16.addWidget(self.label_27)

        self.days_of_month_le = QLineEdit(self.add_video_rec_schedule_tab)
        self.days_of_month_le.setObjectName(u"days_of_month_le")

        self.horizontalLayout_16.addWidget(self.days_of_month_le)

        self.label_28 = QLabel(self.add_video_rec_schedule_tab)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_16.addWidget(self.label_28)

        self.months_le = QLineEdit(self.add_video_rec_schedule_tab)
        self.months_le.setObjectName(u"months_le")

        self.horizontalLayout_16.addWidget(self.months_le)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)


        self.verticalLayout_7.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.configure_video_recording_pb = QPushButton(self.add_video_rec_schedule_tab)
        self.configure_video_recording_pb.setObjectName(u"configure_video_recording_pb")

        self.horizontalLayout_23.addWidget(self.configure_video_recording_pb)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_15)


        self.verticalLayout_7.addLayout(self.horizontalLayout_23)

        self.video_rec_schedule_tw.addTab(self.add_video_rec_schedule_tab, "")

        self.verticalLayout_13.addWidget(self.video_rec_schedule_tw)


        self.verticalLayout_22.addWidget(self.groupBox)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.video_list_pb = QPushButton(self.scrollAreaWidgetContents)
        self.video_list_pb.setObjectName(u"video_list_pb")

        self.horizontalLayout_19.addWidget(self.video_list_pb)

        self.all_video_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.all_video_cb.setObjectName(u"all_video_cb")

        self.horizontalLayout_19.addWidget(self.all_video_cb)

        self.all_new_video_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.all_new_video_cb.setObjectName(u"all_new_video_cb")

        self.horizontalLayout_19.addWidget(self.all_new_video_cb)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_10)


        self.verticalLayout_22.addLayout(self.horizontalLayout_19)

        self.video_list_lw = QListWidget(self.scrollAreaWidgetContents)
        self.video_list_lw.setObjectName(u"video_list_lw")
        sizePolicy1.setHeightForWidth(self.video_list_lw.sizePolicy().hasHeightForWidth())
        self.video_list_lw.setSizePolicy(sizePolicy1)
        self.video_list_lw.setMinimumSize(QSize(0, 250))

        self.verticalLayout_22.addWidget(self.video_list_lw)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.download_videos_pb = QPushButton(self.scrollAreaWidgetContents)
        self.download_videos_pb.setObjectName(u"download_videos_pb")

        self.horizontalLayout_24.addWidget(self.download_videos_pb)

        self.delete_videos_pb = QPushButton(self.scrollAreaWidgetContents)
        self.delete_videos_pb.setObjectName(u"delete_videos_pb")

        self.horizontalLayout_24.addWidget(self.delete_videos_pb)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_17)


        self.verticalLayout_22.addLayout(self.horizontalLayout_24)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)

        self.rpi_tw.addTab(self.video_tab, "")

        self.verticalLayout_3.addWidget(self.rpi_tw)

        self.rasp_output_lb = QLabel(self.layoutWidget1)
        self.rasp_output_lb.setObjectName(u"rasp_output_lb")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.rasp_output_lb.setFont(font2)

        self.verticalLayout_3.addWidget(self.rasp_output_lb)

        self.splitter.addWidget(self.layoutWidget1)

        self.horizontalLayout_3.addWidget(self.splitter)

        self.main_tw.addTab(self.rasp_list_tab, "")
        self.dashboard_tab = QWidget()
        self.dashboard_tab.setObjectName(u"dashboard_tab")
        self.main_tw.addTab(self.dashboard_tab, "")

        self.verticalLayout_2.addWidget(self.main_tw)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 2040, 25))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionEdit_parameters)
        self.menuTools.addAction(self.actionShow_IP_address)
        self.menuTools.addAction(self.action_convert_h264_video_files)

        self.retranslateUi(MainWindow)

        self.main_tw.setCurrentIndex(0)
        self.rpi_tw.setCurrentIndex(0)
        self.tw_picture.setCurrentIndex(0)
        self.picture_schedule_tw.setCurrentIndex(0)
        self.video_rec_schedule_tw.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionShow_IP_address.setText(QCoreApplication.translate("MainWindow", u"Show IP address for all Raspberries Pi", None))
        self.action_convert_h264_video_files.setText(QCoreApplication.translate("MainWindow", u"Convert h264 video files to MP4", None))
        self.actionEdit_parameters.setText(QCoreApplication.translate("MainWindow", u"Edit parameters", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Commands for all detected Raspberry Pi:", None))
        self.get_status_all_pb.setText(QCoreApplication.translate("MainWindow", u"Get status", None))
        self.time_synchro_all_pb.setText(QCoreApplication.translate("MainWindow", u"Synchronize time", None))
        self.shutdown_all_pb.setText(QCoreApplication.translate("MainWindow", u"Shutdown", None))
        self.pb_scan_network.setText(QCoreApplication.translate("MainWindow", u"Scan network", None))
        self.pb_up.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.pb_down.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.raspberry_id_lb.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Time lapse active", None))
        self.free_sd_space_lb.setText("")
        self.wifi_essid_lb.setText("")
        self.time_lapse_active_lb.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Date/time", None))
        self.video_recording_active_lb.setText("")
        self.datetime_lb.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CPU temperature", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"WiFi ESSID", None))
        self.camera_detected_lb.setText("")
        self.ip_address_lb.setText("")
        self.cpu_temp_lb.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"IP address", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Camera detected", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Video streaming active", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Free SD space", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Video recording active", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Uptime", None))
        self.uptime_lb.setText("")
        self.video_streaming_active_lb.setText("")
        self.status_lb.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Server version", None))
        self.server_version_lb.setText("")
        self.status_update_pb.setText(QCoreApplication.translate("MainWindow", u"Update status", None))
        self.time_synchro_pb.setText(QCoreApplication.translate("MainWindow", u"Time synchronization", None))
        self.get_log_pb.setText(QCoreApplication.translate("MainWindow", u"Get log", None))
        self.blink_pb.setText(QCoreApplication.translate("MainWindow", u"Blink", None))
        self.pb_send_command.setText(QCoreApplication.translate("MainWindow", u"Send command", None))
        self.reboot_pb.setText(QCoreApplication.translate("MainWindow", u"Reboot", None))
        self.shutdown_pb.setText(QCoreApplication.translate("MainWindow", u"Shutdown", None))
        self.rpi_tw.setTabText(self.rpi_tw.indexOf(self.status_tab), QCoreApplication.translate("MainWindow", u"Status", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
#if QT_CONFIG(accessibility)
        self.picture_resolution_cb.setAccessibleName(QCoreApplication.translate("MainWindow", u"picture resolution", None))
#endif // QT_CONFIG(accessibility)
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Rotation", None))
#if QT_CONFIG(accessibility)
        self.picture_rotation_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"picture rotation", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.picture_hflip_cb.setAccessibleName(QCoreApplication.translate("MainWindow", u"picture hflip", None))
#endif // QT_CONFIG(accessibility)
        self.picture_hflip_cb.setText(QCoreApplication.translate("MainWindow", u"Horizontal flip", None))
#if QT_CONFIG(accessibility)
        self.picture_vflip_cb.setAccessibleName(QCoreApplication.translate("MainWindow", u"picture vflip", None))
#endif // QT_CONFIG(accessibility)
        self.picture_vflip_cb.setText(QCoreApplication.translate("MainWindow", u"Vertical flip", None))
        self.cb_enable_picture_parameters.setText(QCoreApplication.translate("MainWindow", u"Enable picture parameters", None))
        self.lb_brightness.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
#if QT_CONFIG(accessibility)
        self.picture_brightness_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"picture brightness", None))
#endif // QT_CONFIG(accessibility)
        self.lb_contrast.setText(QCoreApplication.translate("MainWindow", u"Contrast", None))
#if QT_CONFIG(accessibility)
        self.picture_contrast_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"picture contrast", None))
#endif // QT_CONFIG(accessibility)
        self.lb_sharpness.setText(QCoreApplication.translate("MainWindow", u"Sharpness", None))
#if QT_CONFIG(accessibility)
        self.picture_sharpness_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"picture sharpness", None))
#endif // QT_CONFIG(accessibility)
        self.lb_saturation.setText(QCoreApplication.translate("MainWindow", u"Saturation", None))
#if QT_CONFIG(accessibility)
        self.picture_saturation_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"picture saturation", None))
#endif // QT_CONFIG(accessibility)
        self.lb_gain.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
#if QT_CONFIG(accessibility)
        self.picture_gain_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"picture gain", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.picture_annotation_cb.setAccessibleName(QCoreApplication.translate("MainWindow", u"picture annotation", None))
#endif // QT_CONFIG(accessibility)
        self.picture_annotation_cb.setText(QCoreApplication.translate("MainWindow", u"Annotate picture", None))
        self.take_picture_pb.setText(QCoreApplication.translate("MainWindow", u"Take a picture", None))
        self.download_live_pictures_pb.setText(QCoreApplication.translate("MainWindow", u"Download live pictures", None))
        self.download_pictures_pb.setText(QCoreApplication.translate("MainWindow", u"Download time lapse pictures", None))
        self.pb_delete_live_pictures.setText(QCoreApplication.translate("MainWindow", u"Delete live pictures", None))
        self.pb_delete_timelapse_pictures.setText(QCoreApplication.translate("MainWindow", u"Delete time lapse pictures", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Duration (s)", None))
#if QT_CONFIG(accessibility)
        self.time_lapse_duration_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"time lapse duration", None))
#endif // QT_CONFIG(accessibility)
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Time between pictures (s)", None))
#if QT_CONFIG(accessibility)
        self.time_lapse_wait_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"time lapse wait", None))
#endif // QT_CONFIG(accessibility)
        self.start_time_lapse_pb.setText(QCoreApplication.translate("MainWindow", u"Start time lapse", None))
        self.stop_time_lapse_pb.setText(QCoreApplication.translate("MainWindow", u"Stop time lapse", None))
        self.tw_picture.setTabText(self.tw_picture.indexOf(self.tab_manual), QCoreApplication.translate("MainWindow", u"Manual time lapse", None))
        self.view_picture_schedule_pb.setText(QCoreApplication.translate("MainWindow", u"View schedule on Raspberry Pi", None))
        self.delete_picture_schedule_pb.setText(QCoreApplication.translate("MainWindow", u"Delete schedule on Raspberry Pi", None))
        ___qtablewidgetitem = self.time_lapse_schedule_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Minute", None));
        ___qtablewidgetitem1 = self.time_lapse_schedule_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hour", None));
        ___qtablewidgetitem2 = self.time_lapse_schedule_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Day of month", None));
        ___qtablewidgetitem3 = self.time_lapse_schedule_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Month", None));
        ___qtablewidgetitem4 = self.time_lapse_schedule_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Day of week", None));
        ___qtablewidgetitem5 = self.time_lapse_schedule_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        self.picture_schedule_tw.setTabText(self.picture_schedule_tw.indexOf(self.view_picture_schedule), QCoreApplication.translate("MainWindow", u"Time lapse schedule", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Hours", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Minutes", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Days of week (0-6 or SUN-SAT)", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Days of month (1-31)", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Month(s)", None))
        self.configure_picture_pb.setText(QCoreApplication.translate("MainWindow", u"Add schedule to Raspberry Pi", None))
        self.picture_schedule_tw.setTabText(self.picture_schedule_tw.indexOf(self.add_picture_schedule_tab), QCoreApplication.translate("MainWindow", u"New schedule", None))
        self.tw_picture.setTabText(self.tw_picture.indexOf(self.tab_schedula), QCoreApplication.translate("MainWindow", u"Time lapse schedule", None))
        self.picture_lb.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tw_picture.setTabText(self.tw_picture.indexOf(self.tab_view_picture), QCoreApplication.translate("MainWindow", u"View picture", None))
        self.rpi_tw.setTabText(self.rpi_tw.indexOf(self.picture_tab), QCoreApplication.translate("MainWindow", u"Picture", None))
        self.pb_start_video_streaming.setText(QCoreApplication.translate("MainWindow", u"Start video streaming", None))
        self.pb_stop_video_streaming.setText(QCoreApplication.translate("MainWindow", u"Stop video streaming", None))
        self.rpi_tw.setTabText(self.rpi_tw.indexOf(self.streaming_tab), QCoreApplication.translate("MainWindow", u"Video streaming", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Video mode", None))
#if QT_CONFIG(accessibility)
        self.video_mode_cb.setAccessibleName(QCoreApplication.translate("MainWindow", u"video mode", None))
#endif // QT_CONFIG(accessibility)
        self.lb_durations.setText(QCoreApplication.translate("MainWindow", u"Duration (s)", None))
#if QT_CONFIG(accessibility)
        self.video_duration_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"video duration", None))
#endif // QT_CONFIG(accessibility)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Video quality (Mbp/s)", None))
#if QT_CONFIG(accessibility)
        self.video_quality_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"video quality", None))
#endif // QT_CONFIG(accessibility)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
#if QT_CONFIG(accessibility)
        self.video_fps_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"FPS", None))
#endif // QT_CONFIG(accessibility)
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Rotation", None))
#if QT_CONFIG(accessibility)
        self.video_rotation_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"video rotation", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.video_hflip_cb.setAccessibleName(QCoreApplication.translate("MainWindow", u"video hflip", None))
#endif // QT_CONFIG(accessibility)
        self.video_hflip_cb.setText(QCoreApplication.translate("MainWindow", u"Horizontal flip", None))
#if QT_CONFIG(accessibility)
        self.video_vflip_cb.setAccessibleName(QCoreApplication.translate("MainWindow", u"video vflip", None))
#endif // QT_CONFIG(accessibility)
        self.video_vflip_cb.setText(QCoreApplication.translate("MainWindow", u"Vertical flip", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
#if QT_CONFIG(accessibility)
        self.video_brightness_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"video brightness", None))
#endif // QT_CONFIG(accessibility)
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Contrast", None))
#if QT_CONFIG(accessibility)
        self.video_contrast_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"video contrast", None))
#endif // QT_CONFIG(accessibility)
        self.Sharpness_2.setText(QCoreApplication.translate("MainWindow", u"Sharpness", None))
#if QT_CONFIG(accessibility)
        self.video_sharpness_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"video sharpness", None))
#endif // QT_CONFIG(accessibility)
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Saturation", None))
#if QT_CONFIG(accessibility)
        self.video_saturation_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"video saturation", None))
#endif // QT_CONFIG(accessibility)
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
#if QT_CONFIG(accessibility)
        self.video_gain_sb.setAccessibleName(QCoreApplication.translate("MainWindow", u"video gain", None))
#endif // QT_CONFIG(accessibility)
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Manual control", None))
        self.start_video_recording_pb.setText(QCoreApplication.translate("MainWindow", u"Start video recording now", None))
        self.stop_video_recording_pb.setText(QCoreApplication.translate("MainWindow", u"Stop current video recording", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.view_video_recording_schedule_pb.setText(QCoreApplication.translate("MainWindow", u"View schedule on Raspberry Pi", None))
        self.delete_video_recording_schedule_pb.setText(QCoreApplication.translate("MainWindow", u"Delete schedule on Raspberry Pi", None))
        ___qtablewidgetitem6 = self.video_rec_schedule_table.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Minute", None));
        ___qtablewidgetitem7 = self.video_rec_schedule_table.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Hour", None));
        ___qtablewidgetitem8 = self.video_rec_schedule_table.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Day of month", None));
        ___qtablewidgetitem9 = self.video_rec_schedule_table.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Month", None));
        ___qtablewidgetitem10 = self.video_rec_schedule_table.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Day of week", None));
        ___qtablewidgetitem11 = self.video_rec_schedule_table.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        self.video_rec_schedule_tw.setTabText(self.video_rec_schedule_tw.indexOf(self.view_video_rec_schedule), QCoreApplication.translate("MainWindow", u"Video recording schedule", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Hours", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Minutes", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Days of week (0-6 or SUN-SAT)", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Days of month (1-31)", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Month(s)", None))
        self.configure_video_recording_pb.setText(QCoreApplication.translate("MainWindow", u"Add schedule to Raspberry Pi", None))
        self.video_rec_schedule_tw.setTabText(self.video_rec_schedule_tw.indexOf(self.add_video_rec_schedule_tab), QCoreApplication.translate("MainWindow", u"New schedule", None))
        self.video_list_pb.setText(QCoreApplication.translate("MainWindow", u"Get the list of videos", None))
        self.all_video_cb.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.all_new_video_cb.setText(QCoreApplication.translate("MainWindow", u"All new", None))
        self.download_videos_pb.setText(QCoreApplication.translate("MainWindow", u"Download selected videos", None))
        self.delete_videos_pb.setText(QCoreApplication.translate("MainWindow", u"Delete selected videos", None))
        self.rpi_tw.setTabText(self.rpi_tw.indexOf(self.video_tab), QCoreApplication.translate("MainWindow", u"Video recording", None))
        self.rasp_output_lb.setText("")
        self.main_tw.setTabText(self.main_tw.indexOf(self.rasp_list_tab), QCoreApplication.translate("MainWindow", u"Raspberry Pi list", None))
        self.main_tw.setTabText(self.main_tw.indexOf(self.dashboard_tab), QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

