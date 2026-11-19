"""The module defines the ContactListWindow class."""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from ui.base.main_window import MainWindow

__author__ = "Taranpreet Singh"
__version__ = "1.0.0"


class ContactListWindow(MainWindow):
    """Represents the contact manager window of the application."""

    def __init__(self) -> None:
        """Initializes a new instance of the ContactListWindow class."""
        super().__init__()

        self.setWindowTitle("Contact Manager")

        # Initialize widgets to their starting states
        self._name_line_edit.setPlaceholderText("Contact Name")
        self._phone_line_edit.setInputMask("(000) 000-0000;_")

        self._add_button.setDefault(True)
        self._add_button.setEnabled(False)
        self._remove_button.setEnabled(False)

        # Connect signals to slots
        self._name_line_edit.textChanged.connect(self.__on_input_changed)
        self._phone_line_edit.textChanged.connect(self.__on_input_changed)
        self._add_button.clicked.connect(self.__on_add_clicked)
        self._contact_table.itemSelectionChanged.connect(
            self.__on_selection_changed
        )
        self._remove_button.clicked.connect(self.__on_remove_clicked)

    @Slot()
    def __on_input_changed(self) -> None:
        """Enables the add button when name is non-empty and phone has 10 digits."""
        name_valid = len(self._name_line_edit.text().strip()) > 0
        phone_valid = self._phone_line_edit.hasAcceptableInput()

        self._add_button.setEnabled(name_valid and phone_valid)

    @Slot()
    def __on_add_clicked(self) -> None:
        """Adds a new contact row to the table and resets the input fields."""
        name = self._name_line_edit.text().strip()
        phone = self._phone_line_edit.text()

        row = self._contact_table.rowCount()
        self._contact_table.insertRow(row)
        self._contact_table.setItem(row, 0, QTableWidgetItem(name))
        self._contact_table.setItem(row, 1, QTableWidgetItem(phone))

        self._name_line_edit.clear()
        self._phone_line_edit.clear()
        self._name_line_edit.setFocus()

    # @Slot()
    # def __on_selection_changed(self) -> None:
    #     """Enables the remove button when a table row is selected."""
    #     has_selection = len(self._contact_table.selectedItems()) > 0
    #     self._remove_button.setEnabled(has_selection)

    # @Slot()
    # def __on_remove_clicked(self) -> None:
    #     """Prompts confirmation and removes the selected contact from the table."""
    #     row = self._contact_table.currentRow()

    #     if row >= 0:
    #         contact_name = self._contact_table.item(row, 0).text()

    #         reply = QMessageBox.question(
    #             self,
    #             "Remove Contact",
    #             f"Do you want to remove the contact {contact_name}?",
    #             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
    #             QMessageBox.StandardButton.No,
    #         )

    #         if reply == QMessageBox.StandardButton.Yes:
    #             self._contact_table.removeRow(row)
