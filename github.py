# github_info_app.py
import requests

def get_github_user_info(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    user_data = response.json()
    return user_data

def get_github_user_repos(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)
    repos_data = response.json()
    return repos_data

def display_user_info(user_data):
    print(f"GitHub User Information for {user_data['login']}:")
    print(f"Name: {user_data['name']}")
    print(f"Bio: {user_data['bio']}")
    print(f"Public Repositories: {user_data['public_repos']}")

def display_user_repos(repos_data):
    print("\nPublic Repositories:")
    for repo in repos_data:
        print(f" - {repo['name']}")

if __name__ == '__main__':
    while True:
     username = input("Enter a GitHub username: ")

     user_data = get_github_user_info(username)
     repos_data = get_github_user_repos(username)

     display_user_info(user_data)
     display_user_repos(repos_data)
