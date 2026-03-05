
---

## **4. TESTING.md**

```markdown
# Quick-Calc Testing Documentation

## Testing Strategy
We implemented a **multi-layered testing approach**:

### Unit Testing
- Tests individual functions in `Calculator` class.
- Covers:
  - Addition, subtraction, multiplication, division.
  - Edge cases: division by zero, negative numbers, decimals, large numbers.

### Integration Testing
- Tests interaction between GUI and calculation logic.
- Simulates user input sequences:
  - Full calculation: e.g., "5 + 3 = 8"
  - Clear functionality: resets display after operations.

## Lecture Concepts Applied
1. **Testing Pyramid**
   - Unit tests (most numerous)
   - Integration tests (fewer, check GUI + logic)
2. **Black-box vs White-box Testing**
   - Unit tests: white-box (knowledge of code)
   - Integration tests: black-box (simulate user input)
3. **Functional vs Non-Functional Testing**
   - Functional: correctness of operations
   - Non-functional: GUI responsiveness not tested
4. **Regression Testing**
   - Unit and integration tests can be rerun after future updates to ensure functionality is intact.

## Test Results Summary

| Test Name                    | Type          | Status |
|-------------------------------|---------------|--------|
| test_add                      | Unit          | Passed |
| test_subtract                 | Unit          | Passed |
| test_multiply                 | Unit          | Passed |
| test_divide                   | Unit          | Passed |
| test_divide_zero              | Unit          | Passed |
| test_negative_numbers         | Unit          | Passed |
| test_decimal_numbers          | Unit          | Passed |
| test_large_numbers            | Unit          | Passed |
| test_gui_addition_simulation  | Integration   | Passed |
| test_gui_clear_function       | Integration   | Passed |