#!/usr/bin/env python3
"""
Unit tests for student_grades.py

This test suite covers the core functionality of the student grades management system.
Run with: python -m pytest test_student_grades.py -v
Or: python test_student_grades.py
"""

import unittest
import tempfile
import os
from io import StringIO
import sys
from unittest.mock import patch, mock_open

# Import the functions we'll create from student_grades.py
# Note: You'll need to refactor student_grades.py to use these functions
class StudentGradesSystem:
    """Refactored student grades system for testing"""
    
    def __init__(self):
        self.name_list = []
        self.student_id_list = []
        self.class_list = []
        self.grade_list = []
    
    def validate_student_input(self, name, student_id, student_class, grade):
        """Validate student input data"""
        errors = []
        
        if not name or not name.strip():
            errors.append("Name cannot be empty")
        
        if not student_id or not student_id.strip():
            errors.append("Student ID cannot be empty")
        
        if not student_class or not student_class.strip():
            errors.append("Class cannot be empty")
        
        # Validate grade (should be numeric)
        try:
            grade_float = float(grade)
            if grade_float < 0 or grade_float > 100:
                errors.append("Grade must be between 0 and 100")
        except (ValueError, TypeError):
            errors.append("Grade must be a valid number")
        
        return errors
    
    def add_student(self, name, student_id, student_class, grade):
        """Add a student to the lists"""
        errors = self.validate_student_input(name, student_id, student_class, grade)
        if errors:
            raise ValueError("; ".join(errors))
        
        self.name_list.append(name.strip())
        self.student_id_list.append(student_id.strip())
        self.class_list.append(student_class.strip())
        self.grade_list.append(grade.strip())
        
        return True
    
    def get_student_data(self):
        """Combine lists into one list of student data"""
        return [
            [self.name_list[i], self.student_id_list[i], self.class_list[i], self.grade_list[i]]
            for i in range(len(self.name_list))
        ]
    
    def search_student_by_name(self, search_name, case_sensitive=False):
        """Search for a student by name"""
        if not case_sensitive:
            search_name = search_name.lower()
        
        results = []
        for i in range(len(self.name_list)):
            name = self.name_list[i]
            if not case_sensitive:
                name = name.lower()
            
            # Check exact match or partial match
            if search_name in name:
                results.append({
                    'name': self.name_list[i],
                    'student_id': self.student_id_list[i],
                    'class': self.class_list[i],
                    'grade': self.grade_list[i]
                })
        
        return results
    
    def calculate_student_average(self, student_name):
        """Calculate average grade for a specific student (if they have multiple entries)"""
        grades = []
        for i in range(len(self.name_list)):
            if self.name_list[i].lower() == student_name.lower():
                try:
                    grades.append(float(self.grade_list[i]))
                except ValueError:
                    continue
        
        if not grades:
            return None
        
        return sum(grades) / len(grades)
    
    def calculate_class_average(self, class_name):
        """Calculate average grade for a specific class"""
        grades = []
        for i in range(len(self.class_list)):
            if self.class_list[i].lower() == class_name.lower():
                try:
                    grades.append(float(self.grade_list[i]))
                except ValueError:
                    continue
        
        if not grades:
            return None
        
        return sum(grades) / len(grades)
    
    def parse_file_content(self, content):
        """Parse student data from file content"""
        students = []
        for line in content.strip().splitlines():
            if line.strip():
                fields = line.split(",")
                if len(fields) == 4:
                    students.append({
                        'name': fields[0].strip(),
                        'student_id': fields[1].strip(),
                        'class': fields[2].strip(),
                        'grade': fields[3].strip()
                    })
        return students
    
    def format_student_data_for_file(self):
        """Format student data for writing to file"""
        lines = []
        for i in range(len(self.name_list)):
            line = f"{self.name_list[i]},{self.student_id_list[i]},{self.class_list[i]},{self.grade_list[i]}"
            lines.append(line)
        return "\n".join(lines)


class TestStudentGradesSystem(unittest.TestCase):
    """Test cases for the Student Grades System"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.system = StudentGradesSystem()
    
    def test_validate_student_input_valid(self):
        """Test validation with valid student input"""
        errors = self.system.validate_student_input("John Doe", "12345", "Math", "85")
        self.assertEqual(errors, [])
    
    def test_validate_student_input_empty_name(self):
        """Test validation with empty name"""
        errors = self.system.validate_student_input("", "12345", "Math", "85")
        self.assertIn("Name cannot be empty", errors)
    
    def test_validate_student_input_empty_student_id(self):
        """Test validation with empty student ID"""
        errors = self.system.validate_student_input("John Doe", "", "Math", "85")
        self.assertIn("Student ID cannot be empty", errors)
    
    def test_validate_student_input_invalid_grade(self):
        """Test validation with invalid grade"""
        errors = self.system.validate_student_input("John Doe", "12345", "Math", "invalid")
        self.assertIn("Grade must be a valid number", errors)
    
    def test_validate_student_input_grade_out_of_range(self):
        """Test validation with grade out of range"""
        errors = self.system.validate_student_input("John Doe", "12345", "Math", "150")
        self.assertIn("Grade must be between 0 and 100", errors)
    
    def test_add_student_valid(self):
        """Test adding a valid student"""
        result = self.system.add_student("John Doe", "12345", "Math", "85")
        self.assertTrue(result)
        self.assertEqual(len(self.system.name_list), 1)
        self.assertEqual(self.system.name_list[0], "John Doe")
    
    def test_add_student_invalid(self):
        """Test adding an invalid student"""
        with self.assertRaises(ValueError):
            self.system.add_student("", "12345", "Math", "85")
    
    def test_get_student_data(self):
        """Test getting combined student data"""
        self.system.add_student("John Doe", "12345", "Math", "85")
        self.system.add_student("Jane Smith", "67890", "Science", "92")
        
        data = self.system.get_student_data()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0], ["John Doe", "12345", "Math", "85"])
        self.assertEqual(data[1], ["Jane Smith", "67890", "Science", "92"])
    
    def test_search_student_by_name_exact_match(self):
        """Test searching for student by exact name"""
        self.system.add_student("John Doe", "12345", "Math", "85")
        self.system.add_student("Jane Smith", "67890", "Science", "92")
        
        results = self.system.search_student_by_name("John Doe")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['name'], "John Doe")
        self.assertEqual(results[0]['class'], "Math")
    
    def test_search_student_by_name_partial_match(self):
        """Test searching for student by partial name"""
        self.system.add_student("John Doe", "12345", "Math", "85")
        self.system.add_student("Jane Smith", "67890", "Science", "92")
        
        results = self.system.search_student_by_name("john")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['name'], "John Doe")
    
    def test_search_student_by_name_no_match(self):
        """Test searching for student with no match"""
        self.system.add_student("John Doe", "12345", "Math", "85")
        
        results = self.system.search_student_by_name("Bob")
        self.assertEqual(len(results), 0)
    
    def test_calculate_student_average_single_grade(self):
        """Test calculating average for student with single grade"""
        self.system.add_student("John Doe", "12345", "Math", "85")
        
        average = self.system.calculate_student_average("John Doe")
        self.assertEqual(average, 85.0)
    
    def test_calculate_student_average_multiple_grades(self):
        """Test calculating average for student with multiple grades"""
        self.system.add_student("John Doe", "12345", "Math", "85")
        self.system.add_student("John Doe", "12345", "Science", "90")
        
        average = self.system.calculate_student_average("John Doe")
        self.assertEqual(average, 87.5)
    
    def test_calculate_student_average_no_student(self):
        """Test calculating average for non-existent student"""
        average = self.system.calculate_student_average("Bob")
        self.assertIsNone(average)
    
    def test_calculate_class_average(self):
        """Test calculating class average"""
        self.system.add_student("John Doe", "12345", "Math", "85")
        self.system.add_student("Jane Smith", "67890", "Math", "90")
        self.system.add_student("Bob Johnson", "11111", "Science", "75")
        
        math_average = self.system.calculate_class_average("Math")
        self.assertEqual(math_average, 87.5)
        
        science_average = self.system.calculate_class_average("Science")
        self.assertEqual(science_average, 75.0)
    
    def test_calculate_class_average_no_class(self):
        """Test calculating average for non-existent class"""
        average = self.system.calculate_class_average("History")
        self.assertIsNone(average)
    
    def test_parse_file_content(self):
        """Test parsing student data from file content"""
        content = "John Doe,12345,Math,85\nJane Smith,67890,Science,92\n"
        students = self.system.parse_file_content(content)
        
        self.assertEqual(len(students), 2)
        self.assertEqual(students[0]['name'], "John Doe")
        self.assertEqual(students[1]['name'], "Jane Smith")
    
    def test_parse_file_content_invalid_lines(self):
        """Test parsing file content with invalid lines"""
        content = "John Doe,12345,Math,85\nInvalid Line\nJane Smith,67890,Science,92\n"
        students = self.system.parse_file_content(content)
        
        # Should skip invalid line and only return valid entries
        self.assertEqual(len(students), 2)
        self.assertEqual(students[0]['name'], "John Doe")
        self.assertEqual(students[1]['name'], "Jane Smith")
    
    def test_format_student_data_for_file(self):
        """Test formatting student data for file output"""
        self.system.add_student("John Doe", "12345", "Math", "85")
        self.system.add_student("Jane Smith", "67890", "Science", "92")
        
        formatted = self.system.format_student_data_for_file()
        expected = "John Doe,12345,Math,85\nJane Smith,67890,Science,92"
        self.assertEqual(formatted, expected)
    
    def test_edge_case_whitespace_handling(self):
        """Test handling of whitespace in input"""
        self.system.add_student("  John Doe  ", "  12345  ", "  Math  ", "  85  ")
        
        # Should strip whitespace
        self.assertEqual(self.system.name_list[0], "John Doe")
        self.assertEqual(self.system.student_id_list[0], "12345")
        self.assertEqual(self.system.class_list[0], "Math")
        self.assertEqual(self.system.grade_list[0], "85")
    
    def test_grade_validation_edge_cases(self):
        """Test grade validation edge cases"""
        # Test boundary values
        errors_0 = self.system.validate_student_input("John", "123", "Math", "0")
        self.assertEqual(errors_0, [])
        
        errors_100 = self.system.validate_student_input("John", "123", "Math", "100")
        self.assertEqual(errors_100, [])
        
        errors_negative = self.system.validate_student_input("John", "123", "Math", "-1")
        self.assertIn("Grade must be between 0 and 100", errors_negative)
        
        errors_over = self.system.validate_student_input("John", "123", "Math", "101")
        self.assertIn("Grade must be between 0 and 100", errors_over)


def run_tests():
    """Run all tests"""
    unittest.main(verbosity=2)


if __name__ == '__main__':
    print("🧪 Running Student Grades System Tests")
    print("=" * 50)
    run_tests()

