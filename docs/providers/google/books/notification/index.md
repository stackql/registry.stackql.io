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
|:-----|:---------|:------------|
| `doc_type` | `string` |  |
| `iconUrl` | `string` |  |
| `is_document_mature` | `boolean` |  |
| `doc_id` | `string` |  |
| `targetUrl` | `string` |  |
| `kind` | `string` | Resource type. |
| `notification_type` | `string` |  |
| `pcampaign_id` | `string` |  |
| `body` | `string` |  |
| `crmExperimentIds` | `array` | The list of crm experiment ids. |
| `show_notification_settings_action` | `boolean` |  |
| `title` | `string` |  |
| `notificationGroup` | `string` |  |
| `reason` | `string` |  |
| `timeToExpireMs` | `string` |  |
| `dont_show_notification` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `notification_id` |
