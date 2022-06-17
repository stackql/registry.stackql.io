---
title: default
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
<tr><td><b>Name</b></td><td><code>okta.userschema.default</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.userschema.default</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `$schema` | `string` |  |
| `created` | `string` |  |
| `type` | `string` |  |
| `lastUpdated` | `string` |  |
| `_links` | `object` |  |
| `properties` | `object` |  |
| `definitions` | `object` |  |
| `title` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list` | `appInstanceId` | Fetches the Schema for an App User | SELECT |
| `insert` | `appInstanceId` | Partial updates on the User Profile properties of the Application User Schema. | INSERT |
