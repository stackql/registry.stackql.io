---
title: eventhooks
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
<tr><td><b>Name</b></td><td><code>eventhooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.eventhook.eventhooks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `name` | `string` |
| `lastUpdated` | `string` |
| `status` | `string` |
| `channel` | `object` |
| `created` | `string` |
| `_links` | `object` |
| `createdBy` | `string` |
| `verificationStatus` | `string` |
| `events` | `object` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get` | `SELECT` | `eventHookId` |
| `list` | `SELECT` |  |
| `insert` | `INSERT` |  |
| `delete` | `DELETE` | `eventHookId` |
| `activate` | `EXEC` | `eventHookId` |
| `deactivate` | `EXEC` | `eventHookId` |
| `update` | `EXEC` | `eventHookId` |
| `verify` | `EXEC` | `eventHookId` |
