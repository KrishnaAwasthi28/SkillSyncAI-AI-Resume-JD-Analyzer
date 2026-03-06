import "../styles/about.css";

function About(){

  return(
    <div className="about-container">

      <h1>About AlignCV AI</h1>

      <p>
        AlignCV AI is an AI-powered resume analysis platform that helps job seekers
        understand how well their resume matches a specific job description.
      </p>

      <p>
        The system uses advanced AI techniques including Retrieval Augmented
        Generation (RAG), vector embeddings, and large language models to compare
        resumes with job descriptions and provide meaningful insights.
      </p>

      <h2>Features</h2>

      <ul>
        <li>AI-powered resume evaluation</li>
        <li>Match score calculation</li>
        <li>Strength and skill gap analysis</li>
        <li>Personalized recommendations</li>
      </ul>

      <h2>Technology Stack</h2>

      <ul>
        <li>React.js Frontend</li>
        <li>Spring Boot Backend</li>
        <li>FastAPI AI Microservice</li>
        <li>FAISS Vector Search</li>
        <li>RAG Pipeline</li>
      </ul>

    </div>
  )
}

export default About