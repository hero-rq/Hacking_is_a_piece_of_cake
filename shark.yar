How many images contain the string TBFC?

rule TBFC_Keyword_In_File
{
  meta:
    author = "shark "
    description = "Find TBFC:<alphanumeric> in files"

  strings:
    $tbfc = /TBFC:[A-Za-z0-9]+/

  condition:
    $tbfc
}

find me in island, Genius 
