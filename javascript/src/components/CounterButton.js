function CounterButton({ onClick, count }) {
  return <button onClick={onClick}>Clicked {count} times</button>;
}

export default CounterButton;
