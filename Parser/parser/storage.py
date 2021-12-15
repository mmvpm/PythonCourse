"""Reading input & Saving results to local storage."""

import csv
from pathlib import Path
from xml.etree import ElementTree


def read_emails_from(path_to_file):
    """Read emails from .csv file.

    Args:
        path_to_file: str

    Returns:
        list of emails
    """
    with open(path_to_file) as emails:
        return [
            email
            for line in csv.reader(emails)
            for email in line
        ]


def write_xml_to(output_dir, file_name, xml_data, indent='\t'):
    """Write an xml to output_dir/file_name.

    Args:
        output_dir: str
        file_name: str
        xml_data: xml element
        indent: desirable xml indent
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    element_tree = ElementTree.ElementTree(xml_data)
    ElementTree.indent(element_tree, indent, level=0)

    file_name = '{0}/{1}'.format(output_dir, file_name)
    with open(file_name, 'wb') as xml_file:
        element_tree.write(
            xml_file,
            encoding='UTF-8',
            xml_declaration=True,
        )
