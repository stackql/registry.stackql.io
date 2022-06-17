---
title: sms
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
<tr><td><b>Name</b></td><td><code>okta.template.sms</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.template.sms</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `lastUpdated` | `string` |  |
| `template` | `string` |  |
| `translations` | `object` |  |
| `type` | `string` |  |
| `created` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `templateId` | Fetches a specific template by `id` | SELECT |
| `list` | `` | Enumerates custom SMS templates in your organization. A subset of templates can be returned that match a template type. | SELECT |
| `insert` | `` | Adds a new custom SMS template to your organization. | INSERT |
| `delete` | `templateId` | Removes an SMS template. | DELETE |
| `partialUpdate` | `templateId` | Updates only some of the SMS template properties: | EXEC |
| `update` | `templateId` | Updates the SMS template. | EXEC |
