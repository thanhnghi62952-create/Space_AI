from database.models import User

def create_user(
        db,
        user_id,
        email
):
    user = User(
        user_id=user_id,
        email=email
    )
    db.app(user)
    db.commit()
    db.refresh(user)

    return user
def get_user(
        db,
        user_id
):
    return db.query(
        User
    ).filer(
        User.user_id == user_id).first()
    