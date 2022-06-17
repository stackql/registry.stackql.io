---
title: webhook_deliveries
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
  
    
See also:   
[[` SHOW `]](/docs/language-spec/show) [[` DESCRIBE `]](/docs/language-spec/describe)  
* * * 
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webhook_deliveries</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.webhook_deliveries</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the delivery. |
| `response` | `object` |  |
| `status` | `string` | Description of the status of the attempted delivery |
| `installation_id` | `integer` | The id of the GitHub App installation associated with this event. |
| `duration` | `number` | Time spent delivering. |
| `repository_id` | `integer` | The id of the repository associated with this event. |
| `url` | `string` | The URL target of the delivery. |
| `event` | `string` | The event that triggered the delivery. |
| `request` | `object` |  |
| `delivered_at` | `string` | Time when the delivery was delivered. |
| `redelivery` | `boolean` | Whether the delivery is a redelivery. |
| `guid` | `string` | Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event). |
| `action` | `string` | The type of activity for the event that triggered the delivery. |
| `status_code` | `integer` | Status code received when delivery was made. |
## Methods
