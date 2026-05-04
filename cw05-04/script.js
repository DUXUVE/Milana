const buttonOpenModal = document.querySelector("[data-open-modal]");
buttonOpenModal.addEventListener('click', () => {
    // нужно добавить класс active к id modal
    const modal = document.getElementById('modal');
    modal.classList.add('active');
});


const buttonCloseModal = document.querySelector("[data-close-modal]");
buttonCloseModal.addEventListener('click', () => {
    const modal = document.getElementById('modal');
    modal.classList.remove('active');
});


const employeeSaveForm = document.querySelector("#modal form");
employeeSaveForm.addEventListener('submit', (event) => {
    event.preventDefault();
    // создать элемент 
    const employeeCard = document.createElement('div');
    employeeCard.classList.add('card');
    const employeesList = document.querySelector(".employees-list");
    
    const cardName = document.createElement('div');
    cardName.classList.add('name');
    const nameInput = document.querySelector('[name="name"]');
    cardName.textContent = nameInput.value;
    nameInput.value = '';
    employeeCard.appendChild(cardName);

    const inputRole = document.querySelector('[name="role"]');
    const inputContact = document.querySelector('[name="contact"]');
    
    employeesList.appendChild(employeeCard);
});