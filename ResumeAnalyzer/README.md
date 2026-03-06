<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Resume–JD Analyzer</title>
</head>
<body>

<h1>Resume–JD Analyzer</h1>

<p>
An end-to-end <strong>semantic Resume–Job Description matching system</strong> built using
<strong>embeddings, FAISS, and LLM-based explanations</strong>.
This project evaluates how well a resume matches a given job description in a
<strong>deterministic, explainable, and scalable</strong> way.
</p>

<hr/>

<h2>🚀 Key Features</h2>
<ul>
  <li>Loads resume PDFs and job description text files</li>
  <li>Splits documents into semantic chunks using LangChain</li>
  <li>Generates embeddings using Sentence Transformers</li>
  <li>Stores and searches resume embeddings using FAISS</li>
  <li>Determines MATCH / PARTIAL / MISSING using similarity thresholds</li>
  <li>Uses an LLM (ChatGroq – LLaMA 3) only for explanations (no hallucinations)</li>
  <li>Produces human-readable, recruiter-friendly output</li>
</ul>

<hr/>

<h2>🧠 System Design Overview</h2>

<pre>
Resume PDF ──► Loader ──► Chunker ──► Embeddings ──► FAISS Vector Store
                                                      ▲
                                                      │
Job Description TXT ──► Loader ──► Chunker ──► Embeddings ──► Matcher
                                                                  │
                                                                  ▼
                                                          LLM Explainer
                                                                  │
                                                                  ▼
                                                         Final Match Report
</pre>

<hr/>

<h2>📂 Project Structure</h2>

<pre>
ResumeAnalyzer/
│
├── data/
│   ├── resume/
│   │   └── KrishnaAwasthiSDE.pdf
│   └── jobdescription/
│       └── jobdescription.txt
│
├── src/
│   ├── loader.py
│   ├── chunker.py
│   ├── embedding.py
│   ├── vectorstore.py
│   ├── matcher.py
│   └── llm_explainer.py
│
├── main.py
├── README.md
├── requirements.txt
├── pyproject.toml
├── .env
└── .venv/
</pre>

<hr/>

<h2>🛠️ Tech Stack</h2>
<ul>
  <li><strong>Language:</strong> Python</li>
  <li><strong>Embeddings:</strong> Sentence Transformers (all-MiniLM-L6-v2)</li>
  <li><strong>Vector Store:</strong> FAISS (cosine similarity)</li>
  <li><strong>Chunking:</strong> LangChain RecursiveCharacterTextSplitter</li>
  <li><strong>LLM:</strong> ChatGroq (OpenAI/gpt-oss-120b)</li>
  <li><strong>Environment Management:</strong> python-dotenv,UV</li>
</ul>

<hr/>

<h2>⚙️ Setup Instructions</h2>

<h3>1. Clone the repository</h3>
<pre>
git clone https://github.com/&lt;your-username&gt;/Resume-JD-Analyzer.git
cd Resume-JD-Analyzer
</pre>

<h3>2. Create and activate virtual environment</h3>
<pre>
python -m venv .venv
source .venv/bin/activate  <!-- Windows: .venv\Scripts\activate -->
</pre>

<h3>3. Install dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>4. Set environment variables</h3>
<p>Create a <code>.env</code> file in the project root:</p>
<pre>
GROQ_API_KEY=your_groq_api_key_here
</pre>

<hr/>

<h2>▶️ How to Run</h2>

<pre>
python main.py
</pre>

<p>
The program will:
</p>
<ul>
  <li>Load the resume and job description</li>
  <li>Perform semantic matching</li>
  <li>Print match status, similarity score, evidence, and LLM-based explanation</li>
</ul>

<hr/>

<h2>📊 Sample Output</h2>

<pre>
Requirement 1:
JD Requirement : Experience with Spring Boot and REST APIs
Status         : PARTIAL
Score          : 0.52
Evidence       : Worked on backend services using Spring Boot
Explanation    : The resume mentions Spring Boot experience, but REST API
development is not explicitly demonstrated. Adding clear REST API
implementation details would improve the match.
</pre>

<hr/>

<h2>🎯 Design Principles</h2>
<ul>
  <li>Deterministic decision-making using similarity thresholds</li>
  <li>LLM used only for explanation, not for logic</li>
  <li>Separation of concerns (loader, chunker, matcher, explainer)</li>
  <li>API-ready architecture for future extensions</li>
</ul>

<hr/>

<h2>🔮 Future Enhancements</h2>
<ul>
  <li>Expose functionality via FastAPI</li>
  <li>Support multiple resumes and JDs</li>
  <li>Generate overall match percentage</li>
  <li>Export report as JSON or PDF</li>
  <li>Add frontend dashboard</li>
</ul>

<hr/>

<h2>👤 Author</h2>
<p>
<strong>Krishna Awasthi</strong><br/>
Backend & Java-focused Software Engineer with interest in GenAI and RAG systems.
</p>

<hr/>

<h2>📜 License</h2>
<p>
This project is licensed under the MIT License.
</p>

</body>
</html>