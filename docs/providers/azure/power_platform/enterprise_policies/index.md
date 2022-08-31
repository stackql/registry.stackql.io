---
title: enterprise_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - enterprise_policies
  - power_platform
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
<tr><td><b>Name</b></td><td><code>enterprise_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.power_platform.enterprise_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `encryption` | `object` | The encryption settings for a configuration store. |
| `lockbox` | `object` | Settings concerning lockbox. |
| `networkInjection` | `object` | Settings concerning network injection. |
| `systemId` | `string` | The internally assigned unique identifier of the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `kind` | `string` | The Kind (type) of Enterprise Policy |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | The identity of the EnterprisePolicy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `EnterprisePolicies_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieve a list of EnterprisePolicies within a given resource group |
| `EnterprisePolicies_ListBySubscription` | `SELECT` | `subscriptionId` | Retrieve a list of EnterprisePolicies within a subscription |
| `EnterprisePolicies_CreateOrUpdate` | `INSERT` | `enterprisePolicyName, resourceGroupName, subscriptionId, data__kind` | Creates an EnterprisePolicy |
| `EnterprisePolicies_Delete` | `DELETE` | `enterprisePolicyName, resourceGroupName, subscriptionId` | Delete an EnterprisePolicy |
| `EnterprisePolicies_Get` | `EXEC` | `enterprisePolicyName, resourceGroupName, subscriptionId` | Get information about an EnterprisePolicy |
| `EnterprisePolicies_Update` | `EXEC` | `enterprisePolicyName, resourceGroupName, subscriptionId` | Updates an EnterprisePolicy |
