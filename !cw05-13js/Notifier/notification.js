// enum - enumerate - перечисление
import "./notification.css";

/**
 * @enum {string}
 */
export const NotificationType = {
    INFO: 'info',
    WARNING: 'warning',
    SUCCESS: 'success',
    ERROR: 'error',
}

export class Notification {
    /**
     * @param {HTMLElement} element 
     * @param {NotificationType} type 
     * @param {string} text 
     * @param {number} timeoutMs
     */
    constructor(element, type, text, timeoutMs) {
        this._element = element;
        this._type = type;
        this._text = text;
        this._timeoutMs = timeoutMs;
    }

    close() {
        this._element.remove()
    }

    initElement() {
        const closeBtn = document.createElement("button");
        closeBtn.textContent = "x";
        closeBtn.className = "notification-close";
        this._element.appendChild(closeBtn);
        closeBtn.addEventListener('click', () => {
            this.close();
        });
        
        this._element.className = `Notification ${this._getTypeClassName()}`;
        
        const textBox = document.createElement('p');
        textBox.textContent = this._text;
        this._element.appendChild(textBox);

        setTimeout(this.close.bind(this), this._timeoutMs);
    }

    _getTypeClassName() {
        switch (this._type) {
            case NotificationType.INFO: return "Notification_info";
            case NotificationType.WARNING: return "Notification_warning";
            case NotificationType.SUCCESS: return "Notification_success";
            case NotificationType.ERROR: return "Notification_error";
        }
    }
}

// notifier.showWarning(text);
// notifier.showSuccess(text);