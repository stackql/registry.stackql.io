---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - service_fabric_managed_clusters
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_managed_clusters.applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource identifier. |
| `name` | `string` | Azure resource name. |
| `upgradePolicy` | `object` | Describes the policy for a monitored application upgrade. |
| `tags` | `object` | Azure resource tags. |
| `parameters` | `object` | List of application parameters with overridden values from their default values specified in the application manifest. |
| `identity` | `object` | Describes the managed identities for an Azure resource. |
| `location` | `string` | Resource location depends on the parent resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `version` | `string` | The version of the application type as defined in the application manifest.<br />This name must be the full Arm Resource ID for the referenced application type version.<br /> |
| `provisioningState` | `string` | The current deployment or provisioning state, which only appears in the response |
| `managedIdentities` | `array` | List of user assigned identities for the application, each mapped to a friendly name. |
| `type` | `string` | Azure resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Applications_List` | `SELECT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Gets all managed application resources created or in the process of being created in the Service Fabric cluster resource. |
| `Applications_CreateOrUpdate` | `INSERT` | `api-version, applicationName, clusterName, resourceGroupName, subscriptionId` | Create or update a Service Fabric managed application resource with the specified name. |
| `Applications_Delete` | `DELETE` | `api-version, applicationName, clusterName, resourceGroupName, subscriptionId` | Delete a Service Fabric managed application resource with the specified name. |
| `Applications_Get` | `EXEC` | `api-version, applicationName, clusterName, resourceGroupName, subscriptionId` | Get a Service Fabric managed application resource created or in the process of being created in the Service Fabric cluster resource. |
| `Applications_Update` | `EXEC` | `api-version, applicationName, clusterName, resourceGroupName, subscriptionId` | Updates the tags of an application resource of a given managed cluster. |
