"""
Raspberry Pi coordinator

connections
"""

import pprint
from functools import partial

from PySide6.QtWidgets import QCheckBox, QComboBox, QDoubleSpinBox, QSpinBox


def get_widgets_list(self):

    return [
        self.video_mode_cb,
        self.video_duration_sb,
        self.video_quality_sb,
        self.video_fps_sb,
        self.video_rotation_sb,
        self.video_hflip_cb,
        self.video_vflip_cb,
        self.video_brightness_sb,
        self.video_contrast_sb,
        self.video_sharpness_sb,
        self.video_saturation_sb,
        self.video_gain_sb,
        self.picture_resolution_cb,
        self.picture_rotation_sb,
        self.picture_hflip_cb,
        self.picture_vflip_cb,
        self.picture_brightness_sb,
        self.picture_contrast_sb,
        self.picture_sharpness_sb,
        self.picture_saturation_sb,
        self.picture_gain_sb,
        self.picture_annotation_cb,
        self.time_lapse_wait_sb,
        self.time_lapse_duration_sb,
    ]


def connect(self):

    for w in get_widgets_list(self):
        if w.accessibleName():
            if isinstance(w, QComboBox):
                w.currentIndexChanged.connect(partial(widget_value_changed, self, w))
            elif isinstance(w, QSpinBox) or isinstance(w, QDoubleSpinBox):
                w.valueChanged.connect(partial(widget_value_changed, self, w))
            elif isinstance(w, QCheckBox):
                w.clicked.connect(partial(widget_value_changed, self, w))
            else:
                raise
        else:
            raise


def widget_value_changed(self, widget, *args):
    """
    update raspberry_info dictionary when widget value changed
    """

    if not self.current_raspberry_id:
        return

    key = widget.accessibleName()
    info = self.raspberry_info[self.current_raspberry_id]

    if isinstance(widget, QComboBox):
        info[key] = widget.currentText()
    if isinstance(widget, (QSpinBox, QDoubleSpinBox)):
        info[key] = widget.value()
    if isinstance(widget, QCheckBox):
        info[key] = widget.isChecked()


def update_rpi_settings(self, raspberry_id):
    """
    update widget values with raspberry_info values
    """

    for w in get_widgets_list(self):
        if w.accessibleName():
            if isinstance(w, QComboBox):
                w.setCurrentText(self.raspberry_info[raspberry_id][w.accessibleName()])
            elif isinstance(w, (QSpinBox, QDoubleSpinBox)):
                w.setValue(self.raspberry_info[raspberry_id][w.accessibleName()])
            elif isinstance(w, QCheckBox):
                w.setChecked(self.raspberry_info[raspberry_id][w.accessibleName()])
            else:
                raise
        else:
            raise
