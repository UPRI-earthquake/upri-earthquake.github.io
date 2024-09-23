Developer Guide\: Contributing
===============================


## Git Workflow
For all repositories in the EarthquakeHub suite, the following guidelines are used for developer contributions. However, make sure to also check the *CONTRIBUTING.md* of the specific repository you're contributing to.

## 1. Create New Branch from `dev`

The `main` branch of a repository is the branch deployed to the servers, while the dev branch contains all latest developments in that are yet to be deployed. To add a new feature, create new branch on your local (clone or forked) repository based on the `dev` branch:
```bash
git checkout -b feature/new-feature
```

## 2. Commit & Push

Commit your changes with a descriptive commit message then push to upstream. Please refer to the following tags as guide in naming your commit messages and pull request titles:
1. **draft** - to be completed PR/commit
2. **feat** - new feature
3. **fix** - bug fixes
4. **test** - anything related to testing
5. **chore** - (aka housekeeping) cleaning/styling/refactor code, adding comments
6. **docs** - anything related to documentation / comments

## 3. Create a Pull Request

Navigate to UPRI-earthquake's GitHub repository and switch to the new branch. Click the "New Pull Request" button. Be sure to follow the pull request template for each repository and the Pull Request Title format: `type: [TASK ID] SHORTENED TASK TITLE`

## 4. Review & Merge

Another team member will be assigned to review your pull request and to provide feedback if necessary. Once the changes you have made are approved, they will be merged into the dev branch. Final testing will be done before the new-feature is added into the `main` branch and deployed to the online servers.
