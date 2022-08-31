---
title: application_package
hide_title: false
hide_table_of_contents: false
keywords:
  - application_package
  - batch
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
<tr><td><b>Name</b></td><td><code>application_package</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.batch.application_package</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `storageUrlExpiry` | `string` | The UTC time at which the Azure Storage URL will expire. |
| `storageUrl` | `string` | The URL for the application package in Azure Storage. |
| `state` | `string` | The current state of the application package. |
| `etag` | `string` | The ETag of the resource, used for concurrency statements. |
| `format` | `string` | The format of the application package, if the package is active. |
| `lastActivationTime` | `string` | The time at which the package was last activated, if the package is active. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApplicationPackage_List` | `SELECT` | `accountName, applicationName, resourceGroupName, subscriptionId` | Lists all of the application packages in the specified application. |
| `ApplicationPackage_Create` | `INSERT` | `accountName, applicationName, resourceGroupName, subscriptionId, versionName` | Creates an application package record. The record contains a storageUrl where the package should be uploaded to.  Once it is uploaded the `ApplicationPackage` needs to be activated using `ApplicationPackageActive` before it can be used. If the auto storage account was configured to use storage keys, the URL returned will contain a SAS. |
| `ApplicationPackage_Delete` | `DELETE` | `accountName, applicationName, resourceGroupName, subscriptionId, versionName` | Deletes an application package record and its associated binary file. |
| `ApplicationPackage_Activate` | `EXEC` | `accountName, applicationName, resourceGroupName, subscriptionId, versionName, data__format` | Activates the specified application package. This should be done after the `ApplicationPackage` was created and uploaded. This needs to be done before an `ApplicationPackage` can be used on Pools or Tasks. |
| `ApplicationPackage_Get` | `EXEC` | `accountName, applicationName, resourceGroupName, subscriptionId, versionName` | Gets information about the specified application package. |
