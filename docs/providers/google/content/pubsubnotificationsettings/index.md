---
title: pubsubnotificationsettings
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
<tr><td><b>Name</b></td><td><code>pubsubnotificationsettings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.content.pubsubnotificationsettings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `cloudTopicName` | `string` | Cloud pub/sub topic to which notifications are sent (read-only). |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#pubsubNotificationSettings`" |
| `registeredEvents` | `array` | List of event types. Acceptable values are: - "`orderPendingShipment`"  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `merchantId` | Retrieves a Merchant Center account's pubsub notification settings. |
| `update` | `EXEC` | `merchantId` | Register a Merchant Center account for pubsub notifications. Note that cloud topic name should not be provided as part of the request. |
