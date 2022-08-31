---
title: api_schema
hide_title: false
hide_table_of_contents: false
keywords:
  - api_schema
  - api_management
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
<tr><td><b>Name</b></td><td><code>api_schema</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_schema</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `contentType` | `string` | Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml). &lt;/br&gt; - `Swagger` Schema use `application/vnd.ms-azure-apim.swagger.definitions+json` &lt;/br&gt; - `WSDL` Schema use `application/vnd.ms-azure-apim.xsd+xml` &lt;/br&gt; - `OpenApi` Schema use `application/vnd.oai.openapi.components+json` &lt;/br&gt; - `WADL Schema` use `application/vnd.ms-azure-apim.wadl.grammars+xml`. |
| `document` | `object` | Api Schema Document Properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApiSchema_ListByApi` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Get the schema configuration at the API level. |
| `ApiSchema_CreateOrUpdate` | `INSERT` | `apiId, resourceGroupName, schemaId, serviceName, subscriptionId` | Creates or updates schema configuration for the API. |
| `ApiSchema_Delete` | `DELETE` | `If-Match, apiId, resourceGroupName, schemaId, serviceName, subscriptionId` | Deletes the schema configuration at the Api. |
| `ApiSchema_Get` | `EXEC` | `apiId, resourceGroupName, schemaId, serviceName, subscriptionId` | Get the schema configuration at the API level. |
| `ApiSchema_GetEntityTag` | `EXEC` | `apiId, resourceGroupName, schemaId, serviceName, subscriptionId` | Gets the entity state (Etag) version of the schema specified by its identifier. |
