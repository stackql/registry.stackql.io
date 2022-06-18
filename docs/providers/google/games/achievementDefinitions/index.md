---
title: achievementDefinitions
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
<tr><td><b>Name</b></td><td><code>achievementDefinitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.games.achievementDefinitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | The ID of the achievement. |
| `name` | `string` | The name of the achievement. |
| `description` | `string` | The description of the achievement. |
| `initialState` | `string` | The initial state of the achievement. |
| `revealedIconUrl` | `string` | The image URL for the revealed achievement icon. |
| `achievementType` | `string` | The type of the achievement. |
| `experiencePoints` | `string` | Experience points which will be earned when unlocking this achievement. |
| `isUnlockedIconUrlDefault` | `boolean` | Indicates whether the unlocked icon image being returned is a default image, or is game-provided. |
| `unlockedIconUrl` | `string` | The image URL for the unlocked achievement icon. |
| `formattedTotalSteps` | `string` | The total steps for an incremental achievement as a string. |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `games#achievementDefinition`. |
| `isRevealedIconUrlDefault` | `boolean` | Indicates whether the revealed icon image being returned is a default image, or is provided by the game. |
| `totalSteps` | `integer` | The total steps for an incremental achievement. |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list` | `SELECT` |  |
