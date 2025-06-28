#!/usr/bin/env python3
"""
Test runner for student grades system
"""

import subprocess
import sys
import os

def run_tests():
    """Run the test suite with better formatting"""
    print("🧪 Student Grades System - Test Suite")
    print("=" * 60)
    print("📁 Testing File: test_student_grades.py")
    print("🏃 Running tests...\n")
    
    try:
        # Run the tests
        result = subprocess.run([
            sys.executable, 
            "test_student_grades.py"
        ], capture_output=True, text=True)
        
        # Print the output
        print(result.stdout)
        
        if result.stderr:
            print("❌ Errors:")
            print(result.stderr)
        
        # Print summary
        if result.returncode == 0:
            print("✅ All tests passed!")
            print("🎉 Your student grades system is working correctly!")
        else:
            print("❌ Some tests failed!")
            print("🔍 Check the errors above and fix them.")
            
        return result.returncode == 0
        
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return False

def run_with_pytest():
    """Run tests with pytest if available"""
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "test_student_grades.py", 
            "-v", "--tb=short"
        ], capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
            
        return result.returncode == 0
    except:
        return False

if __name__ == "__main__":
    print("🔬 Checking for pytest...")
    
    # Try pytest first (better output)
    if run_with_pytest():
        print("✅ Tests completed with pytest")
    else:
        print("📝 Pytest not available, using unittest...")
        run_tests()
    
    print("\n💡 To run tests manually:")
    print("   python test_student_grades.py")
    print("   or")
    print("   python -m pytest test_student_grades.py -v")

