import os


def test_import_dependencies():
    """
    Smoke test to ensure all critical dependencies install correctly.
    """
    import langchain
    import langgraph
    import langchain_community
    import langchain_core
    import langchain_groq
    import langchain_openai
    import faiss
    import streamlit
    import tavily


