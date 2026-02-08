$cityList = @(
  @{ name = "Berkley"; slug = "berkley" },
  @{ name = "Birmingham"; slug = "birmingham" },
  @{ name = "Bloomfield Hills"; slug = "bloomfield-hills" },
  @{ name = "Brighton"; slug = "brighton" },
  @{ name = "Clarkston"; slug = "clarkston" },
  @{ name = "Commerce"; slug = "commerce" },
  @{ name = "Davisburg"; slug = "davisburg" },
  @{ name = "Dexter"; slug = "dexter" },
  @{ name = "Farmington"; slug = "farmington" },
  @{ name = "Farmington Hills"; slug = "farmington-hills" },
  @{ name = "Fenton"; slug = "fenton" },
  @{ name = "Hartland"; slug = "hartland" },
  @{ name = "Highland"; slug = "highland" },
  @{ name = "Holly"; slug = "holly" },
  @{ name = "Howell"; slug = "howell" },
  @{ name = "Lake Orion"; slug = "lake-orion" },
  @{ name = "Livonia"; slug = "livonia" },
  @{ name = "Madison Heights"; slug = "madison-heights" },
  @{ name = "New Hudson"; slug = "new-hudson" },
  @{ name = "Northville"; slug = "northville" },
  @{ name = "Novi"; slug = "novi" },
  @{ name = "Oakland Township"; slug = "oakland-township" },
  @{ name = "Orchard Lake"; slug = "orchard-lake" },
  @{ name = "Ortonville"; slug = "ortonville" },
  @{ name = "Pinckney"; slug = "pinckney" },
  @{ name = "Plymouth"; slug = "plymouth" },
  @{ name = "Pontiac"; slug = "pontiac" },
  @{ name = "Rochester"; slug = "rochester" },
  @{ name = "Rochester Hills"; slug = "rochester-hills" },
  @{ name = "South Lyon"; slug = "south-lyon" },
  @{ name = "Southfield"; slug = "southfield" },
  @{ name = "Sterling Heights"; slug = "sterling-heights" },
  @{ name = "Troy"; slug = "troy" },
  @{ name = "Walled Lake"; slug = "walled-lake" },
  @{ name = "Warren"; slug = "warren" },
  @{ name = "Waterford"; slug = "waterford" },
  @{ name = "West Bloomfield"; slug = "west-bloomfield" },
  @{ name = "White Lake"; slug = "white-lake" },
  @{ name = "Wixom"; slug = "wixom" },
  @{ name = "Wolverine Lake"; slug = "wolverine-lake" }
)

function New-AreaListItems {
  param(
    [string]$currentSlug,
    [bool]$useAnchorStyle,
    [bool]$highlightCurrent
  )

  $items = foreach ($city in $cityList) {
    $href = "/asphalt-paving-in-$($city.slug)/"
    $aStyle = if ($useAnchorStyle) { ' style="color: white; text-decoration: none;"' } else { '' }
    if ($highlightCurrent -and $city.slug -eq $currentSlug) {
      "          <li class=\"cs-area-item\" style=\"font-weight: 700; background: var(--primaryDark);\"><a href=\"$href\"$aStyle>$($city.name)</a></li>"
    } else {
      "          <li class=\"cs-area-item\"><a href=\"$href\"$aStyle>$($city.name)</a></li>"
    }
  }

  return ($items -join "`r`n")
}

$newCityPages = @(
  @{ name = "Walled Lake"; slug = "walled-lake" },
  @{ name = "Wolverine Lake"; slug = "wolverine-lake" },
  @{ name = "Berkley"; slug = "berkley" },
  @{ name = "Oakland Township"; slug = "oakland-township" },
  @{ name = "Madison Heights"; slug = "madison-heights" },
  @{ name = "Dexter"; slug = "dexter" },
  @{ name = "Brighton"; slug = "brighton" }
)

foreach ($page in $newCityPages) {
  $file = "src\pages\servicepages\cities\asphalt-paving-in-$($page.slug).html"
  if (-not (Test-Path $file)) { continue }

  $content = Get-Content -Raw -Path $file
  $content = $content -replace 'Birmingham', $page.name
  $content = $content -replace 'birmingham', $page.slug
  $content = [regex]::Replace($content, '(?ms)^\s*eleventyNavigation:\r?\n(?:\s+.*\r?\n){0,5}', '')

  $items = New-AreaListItems -currentSlug $page.slug -useAnchorStyle $true -highlightCurrent $true
  $listBlock = "        <ul class=\"cs-areas-list\" style=\"grid-template-columns: repeat(2, 1fr);\">`r`n$items`r`n        </ul>"
  $content = [regex]::Replace($content, '(?s)<ul class=\"cs-areas-list\"[^>]*>.*?</ul>', $listBlock)

  Set-Content -Path $file -Value $content -NoNewline
}

$homepageFile = "src\index.html"
$homepageContent = Get-Content -Raw $homepageFile
$homepageItems = New-AreaListItems -currentSlug "" -useAnchorStyle $false -highlightCurrent $false
$homepageListBlock = "        <ul class=\"cs-areas-list\" style=\"grid-template-columns: repeat(2, 1fr);\">`r`n$homepageItems`r`n        </ul>"
$homepageContent = [regex]::Replace($homepageContent, '(?s)<ul class=\"cs-areas-list\"[^>]*>.*?</ul>', $homepageListBlock)
Set-Content -Path $homepageFile -Value $homepageContent -NoNewline

$serviceFile = "src\pages\servicepages\asphalt-paving.html"
$serviceContent = Get-Content -Raw $serviceFile
$serviceItems = New-AreaListItems -currentSlug "" -useAnchorStyle $true -highlightCurrent $false
$serviceListBlock = "        <ul class=\"cs-areas-list\" style=\"grid-template-columns: repeat(2, 1fr);\">`r`n$serviceItems`r`n        </ul>"
$serviceContent = [regex]::Replace($serviceContent, '(?s)<ul class=\"cs-areas-list\"[^>]*>.*?</ul>', $serviceListBlock)
Set-Content -Path $serviceFile -Value $serviceContent -NoNewline
