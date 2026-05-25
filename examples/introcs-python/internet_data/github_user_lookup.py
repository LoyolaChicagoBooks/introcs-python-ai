import requests


def main() -> None:
    username = input("Enter a GitHub username: ")
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"Name:         {data.get('name', 'N/A')}")
            print(f"Followers:    {data['followers']}")
            print(f"Public repos: {data['public_repos']}")
        elif response.status_code == 404:
            print(f"User '{username}' not found.")
        else:
            print(f"Unexpected error: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Could not connect to GitHub.")


if __name__ == "__main__":
    main()
