const styles = document.createElement('style');
styles.textContent = `
  * { box-sizing: border-box; }
  body { font-family: system-ui, -apple-system, sans-serif; background: #f9fafb; padding: 2rem; color: #111827; }
  .container { max-width: 600px; margin: 0 auto; background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); }
  h1 { margin-top: 0; font-size: 1.5rem; }
  .input-group { position: relative; margin-bottom: 1rem; }
  input { width: 100%; padding: 0.75rem; border: 1px solid #d1d5db; border-radius: 4px; font-size: 1rem; outline: none; }
  input:focus { border-color: #3b82f6; box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2); }
  .status { font-size: 0.875rem; color: #6b7280; margin-bottom: 1rem; min-height: 1.25rem; }
  .user-list { list-style: none; padding: 0; margin: 0; }
  .user-item { padding: 1rem; border: 1px solid #e5e7eb; border-radius: 4px; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 1rem; transition: background-color 0.2s; }
  .user-item:hover { background-color: #f3f4f6; cursor: pointer; }
  .avatar { width: 40px; height: 40px; border-radius: 50%; background: #e5e7eb; }
  .user-info h3 { margin: 0 0 0.25rem 0; font-size: 1rem; }
  .user-info p { margin: 0; font-size: 0.875rem; color: #6b7280; }
`;
document.head.appendChild(styles);

const app = document.createElement('div');
app.className = 'container';
app.innerHTML = `
  <h1>User Directory Search</h1>
  <div class="input-group">
    <input type="text" id="searchInput" placeholder="Type a name to search (e.g. John)..." autocomplete="off" />
  </div>
  <div class="status" id="statusText"></div>
  <ul class="user-list" id="resultsList"></ul>
`;
document.body.appendChild(app);

const searchInput = document.getElementById('searchInput');
const statusText = document.getElementById('statusText');
const resultsList = document.getElementById('resultsList');

let debounceTimeout = null;
let currentAbortController = null;

function renderUsers(users) {
  resultsList.innerHTML = '';
  if (users.length === 0) {
    statusText.textContent = 'No users found.';
    return;
  }
  
  statusText.textContent = `Found ${users.length} user(s).`;
  
  users.forEach(user => {
    const li = document.createElement('li');
    li.className = 'user-item';
    
    const avatarData = user.image || `https://ui-avatars.com/api/?name=${user.firstName}+${user.lastName}&background=random`;
    
    li.innerHTML = `
      <img class="avatar" src="${avatarData}" alt="Avatar">
      <div class="user-info">
        <h3>${user.firstName} ${user.lastName}</h3>
        <p>${user.email} • ${user.company?.title || 'Employee'}</p>
      </div>
    `;
    
    li.addEventListener('click', () => {
      alert(`Selected: ${user.firstName} ${user.lastName}\nPhone: ${user.phone}`);
    });
    
    resultsList.appendChild(li);
  });
}

async function performSearch(query) {
  if (currentAbortController) {
    currentAbortController.abort();
  }
  
  currentAbortController = new AbortController();
  statusText.textContent = 'Searching...';
  resultsList.innerHTML = '';

  try {
    const response = await fetch(`https://dummyjson.com/users/search?q=${encodeURIComponent(query)}&limit=5`, {
      signal: currentAbortController.signal
    });
    
    if (!response.ok) throw new Error('Network response was not ok');
    
    const data = await response.json();
    renderUsers(data.users);
  } catch (error) {
    if (error.name === 'AbortError') return; 
    statusText.textContent = 'An error occurred while fetching results.';
    console.error('Fetch error:', error);
  }
}

searchInput.addEventListener('input', (event) => {
  const query = event.target.value.trim();
  
  clearTimeout(debounceTimeout);
  
  if (!query) {
    if (currentAbortController) currentAbortController.abort();
    statusText.textContent = '';
    resultsList.innerHTML = '';
    return;
  }
  
  statusText.textContent = 'Waiting for you to stop typing...';
  
  debounceTimeout = setTimeout(() => {
    performSearch(query);
  }, 400); 
});