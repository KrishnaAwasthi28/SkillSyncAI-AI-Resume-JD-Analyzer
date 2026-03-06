import "../styles/result.css";
import { CircularProgressbar } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";

function ResultSection({ result }) {

  if (!result) return null;

  const strengths = result.strengths || [];
  const gaps = result.gaps || [];
  const recommendations = result.recommendations || [];

  return (
    <div className="result-box">

      <div className="score-card">

        <div className="score-circle">
          <CircularProgressbar
            value={result.score}
            text={`${result.score}%`}
          />
        </div>

        <div className="status">Status: {result.status}</div>

      </div>

      <div className="result-section strengths">
        <h4>Strengths</h4>
        <ul>
          {strengths.map((item, i) => (
            <li key={i}>{item}</li>
          ))}
        </ul>
      </div>

      <div className="result-section gaps">
        <h4>Gaps</h4>
        <ul>
          {gaps.map((item, i) => (
            <li key={i}>{item}</li>
          ))}
        </ul>
      </div>

      <div className="result-section recommendations">
        <h4>Recommendations</h4>
        <ul>
          {recommendations.map((item, i) => (
            <li key={i}>{item}</li>
          ))}
        </ul>
      </div>

    </div>
  );
}

export default ResultSection;