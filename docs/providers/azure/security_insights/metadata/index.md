---
title: metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata
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
<tr><td><b>Name</b></td><td><code>metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `parentId` | `string` | Full parent resource ID of the content item the metadata is for.  This is the full resource ID including the scope (subscription and resource group) |
| `contentId` | `string` | Static ID for the content.  Used to identify dependencies and content from solutions or community.  Hard-coded/static for out of the box content and solutions. Can be optionally set for user created content to define dependencies.  If an active content item is made from a template, both will have the same contentId. |
| `lastPublishDate` | `string` | last publish date of solution content item |
| `author` | `object` | Publisher or creator of the content item. |
| `customVersion` | `string` | The custom version of the content. A optional free text |
| `icon` | `string` | the icon identifier. this id can later be fetched from the solution template |
| `version` | `string` | Version of the content.  Default and recommended format is numeric (e.g. 1, 1.0, 1.0.0, 1.0.0.0), following ARM template best practices.  Can also be any string, but then we cannot guarantee any version checks |
| `threatAnalysisTactics` | `array` | the tactics the resource covers |
| `contentSchemaVersion` | `string` | Schema version of the content. Can be used to distinguish between different flow based on the schema version |
| `support` | `object` | Support information for the content item. |
| `dependencies` | `object` | Dependencies for the content item, what other content items it requires to work.  Can describe more complex dependencies using a recursive/nested structure. For a single dependency an id/kind/version can be supplied or operator/criteria for complex dependencies. |
| `firstPublishDate` | `string` | first publish date of solution content item |
| `categories` | `object` | ies for the solution content item |
| `kind` | `string` | The kind of content the metadata is for. |
| `previewImagesDark` | `array` | preview image file names. These will be taken from the solution artifacts. used for dark theme support |
| `providers` | `array` | Providers for the solution content item |
| `etag` | `string` | Etag of the azure resource |
| `previewImages` | `array` | preview image file names. These will be taken from the solution artifacts |
| `source` | `object` | The original source of the content item, where it comes from. |
| `threatAnalysisTechniques` | `array` | the techniques the resource covers, these have to be aligned with the tactics being used |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Metadata_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List of all metadata |
| `Metadata_Create` | `INSERT` | `metadataName, resourceGroupName, subscriptionId, workspaceName` | Create a Metadata. |
| `Metadata_Delete` | `DELETE` | `metadataName, resourceGroupName, subscriptionId, workspaceName` | Delete a Metadata. |
| `Metadata_Get` | `EXEC` | `metadataName, resourceGroupName, subscriptionId, workspaceName` | Get a Metadata. |
| `Metadata_Update` | `EXEC` | `metadataName, resourceGroupName, subscriptionId, workspaceName` | Update an existing Metadata. |
