param(
  [Parameter(Mandatory=$true)][string]$Deck,
  [Parameter(Mandatory=$true)][string]$Pdf
)
$ErrorActionPreference = 'Stop'

$Deck = (Resolve-Path $Deck).Path
$Pdf = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($Pdf)

$ppt = New-Object -ComObject PowerPoint.Application
$pres = $null
try {
  # ReadOnly = -1, Untitled = 0, WithWindow = 0
  $pres = $ppt.Presentations.Open($Deck, -1, 0, 0)
  # 32 = ppSaveAsPDF
  $pres.SaveAs($Pdf, 32)
  $pres.Close()
  $pres = $null
  Write-Output "PDF generated: $Pdf"
} finally {
  if ($null -ne $pres) {
    try { [System.Runtime.InteropServices.Marshal]::ReleaseComObject($pres) | Out-Null } catch {}
  }
  $ppt.Quit()
  [System.Runtime.InteropServices.Marshal]::ReleaseComObject($ppt) | Out-Null
}
