---
title: iot_security_solution
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_security_solution
  - security
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
<tr><td><b>Name</b></td><td><code>iot_security_solution</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.iot_security_solution</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `iotHubs` | `array` | IoT Hub resource IDs |
| `status` | `string` | Status of the IoT Security solution. |
| `disabledDataSources` | `array` | Disabled data sources. Disabling these data sources compromises the system. |
| `export` | `array` | List of additional options for exporting to workspace data. |
| `displayName` | `string` | Resource display name. |
| `autoDiscoveredResources` | `array` | List of resources that were automatically discovered as relevant to the security solution. |
| `recommendationsConfiguration` | `array` | List of the configuration status for each recommendation type. |
| `tags` | `object` | Resource tags |
| `workspace` | `string` | Workspace resource ID |
| `additionalWorkspaces` | `array` | List of additional workspaces |
| `unmaskedIpLoggingStatus` | `string` | Unmasked IP address logging status |
| `userDefinedResources` | `object` | Properties of the IoT Security solution's user defined resources. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `location` | `string` | The resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IotSecuritySolution_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Use this method to get the list IoT Security solutions organized by resource group. |
| `IotSecuritySolution_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Use this method to get the list of IoT Security solutions by subscription. |
| `IotSecuritySolution_CreateOrUpdate` | `INSERT` | `api-version, resourceGroupName, solutionName, subscriptionId` | Use this method to create or update yours IoT Security solution |
| `IotSecuritySolution_Delete` | `DELETE` | `api-version, resourceGroupName, solutionName, subscriptionId` | Use this method to delete yours IoT Security solution |
| `IotSecuritySolution_Get` | `EXEC` | `api-version, resourceGroupName, solutionName, subscriptionId` | User this method to get details of a specific IoT Security solution based on solution name |
| `IotSecuritySolution_Update` | `EXEC` | `api-version, resourceGroupName, solutionName, subscriptionId` | Use this method to update existing IoT Security solution tags or user defined resources. To update other fields use the CreateOrUpdate method. |
