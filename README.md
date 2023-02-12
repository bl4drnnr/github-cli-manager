# Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [CLI Documentation](#cli-documentation)
4. [Interactive CLI Documentation](#interactive-cli-documentation)
   1. [List repositories for a user](#list-repositories-for-a-user)
   2. [List organizations for a user](#list-organizations-for-a-user)
   3. [List organization repositories](#list-organization-repositories)
   4. [Get organization's members](#get-organizations-members)
   5. [Get organization's member by username](#get-organizations-member-by-username)
   6. [Get repository's collaborators](#get-repositorys-collaborators)
   7. [Get repository's collaborator by username](#get-repositorys-collaborator-by-username)
   8. [Create a pull request](#create-a-pull-request)
   9. [Update a pull request](#update-a-pull-request)
   10. [Merge a pull request](#merge-a-pull-request)
   11. [Get all pull requests](#get-all-pull-requests)
   12. [Create a repository](#create-a-repository)
   13. [Delete a repository](#delete-a-repository)
5. [References](#references)
6. [License](#license)

---

## Introduction
**GITHUB-MANAGER** - is the simple _**Python terminal-based interactive application**_ that allows you 
to use **_GitHub REST API_** in order to **_read/write/update users/repositories_**
of private or public organizations and repositories.

Application is available in 2 versions:
- interactive terminal-based application with graphic interface
- simple **CLI** application

Documentation for [CLI](#cli-documentation) and for [Interactive CLI](#interactive-cli-documentation) are available below.

---

## Installation

In order to install program for `Linux`/`MacOS`, open terminal and run:

```
bash <(curl -s -S -L https://raw.githubusercontent.com/bl4drnnr/github-cli-manager/master/install.sh)
```

This will download `GitHub Manager`, install and start setup.

---

## CLI Documentation

CLI documentation is available under `-h` or `--help` flag.

The only 2 flags that are required - `token` and one of action flags (everything under `--help` flag). Depending on flag,
other optional arguments could be used.

```
usage: main.py [-o] [-u] [-own] [-r] [-p] [-d] [-b] [-n] [-q] [-h] [--gom] [--gomu] [--grc] [--grcu] [--cpr] [--upr] [--mpr]
               [--cr] [--dr] [--gagt] [--gagtn] [--lrfu] [--lor] [--lofu]
               token

positional arguments:
  token                GitHub developer token.

optional arguments:
  -o , --org           Organization name.
  -u , --username      Username.
  -own , --owner       Owner.
  -r , --repo          Repository.
  -p , --pull-number   Pull number.
  -d , --head          Head branch.
  -b , --base          Base branch.
  -n , --name          Name of repository.
  -q , --query         Query. (Example: --query=?type=all&sort=updated)
  -h, --help           Display this message.
  --gom                Get organization's members.
  --gomu               Get organization's member by username.
  --grc                Get repository's collaborators.
  --grcu               Get repository's collaborator by username.
  --cpr                Create a pull request.
  --upr                Update a pull request.
  --mpr                Merge a pull request.
  --cr                 Create a repository.
  --dr                 Deleting a repository.
  --gagt               Get all gitignore templates.
  --gagtn              Get a gitignore template.
  --lrfu               Lists public repositories for the specified user.
  --lor                Lists repositories for the specified organization.
  --lofu               List public organization memberships for the specified user.
```

---

## Interactive CLI Documentation

Documentation had been already placed inside program - `Documentation` menu - in case if it's needed.

Below will be listed description to every possible menu option (basically, just GitHub REST API endpoint) of application.

---

### List repositories for a user
- **GET /users/{username}/repos** - Lists public repositories for the specified user.
Note: For GitHub AE, this endpoint will list internal repositories for the specified user.

`Path parameters:`

- `username`: string - **required** - The handle for the GitHub user account.

`Query parameters:`

- `type`: string - optional - Limit results to repositories of the specified type: all, owner (default), member.
- `sort`: string - optional - The property to sort the results by.

---

### List organizations for a user
- **GET /users/{username}/orgs** - List public organization memberships for the specified user.
This method only lists public memberships, regardless of authentication. If you need to fetch all the organization memberships (public and private)
for the authenticated user, use the List organizations for the authenticated user API instead.

`Path parameters:`

- `username`: string - **required** - The handle for the GitHub user account.

`Query parameters:`

- `per_page`: integer - optional - The number of results per page (max 100). Default is 30.
- `page`: integer - optional - Page number of the results to fetch. Default is 1.

---

### List organization repositories
 - **GET /orgs/{org}/repos** - Lists repositories for the specified organization.

`Path parameters:`

- `org`: string - **required** - The organization name. The name is not case-sensitive.

`Query parameters:`

- `type`: string - optional - Specifies the types of repositories you want returned.
- `sort`: string - optional - The property to sort the results by: created (default), updated, pushed, full_name.

---

### Get organization's members
 - **GET /orgs/{org}/members** - List organization members.
List all users who are members of an organization. If the authenticated user is also a member of this organization
then both concealed and public members will be returned.

`Path parameters:`

- `org`: string - **required** - The organization name. The name is not case-sensitive.

---

### Get organization's member by username
 - **GET /orgs/{org}/members/{username}** - Check organization membership for a user.
Check if a user is, publicly or privately, a member of the organization.

`Path parameters:`

- `org`: string - **required** - The organization name. The name is not case-sensitive.
- `username`: string - **required** - The handle for the GitHub user account.

---

### Get repository's collaborators
 - **GET /repos/{owner}/{repo}/collaborators** - List repository collaborators.
For organization-owned repositories, the list of collaborators includes outside
collaborators, organization members that are direct collaborators, organization
members with access through team memberships, organization members with
access through default organization permissions, and organization owners.

`Path parameters:`

- `owner`: string - **required** - The account owner of the repository. The name is not case-sensitive.
- `repo`: string - **required** - The name of the repository. The name is not case-sensitive.

---

### Get repository's collaborator by username
 - **GET /repos/{owner}/{repo}/collaborators/{username}** - Check if a user is a repository collaborator.
For organization-owned repositories, the list of collaborators includes outside
collaborators, organization members that are direct collaborators, organization
members with access through team memberships, organization members with
access through default organization permissions, and organization owners.

`Path parameters:`

- `owner`: string - **required** - The account owner of the repository. The name is not case-sensitive.
- `repo`: string - **required** - The name of the repository. The name is not case-sensitive.
- `username`: string - **required** - The handle for the GitHub user account.

---

### Create a pull request
- **POST /repos/{owner}/{repo}/pulls** - Draft pull requests are available in public repositories.
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

### Update a pull request
- **PATCH /repos/{owner}/{repo}/pulls/{pull_number}** - Draft pull requests are available in public repositories.
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

### Merge a pull request
- **PUT /repos/{owner}/{repo}/pulls/{pull_number}/merge** - Merge a pull request.
This endpoint triggers notifications. Creating content too quickly using this
endpoint may result in secondary rate limiting. See "Secondary rate limits" and
"Dealing with secondary rate limits" for details.

`Path parameters:`

- `owner`: string - **required** - The account owner of the repository. The name is not case-sensitive.
- `repo`: string - **required** - The name of the repository. The name is not case-sensitive.
- `pull_number`: integer - **required** - The number that identifies the pull request.

`Body parameters:`

- `commit title`: string - Title for the automatic commit message.
- `commit message`: string - Extra detail to append to automatic commit message.
- `merge method`: string - Merge method to use. Possible values are merge, squash or rebase. Default is merge.

---

### Get all pull requests

- **GET /repos/{owner}/{repo}/pulls** - Allows go get all pull requests

`Path parameters:`

- `owner`: string **required** - The account owner of the repository. The name is not case-sensitive.
- `repo`: string **required** - The name of the repository. The name is not case-sensitive.

`Query parameters:`

- `page`: string - optional - The number of results per page (max 100). Default is 30.\n',
- `per_page`: string - optional - Page number of the results to fetch. Default is 1.\n',
- `state`: string - optional - Either open, closed, or all to filter by state. Default: open.\n'
- `all`: boolean - optional - Set to true if you want to get ALL pull requests. Default is false. If set to true, page and per_page will be ignored.\n\n'

---

### Create a repository
- **POST /user/repos** - Create a new repository for the authenticated user.
In order to specify the repository information, optional parameters could be set.

`Body parameters:`

- `name`: string - **required** - The name of the repository.
- `description`: string - A short description of the repository.
- `homepage`: string - A URL with more information about the repository.
- `private`: boolean - Whether the repository is private.

---

### Delete a repository
- **DELETE /repos/{owner}/{repo}** - Deleting a repository requires admin access. If OAuth is used, the delete_repo scope is required.
If an organization owner has configured the organization to prevent members from deleting organization-owned repositories, you will get a 403 Forbidden response.

`Path parameters:`

- `owner`: string - **required** - The account owner of the repository. The name is not case-sensitive.
- `repo`: string - **required** - The name of the repository. The name is not case-sensitive.
  
---

### Get all gitignore templates
- **GET /gitignore/templates** - List all templates available to pass as an option when creating a repository.

---

### Get a gitignore template
- **GET /gitignore/templates/{name}** - Get gitignore template by name.

`Path parameters`:

- `name`: string - **required** - Name of the template.

---

### References

For more see [GitHub available endpoints list](https://docs.github.com/en/rest/overview/endpoints-available-for-github-apps)

Developer contact - [contact@mikhailbahdashych.me](mailto:contact@mikhailbahdashych.me)

---

### License

Licensed by [MIT License](LICENSE).

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
