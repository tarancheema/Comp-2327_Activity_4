"""This module contains the program for the contact list application."""

from PySide6.QtWidgets import QApplication

from ui.contact_list_window import ContactListWindow

__author__ = "ACE Faculty"
__version__ = "1.0.0"

def main() -> None:
    """The main entry point of the program."""

    # Only one QApplication instance per application
    app = QApplication([])

    # Create an instance of the window class
    window = ContactListWindow()

    # Windows are hidden by default. This shows it.
    window.show()

    # Start the event loop.
    app.exec()

    # The application won't reach here until the main window is closed
    # the event loop has stopped.

if __name__ == "__main__":
    main()
