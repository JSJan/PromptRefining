# Contributing to PromptRefiner

Thank you for your interest in contributing! This guide will help you get started.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you are expected to uphold this code. Report unacceptable behavior via GitHub Issues.

## How Can I Contribute?

### Good First Issues

Look for issues labeled `good first issue` or `help wanted`. These are specifically curated for new contributors.

### Areas Where Help Is Needed

- **New Model Support** — Adding tokenizers and pricing for new LLM providers (Google Gemini, Mistral, etc.)
- **UI/UX Improvements** — Better prompt diff views, syntax highlighting, dark mode
- **Prompt Refinement Strategies** — New refinement templates and techniques
- **Testing** — Expanding test coverage for edge cases
- **Documentation** — Improving guides, adding examples, translating docs
- **Cost Data** — Keeping model pricing up to date

## Development Setup

See [localsetup.md](localsetup.md) for complete environment setup instructions.

Quick version:

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt  # includes pytest, black, ruff
cp .env.example .env

# Frontend
cd frontend
npm install
```

## Pull Request Process

1. **Fork** the repository and create a branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the [coding standards](#coding-standards).

3. **Write tests** for any new functionality:
   ```bash
   # Backend
   cd backend && pytest

   # Frontend
   cd frontend && npm test
   ```

4. **Lint your code**:
   ```bash
   # Backend
   ruff check .
   black --check .

   # Frontend
   npm run lint
   ```

5. **Commit** with a clear message following [Conventional Commits](https://www.conventionalcommits.org/):
   ```
   feat: add Gemini model token counting
   fix: correct GPT-4o pricing calculation
   docs: update API endpoint documentation
   ```

6. **Push** and open a Pull Request against `main`.

7. **Describe your changes** in the PR body:
   - What does this PR do?
   - How was it tested?
   - Any breaking changes?

8. A maintainer will review your PR. Address any feedback, and it will be merged once approved.

## Coding Standards

### Python (Backend)

- **Formatter**: Black (line length 100)
- **Linter**: Ruff
- **Type Hints**: Required for all function signatures
- **Docstrings**: Google style for public functions
- **Testing**: pytest with at least 80% coverage for new code

```python
# Good
def count_tokens(text: str, model: str = "gpt-4o") -> int:
    """Count the number of tokens in text for a given model."""
    ...

# Bad
def count_tokens(text, model="gpt-4o"):
    ...
```

### JavaScript/React (Frontend)

- **Formatter**: Prettier
- **Linter**: ESLint
- **Components**: Functional components with hooks
- **Naming**: PascalCase for components, camelCase for functions/variables

### General

- No commented-out code in PRs
- No `console.log` or `print` statements in production code
- Environment variables for all secrets — never hardcode API keys

## Reporting Bugs

Open a GitHub Issue with:

1. **Summary** — One-line description
2. **Steps to Reproduce** — Numbered steps to trigger the bug
3. **Expected Behavior** — What should happen
4. **Actual Behavior** — What actually happens
5. **Environment** — OS, Python version, Node version, browser
6. **Screenshots/Logs** — If applicable

## Suggesting Features

Open a GitHub Issue with the `enhancement` label:

1. **Problem Statement** — What problem does this solve?
2. **Proposed Solution** — How should it work?
3. **Alternatives Considered** — Other approaches you thought of
4. **Additional Context** — Mockups, references, examples

## Questions?

Open a Discussion on GitHub or comment on a relevant Issue. We're happy to help!
