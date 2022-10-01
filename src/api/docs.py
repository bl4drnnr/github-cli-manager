docs_description = {
    'Get organization\'s members': {
        'endpoint': '/orgs/{org}/members',
        'description': [
            ' - GET /orgs/{org}/members - List organization members\n',
            'List all users who are members of an organization. If the authenticated user is also a member of this organization\n',
            'then both concealed and public members will be returned.\n\n'
        ],
        'method': 'GET'
    },
    'Get organization\'s member by username': {
        'endpoint': '/orgs/{org}/members/{username}',
        'description': [
            ' - GET /orgs/{org}/members/{username} - Check organization membership for a user\n',
            'Check if a user is, publicly or privately, a member of the organization.\n\n'
        ],
        'method': 'GET'
    },
    'Get repository\'s collaborators': {
        'endpoint': '/repos/{owner}/{repo}/collaborators',
        'description': [
            ' - GET /repos/{owner}/{repo}/collaborators - List repository collaborators\n',
            'For organization-owned repositories, the list of collaborators includes outside\n',
            'collaborators, organization members that are direct collaborators, organization\n',
            'members with access through team memberships, organization members with\n',
            'access through default organization permissions, and organization owners.\n\n'
        ],
        'method': 'GET'
    },
    'Get repository\'s collaborator by username': {
        'endpoint': '/repos/{owner}/{repo}/collaborators/{username}',
        'description': [
            ' - GET /repos/{owner}/{repo}/collaborators/{username} - Check if a user is a repository collaborator\n',
            'For organization-owned repositories, the list of collaborators includes outside\n',
            'collaborators, organization members that are direct collaborators, organization\n',
            'members with access through team memberships, organization members with\n',
            'access through default organization permissions, and organization owners.\n\n'
        ],
        'method': 'GET'
    },
    'Create a pull request': {
        'endpoint': '/repos/{owner}/{repo}/pulls',
        'description': [
            ' - POST /repos/{owner}/{repo}/pulls - Draft pull requests are available in public repositories\n',
            'To open or update a pull request in a public repository, you must have write\n',
            'access to the head or the source branch. For organization-owned repositories,\n',
            'you must be a member of the organization that owns the repository to open or\n',
            'update a pull request.\n\n'
        ],
        'method': 'POST',
        'payload': ['title', 'body', 'head', 'base']
    },
    'Update a pull request': {
        'endpoint': '/repos/{owner}/{repo}/pulls/{pull_number}',
        'description': [
            ' - PATCH /repos/{owner}/{repo}/pulls/{pull_number} - Draft pull requests are available in public repositories\n',
            'To open or update a pull request in a public repository, you must have write\n',
            'access to the head or the source branch. For organization-owned repositories,\n',
            'you must be a member of the organization that owns the repository to open or\n',
            'update a pull request.\n\n'
        ],
        'method': 'PATCH'
    },
    'Create a repository': {
        'endpoint': '/user/repos',
        'description': [
            ' - POST /user/repos - Create a new repository for the authenticated user.\n',
            'In order to specify the repository information, optional parameters could be set.\n\n'
        ],
        'method': 'POST',
        'payload': ['name']
    },
    'Delete a repository': {
        'endpoint': '/repos/{owner}/{repo}',
        'description': [
            ' - DELETE /repos/{owner}/{repo} - Deleting a repository requires admin access. If OAuth is used, the delete_repo scope is required.\n',
            'If an organization owner has configured the organization to prevent members from deleting organization-owned repositories, you will get a 403 Forbidden response.\n\n'
        ],
        'method': 'DELETE'
    }
}
