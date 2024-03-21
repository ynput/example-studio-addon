from qtpy import QtWidgets, QtCore

from ayon_core import style


class MyDialog(QtWidgets.QDialog):
    """Basic dialog."""

    finished = QtCore.Signal(bool)

    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)

        self.setWindowTitle("My Dialog")
        self.resize(300, 120)
        # Message label
        message_label = QtWidgets.QLabel("Hello!", self)

        # Buttons
        buttons_widget = QtWidgets.QWidget(self)

        ok_btn = QtWidgets.QPushButton("Ok", buttons_widget)
        cancel_btn = QtWidgets.QPushButton("Cancel", buttons_widget)

        buttons_layout = QtWidgets.QHBoxLayout(buttons_widget)
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        buttons_layout.addStretch(1)
        buttons_layout.addWidget(ok_btn)
        buttons_layout.addWidget(cancel_btn)

        # Main layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.addSpacing(5)
        layout.addWidget(message_label, 0)
        layout.addStretch(1)
        layout.addWidget(buttons_widget, 0)

        ok_btn.clicked.connect(self._on_ok_click)
        cancel_btn.clicked.connect(self._on_cancel_click)


        self._message_label = message_label
        self._final_result = None

        self.setStyleSheet(style.load_stylesheet())

    def result(self):
        return self._final_result

    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            self._on_ok_click()
            return event.accept()
        super(MyDialog, self).keyPressEvent(event)

    def closeEvent(self, event):
        super(MyDialog, self).closeEvent(event)
        self.finished.emit(self.result())

    def _on_ok_click(self):
        self._message_label.setText("Ok was clicked.")

        self._final_result = True


    def _on_cancel_click(self):
        self._message_label.setText("Hello!")
        self.close()
