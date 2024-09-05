import logo from "./logo.svg";
import "./App.css";
import { user, Profile } from "./components/Profile";
import ShoppingList from "./components/ShoppingList";
import CounterButton from "./components/CounterButton";
import { useState } from "react";

function LoginButton() {
  function handleClick() {
    alert("You clicked me!");
  }

  return <button onClick={handleClick}>Login</button>;
}

// let isLoggedIn = true;
// let content;
// if (isLoggedIn) {
//   content = <Profile />;
// } else {
//   content = <LoginButton />;
// }

function App() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div className="App">
      <h1>Welcome to my app {user.name} !</h1>
      {/* {content} */}
      <Profile />
      <ShoppingList />

      <hr />
      <LoginButton />

      <hr />
      <CounterButton count={count} onClick={handleClick} />
      <CounterButton count={count} onClick={handleClick} isEven={true} />

      <h1>{count}</h1>
    </div>
  );
}

export { App };
