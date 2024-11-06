from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import google.generativeai as genai
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

load_dotenv()
api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)


def login_to_linkedin(username, password):

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")


    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.linkedin.com/login')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    username_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')

    username_input.send_keys(username)
    password_input.send_keys(password)
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()

    return driver


def scrape_posts(driver, profile_base_url):
    profile_url = f"{profile_base_url}/recent-activity/all/"
    driver.get(profile_url)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'update-components-text')))

    try:
        posts = driver.find_elements(By.CLASS_NAME, 'update-components-text')
        last_5_posts = [post.text for post in posts[:5]]
    except Exception as e:
        print("Error occurred while scraping:", e)
        last_5_posts = []

    return last_5_posts


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/scrape', methods=['POST'])
def scrape():
    username = request.form['username']
    password = request.form['password']
    profile_url = request.form['profileUrl']

    driver = login_to_linkedin(username, password)
    posts = scrape_posts(driver, profile_url)
    driver.quit()


    instruction = "This is a summary of someone's posts. Create a custom 2-line message to send in a LinkedIn connection request."
    posts_summary = " ".join(posts)

    model = genai.GenerativeModel('gemini-1.5-flash-latest', system_instruction=instruction)
    response = model.generate_content(posts_summary)

    return jsonify({
        'message': response.text,
        'posts': posts
    })


if __name__ == '__main__':
    app.run(debug=True)
