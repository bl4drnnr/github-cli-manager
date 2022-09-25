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

**Get organization's members**
 - **GET /orgs/{org}/members** - List organization members
List all users who are members of an organization. If the authenticated user is also a member of this organization
then both concealed and public members will be returned.

**Get organization's member**
 - **GET /orgs/{org}/members/{username}** - Check organization membership for a user
Check if a user is, publicly or privately, a member of the organization.

**Get repository's collaborators**
 - **GET /repos/{owner}/{repo}/collaborators** - List repository collaborators
For organization-owned repositories, the list of collaborators includes outside
collaborators, organization members that are direct collaborators, organization
members with access through team memberships, organization members with
access through default organization permissions, and organization owners.

**Get repository's collaborator by username**
 - **GET /repos/{owner}/{repo}/collaborators/{username}** - Check if a user is a repository collaborator
For organization-owned repositories, the list of collaborators includes outside
collaborators, organization members that are direct collaborators, organization
members with access through team memberships, organization members with
access through default organization permissions, and organization owners.


### Reference:

For more see [GitHub available endpoints list](https://docs.github.com/en/rest/overview/endpoints-available-for-github-apps)
