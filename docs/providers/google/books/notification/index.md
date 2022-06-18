---
title: notification
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
<tr><td><b>Name</b></td><td><code>notification</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.books.notification</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `is_document_mature` | `boolean` |  |
| `targetUrl` | `string` |  |
| `kind` | `string` | Resource type. |
| `reason` | `string` |  |
| `doc_id` | `string` |  |
| `crmExperimentIds` | `array` | The list of crm experiment ids. |
| `notificationGroup` | `string` |  |
| `pcampaign_id` | `string` |  |
| `dont_show_notification` | `boolean` |  |
| `notification_type` | `string` |  |
| `show_notification_settings_action` | `boolean` |  |
| `timeToExpireMs` | `string` |  |
| `doc_type` | `string` |  |
| `iconUrl` | `string` |  |
| `title` | `string` |  |
| `body` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get` | `SELECT` | `notification_id` |
