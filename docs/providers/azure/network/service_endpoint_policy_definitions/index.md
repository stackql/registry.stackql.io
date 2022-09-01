---
title: service_endpoint_policy_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - service_endpoint_policy_definitions
  - network
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
<tr><td><b>Name</b></td><td><code>service_endpoint_policy_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.service_endpoint_policy_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `description` | `string` | A description for this rule. Restricted to 140 chars. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `provisioningState` | `string` | The current provisioning state. |
| `service` | `string` | Service endpoint name. |
| `serviceResources` | `array` | A list of service resources. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServiceEndpointPolicyDefinitions_ListByResourceGroup` | `SELECT` | `resourceGroupName, serviceEndpointPolicyName, subscriptionId` | Gets all service endpoint policy definitions in a service end point policy. |
| `ServiceEndpointPolicyDefinitions_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceEndpointPolicyDefinitionName, serviceEndpointPolicyName, subscriptionId` | Creates or updates a service endpoint policy definition in the specified service endpoint policy. |
| `ServiceEndpointPolicyDefinitions_Delete` | `DELETE` | `resourceGroupName, serviceEndpointPolicyDefinitionName, serviceEndpointPolicyName, subscriptionId` | Deletes the specified ServiceEndpoint policy definitions. |
| `ServiceEndpointPolicyDefinitions_Get` | `EXEC` | `resourceGroupName, serviceEndpointPolicyDefinitionName, serviceEndpointPolicyName, subscriptionId` | Get the specified service endpoint policy definitions from service endpoint policy. |
