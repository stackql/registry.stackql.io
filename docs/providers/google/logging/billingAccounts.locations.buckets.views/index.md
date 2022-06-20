---
title: billingAccounts.locations.buckets.views
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
<tr><td><b>Name</b></td><td><code>billingAccounts.locations.buckets.views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.logging.billingAccounts.locations.buckets.views</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `views` | `array` | A list of views. |
| `nextPageToken` | `string` | If there might be more results than appear in this response, then nextPageToken is included. To get the next set of results, call the same method again using the value of nextPageToken as pageToken. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `billingAccountsId, bucketsId, locationsId` | Lists views on a log bucket. |
| `create` | `INSERT` | `billingAccountsId, bucketsId, locationsId` | Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |
| `delete` | `DELETE` | `billingAccountsId, bucketsId, locationsId, viewsId` | Deletes a view on a log bucket. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes. |
| `patch` | `EXEC` | `billingAccountsId, bucketsId, locationsId, viewsId` | Updates a view on a log bucket. This method replaces the following fields in the existing view with values from the new view: filter. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes. |