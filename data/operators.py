CMD_OPERATORS = {
    "|": "pipe output",
    "&": "run next command",
    "&&": "run next command if successful",
    "||": "run next command if failed",
    "<": "input redirection",
    ">": "output redirection (overwrite)",
    ">>": "output redirection (append)",
    "2>": "error redirection",
    "2>>": "append errors",
    "2>&1": "merge stderr into stdout"
}

POWERSHELL_OPERATORS = {
    "|": "Passes objects from one command to another. eg. Get-Process | Sort-Object CPU",
    ">": "Redirects success output to a file (overwrite). eg. Get-Process > processes.txt",
    ">>": "Appends success output to a file. eg. Get-Process >> processes.txt",
    "2>": "Redirects error output to a file. eg. Get-Process 2> errors.txt",
    "2>>": "Appends error output to a file. eg. Get-Process 2>> errors.txt",
    "*>": "Redirects all output streams to a file. eg. Get-Process *> output.txt",

    ";": "Separates multiple commands on a line. eg. Get-Date; Get-Location",
    "&&": "Executes the next command only if the previous command succeeds. eg. Test-Path file.txt && Get-Content file.txt",
    "||": "Executes the next command only if the previous command fails. eg. Test-Path file.txt || Write-Output 'Missing'",

    "=": "Assigns a value to a variable. eg. $name = 'John'",
    "+": "Adds numbers or concatenates strings. eg. $a + $b",
    "-": "Subtracts numeric values. eg. $a - $b",
    "*": "Multiplies numeric values. eg. $a * $b",
    "/": "Divides numeric values. eg. $a / $b",
    "%": "Returns the remainder after division. eg. $a % $b",

    "-eq": "Checks equality. eg. $a -eq $b",
    "-ne": "Checks inequality. eg. $a -ne $b",
    "-gt": "Checks if left operand is greater than right operand. eg. $a -gt $b",
    "-ge": "Checks if left operand is greater than or equal to right operand. eg. $a -ge $b",
    "-lt": "Checks if left operand is less than right operand. eg. $a -lt $b",
    "-le": "Checks if left operand is less than or equal to right operand. eg. $a -le $b",

    "-like": "Performs wildcard pattern matching on strings. Supports * and ? wildcards. eg. $_.Name -like '*.txt'",
    "-notlike": "Returns true when a string does not match a wildcard pattern. eg. $_.Name -notlike '*.log'",
    "-match": "Performs regular expression matching on strings. eg. $_.Name -match '^error.*'",
    "-notmatch": "Returns true when a string does not match a regular expression pattern. eg. $_.Name -notmatch '^temp.*'",

    "-contains": "Checks whether a collection contains a specified value. eg. $services -contains 'Spooler'",
    "-notcontains": "Checks whether a collection does not contain a specified value. eg. $services -notcontains 'Spooler'",
    "-in": "Checks whether a value exists in a collection. eg. 'Spooler' -in $services",
    "-notin": "Checks whether a value does not exist in a collection. eg. 'Spooler' -notin $services",

    "-and": "Logical AND. eg. $a -gt 0 -and $b -gt 0",
    "-or": "Logical OR. eg. $a -gt 0 -or $b -gt 0",
    "-not": "Logical NOT. eg. -not (Test-Path file.txt)"
}