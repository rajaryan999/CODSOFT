import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget, QMessageBox
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.phone}"

class ContactManager(QWidget):
    def __init__(self):
        super().__init__()
        self.contacts = []
        self.initUI()

    def initUI(self):
        # Set window properties
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('Contact Manager')
        self.setWindowIcon(QIcon('contact_icon.png'))
        self.setStyleSheet("background-color: #f0f0f0;")

        # Layouts
        main_layout = QVBoxLayout()
        form_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        list_layout = QVBoxLayout()

        # Title
        title = QLabel('Contact Manager')
        title.setFont(QFont('Arial', 24))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #4a4a4a; margin-bottom: 20px;")
        main_layout.addWidget(title)

        # Form fields
        self.name_input = QLineEdit(self)
        self.phone_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        self.address_input = QLineEdit(self)

        self.name_input.setPlaceholderText('Name')
        self.phone_input.setPlaceholderText('Phone')
        self.email_input.setPlaceholderText('Email')
        self.address_input.setPlaceholderText('Address')

        self.name_input.setFont(QFont('Arial', 14))
        self.phone_input.setFont(QFont('Arial', 14))
        self.email_input.setFont(QFont('Arial', 14))
        self.address_input.setFont(QFont('Arial', 14))

        self.name_input.setStyleSheet("padding: 10px; border: 2px solid #4a90e2; border-radius: 5px; margin-bottom: 10px;")
        self.phone_input.setStyleSheet("padding: 10px; border: 2px solid #4a90e2; border-radius: 5px; margin-bottom: 10px;")
        self.email_input.setStyleSheet("padding: 10px; border: 2px solid #4a90e2; border-radius: 5px; margin-bottom: 10px;")
        self.address_input.setStyleSheet("padding: 10px; border: 2px solid #4a90e2; border-radius: 5px; margin-bottom: 10px;")

        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.phone_input)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(self.address_input)

        # Buttons
        add_button = QPushButton('Add', self)
        view_button = QPushButton('View', self)
        search_button = QPushButton('Search', self)
        update_button = QPushButton('Update', self)
        delete_button = QPushButton('Delete', self)

        add_button.setFont(QFont('Arial', 14))
        view_button.setFont(QFont('Arial', 14))
        search_button.setFont(QFont('Arial', 14))
        update_button.setFont(QFont('Arial', 14))
        delete_button.setFont(QFont('Arial', 14))

        add_button.setStyleSheet("background-color: #4caf50; color: white; padding: 10px; border-radius: 5px;")
        view_button.setStyleSheet("background-color: #2196f3; color: white; padding: 10px; border-radius: 5px;")
        search_button.setStyleSheet("background-color: #ff9800; color: white; padding: 10px; border-radius: 5px;")
        update_button.setStyleSheet("background-color: #fbc02d; color: white; padding: 10px; border-radius: 5px;")
        delete_button.setStyleSheet("background-color: #f44336; color: white; padding: 10px; border-radius: 5px;")

        button_layout.addWidget(add_button)
        button_layout.addWidget(view_button)
        button_layout.addWidget(search_button)
        button_layout.addWidget(update_button)
        button_layout.addWidget(delete_button)

        # Contact list display
        self.contact_list = QListWidget(self)
        self.contact_list.setFont(QFont('Arial', 14))
        self.contact_list.setStyleSheet("padding: 10px; border: 2px solid #4a90e2; border-radius: 5px;")

        list_layout.addWidget(self.contact_list)

        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        main_layout.addLayout(list_layout)

        self.setLayout(main_layout)

        # Button actions
        add_button.clicked.connect(self.add_contact)
        view_button.clicked.connect(self.view_contacts)
        search_button.clicked.connect(self.search_contact)
        update_button.clicked.connect(self.update_contact)
        delete_button.clicked.connect(self.delete_contact)

    def add_contact(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        address = self.address_input.text()

        if name and phone:
            new_contact = Contact(name, phone, email, address)
            self.contacts.append(new_contact)
            QMessageBox.information(self, 'Success', 'Contact added successfully!')
            self.clear_form()
        else:
            QMessageBox.warning(self, 'Error', 'Name and phone are required!')

    def view_contacts(self):
        self.contact_list.clear()
        for contact in self.contacts:
            self.contact_list.addItem(str(contact))

    def search_contact(self):
        search_text = self.name_input.text()
        if search_text:
            self.contact_list.clear()
            for contact in self.contacts:
                if search_text.lower() in contact.name.lower() or search_text in contact.phone:
                    self.contact_list.addItem(str(contact))
            if not self.contact_list.count():
                QMessageBox.warning(self, 'Not Found', 'Contact not found.')
        else:
            QMessageBox.warning(self, 'Error', 'Enter name or phone to search!')

    def update_contact(self):
        current_item = self.contact_list.currentItem()
        if current_item:
            contact_info = current_item.text().split(" - ")
            for contact in self.contacts:
                if contact.name == contact_info[0] and contact.phone == contact_info[1]:
                    contact.name = self.name_input.text() or contact.name
                    contact.phone = self.phone_input.text() or contact.phone
                    contact.email = self.email_input.text() or contact.email
                    contact.address = self.address_input.text() or contact.address
                    QMessageBox.information(self, 'Success', 'Contact updated successfully!')
                    self.view_contacts()
                    return
        else:
            QMessageBox.warning(self, 'Error', 'Select a contact to update!')

    def delete_contact(self):
        current_item = self.contact_list.currentItem()
        if current_item:
            contact_info = current_item.text().split(" - ")
            self.contacts = [contact for contact in self.contacts if not (contact.name == contact_info[0] and contact.phone == contact_info[1])]
            QMessageBox.information(self, 'Success', 'Contact deleted successfully!')
            self.view_contacts()
        else:
            QMessageBox.warning(self, 'Error', 'Select a contact to delete!')

    def clear_form(self):
        self.name_input.clear()
        self.phone_input.clear()
        self.email_input.clear()
        self.address_input.clear()

def main():
    app = QApplication(sys.argv)
    contact_manager = ContactManager()
    contact_manager.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
