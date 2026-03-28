import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oauth2_project.settings")
import django
django.setup()

from model_bakery import baker
from oauth2_app.models import Room

def create_dummy_data(count=10):
    print(f"Creating {count} dummy instances of Room...")
    baker.make(Room, _quantity=count)
    print("Data generation complete.")

if __name__ == "__main__":
    create_dummy_data(10)
