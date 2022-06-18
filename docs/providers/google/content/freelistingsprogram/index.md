---
title: freelistingsprogram
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
<tr><td><b>Name</b></td><td><code>freelistingsprogram</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.content.freelistingsprogram</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `regionStatuses` | `array` | Status of the program in each region. Regions with the same status and review eligibility are grouped together in `regionCodes`. |
| `state` | `string` | If program is successfully onboarded for at least one region. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `merchantId` | Retrieves the status and review eligibility for the free listing program. |
| `requestreview` | `EXEC` | `merchantId` | Requests a review for Free Listings program in the provided region. Important: This method is only whitelisted for selected merchants. |
