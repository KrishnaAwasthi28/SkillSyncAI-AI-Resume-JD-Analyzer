import { useEffect, useState } from "react";
import "../styles/loader.css";

function Loader() {

  const messages = [
    "Analyzing Resume with AI...",
    "Extracting resume content...",
    "Matching skills with job description...",
    "Running AI evaluation...",
    "Generating recommendations..."
  ];

  const [index, setIndex] = useState(0);

  useEffect(() => {

    const interval = setInterval(() => {

      setIndex((prev) => (prev + 1) % messages.length);

    }, 2500);

    return () => clearInterval(interval);

  }, []);

  return (
    <div className="loader-overlay">

      <div className="loader-box">

        <div className="spinner"></div>

        <p className="loader-text">{messages[index]}</p>

      </div>

    </div>
  );
}

export default Loader;