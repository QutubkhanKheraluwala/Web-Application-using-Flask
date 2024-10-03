# Flask Application Error Handling and Debug Mode

This Flask application incorporates robust error handling mechanisms and features, enabling effective debugging and error resolution. The text outlines the following key aspects:

## Error Handling and Debug Mode

- Experience an internal server error caused by a unique constraint failure in the user profile editing process.
- Explore the use of debug mode in Flask for improved error handling during development, including the interactive debugger in the browser, the reloader, and the associated security considerations.

## Custom Error Pages and Logging

- Implement custom error pages for HTTP errors 404 and 500, enhancing the user experience and application aesthetics.
- Configure the application to log errors to a file using a RotatingFileHandler, including the formatting of log messages for comprehensive details.

## Email Notifications for Errors

- Set up email notifications for errors using the SMTPHandler, allowing immediate email alerts for critical errors encountered in the application.
- Demonstrate the testing of email notifications using a debugging SMTP server and provide configurations for using a real email server.

## Bug Fix and Debug Mode Permanence

- Address the duplicate username bug by implementing username validation in the edit profile form, preventing username conflicts in most cases.
- Enable debug mode permanently by adding the FLASK_DEBUG environment variable to the .flaskenv file for streamlined development and error handling.

## Credits

This project is created by Qutubkhan while learning from the Flask Mega-Tutorial by Miguel Grinberg, which provides comprehensive guidance for building web applications with Flask.

## GitHub Repository

Find the project on GitHub: [Flask Project](https://github.com/QutubkhanKheraluwala/flask_project/tree/Chp-7)
