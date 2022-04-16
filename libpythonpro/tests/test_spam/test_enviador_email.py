import pytest

from libpythonpro.spam.enviador_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    "destinatario",
    ["sarkan.igor@gmail.com", "cecilia.matos@gmail.com"]
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        "cady.claudia!gmail.com",
        "Curso Python Pro",
        "Testando !!!"
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    "remetente",
    ["", "cecilia.matos"]
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            "cady.claudia!gmail.com",
            "Curso Python Pro",
            "Testando !!!"
        )