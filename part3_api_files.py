#Task 1



# --- Part A: Write and Append ---

# 1. Write the initial notes
initial_notes = [
    "Topic 1: Variables store data. Python is dynamically typed.\n",
    "Topic 2: Lists are ordered and mutable.\n",
    "Topic 3: Dictionaries store key-value pairs.\n",
    "Topic 4: Loops automate repetitive tasks.\n",
    "Topic 5: Exception handling prevents crashes.\n"
]

with open('python_notes.txt', 'w', encoding="utf-8") as file:
    file.writelines(initial_notes)
    
print("✓ File written successfully.")

# 2. Append two custom lines
custom_notes = [
    "Topic 6: Functions wrap logic into reusable blocks of code.\n",
    "Topic 7: File I/O allows data to persist even after the program closes.\n"
]

with open('python_notes.txt', 'a', encoding="utf-8") as file:
    file.writelines(custom_notes)
    
print("✓ Lines appended successfully.\n")


# --- Part B: Read and Process ---
print("--- Reading File Content ---")

# 1. Read the file back
with open('python_notes.txt', 'r', encoding="utf-8") as file:
    # .readlines() reads all lines into a Python list
    saved_lines = file.readlines()

# 2. Print numbered lines and count the total
# enumerate() gives us both the line and a counter (starting at 1)
for i, line in enumerate(saved_lines, start=1):
    print(f"{i}. {line.strip()}")

total_lines = len(saved_lines)
print(f"\nTotal number of lines: {total_lines}\n")

# 3. Keyword Search
keyword = input("Enter a keyword to search for: ").strip()

print(f"\n--- Search Results for '{keyword}' ---")

match_found = False
for line in saved_lines:
    # Convert both the line and the keyword to lowercase for a case-insensitive search
    if keyword.lower() in line.lower():
        print(line.strip())
        match_found = True

# If the loop finishes and match_found is still False, print the helpful message
if not match_found:
    print(f"No matches found for the keyword '{keyword}'. Try another word!")




#Task 2

import requests

# --- Step 1: Fetch and Display Products ---
print("--- Step 1: Top 20 Products ---")
url_20 = "https://dummyjson.com/products?limit=20"
response = requests.get(url_20)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    products = data.get("products", [])
    
    # Print the table header
    print(f"{'ID':<4} | {'Title':<30} | {'Category':<15} | {'Price':<8} | {'Rating':<5}")
    print("-" * 72)
    
    # Print each product row
    for p in products:
        # We slice the title [:30] just in case a product has a massively long name that breaks our table
        print(f"{p['id']:<4} | {p['title'][:30]:<30} | {p['category'][:15]:<15} | ${p['price']:<7.2f} | {p['rating']:<5}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")


# --- Step 2: Filter and Sort ---
print("\n--- Step 2: High-Rated Products (>= 4.5), Sorted by Price (Desc) ---")
# Filter using a list comprehension
high_rated = [p for p in products if p['rating'] >= 4.5]

# Sort using the sorted() function and a lambda function targeting the price
sorted_high_rated = sorted(high_rated, key=lambda x: x['price'], reverse=True)

for p in sorted_high_rated:
    print(f"{p['title']} - ${p['price']} (Rating: {p['rating']})")


# --- Step 3: Search by Category ---
print("\n--- Step 3: Laptops Category ---")
url_laptops = "https://dummyjson.com/products/category/laptops"
response_laptops = requests.get(url_laptops)

if response_laptops.status_code == 200:
    laptops_data = response_laptops.json()
    laptops = laptops_data.get("products", [])
    
    for laptop in laptops:
        print(f"Laptop: {laptop['title']} | Price: ${laptop['price']}")
else:
    print("Failed to fetch laptops category.")


# --- Step 4: POST Request (Simulated Creation) ---
print("\n--- Step 4: Add New Product (POST Request) ---")
url_add = "https://dummyjson.com/products/add"

# This is the dictionary representing the JSON payload we want to send
new_product_payload = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

# Use requests.post() and pass the dictionary to the 'json' parameter
response_post = requests.post(url_add, json=new_product_payload)

# Print the full response returned by the server to prove it worked
print(f"Server Response Status Code: {response_post.status_code}")
print("Server JSON Response:")
print(response_post.json())





#Task 3


import requests

# ==========================================
# Part A: Guarded Calculator
# ==========================================
print("--- Part A: Guarded Calculator ---")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

# Testing Part A
print(f"10 / 2   = {safe_divide(10, 2)}")
print(f"10 / 0   = {safe_divide(10, 0)}")
print(f"'ten'/ 2 = {safe_divide('ten', 2)}\n")


# ==========================================
# Part B: Guarded File Reader
# ==========================================
print("--- Part B: Guarded File Reader ---")

def read_file_safe(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            # Truncating output just to keep the terminal clean
            return f"✓ Success. Read {len(content)} characters."
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    finally:
        print("File operation attempt complete.")

# Testing Part B
# Note: Ensure "python_notes.txt" exists from the previous task!
print(read_file_safe("python_notes.txt"))
print()
read_file_safe("ghost_file.txt")
print()


# ==========================================
# Part C: Robust API Calls
# ==========================================
print("--- Part C: Robust API Call Example ---")

# We wrap the API call logic in a reusable function to handle exceptions cleanly
def make_robust_get_request(url):
    try:
        # Pass timeout=5 as requested
        response = requests.get(url, timeout=5)
        return response
        
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    # Return None if the request failed at the network level
    return None

# Test the robust function
test_response = make_robust_get_request("https://dummyjson.com/products?limit=1")
if test_response and test_response.status_code == 200:
    print("✓ Robust API connection successful.\n")


# ==========================================
# Part D: Input Validation Loop
# ==========================================
print("--- Part D: Product Lookup Loop ---")

while True:
    user_input = input("Enter a product ID to look up (1–100), or 'quit' to exit: ").strip()
    
    # 1. Exit condition
    if user_input.lower() == 'quit':
        print("Exiting product lookup. Goodbye!")
        break
        
    # 2. Input Validation
    try:
        product_id = int(user_input)
        if product_id < 1 or product_id > 100:
            print("⚠️ Warning: Product ID must be between 1 and 100.\n")
            continue # Skip the rest of the loop and ask again
    except ValueError:
        print("⚠️ Warning: Invalid input. Please enter a valid integer.\n")
        continue # Skip the rest of the loop and ask again
        
    # 3. API Execution
    url = f"https://dummyjson.com/products/{product_id}"
    
    # Utilizing our robust request function from Part C
    response = make_robust_get_request(url)
    
    # 4. Status Code Evaluation
    if response is not None:
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Found: {data.get('title')} - ${data.get('price')}\n")
        elif response.status_code == 404:
            print("❌ Product not found.\n")
        else:
            print(f"⚠️ Received unexpected HTTP status code: {response.status_code}\n")





#Task 4


import requests
from datetime import datetime

# --- 1. The Logger Function ---
def log_error(function_name, error_type, message):
    """Generates a timestamp and appends the formatted error to the log file."""
    # Get current time formatted as YYYY-MM-DD HH:MM:SS
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Construct the exact string format requested
    log_entry = f"[{timestamp}] ERROR in {function_name}: {error_type} — {message}\n"
    
    # Open in 'a' (append) mode so we don't overwrite previous logs
    with open("error_log.txt", "a", encoding="utf-8") as file:
        file.write(log_entry)

# --- 2. Triggering a ConnectionError ---
def fetch_products():
    print("Attempting to connect to a non-existent host...")
    try:
        # Intentionally requesting a fake URL to force a network-level failure
        requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
    except requests.exceptions.ConnectionError:
        print("❌ ConnectionError caught! Logging it...\n")
        log_error("fetch_products", "ConnectionError", "No connection could be made")

# --- 3. Triggering an HTTP Error (404) ---
def lookup_product(product_id):
    print(f"Attempting to lookup product ID {product_id}...")
    url = f"https://dummyjson.com/products/{product_id}"
    
    try:
        response = requests.get(url, timeout=5)
        
        # 404 is NOT an exception in Python. We must evaluate the status_code manually.
        if response.status_code != 200:
            print(f"❌ HTTP {response.status_code} received! Logging it...\n")
            # Log the manual HTTP error
            log_error(
                "lookup_product", 
                "HTTPError", 
                f"{response.status_code} Not Found for product ID {product_id}"
            )
        else:
            print("✓ Product found!")
            
    except Exception as e:
        # Fallback for any other unexpected Python errors
        log_error("lookup_product", type(e).__name__, str(e))

# ==========================================
# Execution & Testing
# ==========================================

# Run the triggers
fetch_products()
lookup_product(999)

# --- 4. Read and Print the Log File ---
print("--- Final Contents of error_log.txt ---")
try:
    with open("error_log.txt", "r", encoding="utf-8") as file:
        print(file.read().strip())
except FileNotFoundError:
    print("Error: Log file was not created.")