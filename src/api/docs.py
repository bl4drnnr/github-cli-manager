docs_description = {
    'Get organization\'s members': {
        'endpoint': '/orgs/{org}/members',
        'description': [
            ' - GET /orgs/{org}/members - List organization members\n',
            'List all users who are members of an organization. If the authenticated user is also a member of this organization\n',
            'then both concealed and public members will be returned.\n\n'
        ]
    },
    'Get organization\'s member by username': {
        'endpoint': '/orgs/{org}/members/{username}',
        'description': [
            ' - GET /orgs/{org}/members/{username} - Check organization membership for a user\n',
            'Check if a user is, publicly or privately, a member of the organization.\n\n'
        ]
    },
    'Get repository\'s collaborators': {
        'endpoint': '/repos/{owner}/{repo}/collaborators',
        'description': [
            ' - GET /repos/{owner}/{repo}/collaborators - List repository collaborators\n',
            'For organization-owned repositories, the list of collaborators includes outside\n',
            'collaborators, organization members that are direct collaborators, organization\n',
            'members with access through team memberships, organization members with\n',
            'access through default organization permissions, and organization owners.\n\n'
        ]
    },
    'Get repository\'s collaborator by username': {
        'endpoint': '/repos/{owner}/{repo}/collaborators/{username}',
        'description': [
            ' - GET /repos/{owner}/{repo}/collaborators/{username} - Check if a user is a repository collaborator\n',
            'For organization-owned repositories, the list of collaborators includes outside\n',
            'collaborators, organization members that are direct collaborators, organization\n',
            'members with access through team memberships, organization members with\n',
            'access through default organization permissions, and organization owners.\n\n'
        ]
    }
}
