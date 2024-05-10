import os
import re

# Define the root directory (assuming you want the script to work from a known root)
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))

# Define paths for the input and output files relative to the root directory
input_file = os.path.join(root_dir, 'tekniker_public.ttl')
output_file = os.path.join(root_dir, 'tekniker.ttl')

# Read the content from the input file
with open(input_file, 'r') as file:
    content = file.read()

# Define the pattern to match UUIDs with hyphens and the replacement function
uuid_pattern = re.compile(r'(:EMMO_[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})')

def replace_hyphens_with_underscores(match):
    return match.group(1).replace('-', '_')

# Replace the UUIDs in the content
new_content = uuid_pattern.sub(replace_hyphens_with_underscores, content)

# Write the new content to the output file
with open(output_file, 'w') as file:
    file.write(new_content)

print("UUIDs have been successfully updated in the file.")
