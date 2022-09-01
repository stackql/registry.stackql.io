---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - service_fabric
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource identifier. |
| `name` | `string` | Azure resource name. |
| `provisioningState` | `string` | The current deployment or provisioning state, which only appears in the response |
| `tags` | `object` | Azure resource tags. |
| `serviceKind` | `string` | The kind of service (Stateless or Stateful). |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `serviceDnsName` | `string` | Dns name used for the service. If this is specified, then the service can be accessed via its DNS name instead of service name. |
| `serviceTypeName` | `string` | The name of the service type |
| `type` | `string` | Azure resource type. |
| `partitionDescription` | `object` | Describes how the service is partitioned. |
| `etag` | `string` | Azure resource etag. |
| `servicePackageActivationMode` | `string` | The activation Mode of the service package |
| `location` | `string` | It will be deprecated in New API, resource location depends on the parent resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Services_List` | `SELECT` | `api-version, applicationName, clusterName, resourceGroupName, subscriptionId` | Gets all service resources created or in the process of being created in the Service Fabric application resource. |
| `Services_CreateOrUpdate` | `INSERT` | `api-version, applicationName, clusterName, resourceGroupName, serviceName, subscriptionId` | Create or update a Service Fabric service resource with the specified name. |
| `Services_Delete` | `DELETE` | `api-version, applicationName, clusterName, resourceGroupName, serviceName, subscriptionId` | Delete a Service Fabric service resource with the specified name. |
| `Services_Get` | `EXEC` | `api-version, applicationName, clusterName, resourceGroupName, serviceName, subscriptionId` | Get a Service Fabric service resource created or in the process of being created in the Service Fabric application resource. |
| `Services_Update` | `EXEC` | `api-version, applicationName, clusterName, resourceGroupName, serviceName, subscriptionId` | Update a Service Fabric service resource with the specified name. |
