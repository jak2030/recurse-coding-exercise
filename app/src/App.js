import React, { useEffect, useState } from 'react';
import "./App.css";
import { Line } from "./components/Line";

function App() {
  const [line, setLine] = useState([]);
  const [username, setUsername] = useState("iamcardib");
  const [archetype, setArchetype] = useState("jester");

  useEffect(() => {
    fetch(`/lines?username=${username}&archetype=${archetype}`)
      .then(response => response.json())
      .then(data => {
        setLine(data);
      })
  }, [])


  return (
    <div className="App">
      <Line line={line} />
    </div>
  );
}

export default App;
