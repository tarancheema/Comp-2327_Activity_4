# Intermediate Software Development Activity 4

This activity will help to reinforce learning of the Module 4 concepts of:

- Event Handling
- Signals
- Slots
- PySide6

## Author

Taranpreet Singh

## Additional Information

Implemented the ContactListWindow subclass (ui/contact_list_window.py) to build a desktop Contact Manager application using PySide6:
- Widget Initialization: Configured window title (Contact Manager), name placeholder text, phone input mask ((000) 000-0000;_), and initial disabled button states.
- Signals & Slots: Connected input validation (textChanged), contact creation (clicked), table row selection (itemSelectionChanged), and contact deletion confirmation dialogs (QMessageBox.question).
- User Acceptance Testing (UAT): Verified dynamic button enabling/disabling, contact insertion, focus reset, and prompt-confirmed row removal.