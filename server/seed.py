from app import app
from models import Project, db

with app.app_context():
    print("Clearing previous data...")

    Project.query.delete()

    print("Seeding projects...")

    projects = []

    for _ in range(10):
        pass
