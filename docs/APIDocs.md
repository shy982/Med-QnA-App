# Documentation of APIs, Services, and Modules

# API Documentation

## Overview
This document outlines the available endpoints in the MediMate Q&amp;A application. The application provides endpoints for processing user messages using different methods, including simple text processing, OpenAI's GPT-3.5 model, and a Retrieval-Augmented Generation (RAG) approach.

## Endpoints

### 1. Simple Chat Test
- **Endpoint**: `/v1/chat/simple`
- **Method**: `POST`
- **Description**: A simple test endpoint that capitalizes the last user message. Used primarily for debugging purposes.
- **Request Body**:
  - `messages`: Array of message objects. Each message object should contain a `content` key with the message text.
- **Response**: A string with the last message in uppercase.
- **Example Request**:
  ```json
  {
    "messages": [
      {"content": "hello world"}
    ]
  }
  ```

### 2. Chat with GPT-3.5 (No RAG)
- **Endpoint**: `/v1/chat/openai`
- **Method**: `POST`
- **Description**: Processes messages using OpenAI's GPT-3.5 model without RAG, considering the entire conversation history.
- **Query Parameters**:
  - `model` (optional): Specifies the GPT model to use. Default is "gpt-3.5-turbo-instruct".
- **Request Body**:
  - `messages`: Array of message objects as described above.
  - `medicalHistory` (optional): String containing the medical history to be considered in the response.
- **Response**: A string containing the AI-generated response.
- **Example Request**:
  ```json
  {
    "messages": [
      {"content": "What are the symptoms of a cold?"}
    ],
    "medicalHistory": "Patient has a history of allergies."
  }
  ```

### 3. Chat with RAG
- **Endpoint**: `/v1/chat/openai/rag`
- **Method**: `POST`
- **Description**: Processes messages using a RAG approach, combining GPT-3.5 and external knowledge retrieval.
- **Query Parameters**:
  - `model` (optional): GPT model to use. Default is "gpt-3.5-turbo-instruct".
  - `dataset` (optional): The dataset for knowledge retrieval. Default is "nfcorpus".
- **Request Body**:
  - `messages`: Array of message objects as described above.
  - `medicalHistory` (optional): String containing relevant medical history.
- **Response**: A string containing the AI-generated response with external knowledge context.
- **Example Request**:
  ```json
  {
    "messages": [
      {"content": "Tell me about diabetes management."}
    ],
    "medicalHistory": "Patient has type 2 diabetes."
  }
  ```