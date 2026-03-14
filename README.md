# Document_Portal

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## Overview

Document_Portal is a comprehensive Python project engineered to streamline the development of AI-powered applications leveraging a diverse array of Large Language Models (LLMs). This framework provides seamless integration with popular LLM providers such as Groq, OpenAI, Claude, Hugging Face, Ollama, and Gemini, offering unparalleled flexibility for your NLP initiatives. At its core, Document_Portal supports a variety of embedding models and robust vector databases like Chroma and FAISS, enabling sophisticated semantic search, contextual data retrieval, and efficient information management across your document corpus. With built-in modules for document ingestion, analysis, comparison, and retrieval, it serves as a powerful toolkit for building intelligent systems.

This project was designed as an enterprise-grade solution to automate and streamline high-stakes financial workflows, specifically assisting in the cross-referencing and verification of Invoices, Receipts, and Local Purchase Orders (LPOs). It exists to eliminate the manual overhead of document auditing by leveraging advanced Natural Language Processing to detect discrepancies and validate transaction data across disparate formats.

By abstracting the complexities of multi-source LLM integration and vector-based semantic search, the Document_Portal provides a unified foundation for building intelligent Q&A and verification systems. Whether performing three-way matching between procurement documents or generating instant summaries of financial records, the system offers the modularity and precision required for real-world corporate compliance. Its structured architecture—featuring robust API endpoints, an intuitive Streamlit dashboard for finance teams, and Dockerization for secure, on-premise or cloud deployment—ensures that cutting-edge AI is both accessible to the business and scalable across the organization.

## ✨ Features

*   ✨ **Multi-LLM Integration:** Seamlessly connect with Groq, OpenAI, Claude, Hugging Face, Ollama, and Gemini for diverse AI capabilities.
*   📚 **Advanced Data Retrieval:** Leverage various embedding models and vector databases like Chroma and FAISS for efficient semantic search and contextual information.
*   🔄 **Robust Document Workflow:** Streamline document ingestion, analysis, and comparison with dedicated modules and pipelines.
*   💬 **AI-Powered Chat & Retrieval:** Build sophisticated conversational agents with advanced retrieval-augmented generation (RAG) features.
*   🌐 **Interactive Web Interface:** Engage with your AI applications through a user-friendly web interface powered by Streamlit and integrated APIs.
*   ⚙️ **Modular & Production-Ready:** Benefit from a well-structured, containerized (Docker), and cloud-deployable architecture with robust logging and error handling.

## 📦 Installation

```bash
git clone https://github.com/klan86at/Document_Portal.git
cd Document_Portal
```

## 🚀 Quick Start

To get started with Document_Portal:

1.  **Environment Setup**
    Create and activate a Conda environment, then install dependencies:
    ```bash
    conda create -n document_portal python=3.10 -y
    conda activate document_portal
    pip install -r requirements.txt
    ```
    ## Below commands are for windows (cmd)
    ```
    mkdir <project_folder_name>
    ```
    ```
    cd <project_folder_name>
    ```
    ```
    code.
    ```
    ## For conda env setup
    ```
    conda create -p <env_name> python=3.10 -y
    ```
    ```
    conda activate <path_of_the_env>
    ```
    ```
    pip install -r requirements.txt
    ```
    ## Git commands

    ```
    git init
    ```
    ```
    git add .
    ```
    ```
    git commit -m "<write_commit_msg>"
    ```
    ```
    git push -u origin main
    ```

    ## Minimum requirements for this project

    1. LLM Model ##groq(open source), openai(paid), claude(paid), huggingface(open), ollama(local), gemini

    2. Embedding model ## openai, hf, gemini

    3. Vector database ## Inmemory(chroma, faiss) ## Ondisk ## Cloudbased

2.  **Configuration**
    Edit `config/config.yaml` to add your API keys for chosen LLM providers (e.g., `OPENAI_API_KEY`, `GROQ_API_KEY`).
    *   Get Groq API key: [https://console.groq.com/keys](https://console.groq.com/keys)
    *   Get Google Gemini API key: [https://makers.generativeai.google/app/apikey](https://makers.generativeai.google/app/apikey)

3.  **Run the Application**
    Start the Streamlit UI for an interactive experience:
    ```bash
    streamlit run streamlit_ui.py
    ```
    Alternatively, launch the FastAPI backend service:
    ```bash
    uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
    ```
    This will make the application accessible, allowing you to integrate LLMs and manage documents.

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
