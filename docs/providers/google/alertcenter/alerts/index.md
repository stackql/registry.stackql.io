---
title: alerts
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
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.alertcenter.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `alerts` | `array` | The list of alerts. |
| `nextPageToken` | `string` | The token for the next page. If not empty, indicates that there may be more alerts that match the listing request; this value can be used in a subsequent ListAlertsRequest to get alerts continuing from last result of the current list call. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `alertId` | Gets the specified alert. Attempting to get a nonexistent alert returns `NOT_FOUND` error. |
| `list` | `SELECT` |  | Lists the alerts. |
| `delete` | `DELETE` | `alertId` | Marks the specified alert for deletion. An alert that has been marked for deletion is removed from Alert Center after 30 days. Marking an alert for deletion has no effect on an alert which has already been marked for deletion. Attempting to mark a nonexistent alert for deletion results in a `NOT_FOUND` error. |
| `batchDelete` | `EXEC` |  | Performs batch delete operation on alerts. |
| `batchUndelete` | `EXEC` |  | Performs batch undelete operation on alerts. |
| `getMetadata` | `EXEC` | `alertId` | Returns the metadata of an alert. Attempting to get metadata for a non-existent alert returns `NOT_FOUND` error. |
| `undelete` | `EXEC` | `alertId` | Restores, or "undeletes", an alert that was marked for deletion within the past 30 days. Attempting to undelete an alert which was marked for deletion over 30 days ago (which has been removed from the Alert Center database) or a nonexistent alert returns a `NOT_FOUND` error. Attempting to undelete an alert which has not been marked for deletion has no effect. |
