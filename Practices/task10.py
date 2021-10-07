import requests
from loguru import logger

STATUS_CODE_OK = 200


def get_json_pet_by_id(pet_id):
    base_path = 'https://petstore.swagger.io/v2/pet'
    response = requests.get(f'{base_path}/{pet_id}')
    json_data = response.json()

    if response.status_code == STATUS_CODE_OK:
        name = json_data['name']
        tags = json_data['tags']
        logger.info(f'{name: }, {tags: }')
    else:
        logger.error(json_data['message'])

    return json_data


for index in (1, 2, 3, 4000099):
    get_json_pet_by_id(index)
