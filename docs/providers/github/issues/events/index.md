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
  
    
See also:   
[[` SHOW `]](/docs/language-spec/show) [[` DESCRIBE `]](/docs/language-spec/describe)  
* * * 
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.events</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `url` | `string` |  |
| `dismissed_review` | `object` |  |
| `commit_id` | `string` |  |
| `rename` | `object` | Issue Event Rename |
| `actor` | `object` | Simple User |
| `event` | `string` |  |
| `commit_url` | `string` |  |
| `requested_team` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `milestone` | `object` | Issue Event Milestone |
| `created_at` | `string` |  |
| `label` | `object` | Issue Event Label |
| `requested_reviewer` | `object` | Simple User |
| `assigner` | `object` | Simple User |
| `project_card` | `object` | Issue Event Project Card |
| `node_id` | `string` |  |
| `review_requester` | `object` | Simple User |
| `assignee` | `object` | Simple User |
| `author_association` | `string` | How the author is associated with the repository. |
| `lock_reason` | `string` |  |
| `issue` | `object` | Issues are a great way to keep track of tasks, enhancements, and bugs for your projects. |
## Methods
