---
title: events
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
<tr><td><b>Name</b></td><td><code>github.issues.events</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.events</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `created_at` | `string` |  |
| `commit_id` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `event` | `string` |  |
| `issue` | `object` | Issues are a great way to keep track of tasks, enhancements, and bugs for your projects. |
| `actor` | `object` | Simple User |
| `author_association` | `string` | How the author is associated with the repository. |
| `url` | `string` |  |
| `project_card` | `object` | Issue Event Project Card |
| `dismissed_review` | `object` |  |
| `label` | `object` | Issue Event Label |
| `milestone` | `object` | Issue Event Milestone |
| `node_id` | `string` |  |
| `rename` | `object` | Issue Event Rename |
| `commit_url` | `string` |  |
| `assigner` | `object` | Simple User |
| `assignee` | `object` | Simple User |
| `lock_reason` | `string` |  |
| `review_requester` | `object` | Simple User |
| `requested_team` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `requested_reviewer` | `object` | Simple User |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_event` | `event_id, owner, repo` |  | SELECT |
| `list_events_for_repo` | `owner, repo` |  | SELECT |
