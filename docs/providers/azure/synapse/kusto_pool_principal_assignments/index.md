---
title: kusto_pool_principal_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pool_principal_assignments
  - synapse
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
<tr><td><b>Name</b></td><td><code>kusto_pool_principal_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.kusto_pool_principal_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `principalType` | `string` | Principal type. |
| `aadObjectId` | `string` | The service principal object id in AAD (Azure active directory) |
| `tenantId` | `string` | The tenant id of the principal |
| `role` | `string` | Cluster principal role. |
| `tenantName` | `string` | The tenant name of the principal |
| `principalId` | `string` | The principal ID assigned to the cluster principal. It can be a user email, application ID, or security group name. |
| `principalName` | `string` | The principal name |
| `provisioningState` | `string` | The provisioned state of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `KustoPoolPrincipalAssignments_List` | `SELECT` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Lists all Kusto pool principalAssignments. |
| `KustoPoolPrincipalAssignments_CreateOrUpdate` | `INSERT` | `kustoPoolName, principalAssignmentName, resourceGroupName, subscriptionId, workspaceName` | Create a Kusto pool principalAssignment. |
| `KustoPoolPrincipalAssignments_Delete` | `DELETE` | `kustoPoolName, principalAssignmentName, resourceGroupName, subscriptionId, workspaceName` | Deletes a Kusto pool principalAssignment. |
| `KustoPoolPrincipalAssignments_CheckNameAvailability` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__name, data__type` | Checks that the principal assignment name is valid and is not already in use. |
| `KustoPoolPrincipalAssignments_Get` | `EXEC` | `kustoPoolName, principalAssignmentName, resourceGroupName, subscriptionId, workspaceName` | Gets a Kusto pool principalAssignment. |
