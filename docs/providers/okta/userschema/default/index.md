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
<tr><td><b>Name</b></td><td><code>default</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.userschema.default</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `name` | `string` |
| `$schema` | `string` |
| `title` | `string` |
| `definitions` | `object` |
| `type` | `string` |
| `properties` | `object` |
| `lastUpdated` | `string` |
| `_links` | `object` |
| `created` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list` | `SELECT` | `appInstanceId` | Fetches the Schema for an App User |
| `insert` | `INSERT` | `appInstanceId` | Partial updates on the User Profile properties of the Application User Schema. |
