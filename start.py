import subprocess
import sys
import time


def main():
    print("Starting FastAPI backend...")
    
    backend = subprocess.Popen([
        sys.executable,
        "-m",
        "uvicorn",
        "backend.main:app",
        "--reload",
        "--port",
        "8000",
    ])

    time.sleep(2)

    print("Starting Streamlit frontend...")

    frontend = subprocess.Popen([
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "frontend/user_interface.py",
        "--server.port",
        "8501",
    ])

    try:
        backend.wait()
        frontend.wait()

    except KeyboardInterrupt:
        print("\nShutting down...")

    finally:
        backend.terminate()
        frontend.terminate()


if __name__ == "__main__":
    main()
