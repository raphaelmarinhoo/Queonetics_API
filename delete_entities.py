import time
import requests
from utils import API_BASE_URL, AUTH


def delete_organization(organization_id):
    url = f'{API_BASE_URL}/organization/{organization_id}'
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.delete(url, headers=headers, auth=AUTH)
        response.raise_for_status()
        print('\033[1;42mOrganization deleted!\033[0m')
    except requests.exceptions.RequestException as e:
        if response.status_code == 409:
            print(f'\033[1;41mOrganization deletion failed! Associated with another entity (Driver Team or Group). {e.response.content}\033[0m')
        else:
            print(f'\033[1;41mOrganization not found! {e.response.content}\033[0m')


def delete_driver_team(driver_team_id):
    url = f'{API_BASE_URL}/driverteam/{driver_team_id}'
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.delete(url, headers=headers, auth=AUTH)
        response.raise_for_status()
        print('\033[1;42mDriver team deleted!\033[0m')
    except requests.exceptions.RequestException as e:
        if response.status_code == 400:
            print(f'\033[1;41mDriver team deletion failed! Associated with another entity (Driver). {e.response.content}\033[0m')
        else:
            print(f'\033[1;41mDriver team not found! {e.response.content}\033[0m')


def delete_driver(driver_id):
    url = f'{API_BASE_URL}/driver/{driver_id}'
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.delete(url, headers=headers, auth=AUTH)
        response.raise_for_status()
        print('\033[1;42mDriver deleted!\033[0m')
    except requests.exceptions.RequestException as e:
        print(f'\033[1;41mDriver not found! {e.response.content}\033[0m')


def delete_group(group_id):
    url = f'{API_BASE_URL}/group/{group_id}'
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.delete(url, headers=headers, auth=AUTH)
        response.raise_for_status()
        print('\033[1;42mGroup deleted!\033[0m')
    except requests.exceptions.RequestException as e:
        print(f'\033[1;41mGroup not found! {e.response.content}\033[0m')


def main():
    while True:
        print("Menu:")
        print("1. Delete Organization")
        print("2. Delete Driver Team")
        print("3. Delete Driver")
        print("4. Delete Group")
        print("0. Exit")

        choice = input('Choose an option: ')

        if choice == '1':
            organization_id = input('Enter the ID of the organization to be deleted: ')
            delete_organization(organization_id)
        elif choice == '2':
            driver_team_id = input('Enter the ID of the driver team to be deleted: ')
            delete_driver_team(driver_team_id)
        elif choice == '3':
            driver_id = input('Enter the ID of the driver to be deleted: ')
            delete_driver(driver_id)
        elif choice == '4':
            group_id = input('Enter the ID of the group to be deleted: ')
            delete_group(group_id)
        elif choice == '0':
            print('Leaving the program...')
            time.sleep(0.5)
            break
        else:
            print('Invalid option. Please choose a valid option.')


if __name__ == '__main__':
    main()
