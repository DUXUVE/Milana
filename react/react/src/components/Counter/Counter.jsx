import { useState } from "react";
import "./Counter.css"
import { useEffect } from "react";

function Counter(props) {
    const [count, setCount] = useState(0);
    const [isFlashed, setFlashed] = useState(false);
    const flashTimeoutId = useRef(null);
    console.log(`render ${count} ${props.state}`);

    useEffect(() => {
      setFlashed((isFlashed) => !isFlashed);

      setTimeout(() => {
        setFlashed((isFlashed) => !isFlashed);
      }, 1000)

      return () => { console.log('bye bye') }
    }, [count])

    const increment = () => setCount(count + 1);
    return (
        <button
          type="button"
          className={`Counter ${isFlashed ? 'Counter_flashed' : ''}`}
          onClick={increment}
        >
          Count is {count}
        </button>
    );
}

export default Counter;