"""This script initializes and runs the Flask app for the website."""

# Import the create_app function from the website package
from website import create_app

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the create_app function to create the Flask app instance
    app = create_app()

    # Run the Flask app in debug mode
    app.run(debug=True)
