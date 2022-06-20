---
title: folders.locations.buckets
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
<tr><td><b>Name</b></td><td><code>folders.locations.buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.logging.folders.locations.buckets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `buckets` | `array` | A list of buckets. |
| `nextPageToken` | `string` | If there might be more results than appear in this response, then nextPageToken is included. To get the next set of results, call the same method again using the value of nextPageToken as pageToken. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `bucketsId, foldersId, locationsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `list` | `SELECT` | `foldersId, locationsId` | Lists log buckets. |
| `create` | `INSERT` | `foldersId, locationsId` | Creates a log bucket that can be used to store log entries. After a bucket has been created, the bucket's location cannot be changed. |
| `delete` | `DELETE` | `bucketsId, foldersId, locationsId` | Deletes a view on a log bucket. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes. |
| `patch` | `EXEC` | `bucketsId, foldersId, locationsId` | Updates a view on a log bucket. This method replaces the following fields in the existing view with values from the new view: filter. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes. |
| `undelete` | `EXEC` | `bucketsId, foldersId, locationsId` | Undeletes a log bucket. A bucket that has been deleted can be undeleted within the grace period of 7 days. |
