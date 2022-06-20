---
title: shippingsettings
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
<tr><td><b>Name</b></td><td><code>shippingsettings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.content.shippingsettings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#shippingsettingsListResponse`". |
| `nextPageToken` | `string` | The token for the retrieval of the next page of shipping settings. |
| `resources` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountId, merchantId` | Retrieves the shipping settings of the account. |
| `list` | `SELECT` | `merchantId` | Lists the shipping settings of the sub-accounts in your Merchant Center account. |
| `custombatch` | `EXEC` |  | Retrieves and updates the shipping settings of multiple accounts in a single request. |
| `getsupportedcarriers` | `EXEC` | `merchantId` | Retrieves supported carriers and carrier services for an account. |
| `getsupportedholidays` | `EXEC` | `merchantId` | Retrieves supported holidays for an account. |
| `getsupportedpickupservices` | `EXEC` | `merchantId` | Retrieves supported pickup services for an account. |
| `update` | `EXEC` | `accountId, merchantId` | Updates the shipping settings of the account. Any fields that are not provided are deleted from the resource. |
