import os
import re

def search_for_secrets(directory):
    sensitive_keywords = ["password", "secret", "api_key"]  # Add more keywords as needed
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # Regular expression for emails
    phone_number_pattern = r'\b\d{10}\b'  # Regular expression for 10-digit mobile numbers
    results = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):  # You can expand file extensions or use regex patterns for file types
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    for line_number, line in enumerate(lines, start=1):
                        # Searching for sensitive keywords
                        for keyword in sensitive_keywords:
                            if keyword in line.lower():
                                results.append({
                                    "file": file_path,
                                    "line_number": line_number,
                                    "keyword": keyword,
                                    "text": line.strip()
                                })
                        # Searching for emails
                        emails = re.findall(email_pattern, line)
                        for email in emails:
                            results.append({
                                "file": file_path,
                                "line_number": line_number,
                                "keyword": "Email",
                                "text": email
                            })
                        # Searching for mobile numbers
                        phone_numbers = re.findall(phone_number_pattern, line)
                        for phone_number in phone_numbers:
                            results.append({
                                "file": file_path,
                                "line_number": line_number,
                                "keyword": "Mobile Number",
                                "text": phone_number
                            })
    return results

if __name__ == "__main__":
    directory_to_search = '/path/to/your/directory'  # Replace this with the directory you want to scan
    search_results = search_for_secrets(directory_to_search)

    if search_results:
        print("Potential sensitive information found:")
        for result in search_results:
            print(f"File: {result['file']}, Line Number: {result['line_number']}, Keyword: {result['keyword']}, Text: {result['text']}")
    else:
        print("No sensitive information found.")
