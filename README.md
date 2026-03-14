# Document_Portal

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## Overview

Document_Portal is a sophisticated Python framework designed to build AI-powered applications that seamlessly integrate multiple Large Language Models (LLMs) such as OpenAI, Groq, and Claude. It leverages advanced embedding models and vector databases like Chroma and FAISS to facilitate sophisticated semantic search and contextual data retrieval. This comprehensive solution offers robust modules for streamlined document ingestion, in-depth analysis, intelligent comparison, and dynamic AI-powered chat functionalities, simplifying complex information management across various data types.

The primary motivation behind Document_Portal is to revolutionize and automate high-stakes financial workflows, specifically focusing on the critical tasks of cross-referencing and verifying crucial financial documents like invoices, receipts, and purchase orders. By providing an enterprise-grade solution, the project aims to eliminate the substantial overhead associated with manual auditing processes, drastically improve the detection of discrepancies, and ensure rigorous corporate compliance, thereby mitigating financial risks and operational inefficiencies.

Tailored for financial institutions and enterprises requiring stringent document verification, Document_Portal empowers organizations to achieve greater accuracy and efficiency in their operations. Its modular architecture, evident through dedicated components for data ingestion, analysis, and comparison, combined with a user-friendly Streamlit dashboard and full Docker support, ensures scalability, easy deployment, and maintainability. The framework is built with robustness in mind, featuring custom logging, exception handling, a dedicated API, and prompt management capabilities, making it a reliable solution for critical business applications.

## ✨ Features

*   ✨ Integrates diverse LLMs (OpenAI, Groq, Claude) and various embedding models for flexible AI applications.
*   🔍 Leverages FAISS and ChromaDB for advanced semantic search and contextual data retrieval.
*   📄 Provides robust modules for document ingestion, AI-powered analysis, comparison, and interactive chat.
*   💰 Automates high-stakes financial document verification to detect discrepancies and ensure corporate compliance.
*   🚀 Designed with a modular architecture, robust error handling, and Docker support for enterprise-grade scalability.
*   🖥️ Features an intuitive Streamlit dashboard for seamless user interaction and complex information management.
*   ☁️ Supports cloud-native deployments with Docker and AWS CloudFormation templates.

## 📦 Installation

```bash
git clone https://github.com/klan86at/Document_Portal.git
cd Document_Portal
```

## 🚀 Quick Start

To get started with Document_Portal:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-org/Document_Portal.git
    cd Document_Portal
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure API Keys:**
    Edit `config/config.yaml` to add your LLM API keys (e.g., OpenAI, Groq, Claude) and any other necessary configurations.
4.  **Launch the Streamlit UI:**
    This opens the interactive dashboard for document ingestion, analysis, comparison, and AI-powered chat in your browser.
    ```bash
    streamlit run streamlit_ui.py
    ```
5.  **Alternatively, run with Docker:**
    For containerized deployment, build and run the Docker image:
    ```bash
    docker build -t document-portal .
    docker run -p 8501:8501 document-portal
    ```
    Access the Document_Portal dashboard at `http://localhost:8501`.

## 📁 Project Structure

```
Document_Portal/
├── api
│   └── main.py
├── config
│   └── config.yaml
├── exception
│   ├── __init__.py
│   ├── custom_exception.py
│   └── custom_exception_archive.py
├── faiss_index
│   ├── session_20250819_223702_9d615c2b
│   │   ├── index.faiss
│   │   └── index.pkl
│   ├── index.faiss
│   └── index.pkl
├── infrastructure
│   └── document-portal-cf.yaml
├── logger
│   ├── __init__.py
│   └── custom_logger.py
├── model
│   └── models.py
├── notebook
│   ├── data
│   │   └── sample.pdf
│   ├── exception_experiment.ipynb
│   ├── experiments.ipynb
│   └── logging_experiment.ipynb
├── promptlib
│   ├── __init__.py
│   └── prompt_library.py
├── src
│   ├── doc_analyzer
│   │   ├── __init__.py
│   │   └── data_analysis.py
│   ├── doc_chat
│   │   ├── __init__.py
│   │   └── retrieval.py
│   ├── doc_compare
│   │   ├── __init__.py
│   │   └── doc_comparator.py
│   ├── doc_ingestion
│   │   ├── __init__.py
│   │   └── data_ingestion.py
│   └── __init__.py
├── static
│   └── style.css
├── templates
│   └── index.html
├── utils
│   ├── __init__.py
│   ├── config_loader.py
│   ├── doc_ops.py
│   ├── file_io.py
│   └── model_loader.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
├── streamlit_ui.py
├── test.py
└── version.py
```

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

1. Fork the repository at [https://github.com/klan86at/Document_Portal.git](https://github.com/klan86at/Document_Portal.git)
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

## 📄 License

This project is open source. See the [LICENSE](LICENSE) file for details.