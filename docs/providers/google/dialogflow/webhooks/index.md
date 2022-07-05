---
title: webhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - googlecloudplatform
  - gcp
  - google
  - webhooks
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webhooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.webhooks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique identifier of the webhook. Required for the Webhooks.UpdateWebhook method. Webhooks.CreateWebhook populates the name automatically. Format: `projects//locations//agents//webhooks/`. |
| `displayName` | `string` | Required. The human-readable name of the webhook, unique within the agent. |
| `genericWebService` | `object` | Represents configuration for a generic web service. |
| `serviceDirectory` | `object` | Represents configuration for a [Service Directory](https://cloud.google.com/service-directory) service. |
| `timeout` | `string` | Webhook execution timeout. Execution is considered failed if Dialogflow doesn't receive a response from webhook at the end of the timeout period. Defaults to 5 seconds, maximum allowed timeout is 30 seconds. |
| `disabled` | `boolean` | Indicates whether the webhook is disabled. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_webhooks_get` | `SELECT` | `name` | Retrieves the specified webhook. |
| `projects_locations_agents_webhooks_list` | `SELECT` | `parent` | Returns the list of all webhooks in the specified agent. |
| `projects_locations_agents_webhooks_create` | `INSERT` | `parent` | Creates a webhook in the specified agent. |
| `projects_locations_agents_webhooks_delete` | `DELETE` | `name` | Deletes the specified webhook. |
| `projects_locations_agents_webhooks_patch` | `EXEC` | `name` | Updates the specified webhook. |
