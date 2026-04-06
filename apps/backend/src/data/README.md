# `:data:`

## Structure

```
data/
    gateway/
        nlp_gateway_impl.py
    mapper/
        analysis_entity_mapper.py
        vcs_entity_mapper.py
    remote/
        nlp/
            anthropic/
                adapter.py
                claude_api_service.py
                models.py
            dtos.py
            nlp_api_service.py
        vcs/
            github/
                github_api_service.py
                models.py
            dtos.py
            vcs_api_service.py
    repository/
        vcs_repository_impl.py
```