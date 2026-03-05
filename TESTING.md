# Quick-Calc Testing Documentation

## Overview
This document outlines the testing strategy and results for **Quick-Calc**, a simple calculator application built in Python with a Tkinter GUI. The purpose of testing is to ensure correctness of all calculator operations, handle edge cases, and verify that the GUI interacts correctly with the calculation logic.  

The testing approach follows a **multi-layered strategy**: unit tests for core logic, and integration tests for the GUI and user interaction.

---

## 1. Unit Testing

### 1.1 Purpose
Unit tests verify that individual functions in the `Calculator` class behave correctly in isolation. These tests focus on:

- Correctness of addition, subtraction, multiplication, and division.
- Handling of edge cases, including:
  - Division by zero
  - Negative numbers
  - Decimal numbers
  - Very large numbers

### 1.2 Test Cases and Analysis

| Test Name                | Description                                                                 | Expected Result | Outcome |
|---------------------------|-----------------------------------------------------------------------------|----------------|---------|
| `test_add`                | Adds two positive integers (5 + 3)                                           | 8              | Passed  |
| `test_subtract`           | Subtracts two integers (10 - 4)                                             | 6              | Passed  |
| `test_multiply`           | Multiplies two integers (6 × 7)                                             | 42             | Passed  |
| `test_divide`             | Divides two integers (8 ÷ 2)                                               | 4              | Passed  |
| `test_divide_zero`        | Tests division by zero                                                      | Raises ValueError | Passed |
| `test_negative_numbers`   | Adds two negative numbers (-5 + -3)                                         | -8             | Passed  |
| `test_decimal_numbers`    | Adds decimal numbers (2.5 + 3.5)                                           | 6.0            | Passed  |
| `test_large_numbers`      | Multiplies very large numbers (100000 × 100000)                             | 10000000000    | Passed  |

**Analysis:**  
These unit tests provide a **solid coverage of the Calculator logic**, ensuring both normal and edge cases behave as expected. Unit testing is **white-box testing**, as the tests are designed with knowledge of the underlying code.

---

## 2. Integration Testing

### 2.1 Purpose
Integration tests ensure that the **GUI interacts correctly with the Calculator logic**. They simulate real user interactions, verifying that:

- Input is correctly processed
- Operations return the expected result
- Clear functionality resets the display

### 2.2 Test Cases and Analysis

| Test Name                    | Description                                                                 | Expected Result | Outcome |
|-------------------------------|-----------------------------------------------------------------------------|----------------|---------|
| `test_gui_addition_simulation` | Simulates clicking "5", "+", "3", "="                                       | Display shows "8" | Passed  |
| `test_gui_clear_function`      | Simulates a calculation (e.g., "9*2=") followed by "C"                      | Display shows "" | Passed  |

**Analysis:**  
Integration tests act as **black-box tests**: they focus on user-visible behavior rather than internal logic. By simulating GUI interactions, these tests verify that the **calculator logic and GUI layer work together correctly**.  

---

## 3. Testing Strategy and Concepts

### 3.1 The Testing Pyramid
- **Unit Tests (bottom layer):** Most numerous, cover core logic of calculator.  
- **Integration Tests (middle layer):** Fewer, test user interaction with GUI.  
- **Manual or UI Testing (top layer):** Not automated; would cover look and feel.  

This structure ensures **efficient coverage and maintainability**.

### 3.2 Black-box vs White-box Testing
- **Unit Tests:** White-box testing, knowledge of implementation guides test design.  
- **Integration Tests:** Black-box testing, user actions drive the test without inspecting code.  

### 3.3 Functional vs Non-Functional Testing
- **Functional Testing:** All tests ensure correct arithmetic operations and GUI responses.  
- **Non-Functional Testing:** GUI responsiveness, visual layout, and performance are **not tested**, as the assignment focuses on correctness.  

### 3.4 Regression Testing
The test suite allows **automatic regression checks**:
- Running `pytest` after updates ensures no functionality is broken.  
- Unit tests catch core calculation errors.  
- Integration tests catch errors in GUI-user interaction.  

---

## 4. Summary

**All required tests passed successfully.**  

- **Unit Tests:** 8 tests covering all operations and edge cases.  
- **Integration Tests:** 2 tests simulating realistic GUI flows.  
- **Test Execution Command:**  
```bash
pytest -v