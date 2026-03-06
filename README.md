<h1 align="center">SkillSyncAI – AI Resume JD Analyzer</h1>

<p align="center">
An AI-powered system that evaluates how well a <b>resume matches a job description</b> using 
<b>Retrieval Augmented Generation (RAG)</b>, embeddings, and a Large Language Model.
</p>

<hr>

<h2>🧠 System Architecture</h2>

<pre>
React Frontend
      │
      ▼
Spring Boot Backend
      │
      ▼
FastAPI AI Microservice
      │
      ▼
RAG Pipeline (Embeddings + FAISS)
      │
      ▼
Large Language Model
</pre>

<p>
The frontend sends the resume and job description to the Spring Boot backend, which validates
the request and forwards it to a FastAPI microservice where the AI analysis is performed.
</p>

<hr>

<h2>🧠 RAG Pipeline Architecture</h2>

<pre>
Resume PDF → Loader → Chunker → Embeddings → FAISS Vector Store
                                             ▲
                                             │
Job Description TXT → Loader → Chunker → Embeddings → Matcher
                                                         │
                                                         ▼
                                                    LLM Explainer
                                                         │
                                                         ▼
                                                   Final Match Report
</pre>

<p>
The pipeline uses vector similarity search to match resume content with job description
requirements and then generates explanations using a Large Language Model.
</p>

<hr>

<h2>✨ Features</h2>

<ul>
<li>📄 Upload Resume (PDF)</li>
<li>📝 Paste Job Description</li>
<li>🤖 AI-based Resume Evaluation</li>
<li>📊 Match Score Calculation</li>
<li>✅ Strength Identification</li>
<li>❌ Skill Gap Detection</li>
<li>💡 AI-powered Recommendations</li>
<li>⚡ Fast Microservice Architecture</li>
<li>🎨 Modern Responsive UI</li>
</ul>

<hr>

<h2>🛠 Tech Stack</h2>

<h3>Frontend</h3>
<ul>
<li>React.js</li>
<li>CSS</li>
<li>Axios</li>
</ul>

<h3>Backend</h3>
<ul>
<li>Spring Boot</li>
<li>WebClient</li>
</ul>

<h3>AI Microservice</h3>
<ul>
<li>FastAPI</li>
<li>LangChain</li>
<li>FAISS Vector Database</li>
<li>Sentence Transformers</li>
<li>Groq LLM</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>

<pre>
SkillSyncAI-AI-Resume-JD-Analyzer
│
├── resume-jd-analyzer-frontend
│     └── React application
│
├── resume-jd-analyzer-spring-backend
│     └── Spring Boot backend
│
├── ResumeAnalyzer
│     └── FastAPI AI microservice
│
└── README.md
</pre>

<hr>

<h2>⚙️ Installation & Setup</h2>

<h3>1️⃣ Clone Repository</h3>

<pre>
git clone https://github.com/&lt;your-username&gt;/SkillSyncAI-AI-Resume-JD-Analyzer.git
cd SkillSyncAI-AI-Resume-JD-Analyzer
</pre>

<hr>

<h3>2️⃣ Run Frontend (React)</h3>

<pre>
cd resume-jd-analyzer-frontend
npm install
npm run dev
</pre>

<p>Frontend runs on:</p>

<pre>http://localhost:5173</pre>

<hr>

<h3>3️⃣ Run Spring Boot Backend</h3>

<pre>
cd resume-jd-analyzer-spring-backend
mvn spring-boot:run
</pre>

<p>Backend runs on:</p>

<pre>http://localhost:8080</pre>

<hr>

<h3>4️⃣ Run FastAPI AI Microservice</h3>

<pre>
cd ResumeAnalyzer
pip install -r requirements.txt
uvicorn api:app --reload
</pre>

<p>FastAPI runs on:</p>

<pre>http://localhost:8000</pre>

<p>Swagger documentation:</p>

<pre>http://localhost:8000/docs</pre>

<hr>

<h2>🔐 Environment Variables</h2>

<p>Create a <code>.env</code> file inside the AI microservice folder:</p>

<pre>
GROQ_API_KEY=your_api_key_here
</pre>

<hr>

<h2>📊 Example Output</h2>

<pre>
Status: PARTIAL_MATCH
Score: 67%

Strengths
• Strong proficiency in Java and Spring Boot
• Experience with REST APIs
• Knowledge of MySQL and JWT authentication

Gaps
• No PostgreSQL experience
• Limited microservices exposure

Recommendations
• Add PostgreSQL to skillset
• Build microservices-based projects
• Improve cloud deployment experience
</pre>

<hr>

<h2>🚀 Future Improvements</h2>

<ul>
<li>ATS Resume Optimization</li>
<li>Multiple Resume Comparison</li>
<li>Cloud Deployment</li>
<li>User Authentication</li>
<li>Resume History Tracking</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<p><b>Krishna Awasthi</b></p>

<ul>
<li>GitHub: https://github.com/KrishnaAwasthi28</li>
<li>LinkedIn: https://www.linkedin.com/in/krishna-awasthi-5a26a1213</li>
</ul>

<hr>

<p align="center">
⭐ If you like this project, consider giving it a star on GitHub!
</p>
