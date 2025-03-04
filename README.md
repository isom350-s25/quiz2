# quiz2
Quiz 2 template for Spring 2025

## Instructions for ISOM 350: Business Application Development Class

Students are required to complete the following tasks for the practical quiz:

1. **Task 1 (20 pts): Setup a Django Project and App**
   - Create a Django project named `quiz2_project`.
   - Create an app within the project named `quiz2_app`.

2. **Task 2 (20 pts): Create a Static View**
   - Create a view named `static_view`.
   - Wire the URL to the view.
   - Display a simple, meaningful message in the view. For example, "Welcome to the Quiz 2 Application!".

3. **Task 3 (20 pts): Create a List View**
   - Create a view named `list_view`.
   - Wire the URL to the view.
   - In the view, create the following list:
     ```python
     shopping_list = ['apple', 'banana', 'cherry']
     ```
   - Pass the list to the context and display it in the template as an unordered list. You must use the 'for' loop template tag to display the list.

4. **Task 4 (20 pts): Create a Dynamic View**
   - Create a view named `dynamic_view`.
   - Wire the URL to the view.
   - Display a GET form to the user with a single input field named `name`.
   - When the user submits the form, display a greeting message in the template. For example, if the user enters "John", the message should be "Hello, John".

5. **Task 5 (20 pts): Rewire URLs**
   - Ensure that the URLs use an app-based `urls.py` instead of the root `urls.py`.

## Additional Instructions

- Projects that do not run will receive a minimum grade of 20 points if submitted correctly through GitHub.
- Grades will be assigned to working tasks only.
- Using branches to work on each task and then merging to the main branch will award you **10 bonus points**.