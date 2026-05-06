const modal = document.getElementById('modal');
const cardSaveForm = modal.querySelector('.card-save-form');

const buttonOpenModal = document.querySelector("[data-open-modal]");

let cardFieldElementsToEdit = null;

buttonOpenModal.addEventListener('click', () => {
    // нужно добавить класс active к id modal
    modal.classList.add('active');
});

const buttonCloseModal = document.querySelector("[data-close-modal]");
buttonCloseModal.addEventListener('click', () => {
    const modal = document.getElementById('modal');
    modal.classList.remove('active');
});

const employeesList = document.querySelector(".employees-list");
employeesList.addEventListener('click', (event) => {
    const card = event.target.closest('.card');
    if (!card) return;
    const cardName = card.querySelector(".name");
    const cardRole = card.querySelector(".role");
    const cardContact = card.querySelector(".contact");
    const nameInput = cardSaveForm.elements.name;
    nameInput.value = cardName.textContent;
    const inputRole = cardSaveForm.elements.role;
    inputRole.value = cardRole.textContent;
    const inputContact = cardSaveForm.elements.contact;
    inputContact.value = cardContact.textContent;
    cardFieldElementsToEdit = {name: cardName, role: cardRole, contact: cardContact}
    const modal = document.getElementById('modal');
    modal.classList.add('active');
});

cardSaveForm.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!cardFieldElementsToEdit) {
        // создать элемент 
        cardFieldElementsToEdit = createEmployeeCard();
    }
    updateCardFieldsByInputs(cardFieldElementsToEdit);
});

function updateCardFieldsByInputs(cardFilds) {
    const nameInput = cardSaveForm.elements.name;
    cardFilds.name.textContent = nameInput.value;
    const inputRole = cardSaveForm.elements.role;
    cardFilds.role.textContent = inputRole.value;
    const inputContact = cardSaveForm.elements.contact;
    cardFilds.contact.textContent = inputContact.value;
}

function createEmployeeCard() {
    const employeeCard = document.createElement('div');
    employeeCard.classList.add('card');
    employeesList.appendChild(employeeCard);

    const cardName = document.createElement('div');
    cardName.classList.add('name');
    nameInput.value = '';
    employeeCard.appendChild(cardName);

    const cardRole = document.createElement('div');
    cardRole.classList.add('role');
    inputRole.value = '';
    employeeCard.appendChild(cardRole);
    
    const cardContact = document.createElement('div');
    cardContact.classList.add('contact');
    inputContact.value = '';
    employeeCard.appendChild(cardContact);

    return {name: cardName, role: cardRole, contact: cardContact}
}