import pytest

from libpythonpro.spam.enviador_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modela import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome="Igor", email="igor@email.com"),
            Usuario(nome="Cecilia", email="igor@email.com")
        ],
        [
            Usuario(nome="Igor", email="igor@email.com")
        ]
    ]
)

def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salva(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        "sarkan.igor@gmail.com",
        "Curso python pro",
        "Teste"
    )
    assert len(usuarios) == enviador.qtd_email_enviador