from fastapi import Header, HTTPException

async def authenticated_context(
    x_user_id: str | None = Header(default=None),
    x_user_role: str | None = Header(default=None),
):
    # O Java/API Gateway deve autenticar, autorizar e inserir estes headers.
    # Não aceitar esses headers diretamente de clientes externos sem gateway confiável.
    if not x_user_id:
        raise HTTPException(status_code=401, detail="Contexto autenticado ausente")
    return {"user_id": x_user_id, "role": x_user_role}
