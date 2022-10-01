docs_description = {
    'Get organization\'s members': {
        'endpoint': '/orgs/{org}/members',
        'description': [
            ' - GET /orgs/{org}/members - List organization members\n',
            'List all users who are members of an organization. If the authenticated user is also a member of this organization\n',
            'then both concealed and public members will be returned.\n\n'
        ],
        'params_description': {
            'path_params': [
                ' - org: string (required) - The organization name. The name is not case-sensitive.\n'
            ]
        },
        'method': 'GET'
    },
    'Get organization\'s member by username': {
        'endpoint': '/orgs/{org}/members/{username}',
        'description': [
            ' - GET /orgs/{org}/members/{username} - Check organization membership for a user\n',
            'Check if a user is, publicly or privately, a member of the organization.\n\n'
        ],
        'params_description': {
            'path_params': [
                ' - org: string (required) - The organization name. The name is not case-sensitive.\n',
                ' - username: string (required) - The handle for the GitHub user account.\n'
            ]
        },
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
        'params_description': {
            'path_params': [
                ' - owner: string (required) - The account owner of the repository. The name is not case-sensitive.\n',
                ' - repo: string (required) - The name of the repository. The name is not case-sensitive.\n'
            ]
        },
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
        'params_description': {
            'path_params': [
                ' - owner: string (required) - The account owner of the repository. The name is not case-sensitive.\n',
                ' - repo: string (required) - The name of the repository. The name is not case-sensitive.\n',
                ' - username: string (required) - The handle for the GitHub user account.\n'
            ]
        },
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
        'params_description': {
            'path_params': [
                ' - owner: string (required) - The account owner of the repository. The name is not case-sensitive.\n',
                ' - repo: string (required) - The name of the repository. The name is not case-sensitive.\n',
            ],
            'body_params': [
                ' - head: string (required) - The name of the branch where your changes are implemented. For cross-repository pull requests in the same network, namespace head with a user like this: username:branch.\n',
                ' - base: string (required) - The name of the branch you want the changes pulled into. This should be an existing branch on the current repository. You cannot submit a pull request to one repository that requests a merge to a base of another repository.\n'
            ]
        },
        'method': 'POST',
        'payload': {
            'required': ['head', 'base'],
            'optional': ['title', 'body']
        }
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
        'params_description': {
            'path_params': [
                ' - owner: string (required) - The account owner of the repository. The name is not case-sensitive.\n',
                ' - repo: string (required) - The name of the repository. The name is not case-sensitive.\n',
                ' - pull_number: integer (required) - The number that identifies the pull request.\n'
            ],
            'body_params': [
                ' - title: string - The title of the pull request.\n',
                ' - body: string - The contents of the pull request.\n',
                ' - state: string - State of this Pull Request. Either open or closed.\n',
                ' - base: string - The name of the branch you want your changes pulled into. This should be an existing branch on the current repository. You cannot update the base branch on a pull request to point to another repository.\n'
            ]
        },
        'method': 'PATCH',
        'payload': {
            'optional': ['title', 'body', 'state']
        }
    },
    'Create a repository': {
        'endpoint': '/user/repos',
        'description': [
            ' - POST /user/repos - Create a new repository for the authenticated user.\n',
            'In order to specify the repository information, optional parameters could be set.\n\n'
        ],
        'params_description': {
            'body_params': [
                ' - name: string (required) - The name of the repository.\n',
                ' - description: string - A short description of the repository.\n',
                ' - homepage: string - A URL with more information about the repository.\n',
                ' - private: boolean - Whether the repository is private.\n'
            ]
        },
        'method': 'POST',
        'payload': {
            'required': ['name'],
            'optional': ['description', 'homepage', 'private']
        }
    },
    'Delete a repository': {
        'endpoint': '/repos/{owner}/{repo}',
        'description': [
            ' - DELETE /repos/{owner}/{repo} - Deleting a repository requires admin access. If OAuth is used, the delete_repo scope is required.\n',
            'If an organization owner has configured the organization to prevent members from deleting organization-owned repositories, you will get a 403 Forbidden response.\n\n'
        ],
        'params_description': {
            'path_params': [
                ' - owner: string (required) - The account owner of the repository. The name is not case-sensitive.\n',
                ' - repo: string (required) - The name of the repository. The name is not case-sensitive.\n'
            ]
        },
        'method': 'DELETE'
    }
}
