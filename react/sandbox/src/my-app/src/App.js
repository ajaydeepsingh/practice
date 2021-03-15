import * as React from "react";
import axios from "axios";
import "./styles.css";

const { userEffect, useState } = React;

const fetchUserData = () => {
  return axios
    .get("https://randomuser.me/api")
    .then((res) => {
      console.log(res);
      return JSON.stringify(res);
    })
    .catch((err) => {
      console.error(err);
    });
};

export default function App() {
  const [counter, setCounter] = useState(0);
  const [randomUserDataJSON, setRandomUserDataJSON] = useState('');


  return (
    <div className="App">
      <h1>React Sandbox</h1>
      <h2>Start editing to see some magic happen!</h2>
      <p>{counter}</p>
      <button
        onClick={() => {
          setCounter(counter + 1);
        }}
      >
        Increase Counter
      </button>

      <button
        onClick={() => {
          fetchUserData();
        }}
      >
        Get Random User Info
      </button>
    </div>
  );
}
