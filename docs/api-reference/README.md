# API Adapter Guide

## Implementing a New Adapter

1. Create a new file in `src/api/`
2. Subclass `BaseAPIAdapter`
3. Implement `generate()`, `health_check()`, and `estimate_cost()`
4. Register the adapter in `config/settings.yaml`

```python
from src.api.base import BaseAPIAdapter
from src.models.schemas import GenerationRequest, GenerationResponse

class MyProviderAdapter(BaseAPIAdapter):
    async def generate(self, request: GenerationRequest) -> GenerationResponse:
        ...
```

## Existing Adapters

| Adapter          | Status      | File                  |
|------------------|-------------|-----------------------|
| NovelAI          | Placeholder | `src/api/novelai.py`  |
| Stability AI     | Placeholder | `src/api/stability.py`|
