def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and attendees list.
    
    Args:
        template (str): Template string with placeholders
        attendees (list): List of dictionaries containing attendee data
    """
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries")
        return
    
    # Verify all items in attendees are dictionaries
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Attendees must be a list of dictionaries")
            return
    
    # Handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Create a copy of the template for this attendee
        output_content = template
        
        # Replace placeholders with actual values or "N/A"
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            # Replace None or missing values with "N/A"
            if value is None or value == "":
                value = "N/A"
            output_content = output_content.replace(f"{{{placeholder}}}", str(value))
        
        # Write to output file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(output_content)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
