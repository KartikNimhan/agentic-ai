# **Agentic AI: A Multi-Agent System for Web and Finance Insights**

**Agentic AI** is a Python-based multi-agent system designed to gather web-based information and stock data using cutting-edge AI models. It integrates powerful tools like **Groq** for efficient AI computation and utilizes **DuckDuckGo** for web search and **Yahoo Finance (YFinance)** for financial data. The system's architecture is composed of individual agents, each with specific roles, including a **Web Search Agent** and a **Finance Agent**. These agents work in tandem to provide real-time stock insights and web-based information, displaying results in structured formats like tables for easy interpretation.

## Key Features:

- **Web Search Agent**: Searches the web for relevant information using DuckDuckGo and provides answers with proper source attribution.
- **Finance Agent**: Retrieves real-time stock data, including stock price, analyst recommendations, company news, and stock fundamentals from Yahoo Finance.
- **Multi-Agent Collaboration**: Combines the efforts of multiple agents to enhance data retrieval, providing more comprehensive answers with well-structured outputs.
- **Groq Model Integration**: Utilizes the advanced Groq model for efficient processing, ensuring high performance in tasks involving large-scale data.

## **Technologies Used:**
- **Groq Model**: AI model used for high-performance computation and data analysis.
- **DuckDuckGo API**: For retrieving web-based information securely and anonymously.
- **YFinance API**: For fetching real-time stock data, analyst recommendations, news, and more.
- **dotenv**: For loading environment variables securely, such as API keys.
- **Python**: The primary language for building and executing the agent system.

## **Setup Instructions:**

1. Clone this repository:
   ```bash
   git clone https://github.com/KartikNimhan/agentic-ai.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root with your **GROQ_API_KEY**:
   ```plaintext
   GROQ_API_KEY=your_api_key_here
   ```

4. Run the main application:
   ```bash
   python app.py
   ```

## **Usage Example:**
The multi-agent system can be queried for specific tasks, such as:
```python
multi_agent.print_response("summarize analyst recommendations and share the latest news for Google", stream=True)
```

## **Contributing:**
Feel free to fork the repository, make improvements, or create issues for any bugs or feature requests.

---

### **License**
Include any licenses if necessary (e.g., MIT License).

---

This description gives potential users and contributors a clear understanding of the purpose of the project, the technologies used, and how to get started.