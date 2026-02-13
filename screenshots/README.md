# Screenshots Guide - Assignment Submission

මේ folder එකේ assignment එකට ඕන screenshots save කරන්න.

## ගන්න ඕන Screenshots:

### 1. Project Structure (01_project_structure.png)
VS Code එකේ file explorer එක screenshot කරන්න:
- `python_tests` folder එක expand කරලා
- සියලුම files පෙන්වන්න

### 2. All Tests Running - Terminal Output (02_all_tests_terminal.png)
Terminal එකේ run කරන command එක සහ output එක:
```bash
python3 -m pytest test_assignment.py -v
```
Output එකේ මේවා පෙන්වන්න:
- 4 PASSED tests
- Test execution time

### 3. Task 1 Execution (03_task1_execution.png)
```bash
python3 task1_open_website_real.py
```
Terminal output එකේ:
- Website title
- Success message

### 4. Task 2 Execution (04_task2_execution.png)
```bash
python3 task2_user_registration_real.py
```
Terminal output එකේ:
- Registration data
- "ACCOUNT CREATED!" message

### 5. Task 3 Execution (05_task3_execution.png)
```bash
python3 task3_user_login_real.py
```
Terminal output එක

### 6. Task 4 Execution (06_task4_execution.png)
```bash
python3 task4_simple_search.py
```
Terminal output එක

### 7. Browser Window - Maximized (07_browser_maximized.png)
Test එකක් run වෙන කාලෙ browser එක screenshot කරන්න:
- Maximized window
- Website loaded (automationexercise.com හෝ google.com)

### 8. Pytest HTML Report (Optional) (08_pytest_report.png)
HTML report එක generate කරලා:
```bash
python3 -m pytest test_assignment.py --html=report.html --self-contained-html
```
Report එක browser එකේ open කරලා screenshot කරන්න

### 9. Python & Selenium Versions (09_versions.png)
```bash
python3 --version
pip3 list | grep selenium
```

### 10. Success Summary (10_all_passed.png)
සියලුම tests pass වෙලා තියෙනවා පෙන්වන screenshot එකක්

---

## Screenshot කරන විදිය:

### macOS:
- **Full Screen**: `Cmd + Shift + 3`
- **Selected Area**: `Cmd + Shift + 4`
- **Window**: `Cmd + Shift + 4`, then press `Space`, click window

### Windows:
- **Snipping Tool**: `Windows + Shift + S`
- **Full Screen**: `PrtScn`

---

## Screenshots Save කරන්නේ කොහෙද:

මේ folder එකට save කරන්න:
```
/Users/gavinkahanda/Desktop/Selanium/screenshots/
```

---

## Final Submission Structure:

```
Selanium/
├── python_tests/
│   ├── test_assignment.py
│   ├── task1_open_website_real.py
│   ├── task2_user_registration_real.py
│   ├── task3_user_login_real.py
│   ├── task4_simple_search.py
│   ├── base_test.py
│   ├── requirements.txt
│   └── README.md
├── screenshots/
│   ├── 01_project_structure.png
│   ├── 02_all_tests_terminal.png
│   ├── 03_task1_execution.png
│   ├── 04_task2_execution.png
│   ├── 05_task3_execution.png
│   ├── 06_task4_execution.png
│   ├── 07_browser_maximized.png
│   ├── 08_pytest_report.png (optional)
│   ├── 09_versions.png
│   └── 10_all_passed.png
└── README.md
```

---

## Quick Checklist:

- [ ] All Python test files තියෙනවාද?
- [ ] Tests run වෙනවාද (4 PASSED)?
- [ ] Screenshots ගත්තාද (අවම වශයෙන් 7)?
- [ ] Browser maximize වෙනවා පෙන්වනවාද?
- [ ] Success messages පෙනෙනවාද?
- [ ] README file තියෙනවාද?

---

Good luck! 🎉
