import * as React from "react";
import axios from "axios";
import "./styles.css";

const { useEffect, useState } = React;

interface UserName {
  first: string;
  last: string;
  title: string;
}

interface UserPicture {
  thumbnail: string;
}

interface UserInfo {
  name: UserName;
  picture: UserPicture;
}

const fetchUserData = async () => {
  try {
    const { data } = await axios
      .get("https://randomuser.me/api");
    console.log(data);
    return data;
  } catch (err) {
    console.error(err);
  }
};

const getFullUserName = (userInfo: UserInfo) => {
  const first = userInfo.name.first;
  const last = userInfo.name.last;
  return first + " " + last;
}

export default function App() {
  const [counter, setCounter] = useState(0);
  const [userInfos, setUserInfos] = useState<any>([]);
  const [randomUserDataJSON, setRandomUserDataJSON] = useState("");

  useEffect(() => {
    fetchUserData().then((randomData) => {;
    setRandomUserDataJSON(JSON.stringify(randomData, null, 2) || 'No user data found');
    setUserInfos(randomData.results);
    console.log(randomData);
  })
  }, []);

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

      
      {
        userInfos.map((userInfo: UserInfo, idx: number) => (
          <div key={idx}>
          <p>{getFullUserName(userInfo)}</p>
          <img src={userInfo.picture.thumbnail}/>
          </div>
        ))
      }

    </div>
  );
}
