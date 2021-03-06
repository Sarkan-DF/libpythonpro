import requests


def buscar_avatar(usuario):
    """
    Busca avatar de usuario o Github
    :param usuario: str com o nome do avatar do Github
    :return: str com o link do avatar
    """
    url = f"https://api.github.com/users/{usuario}"
    resp = requests.get(url)
    return resp.json()['avatar_url']