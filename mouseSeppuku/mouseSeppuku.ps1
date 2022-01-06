$deviceName="HID-compliant mouse"
foreach ($dev in (Get-PnpDevice | Where-Object{$_.Name -eq $deviceName})) {
  &"pnputil" /remove-device $dev.InstanceId
}