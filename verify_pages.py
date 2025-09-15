import os
import re

def verify_pages():
    html_files = sorted([f for f in os.listdir('.') if f.startswith('day_') and f.endswith('.html')])
    html_files.append('curriculam.html')
    html_files.append('30_days_progress.html')

    header_string = '<header class="bg-stone-800 text-white shadow-md">'
    footer_string = '<footer class="bg-stone-800 text-white mt-12 py-6">'

    print("--- Verification Report ---")
    all_correct = True
    for filename in html_files:
        if not os.path.exists(filename):
            print(f"File: {filename} - SKIPPED (Not found)")
            continue

        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        issues = []
        # 1. Check for shared header
        if header_string not in content:
            # The main page has a slightly different header
            if not (filename == '30_days_progress.html' and '<h1 class="text-xl md:text-2xl font-bold">Problem Solving Roadmap</h1>' in content):
                 issues.append("Missing shared header.")

        # 2. Check for shared footer
        if footer_string not in content:
            issues.append("Missing shared footer.")

        # 3. Check for duplicate <header> tags inside <body>
        body_match = re.search(r'<body.*?>(.*)</body>', content, re.DOTALL)
        if body_match:
            body_content = body_match.group(1)
            # Find all <header> tags, being careful about case and attributes
            headers = re.findall(r'<header[\s>]', body_content, re.IGNORECASE)
            if len(headers) > 1:
                issues.append(f"Found {len(headers)} <header> tags in body (should be 1).")

        if issues:
            print(f"File: {filename} - FAILED")
            for issue in issues:
                print(f"  - {issue}")
            all_correct = False
        else:
            print(f"File: {filename} - OK")

    print("\n--- Summary ---")
    if all_correct:
        print("All files are correct.")
    else:
        print("Some files have issues.")

if __name__ == "__main__":
    verify_pages()
