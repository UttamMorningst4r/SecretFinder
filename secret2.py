import os
import re

def search_for_urls(directory):
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[-\w]+(?:\.(?:%[\da-fA-F]{2}|[-\w]|‌​(?:%[\da-fA-F]{2}))+)*(:\d+)?(?:/[^/?#]+)+\.(?:js|php|css|json)'  # URL pattern

    results = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.js', '.php', '.css', '.json')):  # Files with these extensions
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    for line_number, line in enumerate(lines, start=1):
                        urls = re.findall(url_pattern, line)
                        for url in urls:
                            results.append({
                                "file": file_path,
                                "line_number": line_number,
                                "url": url
                            })
    return results

if __name__ == "__main__":
    directory_to_search = '/path/to/your/directory'  # Directory containing files
    search_results = search_for_urls(directory_to_search)

    if search_results:
        print("URLs found in files:")
        for result in search_results:
            print(f"File: {result['file']}, Line Number: {result['line_number']}, URL: {result['url']}")
    else:
        print("No URLs found.")
