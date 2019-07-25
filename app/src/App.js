import React, {useEffect, useState} from 'react';
import "./App.css";
import {Law} from "./components/Law";

function App() {
  const [law, setLaw] = useState([]);
  
  useEffect(() =>{
    fetch('/texts').then(response => response.json()).then(data => {
      setLaw(data);
    })
  }, [])

 
  return (
    <div className="App">
    <Law law={law}/>
    </div>
  );
}

export default App;
