---
title: leaderboards
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
<tr><td><b>Name</b></td><td><code>leaderboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.games.leaderboards</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The leaderboard ID. |
| `name` | `string` | The name of the leaderboard. |
| `isIconUrlDefault` | `boolean` | Indicates whether the icon image being returned is a default image, or is game-provided. |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `games#leaderboard`. |
| `order` | `string` | How scores are ordered. |
| `iconUrl` | `string` | The icon for the leaderboard. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `leaderboardId` | Retrieves the metadata of the leaderboard with the given ID. |
| `list` | `SELECT` |  | Lists all the leaderboard metadata for your application. |