from unittest.mock import patch

import pytest

from src.main import (
    Estudante,
    create_estudante,
    delete_estudante,
    funcaoTeste,
    root,
    update_estudante,
)


@pytest.mark.asyncio
async def test_root():
    assert await root() == {"message": "Hello World"}


@pytest.mark.asyncio
async def test_funcao_teste():
    with patch("src.main.random.randint", return_value=12345):
        result = await funcaoTeste()

    assert result == {"teste": True, "num_aleatorio": 12345}


@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)

    assert estudante_teste == await create_estudante(estudante_teste)


@pytest.mark.asyncio
async def test_update_estudante_negativo():
    assert not await update_estudante(-5)


@pytest.mark.asyncio
async def test_update_estudante_positivo():
    assert await update_estudante(10)


@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    assert not await delete_estudante(-5)


@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    assert await delete_estudante(10)
