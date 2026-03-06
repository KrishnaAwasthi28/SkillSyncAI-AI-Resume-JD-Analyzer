import { useState } from "react";
import axios from "axios";
import "../styles/upload.css";
import Loader from "../components/Loader";

function UploadSection({ setResult }) {
  const [jd, setJd] = useState("");
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!file || !jd.trim()) {
      alert("Please upload resume and paste job description.");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);
    formData.append("jobDescription", jd);

    try {
      setLoading(true);

      const response = await axios.post(
        "http://localhost:8080/api/analyze",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        },
      );

      setResult(response.data);
    } catch (error) {
      alert("Something went wrong!");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
    {loading && <Loader />}
    <div className="upload-box">
      <label>Upload Resume (PDF)</label>
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <label>Paste Job Description</label>
      <textarea
        value={jd}
        onChange={(e) => setJd(e.target.value)}
        placeholder="Paste job description here..."
      />

      <button className="analyze-btn" onClick={handleAnalyze}>
        {loading ? "Analyzing with AI..." : "Analyze Resume"}
      </button>
    </div>
    </>
  );
}

export default UploadSection;
