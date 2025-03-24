**classe base para auditoria** usando `contextvars`, tornando-a agnóstica ao framework. Essa classe pode ser utilizada em qualquer aplicação (Flask, FastAPI, Django, etc.) para rastrear informações da requisição, como um **trace_id**.  

---

### 🔹 **Implementação da Classe Base de Auditoria (`AuditContext`)**
```python
import uuid
import contextvars

class AuditContext:
    """Classe base para auditoria usando contextvars"""

    _trace_id = contextvars.ContextVar("trace_id", default=None)
    _user_id = contextvars.ContextVar("user_id", default=None)

    @staticmethod
    def start_trace(user_id: str = None):
        """Inicia um novo trace_id e opcionalmente define um user_id"""
        trace_id = str(uuid.uuid4())  # Gera um UUID único para o trace
        AuditContext._trace_id.set(trace_id)
        if user_id:
            AuditContext._user_id.set(user_id)

    @staticmethod
    def get_trace_id():
        """Retorna o trace_id atual"""
        return AuditContext._trace_id.get()

    @staticmethod
    def get_user_id():
        """Retorna o user_id atual"""
        return AuditContext._user_id.get()

    @staticmethod
    def clear():
        """Limpa os valores do contexto"""
        AuditContext._trace_id.set(None)
        AuditContext._user_id.set(None)
```

---

### 🔹 **Como Usar essa Classe no Flask**
Agora, vamos integrá-la ao Flask. O `AuditContext` será configurado automaticamente no início de cada requisição e poderá ser acessado em qualquer parte do código.

```python
from flask import Flask, request
from audit_context import AuditContext  # Importando nossa classe de auditoria

app = Flask(__name__)

@app.before_request
def before_request():
    """Configura o trace_id e user_id no início de cada requisição"""
    user_id = request.headers.get("X-User-ID")  # Pegando um possível user_id do header
    AuditContext.start_trace(user_id)

@app.after_request
def after_request(response):
    """Limpa o contexto após a requisição"""
    AuditContext.clear()
    return response

@app.route("/")
def index():
    return {
        "trace_id": AuditContext.get_trace_id(),
        "user_id": AuditContext.get_user_id() or "anonymous"
    }

if __name__ == "__main__":
    app.run(debug=True)
```

---

### 🔹 **Exemplo de Uso**
Se você fizer uma requisição com um `X-User-ID` no header:
```bash
curl -H "X-User-ID: 123" http://127.0.0.1:5000/
```
Resposta esperada:
```json
{
    "trace_id": "550e8400-e29b-41d4-a716-446655440000",
    "user_id": "123"
}
```
Se não enviar um `X-User-ID`, o `user_id` será `"anonymous"`.

---

## 🚀 **Vantagens Dessa Abordagem**
✅ **Agnóstico ao Framework** – Pode ser usado em Flask, FastAPI, Django, etc.  
✅ **Thread-Safe e Async-Safe** – `contextvars` funciona corretamente em ambientes concorrentes.  
✅ **Centralizado** – O `trace_id` pode ser acessado de qualquer lugar da aplicação sem precisar passar explicitamente.

Isso permite que você adicione logs, rastreamento distribuído e auditoria facilmente! 🎯