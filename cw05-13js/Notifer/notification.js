/**
 * @enum {string}
 */
export const NotificationType = {
    info: 'info',
    warning: 'warnin',
    error: 'error',
    success: 'success'
}
/**
 * @type {NotificationType}
 */
export class Notification {
    
    constructor(element, type, text) {
        this._element = element;
        this._type = type;
        this._text = Text;
    }

    show (parms) {

    }

    _hide () {

    }

    initElement() {
        
    }
}


// notifer.showWarning(text);
// notifer.showSuccess(text);