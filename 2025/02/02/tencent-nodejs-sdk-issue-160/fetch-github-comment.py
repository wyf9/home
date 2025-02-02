# coding: utf-8
# import requests
# url = 'https://api.github.com/repos/TencentCloud/tencentcloud-sdk-nodejs/issues/160/comments'

from github import Github
from tokenstr import token
from github import Auth
import json

# --- functions


def save(filename: str, obj: dict, mode: str = 'w', indent: int = 4):
    '''
    save a dict to json file
    '''
    with open(filename, mode) as f:
        json.dump(obj, f, ensure_ascii=False, separators=(',', ': '), indent=indent)
        f.close()

# --- auth


# get auth
auth = Auth.Token(token)

# get github obj
g = Github(
    auth=auth,
    retry=5,
    per_page=100,
    seconds_between_requests=0.25
)

# --- base info

# use this
repo_name = 'TencentCloud/tencentcloud-sdk-nodejs'
issue_id = 160

# for testing
# repo_name: str = 'wyf9/sleepy'
# issue_id: int = 3

print(f'fetching issue {repo_name}#{issue_id}...')

# get repo
repo = g.get_repo(repo_name)

# get issue
issue = repo.get_issue(issue_id)

# get issue info
issue_username = issue.user.login
issue_titie = issue.title

# get issue body
issue_body = issue.body


# --- comments

# get issue comments
issue_comments = issue.get_comments()

# get issue comment count
comment_count = issue_comments.totalCount
print(f'got comment count: {comment_count}')

comments = []

num = 0
for i in issue_comments:
    num += 1
    print(f'fetching comment {num}/{comment_count}...')
    comments.append({
        'url': i.url,
        'created_at': i.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'id': i.id,
        'user': i.user.login,
        'body': i.body,
        'reactions': i.reactions
    })


# --- save

print('saving data...')

save('issue_info.json', {
    'repo': repo_name,
    'issue_id': issue_id,
    'username': issue_username,
    'title': issue_titie,
    'body': issue_body,
    'comment_count': comment_count
})

print('issue info saved to issue_info.json')

save('issue_comments.json', comments)

print('issue comments saved to issue_comments.json')

g.close()
