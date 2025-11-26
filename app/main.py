from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from .nlp import basic_stats

app = FastAPI(title="Text Analyzer Demo")


class TextRequest(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
def ui():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8" />
        <title>Text Analyzer UI</title>
        <style>
            body {
                font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
                margin: 2rem;
                max-width: 800px;
            }
            textarea {
                width: 100%;
                height: 150px;
                font-family: inherit;
                font-size: 14px;
                padding: 0.5rem;
            }
            button {
                margin-top: 0.5rem;
                padding: 0.5rem 1rem;
                cursor: pointer;
            }
            pre {
                background: #f5f5f5;
                padding: 1rem;
                white-space: pre-wrap;
            }
            .result {
                margin-top: 1.5rem;
            }
        </style>
    </head>
    <body>
        <h1>Text Analyzer Demo</h1>
        <p>Введите текст и нажмите «Анализировать».</p>
        
        <textarea id="text" placeholder="Например: Привет, мир!"></textarea>
        <br />
        <button onclick="analyze()">Анализировать</button>

        <div class="result">
            <h2>Результат</h2>
            <pre id="result">Пока ничего нет</pre>
        </div>

        <script>
            async function analyze() {
                const text = document.getElementById('text').value;
                const resultEl = document.getElementById('result');

                if (!text.trim()) {
                    resultEl.textContent = 'Введите текст для анализа.';
                    return;
                }

                try {
                    const response = await fetch('/api/analyze', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ text })
                    });

                    if (!response.ok) {
                        resultEl.textContent = 'Ошибка: ' + response.status + ' ' + response.statusText;
                        return;
                    }

                    const data = await response.json();
                    resultEl.textContent = JSON.stringify(data, null, 2);
                } catch (err) {
                    resultEl.textContent = 'Ошибка запроса: ' + err;
                }
            }
        </script>
    </body>
    </html>
    """


@app.post("/api/analyze")
def analyze(request: TextRequest):
    stats = basic_stats(request.text)
    return stats