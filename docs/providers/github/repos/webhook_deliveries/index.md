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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>github.repos.webhook_deliveries</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.webhook_deliveries</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the delivery. |
| `action` | `string` | The type of activity for the event that triggered the delivery. |
| `delivered_at` | `string` | Time when the delivery was delivered. |
| `status` | `string` | Description of the status of the attempted delivery |
| `event` | `string` | The event that triggered the delivery. |
| `repository_id` | `integer` | The id of the repository associated with this event. |
| `status_code` | `integer` | Status code received when delivery was made. |
| `guid` | `string` | Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event). |
| `response` | `object` |  |
| `url` | `string` | The URL target of the delivery. |
| `redelivery` | `boolean` | Whether the delivery is a redelivery. |
| `installation_id` | `integer` | The id of the GitHub App installation associated with this event. |
| `request` | `object` |  |
| `duration` | `number` | Time spent delivering. |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_webhook_delivery` | `delivery_id, hook_id, owner, repo` | Returns a delivery for a webhook configured in a repository. | SELECT |
| `list_webhook_deliveries` | `hook_id, owner, repo` | Returns a list of webhook deliveries for a webhook configured in a repository. | SELECT |
| `redeliver_webhook_delivery` | `delivery_id, hook_id, owner, repo` | Redeliver a webhook delivery for a webhook configured in a repository. | EXEC |
