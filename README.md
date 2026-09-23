# LangChain Learning

A small Python workspace for learning LangChain integrations with hosted chat models, Hugging Face, embeddings, and LLM workflows.

## Project Structure

```text
.
├── chatsmodel/
│   ├── chatmodel_google.py   # Google Gemini chat example
│   └── Hugging_Face_api.py   # Hugging Face example placeholder
├── Embeddings/               # Embedding experiments
├── llms/                     # LLM experiments
├── requirements.txt          # Python dependencies
└── test.py                   # LangChain installation check
```

## Setup on Windows

Create and activate a virtual environment in PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root. Keep it private because it contains API credentials:

```env
Google_Gemini_API_KEY=your_google_gemini_api_key
```

The `.env` file is ignored by Git.

## Run the Examples

Check that LangChain is installed:

```powershell
python test.py
```

Run the Google Gemini chat example:

```powershell
python .\chatsmodel\chatmodel_google.py
```

The Gemini example sends a prompt to the configured model and prints the response. API usage may incur provider charges and requires a valid Google Gemini API key.

## Development Notes

- Add new experiments to the relevant folder.
- Keep secrets and local virtual environments out of version control.
- Add any new packages to `requirements.txt` so the environment can be reproduced.