// TODO: панелька с уведомлениями 
import {Notification, NotificationType} from "./notification.js"

export class Notifier {
    constructor(element) {
        this._element = element;
    }

    showWarning(text) {
        this._showNotification(NotificationType.WARNING, text)
    }

    showError(text) {
        this._showNotification(NotificationType.ERROR, text)
    }

    showSuccess(text) {
        this._showNotification(NotificationType.SUCCESS, text)
    }

    showInfo(text) {
        this._showNotification(NotificationType.INFO, text)
    }

    _showNotification(notificationType, text) {
        const item = document.createElement("li");
        const notification = new Notification(item, notificationType, text);
        notification.initElement();
        this._element.appendChild(item);
    }

    static createAttachedElement() {
        const boxNotifier = document.createElement('ul');
        boxNotifier.className = "box-notifier";
        document.body.appendChild(boxNotifier);
        return new Notifier(boxNotifier);
    }
}
