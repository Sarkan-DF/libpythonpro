from libpythonpro.spam.enviador_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam


def test_enviador_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        "sarkan.igor@gmail.com",
        "Curso python pro",
        "Teste"
    )