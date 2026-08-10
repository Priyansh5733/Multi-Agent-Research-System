# Multi-Agent Research System

An AI-powered multi-agent research system built with LangChain and Mistral AI. The system uses specialized agents to search for information, extract relevant content, generate a structured research report, and critically review the final output.

## Features

- 🔍 Search Agent — Searches for recent, reliable, and relevant information.
- 📖 Reader Agent — Selects relevant sources and extracts deeper content.
- ✍️ Writer Chain — Generates a structured research report.
- 🧐 Critic Chain — Reviews the generated report and provides feedback.
- 🤖 Multi-Agent Architecture — Uses specialized agents for different research tasks.
- 🌐 Web Search & Scraping — Collects and processes information from online sources.
- 🖥️ Streamlit UI — Provides an interactive interface for running the research pipeline.
- 📄 Report Export — Allows generated reports to be downloaded as text files.

## Architecture

```text
                    User
                     │
                     ▼
              Research Topic
                     │
                     ▼
             ┌───────────────┐
             │  Search Agent │
             └───────┬───────┘
                     │
                     ▼
              Search Results
                     │
                     ▼
             ┌───────────────┐
             │  Reader Agent │
             └───────┬───────┘
                     │
                     ▼
              Scraped Content
                     │
                     ▼
             ┌───────────────┐
             │ Writer Chain  │
             └───────┬───────┘
                     │
                     ▼
              Research Report
                     │
                     ▼
             ┌───────────────┐
             │ Critic Chain  │
             └───────┬───────┘
                     │
                     ▼
              Critic Feedback
```

## How It Works

### 1. Search Agent

The Search Agent receives a research topic and searches for recent, reliable, and detailed information.

```text
Research Topic
      ↓
Search Agent
      ↓
Relevant Search Results
```

### 2. Reader Agent

The Reader Agent analyzes the search results, selects a relevant source, and extracts deeper information from the selected webpage.

```text
Search Results
      ↓
Source Selection
      ↓
Web Scraping
      ↓
Detailed Content
```

### 3. Writer Chain

The Writer Chain combines the search results and scraped content to generate a structured research report.

```text
Search Results
      +
Scraped Content
      ↓
Writer Chain
      ↓
Research Report
```

### 4. Critic Chain

The Critic Chain evaluates the generated report and provides feedback on its quality, completeness, and potential improvements.

```text
Research Report
      ↓
Critic Chain
      ↓
Critical Feedback
```

## Tech Stack

- Python
- LangChain
- Mistral AI
- Streamlit
- Pydantic
- Web Search Tools
- Web Scraping
- python-dotenv

## Project Structure

```text
MultiAgentSystem/
│
├── agents.py
├── app.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### File Description

| File | Description |
|------|-------------|
| `agents.py` | Contains the Search Agent, Reader Agent, Writer Chain, and Critic Chain |
| `app.py` | Streamlit user interface |
| `pipeline.py` | Main research pipeline that coordinates the agents |
| `tools.py` | Search and web scraping tools |
| `requirements.txt` | Python dependencies |
| `.env` | API keys and environment variables |
| `.gitignore` | Files and folders excluded from Git |
| `README.md` | Project documentation |

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd MultiAgentSystem
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key
```

Do not upload your `.env` file to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
.streamlit/secrets.toml
```

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application provides an interface where you can enter a research topic and start the complete multi-agent research workflow.

## Running the Pipeline Without Streamlit

The core research pipeline can also be executed directly from the terminal:

```bash
python pipeline.py
```

The program will ask for a research topic and execute the complete workflow.

## Example

### Input

```text
Impact of Generative AI on Data Science
```

### Workflow

```text
Research Topic
      ↓
Search Agent
      ↓
Search Results
      ↓
Reader Agent
      ↓
Scraped Content
      ↓
Writer Chain
      ↓
Research Report
      ↓
Critic Chain
      ↓
Final Feedback
```

### Output

The system produces:

- Search results
- Detailed scraped content
- Generated research report
- Critic feedback

## Future Improvements

- Automatic citation generation
- Improved source ranking and validation
- PDF report generation
- Research history and persistence
- Parallel agent execution
- Improved report formatting
- Source previews and direct links
- Additional specialized research agents
- Improved Streamlit interface

## Disclaimer

The system uses LLM-generated content and information retrieved from external sources. Generated research should be verified against reliable primary sources before being used for academic, professional, or high-stakes purposes.

## License

This project is licensed under the MIT License.
