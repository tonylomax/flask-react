import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/api/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);


  return (
    <div className="App">
      <header className="App-header">
        <h1> Hello world, the unix time is: </h1>
        <p>The current time is {currentTime}.</p>
      </header>
    </div>
  );
}

export default App;
