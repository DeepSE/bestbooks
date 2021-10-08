from datetime import datetime
import logging
from github import Github

from dotenv import load_dotenv
import os

load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# does not raise an exception, but returns None
git_token = os.getenv('GITHUB_TOKEN')

if git_token is None:
    logger.error('Specify GITHUB_TOKEN as an environment variable.')
    exit(-1)

gh = Github(git_token)

def write_comment(comment, repos_name, issueid):
    repo = gh.get_repo(repos_name)

    thread_issue = repo.get_issue(number=int(issueid))
    if thread_issue:
        res = thread_issue.create_comment(comment)
        logger.info("Comment on " + str(res))
        return

def create_issue(repos_name, title, body):
    repo = gh.get_repo(repos_name)
    return repo.create_issue(title=title, body=body)

if __name__ == '__main__':
    write_comment("Test", 'hunkim/digital-human', 1)