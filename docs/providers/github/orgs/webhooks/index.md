---
title: webhooks
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
<tr><td><b>Name</b></td><td><code>github.orgs.webhooks</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.webhooks</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `type` | `string` |  |
| `created_at` | `string` |  |
| `events` | `array` |  |
| `url` | `string` |  |
| `active` | `boolean` |  |
| `deliveries_url` | `string` |  |
| `updated_at` | `string` |  |
| `config` | `object` |  |
| `ping_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_webhook` | `hook_id, org` | Returns a webhook configured in an organization. To get only the webhook `config` properties, see "[Get a webhook configuration for an organization](/rest/reference/orgs#get-a-webhook-configuration-for-an-organization)." | SELECT |
| `list_webhooks` | `org` |  | SELECT |
| `create_webhook` | `org, data__config, data__name` | Here's how you can create a hook that posts payloads in JSON format: | INSERT |
| `delete_webhook` | `hook_id, org` |  | DELETE |
| `ping_webhook` | `hook_id, org` | This will trigger a [ping event](https://docs.github.com/webhooks/#ping-event) to be sent to the hook. | EXEC |
| `update_webhook` | `hook_id, org` | Updates a webhook configured in an organization. When you update a webhook, the `secret` will be overwritten. If you previously had a `secret` set, you must provide the same `secret` or set a new `secret` or the secret will be removed. If you are only updating individual webhook `config` properties, use "[Update a webhook configuration for an organization](/rest/reference/orgs#update-a-webhook-configuration-for-an-organization)." | EXEC |
