---
title: domain_topics
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_topics
  - event_grid
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
<tr><td><b>Name</b></td><td><code>domain_topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.domain_topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `provisioningState` | `string` | Provisioning state of the domain topic. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DomainTopics_ListByDomain` | `SELECT` | `domainName, resourceGroupName, subscriptionId` | List all the topics in a domain. |
| `DomainTopics_CreateOrUpdate` | `INSERT` | `domainName, domainTopicName, resourceGroupName, subscriptionId` | Asynchronously creates or updates a new domain topic with the specified parameters. |
| `DomainTopics_Delete` | `DELETE` | `domainName, domainTopicName, resourceGroupName, subscriptionId` | Delete existing domain topic. |
| `DomainTopics_Get` | `EXEC` | `domainName, domainTopicName, resourceGroupName, subscriptionId` | Get properties of a domain topic. |
