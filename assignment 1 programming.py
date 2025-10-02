def display_info():
    """Display program information."""
    print("\n" + "=" * 40)
    print("PROGRAM INFORMATION")
    print("=" * 40)
    print("Program: Python CLI File Manager")
    print("Purpose: Week 1 Python fundamentals practice")
    print("Concepts: Variables, expressions, statements, functions")
    print("Features:")
      print("- File size calculation")
    print("- Interactive command system")
    print("- Help system")
    print("- Standard library only")
    print()
    print("Author: CS212 Assignment 1")
    print("Python Version:", sys.version.split()[0])
    def main():
    display_welcome()
    """Main program loop."""
    # Display welcome message
    # TODO: Call the function to display the welcome message

    # Main command loop
    running = True
    while running:
        try:
            choice = get_user_choice()
             main()