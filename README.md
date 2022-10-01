```
+-------------------------------------------------------------------------+
|  _________________ ____  _____      __  ______   _  _____  ____________ |
| / ___/  _/_  __/ // / / / / _ )____/  |/  / _ | / |/ / _ |/ ___/ __/ _ \|
|/ (_ // /  / / / _  / /_/ / _  /___/ /|_/ / __ |/    / __ / (_ / _// , _/|
|\___/___/ /_/ /_//_/\____/____/   /_/  /_/_/ |_/_/|_/_/ |_\___/___/_/|_| |
+-------------------------------------------------------------------------+
```
---

**GITHUB-MANAGER** - is the simple _**Python terminal-based interactive application**_ that allows you 
to use **_GitHub REST API_** in order to **_read/write/update users/repositories_**
of your private or organization GitHub account.

### Documentation

Documentation had been already placed inside program - `Documentation` menu - in case if it's needed.


Below will be listed description to every possible menu option (basically, just GitHub REST API endpoint) of application.

---

**Get organization's members**
 - **GET /orgs/{org}/members** - List organization members
List all users who are members of an organization. If the authenticated user is also a member of this organization
then both concealed and public members will be returned.

`Path parameters:`

- `org`: string - **required** - The organization name. The name is not case-sensitive.

---

**Get organization's member by username**
 - **GET /orgs/{org}/members/{username}** - Check organization membership for a user
Check if a user is, publicly or privately, a member of the organization.

`Path parameters:`

- `org`: string - **required** - The organization name. The name is not case-sensitive.
- `username`: string - **required** - The handle for the GitHub user account.

---

**Get repository's collaborators**
 - **GET /repos/{owner}/{repo}/collaborators** - List repository collaborators
For organization-owned repositories, the list of collaborators includes outside
collaborators, organization members that are direct collaborators, organization
members with access through team memberships, organization members with
access through default organization permissions, and organization owners.

`Path parameters:`

- `owner`: string - **required** - The account owner of the repository. The name is not case-sensitive.
- `repo`: string - **required** - The name of the repository. The name is not case-sensitive.

---

**Get repository's collaborator by username**
 - **GET /repos/{owner}/{repo}/collaborators/{username}** - Check if a user is a repository collaborator
For organization-owned repositories, the list of collaborators includes outside
collaborators, organization members that are direct collaborators, organization
members with access through team memberships, organization members with
access through default organization permissions, and organization owners.

`Path parameters:`

- `owner`: string - **required** - The account owner of the repository. The name is not case-sensitive.
- `repo`: string - **required** - The name of the repository. The name is not case-sensitive.
- `username`: string - **required** - The handle for the GitHub user account.

---

**Create a pull request**
- **POST /repos/{owner}/{repo}/pulls** - Draft pull requests are available in public repositories
To open or update a pull request in a public repository, you must have write
access to the head or the source branch. For organization-owned repositories,
you must be a member of the organization that owns the repository to open or
update a pull request.

`Path parameters:`

- `owner`: string - **required** - The account owner of the repository. The name is not case-sensitive.
- `repo`: string - **required** - The name of the repository. The name is not case-sensitive.

`Body parameters:`

- `head`: string - **required** - The name of the branch where your changes are implemented. For cross-repository pull requests in the same network, namespace `head` with a user like this: `username:branch`.
- `base`: string - **required** - The name of the branch you want the changes pulled into. This should be an existing branch on the current repository. You cannot submit a pull request to one repository that requests a merge to a base of another repository.

---

**Update a pull request**
- **PATCH /repos/{owner}/{repo}/pulls/{pull_number}** - Draft pull requests are available in public repositories
To open or update a pull request in a public repository, you must have write
access to the head or the source branch. For organization-owned repositories,
you must be a member of the organization that owns the repository to open or
update a pull request.

`Path parameters:`

- `owner`: string - **required** - The account owner of the repository. The name is not case-sensitive.
- `repo`: string - **required** - The name of the repository. The name is not case-sensitive.
- `pull_number`: integer - **required** - The number that identifies the pull request.

`Body parameters:`

- `title`: string - The title of the pull request.
- `body`: string - The contents of the pull request.
- `state`: string - State of this Pull Request. Either `open` or `closed`.
- `base`: string - The name of the branch you want your changes pulled into. This should be an existing branch on the current repository. You cannot update the base branch on a pull request to point to another repository.

---

**Create a repository**
- **POST /user/repos** - Create a new repository for the authenticated user.
In order to specify the repository information, optional parameters could be set.

`Body parameters:`

- `name`: string - **required** - The name of the repository.
- `description`: string - A short description of the repository.

---

**Delete a repository**
- **DELETE /repos/{owner}/{repo}** - Deleting a repository requires admin access. If OAuth is used, the delete_repo scope is required.
If an organization owner has configured the organization to prevent members from deleting organization-owned repositories, you will get a 403 Forbidden response.

`Path parameters:`

- `owner`: string - **required** - The account owner of the repository. The name is not case-sensitive.
- `repo`: string - **required** - The name of the repository. The name is not case-sensitive.
  
---

### References:

For more see [GitHub available endpoints list](https://docs.github.com/en/rest/overview/endpoints-available-for-github-apps)

Developer contact - [mikhail.bahdashych@protonmail.com](mailto:mikhail.bahdashych@protonmail.com)
