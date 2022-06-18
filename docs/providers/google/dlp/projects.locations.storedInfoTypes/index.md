---
title: projects.locations.storedInfoTypes
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects.locations.storedInfoTypes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dlp.projects.locations.storedInfoTypes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `storedInfoTypes` | `array` | List of storedInfoTypes, up to page_size in ListStoredInfoTypesRequest. |
| `nextPageToken` | `string` | If the next page is available then the next page token to be used in following ListStoredInfoTypes request. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `locationsId, projectsId, storedInfoTypesId` | Gets a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists stored infoTypes. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a pre-built stored infoType to be used for inspection. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `delete` | `DELETE` | `locationsId, projectsId, storedInfoTypesId` | Deletes a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `patch` | `EXEC` | `locationsId, projectsId, storedInfoTypesId` | Updates the stored infoType by creating a new version. The existing version will continue to be used until the new version is ready. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
