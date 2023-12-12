```
Med-QnA-App/
├── src/
│   ├── main/
│   │   ├── backend/
│   │   │   ├── marshaler/
│   │   │   │   └── chat_io_service.py      # Handles chat input/output operations
│   │   │   └── qna_service/
│   │   │       └── open_ai_client.py       # Manages interactions with OpenAI API
│   │   └── ui/web/medi-mate/               # Main UI codebase
│   │       ├── components/
│   │       │   ├── Chat/
│   │       │   │   └── ...                 # Chat related components
│   │       │   ├── Layout/
│   │       │   │   ├── Footer.js           # Footer component
│   │       │   │   └── Navbar.js           # Navbar component
│   │       │   ├── ModelSelection/
│   │       │   │   ├── RAGToggle.js        # Toggle for RAG feature
│   │       │   │   └── ...                 # Other model selection components
│   │       │   └── ...
│   │       ├── App.js                      # Main application component
│   │       └── index.js                    # Entry point for the React application
│   |── test/                               # Test files
│   └── experiments/                        # RAG experiments, evaluations, and results
├── public/
│   ├── index.html                          # HTML template
│   └── ...
├── .env                                    # Environment configuration file
├── package.json                            # NPM package configuration
├── requirements.txt                        # Python dependencies
└── ...                                     # Docker compose and other files
```