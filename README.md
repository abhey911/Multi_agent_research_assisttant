# Multi-Agent Research Assistant 🤖

An intelligent research system powered by multiple specialized AI agents that collaborate to research topics, analyze information, synthesize findings, and produce comprehensive research reports.

## 🌟 Features

- **Multi-Agent Collaboration**: Specialized agents work together (Researcher, Analyzer, Writer, Critic)
- **Autonomous Research**: Agents independently gather and process information
- **Quality Assurance**: Built-in review and revision cycle
- **Interactive UI**: User-friendly Streamlit web interface
- **Comprehensive Reports**: Well-structured, properly cited research documents
- **Customizable**: Adjustable research depth and configuration

## 🏗️ Architecture

The system uses four specialized agents:

1. **🔍 Researcher Agent**: Gathers information from web sources
2. **📊 Analyzer Agent**: Processes data and extracts insights
3. **✍️ Writer Agent**: Creates comprehensive research reports
4. **🔎 Critic Agent**: Reviews and ensures quality

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- Internet connection for web searches

## 🚀 Installation

### 1. Clone or Download the Repository

```bash
cd multi-agent-research
```

### 2. Create Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
2. Edit `.env` and add your API keys:
   ```env
   GOOGLE_API_KEY=your_google_gemini_api_key_here
   SERPAPI_API_KEY=your_serpapi_key_here  # Optional
   ```

To get a Google Gemini API key:
- Visit: https://makersuite.google.com/app/apikey
- Sign in with your Google account
- Create a new API key
- Copy and paste it into your `.env` file

## 💻 Usage

### Running the Application

Start the Streamlit web interface:

```bash
streamlit run streamlit_app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Using the Interface

1. **Enter Research Topic**: Type your research query in the text area
2. **Select Research Depth**: Choose between Quick, Standard, or Deep
3. **Start Research**: Click the "Start Research" button
4. **Monitor Progress**: Watch the agent progress indicators
5. **View Report**: Read the generated research report
6. **Download/Copy**: Save or copy the report as needed

### Example Research Topics

- "Current state of quantum computing and its applications in cryptography"
- "Impact of artificial intelligence on healthcare diagnostics"
- "Renewable energy technologies and their economic viability"
- "Evolution of blockchain technology beyond cryptocurrency"
- "Latest developments in gene therapy and CRISPR technology"

## 📁 Project Structure

```
multi-agent-research/
├── src/
│   ├── agents/              # Agent implementations
│   │   ├── researcher.py    # Research agent
│   │   ├── analyzer.py      # Analysis agent
│   │   ├── writer.py        # Writing agent
│   │   └── critic.py        # Review agent
│   ├── tools/               # Agent tools
│   │   ├── search_tool.py   # Web search functionality
│   │   ├── scraping_tool.py # Web scraping functionality
│   │   └── processing_tool.py # Data processing
│   ├── tasks/               # Task definitions
│   │   └── research_tasks.py # Research workflow tasks
│   └── utils/               # Utility functions
│       ├── config.py        # Configuration management
│       └── helpers.py       # Helper functions
├── config/
│   └── agents_config.yaml   # Agent and task configurations
├── outputs/
│   └── reports/             # Generated research reports
├── streamlit_app.py         # Main application
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variables template
└── README.md                # This file
```

## ⚙️ Configuration

### Agent Configuration

Modify `config/agents_config.yaml` to customize agent behavior:

```yaml
agents:
  researcher:
    role: "Research Specialist"
    goal: "Gather comprehensive information on {topic}"
    max_iterations: 10
  # ... other agents
```

### Environment Variables

Available configuration options in `.env`:

```env
# Required
GOOGLE_API_KEY=your_key_here

# Optional
SERPAPI_API_KEY=your_key_here
MAX_SEARCH_RESULTS=10
MAX_ITERATIONS=5
RESEARCH_DEPTH=standard
```

## 🛠️ Troubleshooting

### Common Issues

**1. ModuleNotFoundError**
```bash
# Ensure virtual environment is activated and dependencies are installed
pip install -r requirements.txt
```

**2. API Key Errors**
- Verify your `.env` file exists and contains valid API keys
- Check that GOOGLE_API_KEY is set correctly

**3. Search Tool Issues**
- The system uses DuckDuckGo by default (no API key needed)
- For Google search, add SERPAPI_API_KEY to your `.env`

**4. Slow Performance**
- Research can take 3-5 minutes depending on topic complexity
- Reduce MAX_SEARCH_RESULTS in `.env` for faster results

## 📊 How It Works

### Workflow

1. **User Input** → Research topic submitted
2. **Manager** → Coordinates agent workflow
3. **Researcher** → Searches web and gathers information
4. **Analyzer** → Processes findings and extracts insights
5. **Writer** → Creates structured research report
6. **Critic** → Reviews quality and suggests improvements
7. **Output** → Final polished research report

### Agent Communication

Agents communicate through a sequential workflow where each agent's output becomes the input for the next:

```
Researcher → Analyzer → Writer → Critic
   ↓            ↓         ↓         ↓
Sources → Insights → Draft → Review → Final Report
```

## 🎯 Use Cases

- **Academic Research**: Literature reviews, topic summaries
- **Market Research**: Industry analysis, competitor research
- **Technical Documentation**: Technology assessments, feasibility studies
- **Due Diligence**: Company research, risk analysis
- **Content Creation**: In-depth articles, white papers
- **Learning**: Study guides, topic explorations

## 🔒 Privacy & Security

- All processing happens locally except API calls to Google Gemini
- No data is stored or transmitted to third parties
- Reports are saved locally in the `outputs/reports` directory
- API keys are stored in `.env` (never commit this file)

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Additional search tools and data sources
- Parallel agent execution
- Enhanced UI features
- Custom report templates
- Multi-language support

## 📝 License

This project is provided as-is for educational and research purposes.

## 🙏 Acknowledgments

Built with:
- [CrewAI](https://github.com/joaomdmoura/crewAI) - Multi-agent framework
- [Google Gemini](https://deepmind.google/technologies/gemini/) - Language models
- [Streamlit](https://streamlit.io/) - Web interface
- [LangChain](https://www.langchain.com/) - LLM framework

## 📧 Support

For issues and questions:
1. Check the troubleshooting section
2. Review configuration files
3. Ensure all dependencies are installed
4. Verify API keys are valid

## 🔄 Version History

- **v1.0.0** (December 2025) - Initial release
  - Multi-agent research system
  - Streamlit web interface
  - Google Gemini integration
  - Web search and scraping tools

---

**Happy Researching! 🚀**
