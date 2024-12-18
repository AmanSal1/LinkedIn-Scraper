# LinkedIn Scraper

## Setting Up Your Environment

To get started with this project, you'll need to create a virtual environment to manage dependencies. Follow the steps below to set up your environment.

### Step 1: Install Python and Chrome Driver

Ensure that Python 3.x is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

Ensure that Chrome Driver is installed on  your system. You can download it from the https://googlechromelabs.github.io/chrome-for-testing/

### Step 2: Create a Virtual Environment

Once Python is installed, you can create a virtual environment by running the following command in your terminal or command prompt.

#### On macOS/Linux:
```bash
python3 -m venv venv
```
#### On Windows:
```
python -m venv venv
```

This will create a directory called venv in your project folder containing the virtual environment.

### Step 3: Activate the Virtual Environment

To activate the virtual environment, run the appropriate command based on your operating system.

#### On macOS/Linux:
```bash
source venv/bin/activate
```
#### On Windows:
```
.\venv\Scripts\activate
```
or
```
.\.venv\Scripts\activate
```

You should see the virtual environment's name in your terminal prompt indicating that it is now active.

### Step 4: Install Dependencies

Once your virtual environment is active, you can install the project dependencies. Run the following command:

```
pip install -r requirements.txt
```

### Step 5: Create a ```.env``` file for API Keys

In order to securely store your API key for the Gemini API, you'll need to create a ```.env``` file in the root of your project directory.

- Create a file named .env in the project root.
- Add your Gemini API key to the .env file in the following format:

```
API_KEY='your_gemini_api_key_here'
```

Replace ```your_gemini_api_key_here``` with your actual Gemini API key.

### Step 6: Start the App

Once everything is set up, you can start the app by running the following command:


#### On macOS/Linux:
```bash
python3 app.py
```
#### On Windows:
```
python app.py
```

This will start the application. You should see output in the terminal indicating that the app is running.


## Screenshots
![image](https://github.com/user-attachments/assets/1331cbdb-f3ed-46de-b781-7edc0ce112cc)


- Enter your username and password for LinkedIn, as well as the profile URL you want to scrape, and let the magic happen!
- Example Profile Link Format : https://www.linkedin.com/in/aman-salwan/


## Using Docker  

```
docker pull amansal1/linkedin-scraper:v1
```

```
docker run -e API_KEY=Your_API_Key -p 8000:8000 amansal1/linkedin-scraper:v1
```

## Resources

- ChatGPT
- https://ai.google.dev/api?lang=python
