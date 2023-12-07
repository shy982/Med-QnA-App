// APIConfig.js

const API_BASE_URL = "http://127.0.0.1:5000";

const API_ENDPOINTS = {
    SIMPLE_CHAT: "/v1/chat/simple",
    OPENAI_CHAT: "/v1/chat/openai",
    RAG_CHAT: "/v1/chat/rag",
    RAG_LLAMA: "/v2/chat/rag"
};

export {API_BASE_URL, API_ENDPOINTS};
