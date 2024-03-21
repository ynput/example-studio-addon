// My React App.

import AYONLogo from "./assets/ayon.svg";
import React, { useState } from "react";
import "./App.css";


function App() {
  const [count, setCount] = useState(0);

  return (
    <>
    <div className="content">
      <a href="https://ynput.io/" target="_blank">
        <img src={AYONLogo} className="logo" alt="AYON logo" />
      </a>

      <h1>Welcome to Our Studio!</h1>

      <p className="read-the-docs">Click on the logo to learn more.</p>
      </div>
    </>
  );
}

export default App;
