# ASTRA – AI System for Ticket Routing & Assistance

This project presents a modular, AI-driven multi-agent customer support system designed to enhance the efficiency of support workflows. It simulates how an organization can automate issue analysis, ticket classification, routing, solution recommendation, and resolution time estimation using multiple intelligent agents working in sync.

## Problem Statement

Manual customer support systems are time-consuming and error-prone. Agents often sift through large volumes of tickets, resulting in delayed responses, inconsistent routing, and inefficient resolutions. This project addresses these challenges by introducing a multi-agent system that automates support processes through LLMs and semantic search on historical data.

## Solution

Our system leverages a locally run LLaMA3 model via Ollama to power five independent agents, each responsible for a specific task in the support pipeline:

- **Summarization Agent**: Converts user descriptions into concise summaries.
- **Retriever Agent**: Fetches relevant historical tickets using vector embeddings.
- **Routing Agent**: Assigns the issue to the correct support team.
- **Resolver Agent**: Recommends actionable and accurate resolution steps.
- **Time Estimator Agent**: Predicts how long it may take to resolve the issue.

This architecture ensures that customer issues are processed swiftly and intelligently without relying on predefined responses.

## Features

- Runs entirely offline using local LLMs (LLaMA3 with Ollama)
- Semantic search over historical ticket data using FAISS
- Modular agent design for extensibility
- Context-aware resolution recommendations
- Real-time routing and time prediction

## Tech Stack

- Python 3.10+
- FAISS for vector similarity search
- Ollama (for running local LLaMA3)
- Pandas, Scikit-learn, NumPy
- Langchain (optional)

