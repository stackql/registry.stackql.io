---
title: webhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - webhooks
  - container_registry
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webhooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.webhooks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `provisioningState` | `string` | The provisioning state of the webhook at the time the operation was called. |
| `status` | `string` | The status of the webhook at the time the operation was called. |
| `type` | `string` | The type of the resource. |
| `scope` | `string` | The scope of repositories where the event can be triggered. For example, 'foo:*' means events for all tags under repository 'foo'. 'foo:bar' means events for 'foo:bar' only. 'foo' is equivalent to 'foo:latest'. Empty means all events. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `actions` | `array` | The list of actions that trigger the webhook to post notifications. |
| `location` | `string` | The location of the resource. This cannot be changed after the resource is created. |
| `tags` | `object` | The tags of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Webhooks_List` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all the webhooks for the specified container registry. |
| `Webhooks_Create` | `INSERT` | `registryName, resourceGroupName, subscriptionId, webhookName, data__location` | Creates a webhook for a container registry with the specified parameters. |
| `Webhooks_Delete` | `DELETE` | `registryName, resourceGroupName, subscriptionId, webhookName` | Deletes a webhook from a container registry. |
| `Webhooks_Get` | `EXEC` | `registryName, resourceGroupName, subscriptionId, webhookName` | Gets the properties of the specified webhook. |
| `Webhooks_GetCallbackConfig` | `EXEC` | `registryName, resourceGroupName, subscriptionId, webhookName` | Gets the configuration of service URI and custom headers for the webhook. |
| `Webhooks_ListEvents` | `EXEC` | `registryName, resourceGroupName, subscriptionId, webhookName` | Lists recent events for the specified webhook. |
| `Webhooks_Ping` | `EXEC` | `registryName, resourceGroupName, subscriptionId, webhookName` | Triggers a ping event to be sent to the webhook. |
| `Webhooks_Update` | `EXEC` | `registryName, resourceGroupName, subscriptionId, webhookName` | Updates a webhook with the specified parameters. |
