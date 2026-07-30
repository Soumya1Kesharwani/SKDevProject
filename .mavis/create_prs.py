import urllib.request, json

GH_TOKEN = "${GH_TOKEN}"

def create_pr(issue_num, branch_name, title, body):
    data = json.dumps({
        'title': title,
        'body': body,
        'head': f'tmdeveloper007:{branch_name}',
        'base': 'main'
    }).encode()

    req = urllib.request.Request(
        'https://api.github.com/repos/komalharshita/devpath/pulls',
        data=data,
        headers={'Authorization': f'token {GH_TOKEN}', 'Content-Type': 'application/json'}
    )
    try:
        resp = urllib.request.urlopen(req)
        pr = json.loads(resp.read())
        print(f"PR #{pr['number']} ({issue_num}): {pr['html_url']}")
        return pr['number']
    except urllib.error.HTTPError as e:
        body_err = e.read()
        print(f"HTTP {e.code} for #{issue_num}: {body_err.decode()}")
        return None

# PR 1417
create_pr(1417, 'pr-tm-1417',
    'fix : removed unused make_response import and duplicate has_request_context imports in errors/handlers.py',
    '## Summary of What Has Been Done\n\nIn `src/errors/handlers.py`, two import issues were fixed:\n1. `make_response` was imported from Flask but never used - removed from the import line.\n2. `has_request_context` was imported twice (once in the group import, and then twice separately) - consolidated to a single occurrence in the group import.\n\n## Changes Made\n\n- Removed `make_response` from the Flask import line.\n- Removed the duplicate `from flask import has_request_context, request` line.\n- Removed the duplicate `from flask import has_request_context` line.\n- Kept `has_request_context` in the main Flask import line.\n\n## Impact it Made\n\n- Removes dead code and eliminates duplicate imports.\n- Follows Python import hygiene best practices.\n- Makes the file cleaner and easier to maintain.\n\n## Note: Please assign this PR to the `tmdeveloper007` account.\n\nCloses #1417'
)
