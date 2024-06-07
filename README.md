<h1 align="center" id="title">Test summarizer</h1>

<p id="description">Test summarizer features authentication and user management using Django's authentication system. It enables secure user registration, login, logout, and user CRUD operations via APIs. The text summarization aspect utilizes third-party APIs to summarize large text inputs. Additionally, a user search API returns a list of users based on search terms, including a concatenated "nameEmail" field with user details.</p>

<h2>🚀 Documentation</h2>

[https://www.postman.com/varsitypro-3710/workspace/varsityassignment/documentation/34380419-adf4152d-8d7b-46f4-850e-e18038e69634](Postman documentation)

  
<h2>🛠️ Installation Steps:</h2>

1. Clone the repository:

```CMD
git clone https://github.com/aditya-Kumar421/TextSummarizer.git
```

To run the server, you need to have Python installed on your machine. If you don't have it installed, you can follow the instructions [here](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) to install it.

2. Install and Create a virtual environment:

```CMD
python -m venv env
```

Activate the virtual environment

```CMD
env\Scripts\activate
```

3. Install the dependencies:

```CMD
pip install -r requirements.txt
```

<p>5. Set Up Database:</p>

```
python manage.py migrate
```

<p>6. Run the Development Server:</p>

```
python manage.py runserver
```

<p>7. Access the Endpoints:</p>

```
http://127.0.0.1:8000/swagger/
```

<h2>🍰 Contribution Guidelines:</h2>

Please contribute using GitHub Flow. Create a branch add commits and open a pull request
