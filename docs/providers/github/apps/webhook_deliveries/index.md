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
<tr><td><b>Name</b></td><td><code>github.apps.webhook_deliveries</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.webhook_deliveries</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the delivery. |
| `action` | `string` | The type of activity for the event that triggered the delivery. |
| `response` | `object` |  |
| `duration` | `number` | Time spent delivering. |
| `request` | `object` |  |
| `guid` | `string` | Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event). |
| `installation_id` | `integer` | The id of the GitHub App installation associated with this event. |
| `status` | `string` | Description of the status of the attempted delivery |
| `status_code` | `integer` | Status code received when delivery was made. |
| `repository_id` | `integer` | The id of the repository associated with this event. |
| `event` | `string` | The event that triggered the delivery. |
| `url` | `string` | The URL target of the delivery. |
| `delivered_at` | `string` | Time when the delivery was delivered. |
| `redelivery` | `boolean` | Whether the delivery is a redelivery. |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_webhook_delivery` | `delivery_id` | Returns a delivery for the webhook configured for a GitHub App.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. | SELECT |
| `list_webhook_deliveries` | `` | Returns a list of webhook deliveries for the webhook configured for a GitHub App.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. | SELECT |
| `redeliver_webhook_delivery` | `delivery_id` | Redeliver a delivery for the webhook configured for a GitHub App.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. | EXEC |
