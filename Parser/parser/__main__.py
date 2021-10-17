"""Entry point."""

import argparse
import time

import network
import process
import storage
from loguru import logger


def parse_arguments():
    """Parse console arguments.

    Returns:
        path to .csv file and path to output directory
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input_file',
        type=str,
        help='path to .csv file',
    )
    parser.add_argument(
        'output_dir',
        type=str,
        help='path to output directory',
    )
    args = parser.parse_args()
    return args.input_file, args.output_dir


if __name__ == '__main__':
    input_file, output_dir = parse_arguments()

    emails = storage.read_emails_from(input_file)
    user_ids = network.get_ids_by(set(emails))
    logger.info('Number of users: {0}'.format(len(emails)))

    for user_id, email in zip(user_ids, emails):
        logger.info('Starts parsing for {0}'.format(email))

        start_time = time.time()
        user = network.download_user_by(user_id, email)
        measured_time = time.time() - start_time
        logger.info('Finished in {0} seconds'.format(measured_time))

        user_xml = process.create_user_xml(user)
        storage.write_xml_to('users', '{0}.xml'.format(user.id), user_xml)
