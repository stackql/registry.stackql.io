---
title: outside_collaborators
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
<tr><td><b>Name</b></td><td><code>github.orgs.outside_collaborators</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.outside_collaborators</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `gravatar_id` | `string` |  |
| `organizations_url` | `string` |  |
| `login` | `string` |  |
| `site_admin` | `boolean` |  |
| `gists_url` | `string` |  |
| `repos_url` | `string` |  |
| `type` | `string` |  |
| `following_url` | `string` |  |
| `subscriptions_url` | `string` |  |
| `email` | `string` |  |
| `url` | `string` |  |
| `followers_url` | `string` |  |
| `events_url` | `string` |  |
| `received_events_url` | `string` |  |
| `html_url` | `string` |  |
| `starred_at` | `string` |  |
| `starred_url` | `string` |  |
| `node_id` | `string` |  |
| `avatar_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_outside_collaborators` | `org` | List all users who are outside collaborators of an organization. | SELECT |
| `remove_outside_collaborator` | `org, username` | Removing a user from this list will remove them from all the organization's repositories. | DELETE |
| `convert_member_to_outside_collaborator` | `org, username` | When an organization member is converted to an outside collaborator, they'll only have access to the repositories that their current team membership allows. The user will no longer be a member of the organization. For more information, see "[Converting an organization member to an outside collaborator](https://docs.github.com/articles/converting-an-organization-member-to-an-outside-collaborator/)". | EXEC |
