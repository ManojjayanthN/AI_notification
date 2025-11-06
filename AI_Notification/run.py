from backend.app import create_app
from backend.modules.scheduler import run_scheduler
import threading

app = create_app()

# Run scheduler in separate thread
scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()

if __name__ == "__main__":
    app.run(debug=True)
