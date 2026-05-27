import { Notification, NotificationType } from "./Notifier/notification.js";
import { Notifier } from "./Notifier/notifier.js";

const element = document.createElement('div');

const notification = new Notification(element, NotificationType.WARNING,"123123123123123");
notification.initElement();
document.body.appendChild(element);

const notifier = Notifier.createAttachedElement();

notifier.setDefaultTimeout(200);
notifier.showWarning("рфпфп");
notifier.showError("error");
notifier.showInfo("dsgsgd");
notifier.showSuccess("sdgsgcd");
