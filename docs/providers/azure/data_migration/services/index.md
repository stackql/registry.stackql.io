---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - data_migration
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
<tr><td><b>Id</b></td><td><code>azure.data_migration.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` |  |
| `systemData` | `object` |  |
| `virtualSubnetId` | `string` | The ID of the Microsoft.Network/virtualNetworks/subnets resource to which the service should be joined |
| `deleteResourcesOnStop` | `boolean` | Whether service resources should be deleted when stopped. (Turned on by default) |
| `provisioningState` | `string` | The resource's provisioning state |
| `etag` | `string` | HTTP strong entity tag value. Ignored if submitted |
| `tags` | `object` |  |
| `sku` | `object` | An Azure SKU instance |
| `virtualNicId` | `string` | The ID of the Microsoft.Network/networkInterfaces resource which the service have |
| `publicKey` | `string` | The public key of the service, used to encrypt secrets sent to the service |
| `kind` | `string` | The resource kind. Only 'vm' (the default) is supported. |
| `type` | `string` |  |
| `location` | `string` |  |
| `autoStopDelay` | `string` | The time delay before the service is auto-stopped when idle. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Services_List` | `SELECT` | `api-version, subscriptionId` | The services resource is the top-level resource that represents the Database Migration Service. This method returns a list of service resources in a subscription. |
| `Services_ListByResourceGroup` | `SELECT` | `api-version, groupName, subscriptionId` | The Services resource is the top-level resource that represents the Database Migration Service. This method returns a list of service resources in a resource group. |
| `Services_CreateOrUpdate` | `INSERT` |  | The services resource is the top-level resource that represents the Database Migration Service. The PUT method creates a new service or updates an existing one. When a service is updated, existing child resources (i.e. tasks) are unaffected. Services currently support a single kind, "vm", which refers to a VM-based service, although other kinds may be added in the future. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request ("ServiceIsBusy"). The provider will reply when successful with 200 OK or 201 Created. Long-running operations use the provisioningState property. |
| `Services_Delete` | `DELETE` |  | The services resource is the top-level resource that represents the Database Migration Service. The DELETE method deletes a service. Any running tasks will be canceled. |
| `Services_CheckChildrenNameAvailability` | `EXEC` | `api-version, groupName, serviceName, subscriptionId` | This method checks whether a proposed nested resource name is valid and available. |
| `Services_CheckNameAvailability` | `EXEC` | `api-version, location, subscriptionId` | This method checks whether a proposed top-level resource name is valid and available. |
| `Services_CheckStatus` | `EXEC` | `api-version, groupName, serviceName, subscriptionId` | The services resource is the top-level resource that represents the Database Migration Service. This action performs a health check and returns the status of the service and virtual machine size. |
| `Services_Get` | `EXEC` |  | The services resource is the top-level resource that represents the Database Migration Service. The GET method retrieves information about a service instance. |
| `Services_ListSkus` | `EXEC` | `api-version, groupName, serviceName, subscriptionId` | The services resource is the top-level resource that represents the Database Migration Service. The skus action returns the list of SKUs that a service resource can be updated to. |
| `Services_Start` | `EXEC` | `api-version, groupName, serviceName, subscriptionId` | The services resource is the top-level resource that represents the Database Migration Service. This action starts the service and the service can be used for data migration. |
| `Services_Stop` | `EXEC` | `api-version, groupName, serviceName, subscriptionId` | The services resource is the top-level resource that represents the Database Migration Service. This action stops the service and the service cannot be used for data migration. The service owner won't be billed when the service is stopped. |
| `Services_Update` | `EXEC` |  | The services resource is the top-level resource that represents the Database Migration Service. The PATCH method updates an existing service. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request ("ServiceIsBusy"). |
