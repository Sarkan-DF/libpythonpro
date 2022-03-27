from libpythonpro.spam.modela import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome="Igor")
    sessao.salva(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome="Igor"), Usuario(nome="Cecilia")]
    for usuario in usuarios:
        sessao.salva(usuario)
    assert usuarios == sessao.listar()
