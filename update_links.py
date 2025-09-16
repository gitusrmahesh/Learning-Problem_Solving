import os
import re
import math

def get_week_number(day_number):
    if 1 <= day_number <= 7:
        return 1
    elif 8 <= day_number <= 14:
        return 2
    elif 15 <= day_number <= 21:
        return 3
    elif 22 <= day_number <= 30:
        return 4
    else:
        # Fallback for any unexpected day numbers
        return math.floor((day_number - 1) / 7) + 1

def update_links():
    day_files = [f for f in os.listdir('.') if f.startswith('day_') and f.endswith('.html')]

    print("--- Starting Link Update Process ---")

    for filename in day_files:
        try:
            day_match = re.search(r'day_(\d+)\.html', filename)
            if not day_match:
                print(f"Could not extract day number from: {filename}. Skipping.")
                continue

            day_number = int(day_match.group(1))
            week_number = get_week_number(day_number)

            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            new_link = f'href="30_days_progress.html?week={week_number}"'

            # This regex finds the link, with or without an existing week parameter
            pattern = re.compile(r'href="30_days_progress\.html(?:\?week=\d+)?"')

            if pattern.search(content):
                new_content, count = pattern.subn(new_link, content)
                if count > 0:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filename}: Set link to week {week_number}.")
                else:
                    print(f"No update needed for {filename} (already correct).")
            else:
                print(f"Link pattern not found in {filename}. Skipping.")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

    print("\n--- Link Update Process Finished ---")

if __name__ == "__main__":
    update_links()
