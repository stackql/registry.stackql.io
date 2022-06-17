---
title: clients
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
<tr><td><b>Name</b></td><td><code>clients</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.clients</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `logo_uri` | `string` |
| `_links` | `object` |
| `client_id` | `string` |
| `client_name` | `string` |
| `client_uri` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list` | `SELECT` | `authServerId` |
