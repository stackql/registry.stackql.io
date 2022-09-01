---
title: ou_container
hide_title: false
hide_table_of_contents: false
keywords:
  - ou_container
  - aad_domain_services
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
<tr><td><b>Name</b></td><td><code>ou_container</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.aad_domain_services.ou_container</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `containerId` | `string` | The OuContainer name |
| `location` | `string` | Resource location |
| `distinguishedName` | `string` | Distinguished Name of OuContainer instance |
| `type` | `string` | Resource type |
| `tenantId` | `string` | Azure Active Directory tenant id |
| `deploymentId` | `string` | The Deployment id |
| `tags` | `object` | Resource tags |
| `serviceStatus` | `string` | Status of OuContainer instance |
| `domainName` | `string` | The domain name of Domain Services. |
| `provisioningState` | `string` | The current deployment or provisioning state, which only appears in the response. |
| `accounts` | `array` | The list of container accounts |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `etag` | `string` | Resource etag |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `OuContainer_List` | `SELECT` | `domainServiceName, resourceGroupName, subscriptionId` | The List of OuContainers in DomainService instance. |
| `OuContainer_Create` | `INSERT` | `domainServiceName, ouContainerName, resourceGroupName, subscriptionId` | The Create OuContainer operation creates a new OuContainer under the specified Domain Service instance. |
| `OuContainer_Delete` | `DELETE` | `domainServiceName, ouContainerName, resourceGroupName, subscriptionId` | The Delete OuContainer operation deletes specified OuContainer. |
| `OuContainer_Get` | `EXEC` | `domainServiceName, ouContainerName, resourceGroupName, subscriptionId` | Get OuContainer in DomainService instance. |
| `OuContainer_Update` | `EXEC` | `domainServiceName, ouContainerName, resourceGroupName, subscriptionId` | The Update OuContainer operation can be used to update the existing OuContainers. |
