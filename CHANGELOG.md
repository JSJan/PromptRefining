# Changelog

All notable changes to PromptRefiner will be documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Project scaffold with Python FastAPI backend and React frontend
- Token counting using tiktoken (OpenAI models) and anthropic-tokenizer
- Cost estimation for GPT-4o, GPT-4o-mini, GPT-3.5-turbo, Claude 3.5 Sonnet, Claude 3 Haiku
- LLM-powered prompt refinement via OpenAI and Anthropic APIs
- Side-by-side comparison of original vs refined prompts
- Model selector supporting both OpenAI and Anthropic providers
- FastAPI endpoints: `/api/analyze`, `/api/refine`, `/api/models`, `/api/health`
- React frontend with TailwindCSS styling
- README, CONTRIBUTING, ENHANCEMENTS, localsetup, CurrentApp documentation
- `.env.example` files for backend and frontend configuration

## [0.1.0] — 2026-04-26

### Added
- Initial project setup and documentation
- Project structure and scaffold files
