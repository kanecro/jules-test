import sys
import os

# Add the project root to sys.path to allow importing main
# Common way to handle imports for tests in a simple project structure.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from main import get_hello_world_message  # noqa: E402


def test_returns_hello_world():
    """Tests if get_hello_world_message returns 'hello world'."""
    message = get_hello_world_message()
    assert message == "hello world"
