from src.services import Services
from src.ui import UI
from src.repository import FileRepo

if __name__ == "__main__":
    repo = FileRepo()
    services = Services(repo)
    UI(services).run()
