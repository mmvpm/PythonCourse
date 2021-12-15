"""Processing data."""

from xml.etree import ElementTree


def _write_items_to_xml(root_element, item_list, item_name):
    """Write items from item_list to root_element.

    Args:
        root_element: an existent xml element
        item_list: items to write, format: [{'id': 0, ...}, ...]
        item_name: future item names in xml
    """
    for user_item in item_list:
        item_xml = ElementTree.SubElement(root_element, item_name)
        for tag, tag_value in user_item.items():
            if tag == 'userId':  # ignore user id
                continue
            tag_xml = ElementTree.SubElement(item_xml, tag)
            tag_xml.text = str(tag_value)


def create_user_xml(user):
    """Create an xml element for user by the data.

    Args:
        user_id: int
        email: str
        posts: list of posts by this user
        albums: list of albums by this user
        todos: list of todos by this user

    Returns:
        xml element with all the information above
    """
    user_xml = ElementTree.Element('user')

    ElementTree.SubElement(user_xml, 'id').text = str(user.id)
    ElementTree.SubElement(user_xml, 'email').text = user.email

    for item_name, item_data in user.get_content().items():
        item_xml = ElementTree.SubElement(user_xml, item_name)
        _write_items_to_xml(item_xml, item_data, item_name)

    return user_xml
