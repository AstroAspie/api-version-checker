import requests
import sys

def output_success_message(version, url):
    print(f"\033[92m[SUCCESS]\033[0m \033[94m[v{version}]\033[0m {url}")

def output_error_message(version, url):
    print(f"\033[91m[ERROR]\033[0m \033[94m[v{version}]\033[0m {url}")

def check_swagger_versions(base_url, version):
    url = f"{base_url}/v{version}/swagger.json"
    response = requests.get(url)
    if response.status_code == 200:
        output_success_message(version, url)

def enumerate_api_versions(base_url, max_version):
    for version in range(1, max_version + 1):
        check_swagger_versions(base_url, version)

if __name__ == "__main__":
    base_url = sys.argv[1]
    max_version = 10
    enumerate_api_versions(base_url, max_version)