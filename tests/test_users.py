from fixture_users import user


def test_user_id(user):
    assert user["id"] == 1


def test_user_email(user):
    assert user["email"] is not None
