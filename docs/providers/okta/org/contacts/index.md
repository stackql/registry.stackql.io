---
title: contacts
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
<tr><td><b>Name</b></td><td><code>okta.org.contacts</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.org.contacts</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `_links` | `object` |  |
| `contactType` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `contactType` | Retrieves the URL of the User associated with the specified Contact Type. | SELECT |
| `list` | `` | Gets Contact Types of your organization. | SELECT |
| `update` | `contactType` | Updates the User associated with the specified Contact Type. | EXEC |
