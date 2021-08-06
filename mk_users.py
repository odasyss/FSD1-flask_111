from app.routes import db, User


def create_my_user(first_name, last_name, hobbies):
    db.session.add(
        User(
            first_name=first_name,
            last_name=last_name,
            hobbies=hobbies,
        )
    )
    db.session.commit()


if __name__ == "__main__":
    create_my_user("Odasys", "Soberanes", "Sleeping")
    users = User.query.all()
    print(users)
    create_my_user("Mike", "Tyson", "Boxer")
    user = User.query.filter_by(first_name="Mike").first()
    print(user)
