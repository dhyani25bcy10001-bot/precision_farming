
# 	PROJECT TITLE
      
 Precision agriculture

# OVERVIEW OF THE PROJECT
⦁	Our project offers a wide variety of information to the farmers of not only rich but also poor farmers of the villages for better agriculture and their profit.
⦁	Smart farming integrates modern technology with traditional agriculture practices to increase efficiency, productivity, and sustainability in farming operations. 
⦁	This innovative approach aims to optimize production efficiency, enhance crop yields, and minimize resource wastage through application sensors, data analytics and automation.
⦁	By harnessing real-time data and actionable insights, smart farming empowers farmers to make informed decisions promptly, thereby revolutionizing the agricultural landscape.
⦁	This project seeks to explore the implementation and impact of smart farming techniques, highlighting its potential to address  challenges such as climate change resilience, resource scarcity, and food security in the 21st century.

# FEATURES
⦁	Our program mainly concentrates on better irrigation methods and crop yield prediction. These factors help the farmers to cultivate the best food crops with accordance to environmental components. Also the farmers can adapt to climate changes to some degree by shifting planting dates, choosing varieties of crops with different growth duration, or changing crop rotations.  
⦁	For experimental analysis, the statistical numeric data related to agriculture is undertaken. The agricultural data aids the farmers to decide on the crop they would like to plant for the forthcoming year leading to maximum profit.
⦁	For example, summary information about the crop production can help the farmers identify the crop losses and prevent it in future. Crop yield prediction is an important agricultural problem. Every farmer wants to know how much yield he will get. In past, yield prediction was calculated by analysing farmer’s previous experience on a particular crop. Accurate information about history of crop yield is an important thing for making decisions related to agricultural risk management. Therefore, this project proposes an idea to predict the yield of the crop.
⦁	The framer will check the yield of the crop as per the area, before cultivating onto the field

# TECHNOLOGIES/TOOLS USED
##	Hardware Requirements
Hard Disk- 64 GB (minimum) and 
Ram- 1.5 GB
Keyboard- Any keyboard(QWERTY)
Mouse- Any standard mouse
Monitor- Any monitor with standard resolution(1080p)

##	Software Requirements
Operating System- Windows 8 or higher(64-bit)
Platform- Python 3.11
Database- MySQL SERVER 8.0 or higher
Languages- Python
Text Editor- Notepad

##	Modules used
Mysql.connector

Sys

##	Functions used
homepage()
working_menu()
search_crop_details()
program_schemes()
yield_data()
update_status()
suggestions()
admin_insert_crop()
admin_view_records()
admin_delete_data()
insert_admin_name_login()
admin_login()
user_login()
user_admin()
signup_user()
entry_menu()

# STEPS TO INSTALL AND RUN THE PROJECT
##	Python Installation Steps
Download Python from the official website (https://python.org) and choose the correct installer for your operating system.​
Run the installer and ensure you select "Add Python to PATH" during installation for easier command-line access.​
After installation, confirm it works by opening the command prompt or terminal and typing:
python --version
This should output the installed Python version.​

##	MySQL Installation Steps
Go to the MySQL website (https://dev.mysql.com/downloads/installer/) and download the MySQL Installer for Windows.​

Run the installer and choose "Full" or "Developer Default" for a complete installation.

##	Install Visual Studio Code
Go to the official site: search for “Download Visual Studio Code” and open the code.visualstudio.com download page.
Download the installer for your OS (Windows/macOS/Linux).​
Run the installer and accept the license, keep default install location, and finish the setup. On Windows, this typically adds code to your PATH so you can open folders with code . from a terminal.​

## Add Python support in VS Code
Open VS Code.
Go to the Extensions view (left sidebar icon that looks like four squares, or press Ctrl+Shift+X).
In the search box, type Python.
Install the official “Python” extension from Microsoft (it provides IntelliSense, debugging, environment selection, etc.).​
After installation, open a .py file; VS Code will prompt you to select a Python interpreter—choose the one where you installed Python.

##	Add MySQL support in VS Code
There is no single “official” MySQL extension, but you can install a database extension that supports MySQL so you can browse and run queries.
In VS Code, open the Extensions view again (Ctrl+Shift+X).
Search for extensions like:“MySQL”
Pick one with good ratings and explicit MySQL support, then click Install. These extensions usually add a database icon in the Activity Bar for managing connections.​

##	Connect to MySQL from VS Code
Make sure MySQL Server is installed and running on your machine.
In the database/MySQL extension panel, create a new connection.
Enter: host (often localhost), port (3306 by default), username (e.g., root), and password, and test the connection.
Once connected, you can expand databases and run SQL queries directly in VS Code.

# INSTRUCTIONS FOR TESTING
Ensure all required dependencies (including Python, mysql-connector, and database access) are installed and properly configured before running tests.​
Set up a test environment, ideally using a separate test database, to prevent data loss or corruption in production data.​
Verify that all necessary database tables (users, userdata, cropdetails, etc.) are created and initialized as specified in the project documentation.​
## Review and execute the code paths for both user and admin functionalities:
Test user sign-up and login with various combinations of valid and invalid credentials.​
Input new user data and check if updates (age, location, crop, etc.) reflect correctly in the database and application menus.​
Search for crop details including available and non-available crops to assess error handling.​
Explore admin features: inserting crop data, deleting user records, and viewing entries to confirm database integrity after each operation.​
Simulate edge cases such as duplicate usernames, invalid field entries, and attempts to access crops or users not present in the database.​
Check all user interface prompts and error messages for clarity and correctness.​
After making any changes, verify data by directly inspecting the database tables or using the provided view features.​
Automate the above test scenarios using Python testing tools like unittest or pytest when feasible, and ensure all test cases can be rerun reliably.​​

Document any issues found during testing and steps to reproduce them for future debugging and improvement.

