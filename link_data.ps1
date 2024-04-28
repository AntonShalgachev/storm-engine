$SolutionDir = $args[0]
$ProjectDir = $args[1]
$OutputDir = $args[2]

$DataSourceDirectory = "D:\Documents\Development\Sea Dogs - City of Abandoned Ships - Eng"

function New-DataLink {
    param (
        $Destination,
        $Source
    )

    if (Test-Path $Destination) {
        (Get-Item -Path $Destination).Delete()
    }

    if (Test-Path $Source) {
        New-Item -Path $Destination -ItemType Junction -Value $Source
    }
}

New-DataLink "$OutputDir\modules\techniques" "$ProjectDir\modules\techniques"
New-DataLink "$OutputDir\LANGUAGE" "$DataSourceDirectory\LANGUAGE"
New-DataLink "$OutputDir\PROGRAM" "$DataSourceDirectory\PROGRAM"
New-DataLink "$OutputDir\RESOURCE" "$DataSourceDirectory\RESOURCE"
Copy-Item "$DataSourceDirectory\engine.ini" "$OutputDir\engine.ini"
Copy-Item "$SolutionDir\extern\fmodex\api\fmodex.dll" "$OutputDir\fmodex.dll"
