# financial_agentic-ai


# Multi-Agent AI System for Financial Analysis & Web Research

## 📖 Overview
This project is a **dual-agent reasoning system** built using the **Phi (Phidata)** framework. It is designed to provide comprehensive financial analysis and market intelligence. By leveraging a specialized AI agent for real-time financial data and another for broader web research, the system can deliver highly accurate, cited, and actionable insights for investors and analysts.

## 🎯 Key Features
- **Financial Data Agent:** Retrieves real-time stock prices, analyst recommendations, company fundamentals, and the latest market news using the `YFinanceTools` library.
- **Web Search Agent:** Scrapes the internet via `DuckDuckGo` to gather up-to-date news, trends, and contextual information, ensuring no critical data is missed.
- **Groq-Powered LLMs:** Utilizes highly efficient, low-latency Large Language Models (`llama-3.3-70b-versatile`) deployed on Groq for rapid inference.
- **Multi-Agent Orchestration:** The primary agent intelligently delegates tasks to the specialized agents, synthesizing their results into a cohesive, structured response.
- **Interactive Playground:** Includes a built-in web-based UI (via `phi.playground`) to easily test and interact with the agents in real-time.
- **Transparent Sources:** All generated responses include verifiable citations and sources for complete transparency.

## 🛠️ Technology Stack
- **Framework:** Phi (Phidata) 2.0+
- **LLM Provider:** Groq (with LLaMA 3.3 70B model)
- **Financial API:** YFinanceTools (Stock price, news, fundamentals)
- **Search API:** DuckDuckGo Search
- **Deployment:** Phi Playground & Flask
- **Environment Management:** Python-dotenv

## 🚀 Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:
- **Python 3.9+**
- **Pip** (Python package installer)
- **Groq API Key** (Sign up at [console.groq.com](https://console.groq.com))
- **Phi API Key** (Sign up at [phidata.com](https://phidata.com))

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sws121-logo/saurabh-kumar-wasserstoff-AiTask
   cd saurabh-kumar-wasserstoff-AiTask
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: Ensure `requirements.txt` includes `phidata`, `groq`, `yfinance`, `duckduckgo-search`, `python-dotenv`, and `flask`)*.

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory of the project and add your API keys:
   ```env
   PHI_API_KEY=your_phi_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 🖥️ How to Use

### Option 1: Run the Multi-Agent System via Command Line
To execute the agents directly in your terminal and get a response for a specific query (e.g., NVIDIA stock analysis):
```bash
python multi_agent.py
```

### Option 2: Launch the Interactive Playground UI
To interact with the agents via a clean web-based interface:
```bash
python playground.py
```
Once the server starts, open your browser and navigate to `http://localhost:7777` (or the port specified in your terminal) to access the Playground dashboard.

## 📂 Project Structure
```
├── multi_agent.py          # Core script for executing the multi-agent system
├── playground.py           # Script to launch the web-based Playground UI
├── requirements.txt        # List of Python dependencies
├── .env                    # Environment variables file (API Keys)
├── README.md               # Project documentation
```

## 🔮 Use Cases
- **Investment Research:** Quickly gather a 360-degree view of a specific stock (Price + Analyst Sentiment + Latest News).
- **Market Monitoring:** Automate daily briefings on portfolio performance and global tech/sector trends.
- **Due Diligence:** Cross-reference company financials with independent web news to validate claims.

## 👨‍💻 Author
**Saurabh Kumar**
- LinkedIn: [https://www.linkedin.com/in/saurabh-kumar-742449171/](https://www.linkedin.com/in/saurabh-kumar-742449171/)
- GitHub: [https://github.com/sws121-logo](https://github.com/sws121-logo)

----
