const sessionApi = {
    get() {
        let uuid = localStorage.getItem('sessionId');
        if (!uuid) {
            uuid = crypto.randomUUID();
            localStorage.setItem('sessionId', uuid);
        }
        return uuid;
    }
}

export default sessionApi 