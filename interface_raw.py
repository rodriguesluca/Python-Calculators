from abc import ABC, abstractmethod


class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass


class EmailNotificationSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f"Email: {message}")


class SMSNotificationSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f"SMS: {message}")


class Notificator:
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.notification_sender = notification_sender

    def send(self, message: str) -> None:
        if not message:
            raise ValueError("Message cannot be empty")
        self.notification_sender.send_notification(message)


obj = Notificator(EmailNotificationSender())
obj.notify("Hello World")
