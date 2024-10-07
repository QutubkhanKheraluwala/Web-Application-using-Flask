## 1. Blog Post Submission Form:

- A form class, ```PostForm```, is created in ```app/forms.py``` to facilitate blog post submissions. It includes a ```TextAreaField``` for users to input their posts and a ```SubmitField``` for submitting the post.
- The ```PostForm``` is integrated into the ```index.html``` template using Jinja templating. Users can input new posts using the provided form.

## 2. Post Submission and Display:

- The ```index()``` view function in ```app/routes.py``` handles the post submission logic. It processes the form data, adds the new post to the database, and redirects the user to the home page. It also retrieves and displays posts from followed users.
- The ```explore()``` view function provides a global post stream for all users to explore and view posts from users they do not follow.

## 3. Pagination of Blog Posts:

- Pagination is implemented to manage the display of a large number of posts. The ```db.paginate()``` function retrieves a limited number of posts per page, allowing for efficient handling of large post collections.
- Pagination links for navigating to the previous and next pages are added to the home page and explore page using the ```Pagination``` object's attributes and the ```url_for()``` function.

## 4. User Profile Page Pagination:

- The user profile page is updated to include pagination for the user's posts. The changes are made in the ```user()``` view function, which now displays the user's posts with pagination links for navigation.

## Credits

This project is created by Qutubkhan while learning from the Flask Mega-Tutorial by Miguel Grinberg, which provides comprehensive guidance for building web applications with Flask.

## GitHub Repository

Find the project on GitHub: [Flask Project](https://github.com/QutubkhanKheraluwala/flask_project/tree/Chp-9)
