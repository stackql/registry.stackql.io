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
<tr><td><b>Name</b></td><td><code>github.activity.events</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.events</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `public` | `boolean` |  |
| `repo` | `object` |  |
| `type` | `string` |  |
| `actor` | `object` | Actor |
| `created_at` | `string` |  |
| `org` | `object` | Actor |
| `payload` | `object` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_events_for_authenticated_user` | `username` | If you are authenticated as the given user, you will see your private events. Otherwise, you'll only see public events. | SELECT |
| `list_org_events_for_authenticated_user` | `org, username` | This is the user's organization dashboard. You must be authenticated as the user to view this. | SELECT |
| `list_repo_events` | `owner, repo` |  | SELECT |
