import { useState } from "react";
import Navbar from "../components/Navbar";
import UploadSection from "../components/UploadSection";
import ResultSection from "../components/ResultSection";
import "../styles/home.css";

function Home() {
  const [result, setResult] = useState(null);

  return (
    <>
      <div className="container">
        <h1 className="title">Align your resume with job descriptions using AI</h1>
        <UploadSection setResult={setResult} />
        <ResultSection result={result} />
      </div>
    </>
  );
}

export default Home;