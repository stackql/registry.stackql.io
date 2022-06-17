---
title: installations
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
<tr><td><b>Name</b></td><td><code>github.apps.installations</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.installations</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | The ID of the installation. |
| `suspended_by` | `object` | Simple User |
| `repository_selection` | `string` | Describe whether all repositories have been selected or there's a selection involved |
| `single_file_paths` | `array` |  |
| `suspended_at` | `string` |  |
| `updated_at` | `string` |  |
| `app_slug` | `string` |  |
| `permissions` | `object` | The permissions granted to the user-to-server access token. |
| `account` | `` |  |
| `target_type` | `string` |  |
| `app_id` | `integer` |  |
| `events` | `array` |  |
| `created_at` | `string` |  |
| `repositories_url` | `string` |  |
| `single_file_name` | `string` |  |
| `contact_email` | `string` |  |
| `html_url` | `string` |  |
| `has_multiple_single_files` | `boolean` |  |
| `access_tokens_url` | `string` |  |
| `target_id` | `integer` | The ID of the user or organization this token is being scoped to. |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_installation` | `installation_id` | Enables an authenticated GitHub App to find an installation's information using the installation id.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. | SELECT |
| `get_org_installation` | `org` | Enables an authenticated GitHub App to find the organization's installation information.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. | SELECT |
| `get_repo_installation` | `owner, repo` | Enables an authenticated GitHub App to find the repository's installation information. The installation's account type will be either an organization or a user account, depending which account the repository belongs to.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. | SELECT |
| `list_installations` | `` | You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.<br /><br />The permissions the installation has are included under the `permissions` key. | SELECT |
| `delete_installation` | `installation_id` | Uninstalls a GitHub App on a user, organization, or business account. If you prefer to temporarily suspend an app's access to your account's resources, then we recommend the "[Suspend an app installation](https://docs.github.com/rest/reference/apps/#suspend-an-app-installation)" endpoint.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. | DELETE |
| `create_installation_access_token` | `installation_id` | Creates an installation access token that enables a GitHub App to make authenticated API requests for the app's installation on an organization or individual account. Installation tokens expire one hour from the time you create them. Using an expired token produces a status code of `401 - Unauthorized`, and requires creating a new installation token. By default the installation token has access to all repositories that the installation can access. To restrict the access to specific repositories, you can provide the `repository_ids` when creating the token. When you omit `repository_ids`, the response does not contain the `repositories` key.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. | EXEC |
| `suspend_installation` | `installation_id` | Suspends a GitHub App on a user, organization, or business account, which blocks the app from accessing the account's resources. When a GitHub App is suspended, the app's access to the GitHub API or webhook events is blocked for that account.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. | EXEC |
| `unsuspend_installation` | `installation_id` | Removes a GitHub App installation suspension.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. | EXEC |
