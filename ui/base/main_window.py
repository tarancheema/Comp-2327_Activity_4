"""The module defines the MainWindow class."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QMainWindow,
                               QWidget,
                               QLineEdit,
                               QPushButton,
                               QTableWidget,
                               QAbstractItemView,
                               QHeaderView,
                               QLayout,
                               QVBoxLayout)

__author__ = "ACE Faculty"
__version__ = "1.0.0"

class MainWindow(QMainWindow):
    """Represents the main window of the application."""

    def __init__(self):
        """Initializes a new instance of the ContactList class."""

        super().__init__()

        self.setFixedSize(400, 500)

        container = QWidget()
        layout = QVBoxLayout(container)
        self.setCentralWidget(container)

        # Disable the maximize button
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)

        self.__initialize_widgets(layout)

    def __initialize_widgets(self, layout: QLayout):
        """Initializes the widgets on this Window.

        Args:
            layout (QLayout): The main layout of the window.
        """

        self._name_line_edit = QLineEdit(self)
        self._phone_line_edit = QLineEdit(self)

        self._remove_button = QPushButton(self)
        self._remove_button.setText("Remove Contact")

        self._add_button = QPushButton(self)
        self._add_button.setText("Add Contact")

        self._contact_table = QTableWidget(self)
        self._contact_table.setColumnCount(2)
        self._contact_table.setHorizontalHeaderLabels(["Name", "Phone"])
        self._contact_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self._contact_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self._contact_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        header = self._contact_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        layout.addWidget(self._name_line_edit)
        layout.addWidget(self._phone_line_edit)
        layout.addWidget(self._add_button)
        layout.addWidget(self._contact_table)
        layout.addWidget(self._remove_button)

    def keyPressEvent(self, event) -> None:
        """Handles keypress events.

        Args:
            event: Contains data about the event that took place.
        """

        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            if self._add_button.isEnabled():
                self._add_button.click()
                return

        super().keyPressEvent(event)
