import requests
from bs4 import BeautifulSoup
import re
import os

# Function to clean up the text
def clean_text(text):
    # Remove multiple newlines and spaces
    text = re.sub(r'\n\s*\n', '\n', text)
    
    # Remove specific redundant sections
    redundant_patterns = [
        r'Some parts of the website may not work in Internet Explorer. Please use Chrome, Safari, Edge, or Firefox instead.',
        r'Visit\nApply\nGive',
        r'Menu',
        r'Admission\n\+',
        r'Academics\n\+',
        r'Research\n\+',
        r'About\n\+',
        r'© 2020 THE UNIVERSITY OF TOLEDO.*',
        r'A - Z List \| Careers \| Report a Concern \| Nondiscrimination \| Accessibility \| Web Privacy \| Feedback \| Contact Us',
        r'Last Updated:.*',
        r'UToledo Mascots',
        r'Admission',
        r'Undergraduate',
        r'Online',
        r'Transfer',
        r'International',
        r'Graduate/Professional',
        r'College Credit Plus',
        r'Guest',
        r'Admitted/New Rocket',
        r'Explore Majors and Programs',
        r'Academic Colleges',
        r'Arts and Letters',
        r'Business and Innovation',
        r'Education',
        r'Engineering',
        r'Graduate Studies',
        r'Health and Human Services',
        r'Honors',
        r'Law',
        r'Medicine and Life Sciences',
        r'Natural Sciences and Mathematics',
        r'Nursing',
        r'Pharmacy and Pharmaceutical Sciences',
        r'University College',
        r'Areas of Research Excellence',
        r'Research News',
        r'Research and Sponsored Programs',
        r'Tech Transfer',
        r'Research Compliance',
        r'Human Research Protection Program',
        r'Economic Development',
        r'About UToledo',
        r'Mission',
        r'Administration',
        r'Accreditation',
        r'Diversity',
        r'Student Outcomes',
        r'Expression on Campus',
        r'Athletics',
        r'Alumni',
        r'UToledo Health',
        r'Giving',
        r'MyUT',
        r'Main',
        r'Home',
        r'Contact Rocky and Rocksy',
        r'Apply to be Rocky or Rocksy',
        r'The History of Rocky and Rocksy',
        r'Contact Us',
        r'Main Campus',
        r'Memorial Field House',
        r'419.530.2416utmascot@utoledo.edu'
    ]
    
    for pattern in redundant_patterns:
        text = re.sub(pattern, '', text)
    
    # Remove multiple newlines again after removing patterns
    text = re.sub(r'\n\s*\n', '\n', text)
    
    return text.strip()

# List of URLs to fetch
urls = [
    'https://www.utoledo.edu/Mascot/',
    'https://www.utoledo.edu/campus/about/',
    'https://www.utoledo.edu/campus/about/mission.html',
    'https://www.utoledo.edu/engineering/',
    'https://www.utoledo.edu/campus/about/student-outcomes/',
    'https://www.utoledo.edu/events/university-events/'
]

# Directory to save the cleaned text files
output_dir = 'cleaned up text files'

# Ensure the directory exists
os.makedirs(output_dir, exist_ok=True)

for url in urls:
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the text content from the HTML
        text_content = soup.get_text()

        # Clean the text content
        cleaned_text = clean_text(text_content)

        # Create a unique filename for each webpage
        filename = url.replace('https://', '').replace('http://', '').replace('/', '_') + '.txt'
        output_filepath = os.path.join(output_dir, filename)

        # Save the cleaned text content to a file
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)

        print(f"Cleaned text content saved to {output_filepath}")

    except Exception as e:
        print(f"Failed to fetch the webpage {url}: {e}")
