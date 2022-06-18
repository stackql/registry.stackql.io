---
title: management.unsampledReports
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
<tr><td><b>Name</b></td><td><code>management.unsampledReports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analytics.management.unsampledReports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | Unsampled report ID. |
| `status` | `string` | Status of this unsampled report. Possible values are PENDING, COMPLETED, or FAILED. |
| `dimensions` | `string` | The dimensions for the unsampled report. |
| `accountId` | `string` | Account ID to which this unsampled report belongs. |
| `driveDownloadDetails` | `object` | Download details for a file stored in Google Drive. |
| `selfLink` | `string` | Link for this unsampled report. |
| `cloudStorageDownloadDetails` | `object` | Download details for a file stored in Google Cloud Storage. |
| `created` | `string` | Time this unsampled report was created. |
| `end-date` | `string` | The end date for the unsampled report. |
| `downloadType` | `string` | The type of download you need to use for the report data file. Possible values include `GOOGLE_DRIVE` and `GOOGLE_CLOUD_STORAGE`. If the value is `GOOGLE_DRIVE`, see the `driveDownloadDetails` field. If the value is `GOOGLE_CLOUD_STORAGE`, see the `cloudStorageDownloadDetails` field. |
| `metrics` | `string` | The metrics for the unsampled report. |
| `updated` | `string` | Time this unsampled report was last modified. |
| `webPropertyId` | `string` | Web property ID to which this unsampled report belongs. The web property ID is of the form UA-XXXXX-YY. |
| `start-date` | `string` | The start date for the unsampled report. |
| `title` | `string` | Title of the unsampled report. |
| `profileId` | `string` | View (Profile) ID to which this unsampled report belongs. |
| `kind` | `string` | Resource type for an Analytics unsampled report. |
| `segment` | `string` | The segment for the unsampled report. |
| `filters` | `string` | The filters for the unsampled report. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `accountId, profileId, unsampledReportId, webPropertyId` | Returns a single unsampled report. |
| `list` | `SELECT` | `accountId, profileId, webPropertyId` | Lists unsampled reports to which the user has access. |
| `insert` | `INSERT` | `accountId, profileId, webPropertyId` | Create a new unsampled report. |
| `delete` | `DELETE` | `accountId, profileId, unsampledReportId, webPropertyId` | Deletes an unsampled report. |
