---
title: organization
hide_title: false
hide_table_of_contents: false
keywords:
  - organization
  - confluent
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
<tr><td><b>Name</b></td><td><code>organization</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.confluent.organization</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ARM id of the resource. |
| `name` | `string` | The name of the resource. |
| `createdTime` | `string` | The creation time of the resource. |
| `userDetail` | `object` | Subscriber detail |
| `organizationId` | `string` | Id of the Confluent organization. |
| `tags` | `object` | Organization resource tags |
| `location` | `string` | Location of Organization resource |
| `type` | `string` | The type of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `provisioningState` | `string` | Provision states for confluent RP |
| `ssoUrl` | `string` | SSO url for the Confluent organization. |
| `offerDetail` | `object` | Confluent Offer detail |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Organization_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |
| `Organization_ListBySubscription` | `SELECT` | `subscriptionId` |
| `Organization_Create` | `INSERT` | `organizationName, resourceGroupName, subscriptionId` |
| `Organization_Delete` | `DELETE` | `organizationName, resourceGroupName, subscriptionId` |
| `Organization_Get` | `EXEC` | `organizationName, resourceGroupName, subscriptionId` |
| `Organization_Update` | `EXEC` | `organizationName, resourceGroupName, subscriptionId` |
