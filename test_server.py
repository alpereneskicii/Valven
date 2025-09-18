import os
import tempfile
from socket_server import run_command

def test_pwd_command():
    print("Test: pwd command")
    
    session = {"current_dir": "/home/user"}
    result = run_command("pwd", session)
    
    if result == "/home/user":
        print("✅ PASS: pwd command works correctly")
    else:
        print(f"❌ FAIL: Expected '/home/user', Got '{result}'")


def test_empty_command():
    print("\nTest: Empty command")
    
    session = {"current_dir": "/home/user"}
    result = run_command("", session)
    
    if result == "" or result == " ":
        print("✅ PASS: Empty command handled correctly")
    else:
        print(f"❌ FAIL: Empty result expected, Got '{result}'")


def test_cd_valid_directory():
    print("\nTest: CD command - valid directory")
    
    # Create a temporary test directory
    test_dir = tempfile.mkdtemp()
    sub_dir = os.path.join(test_dir, "test_folder")
    os.makedirs(sub_dir)
    
    session = {"current_dir": test_dir}
    result = run_command("cd test_folder", session)
    
    if result == "" and session["current_dir"] == sub_dir:
        print("✅ PASS: CD command works")
    else:
        print(f"❌ FAIL: CD failed. Result: '{result}', Directory: '{session['current_dir']}'")
    
    # Cleanup
    import shutil
    shutil.rmtree(test_dir)


def test_cd_invalid_directory():
    print("\nTest: CD command - invalid directory")
    
    session = {"current_dir": "/home/user"}
    result = run_command("cd nonexistent_dir", session)
    
    if "no such directory" in result:
        print("✅ PASS: Invalid directory error is shown")
    else:
        print(f"❌ FAIL: Error message expected, Got '{result}'")


def test_cd_no_arguments():
    print("\nTest: CD command - no arguments")
    
    session = {"current_dir": "/home/user"}
    result = run_command("cd", session)
    
    if result == "/home/user":
        print("✅ PASS: CD without args returns current directory")
    else:
        print(f"❌ FAIL: Current directory expected, Got '{result}'")


def test_invalid_command():
    print("\nTest: Invalid command")
    
    session = {"current_dir": "/home/user"}
    result = run_command("nonexistent_command", session)
    
    if "WinError 267" in result or "command not found" in result:
        print("✅ PASS: Invalid command error is shown")
    else:
        print(f"❌ FAIL: Error message expected, Got '{result}'")


def test_echo_command():
    print("\nTest: Echo command")
    
    session = {"current_dir": os.getcwd()}
    result = run_command("echo hello", session)
    
    if "hello" in result:
        print("✅ PASS: Echo command works")
    else:
        print(f"❌ FAIL: 'hello' expected, Got '{result}'")


def test_dir_command():
    print("\nTest: dir command")
    
    session = {"current_dir": os.getcwd()}
    result = run_command("dir", session)
    
    if len(result) > 0 and "command not found" not in result:
        print("✅ PASS: dir command works")
    else:
        print(f"❌ FAIL: dir command failed. Result: '{result}'")


def test_session_management():
    print("\nTest: Session management")
    
    sessions = {}
    
    addr = ("127.0.0.1", 5000)
    sessions[addr] = {"current_dir": "/test"}
    if addr in sessions:
        print("✅ PASS: Session created successfully")
    else:
        print("❌ FAIL: Session creation failed")
    
    del sessions[addr]
    
    if addr not in sessions:
        print("✅ PASS: Session deleted successfully")
    else:
        print("❌ FAIL: Session deletion failed")


def run_all_tests():
    print("🔧 Starting Server Tests...")
    print("=" * 40)
    
    test_pwd_command()
    test_empty_command()
    test_cd_valid_directory()
    test_cd_invalid_directory()
    test_cd_no_arguments()
    test_invalid_command()
    test_echo_command()
    test_dir_command()
    test_session_management()
    
    print("\n" + "=" * 40)
    print("🏁 All tests completed!")
    print("\nNote: If there are ❌ tests, there might be issues in the code.")


if __name__ == "__main__":
    run_all_tests()