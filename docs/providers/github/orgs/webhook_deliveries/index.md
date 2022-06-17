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
<tr><td><b>Id</b></td><td><code>github.orgs.webhook_deliveries</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the delivery. |
| `action` | `string` | The type of activity for the event that triggered the delivery. |
| `repository_id` | `integer` | The id of the repository associated with this event. |
| `delivered_at` | `string` | Time when the delivery was delivered. |
| `event` | `string` | The event that triggered the delivery. |
| `response` | `object` |  |
| `status_code` | `integer` | Status code received when delivery was made. |
| `url` | `string` | The URL target of the delivery. |
| `status` | `string` | Description of the status of the attempted delivery |
| `duration` | `number` | Time spent delivering. |
| `request` | `object` |  |
| `installation_id` | `integer` | The id of the GitHub App installation associated with this event. |
| `redelivery` | `boolean` | Whether the delivery is a redelivery. |
| `guid` | `string` | Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event). |
## Methods
