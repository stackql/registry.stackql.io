---
title: public_memberships
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
<tr><td><b>Name</b></td><td><code>github.orgs.public_memberships</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.public_memberships</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `remove_public_membership_for_authenticated_user` | `org, username` |  | DELETE |
| `check_public_membership_for_user` | `org, username` |  | EXEC |
| `set_public_membership_for_authenticated_user` | `org, username` | The user can publicize their own membership. (A user cannot publicize the membership for another user.)<br /><br />Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." | EXEC |
