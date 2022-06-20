---
title: bidders.accounts.filterSets
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
<tr><td><b>Name</b></td><td><code>bidders.accounts.filterSets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.adexchangebuyer2.bidders.accounts.filterSets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `filterSets` | `array` | The filter sets belonging to the buyer. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in the ListFilterSetsRequest.pageToken field in the subsequent call to the accounts.filterSets.list method to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountsId, biddersId, filterSetsId` | Retrieves the requested filter set for the account with the given account ID. |
| `list` | `SELECT` | `accountsId, biddersId` | Lists all filter sets for the account with the given account ID. |
| `create` | `INSERT` | `accountsId, biddersId` | Creates the specified filter set for the account with the given account ID. |
| `delete` | `DELETE` | `accountsId, biddersId, filterSetsId` | Deletes the requested filter set from the account with the given account ID. |
