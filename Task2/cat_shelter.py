import sys

def analyze_cat_shelter_log(log_file):
    """Analyze log file and print statistics."""
    
    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f'Cannot open "{log_file}"')
        return

    # Initialize variables
    cat_visits = 0  
    other_cats = 0
    total_time = 0
    durations = []
    
    # Process each line
    for line in lines:
        if line.strip() == 'END':
            break
        
        # Get data    
        cat_type, entry, exit = line.strip().split(',')  
        entry = int(entry)
        exit = int(exit)
        
        # Calculate duration
        duration = exit - entry  
        
        # Update counts and totals
        if cat_type == 'OURS':
            cat_visits += 1
            durations.append(duration)
            total_time += duration
        elif cat_type == 'THEIRS':
            other_cats += 1
            
    # Calculate statistics  
    if cat_visits > 0:
        avg_duration = total_time / cat_visits 
        longest_duration = max(durations)  
        shortest_duration = min(durations) 
    else:
        avg_duration = longest_duration = shortest_duration = 0
        
    # Inside analyze_cat_shelter_log()
    print_stats(log_file, cat_visits, other_cats, total_time, avg_duration, longest_duration, shortest_duration)

def print_stats(log_file, cat_visits, other_cats, total_time, 
               avg_duration, longest, shortest):
    """Print formatted statistics."""
    
    print(f'$ ./cat_shelter.py {log_file}\n')
    print('Log File Analysis')
    print('='*17)
    
    print(f'\nCat Visits: {cat_visits}')
    print(f'Other Cats: {other_cats}\n')   
    print(f'Total Time in House: {format_time(total_time)}\n')
    print(f'Average Visit Length: {format_time(avg_duration)}')
    print(f'Longest Visit:        {format_time(longest)}') 
    print(f'Shortest Visit:       {format_time(shortest)}')

def format_time(minutes):
    """Format time in minutes to string."""
    
    hours, mins = divmod(minutes, 60)
    if hours > 0:
        return f'{int(hours)} Hours, {int(mins)} Minutes'
    else:
        return f'{int(mins)} Minutes'
        
if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Missing command line argument!')
    else:
        analyze_cat_shelter_log(sys.argv[1])

