import time
import requests
from utils import API_BASE_URL, AUTH, PARENT_ORGANIZATION_ID


def create_organization():
    url = f'{API_BASE_URL}/organization'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'name': '',
        'description': '',
        'state': '',
        'country': '',
        'gmt': -180,
        'dst': 'false',
        'hierarchicalLevel': {
            'id': 3
        },
        'parentOrganization': {
            'id': PARENT_ORGANIZATION_ID
        }
    }
    response = requests.post(url, json=data, headers=headers, auth=AUTH)
    response.raise_for_status()
    print('\033[42mOrganization created!\033[0m')
    return response.json()


def create_driver_team(organization_id):
    url = f'{API_BASE_URL}/driverteam'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'name': '',
        'description': '',
        'organization': {
            'id': organization_id
        },
        'drivers': [],
        'filiationType': '',  #INHERENT, OUTSOURCED
        'representatives': [
            570
        ]
    }
    response = requests.post(url, json=data, headers=headers, auth=AUTH)
    response.raise_for_status()
    print('\033[42mDriver Team created!\033[0m')
    return response.json()


def create_driver(driver_team_id):
    url = f'{API_BASE_URL}/driver'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'name': '',
        'type': '',  #DRIVER, MECHANIC, VALET_PARKING, CANDIDATE
        'registration': '',
        'driverTeam': {'id': driver_team_id},
        'status': '',  #ACTIVE, INACTIVE, INOPERATIVE
        'hiringType': '',  #TEMPORARY OR FIXED
        'birthDate': '2024-05-16T03:00:00.000Z',
        'license': '',
        'licenseRegister': '',
        'licenseNationalRegister': '',
        'licenseCategory': '[]',  #ACC, A, B, C, D
        'licenseExpedition': '2023-07-11T00:00:00.000Z',
        'licenseExpiration': '2023-11-15T00:00:00.000Z',
        'firstLicense': '2022-12-04T03:00:00.000Z',
        'licenses': [
            {
                'license': ''  #ACC, A, B, C, D
            },
        ]
    }
    response = requests.post(url, json=data, headers=headers, auth=AUTH)
    response.raise_for_status()
    print('\033[42mDriver created!\033[0m')
    return response.json()


def create_group(organization_id):
    url = f'{API_BASE_URL}/group'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'name': '',
        'disabled': '',  #TRUE or FALSE
        'organization': {'id': organization_id},
    }
    response = requests.post(url, json=data, headers=headers, auth=AUTH)
    response.raise_for_status()
    print('\033[42mGroup created!\033[0m')
    return response.json()


def main():
    try:
        organization = create_organization()
        organization_id = organization['id']
        print(f'Organization: {organization}')
        time.sleep(0.5)

        driver_team = create_driver_team(organization_id)
        driver_team_id = driver_team['id']
        print(f'Driver Team: {driver_team}')
        time.sleep(0.5)

        driver = create_driver(driver_team_id)
        print(f'Driver: {driver}')
        time.sleep(0.5)

        group = create_group(organization_id)
        print(f'Group: {group}')
        time.sleep(0.5)

        print('\033[1;42mRegistration completed successfully!\033[0m')

    except requests.exceptions.RequestException as e:
        print('\033[1mThere was a registration failure.\033[0m')
        print(f'\033[1;41mRequest error: {e.response.content}\033[0m')


if __name__ == '__main__':
    main()
