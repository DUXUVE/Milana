import { useState } from 'react';
import './App.css'
import Counter from './components/Counter/Counter.jsx'

function App() {
  const [test, setTest] = useState(false);
  return (
  <section className="App__container">
    <Counter state={test} />
    { test ? < Counter /> : null }
    <button onClick={() => setTest(!test)}>test</button>
  </section>
  );
}

export default App;
