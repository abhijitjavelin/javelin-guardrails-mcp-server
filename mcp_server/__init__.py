"""
Javelin MCP Server - AI Security Guardrails for Model Context Protocol

This package provides an MCP (Model Context Protocol) server that integrates with
Javelin's AI security platform to offer comprehensive guardrails including:
- Prompt injection detection
- Trust & safety filtering 
- Language detection and validation

The server exposes Javelin's standalone guardrails API through the MCP protocol,
allowing AI applications to easily integrate advanced security measures.
"""

__version__ = "0.1.0"
__author__ = "Javelin"
__email__ = "support@getjavelin.com"

from .server import create_server, main

__all__ = ["create_server", "main"]
