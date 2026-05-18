// enum - enumerate - перечисление

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
     */
    constructor(element, type, text) {
        this._element = element;
        this._type = type;
        this._text = text;
    }

    show(params) {

    }

    _hide() {

    }

    initElement() {
        const close = document.createElement ("button");
        this._element.appendChild(close);
        this._element.className = `Notification ${this._getTypeClassName()} `;
        this._element.textContent = this._text;
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