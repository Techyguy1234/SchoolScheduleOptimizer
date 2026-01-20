import csv


def save_schedules(schedules, filename="optimized_schedule.csv"):
    """
    Save student schedules to a CSV file in the same format as the original.
    Adds placeholder SEM2 classes after SEM1 classes to maintain parser compatibility.
    
    Args:
        schedules: List of student schedules, where each schedule is a list of rows
        filename: Output filename (default: "optimized_schedule.csv")
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header row
        writer.writerow(['Grade', 'Course Name', 'Period', 'Teacher', 'Location', 'Term'])
        
        # Write all schedule rows
        for schedule in schedules:
            for row in schedule:
                writer.writerow(row)
                
                # If this is a SEM1 class, add a placeholder SEM2 class
                if row[5] == 'SEM1':
                    # Create placeholder row with SEM2
                    placeholder_row = [row[0], row[1], '10', row[3], row[4], 'SEM2']
                    writer.writerow(placeholder_row)
    
    print(f"Schedule saved to {filename}")
