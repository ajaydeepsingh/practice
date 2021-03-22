import * as React from "react";
import axios from "axios";
import { useRef } from "react";
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

const fetchUserData = (pageNumber: number) => {
  return axios
  .get('https://randomuser.me/api?page=${pageNumber}')
  .then(({ data }) => data)
  .catch((err) => {
    console.error(err);
  });
};

const getFullUserName = (userInfo: UserInfo) => {
  const first = userInfo.name.first;
  const last = userInfo.name.last;
  return `${first} ${last}`;
}

export default function App() {
  const [counter, setCounter] = useState(0);
  const [nextPageNumber, setNextPageNumber] = useState(1);
  const [userInfos, setUserInfos] = useState<any>([]);
  const [randomUserDataJSON, setRandomUserDataJSON] = useState("");

  const fetchNextUser = useRef(() => {});

  fetchNextUser.current = () => {
    fetchUserData(nextPageNumber).then((randomData) => {
      const newUserInfos = [...userInfos, ...randomData.results];
      setUserInfos(newUserInfos);
      setNextPageNumber(randomData.info.page + 1);
    });
  };

  useEffect(() => {
    fetchNextUser.current();
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
      <button
        onClick={() => {
          fetchNextUser.current();
        }}
      >
        Add user
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
