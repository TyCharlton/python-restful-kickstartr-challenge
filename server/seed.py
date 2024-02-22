from app import app
from models import Project, db
from faker import Faker

with app.appcontext():

    print("Clearing previous data...")

    Project.query.delete()

    print("Seeding projects...")

    projects = []

    fake = Faker()

    for _ in range(10):
        project = Project(
            title=fake.job(),
            creator=fake.name()
        )
        projects.append(project)

    db.session.add_all(projects)
    db.session.commit()