from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modela import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome="Igor", email="igor@gmail.com"),
            Usuario(nome="Cecilia", email="cecilia@gmail.com")
        ],
        [
            Usuario(nome="Igor", email="igor@gmail.com")
        ]
    ]
)

def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salva(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        "sarkan.igor@gmail.com",
        "Curso python pro",
        "Teste"
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome="Igor", email="igor@gmail.com")
    sessao.salva(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        "cecilia@gmail.com",
        "Curso python pro",
        "Teste"
    )
    enviador.enviar.assert_called_once_with(
        "cecilia@gmail.com",
        "igor@gmail.com",
        "Curso python pro",
        "Teste"
    )