---
title: following
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
<tr><td><b>Name</b></td><td><code>github.users.following</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.users.following</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `organizations_url` | `string` |  |
| `gravatar_id` | `string` |  |
| `starred_url` | `string` |  |
| `site_admin` | `boolean` |  |
| `events_url` | `string` |  |
| `subscriptions_url` | `string` |  |
| `repos_url` | `string` |  |
| `gists_url` | `string` |  |
| `login` | `string` |  |
| `type` | `string` |  |
| `html_url` | `string` |  |
| `followers_url` | `string` |  |
| `email` | `string` |  |
| `received_events_url` | `string` |  |
| `following_url` | `string` |  |
| `node_id` | `string` |  |
| `starred_at` | `string` |  |
| `avatar_url` | `string` |  |
| `url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_followed_by_authenticated_user` | `` | Lists the people who the authenticated user follows. | SELECT |
| `list_following_for_user` | `username` | Lists the people who the specified user follows. | SELECT |
| `check_following_for_user` | `target_user, username` |  | EXEC |
| `check_person_is_followed_by_authenticated` | `username` |  | EXEC |
| `follow` | `username` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)."<br /><br />Following a user requires the user to be logged in and authenticated with basic auth or OAuth with the `user:follow` scope. | EXEC |
| `unfollow` | `username` | Unfollowing a user requires the user to be logged in and authenticated with basic auth or OAuth with the `user:follow` scope. | EXEC |
