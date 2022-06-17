---
title: oktacommunication
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
<tr><td><b>Name</b></td><td><code>okta.org.oktacommunication</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.org.oktacommunication</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `optOutEmailUsers` | `boolean` |  |
| `_links` | `object` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `` | Gets Okta Communication Settings of your organization. | SELECT |
| `optIn` | `` | Opts in all users of this org to Okta Communication emails. | EXEC |
| `optOut` | `` | Opts out all users of this org from Okta Communication emails. | EXEC |
