from PySide6.QtWidgets import QMessageBox


class MessageDialogs:

    @staticmethod
    def show_error(parent, message):

        QMessageBox.critical(
            parent,
            "Error",
            message
        )


    @staticmethod
    def show_info(parent, message):

        QMessageBox.information(
            parent,
            "Information",
            message
        )