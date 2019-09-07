from doerffelbot import functions as func


def test_download_vertretung():
    ret = func.download_vertretung()
    assert ret is None
