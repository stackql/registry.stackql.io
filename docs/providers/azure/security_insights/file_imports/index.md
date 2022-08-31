---
title: file_imports
hide_title: false
hide_table_of_contents: false
keywords:
  - file_imports
  - security_insights
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
<tr><td><b>Name</b></td><td><code>file_imports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.file_imports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `createdTimeUTC` | `string` | The time the file was imported. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `state` | `string` | The state of the file import. |
| `ingestedRecordCount` | `integer` | The number of records that have been successfully ingested. |
| `importValidUntilTimeUTC` | `string` | The time the file import record is soft deleted from the database and history. |
| `errorsPreview` | `array` | An ordered list of some of the errors that were encountered during validation. |
| `validRecordCount` | `integer` | The number of records that have passed validation. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `totalRecordCount` | `integer` | The number of records in the file. |
| `importFile` | `object` | Represents a file. |
| `ingestionMode` | `string` | Describes how to ingest the records in the file. |
| `errorFile` | `object` | Represents a file. |
| `source` | `string` | The source for the data in the file. |
| `contentType` | `string` | The content type of this file. |
| `filesValidUntilTimeUTC` | `string` | The time the files associated with this import are deleted from the storage account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FileImports_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all file imports. |
| `FileImports_Create` | `INSERT` | `fileImportId, resourceGroupName, subscriptionId, workspaceName` | Creates the file import. |
| `FileImports_Delete` | `DELETE` | `fileImportId, resourceGroupName, subscriptionId, workspaceName` | Delete the file import. |
| `FileImports_Get` | `EXEC` | `fileImportId, resourceGroupName, subscriptionId, workspaceName` | Gets a file import. |
