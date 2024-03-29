---
title: moving_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - moving_addresses
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>moving_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.moving_addresses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `moveStatus` | `string` | The status of the Elastic IP address that's being moved to the EC2-VPC platform, or restored to the EC2-Classic platform. |
| `publicIp` | `string` | The Elastic IP address. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `moving_addresses_Describe` | `SELECT` |  |
