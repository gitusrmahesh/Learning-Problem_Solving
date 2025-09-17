import os

def update_footer_text():
    # Define the old and new footer text
    old_text = "&copy; 2025 30-Day Problem Solving Roadmap. All Rights Reserved."
    new_text = "&copy; 2025 30-Day Problem Solving Roadmap By Mr. Mahesh Singare. All Rights Reserved."

    # Get a list of all HTML files in the current directory
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]

    print("--- Starting Footer Update Process ---")
    updated_count = 0

    for filename in html_files:
        try:
            # Read the content of the file
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if the old text exists and replace it
            if old_text in content:
                new_content = content.replace(old_text, new_text)

                # Write the updated content back to the file
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                print(f"Updated footer in: {filename}")
                updated_count += 1
            else:
                print(f"Old footer text not found in: {filename}. Skipping.")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

    print("\n--- Footer Update Process Finished ---")
    print(f"Total files updated: {updated_count}")

if __name__ == "__main__":
    update_footer_text()
