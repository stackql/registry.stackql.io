---
title: branch_protection
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>github.repos.branch_protection</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.branch_protection</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` |  |
| `enabled` | `boolean` |  |
| `required_signatures` | `object` |  |
| `protection_url` | `string` |  |
| `required_pull_request_reviews` | `object` | Protected Branch Pull Request Review |
| `required_conversation_resolution` | `object` |  |
| `url` | `string` |  |
| `required_linear_history` | `object` |  |
| `required_status_checks` | `object` | Protected Branch Required Status Check |
| `restrictions` | `object` | Branch Restriction Policy |
| `allow_deletions` | `object` |  |
| `allow_force_pushes` | `object` |  |
| `enforce_admins` | `object` | Protected Branch Admin Enforced |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_branch_protection` | `branch, owner, repo` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation. | SELECT |
| `delete_branch_protection` | `branch, owner, repo` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation. | DELETE |
| `update_branch_protection` | `branch, owner, repo, data__enforce_admins, data__required_pull_request_reviews, data__required_status_checks, data__restrictions` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Protecting a branch requires admin or owner permissions to the repository.<br /><br />**Note**: Passing new arrays of `users` and `teams` replaces their previous values.<br /><br />**Note**: The list of users, apps, and teams in total is limited to 100 items. | EXEC |
